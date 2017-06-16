# pylint cleanup stuff
mgr=mgr # pylint:disable=invalid-name,used-before-assignment
scriptdir=scriptdir # pylint:disable=invalid-name,used-before-assignment

import sys, glob, re, math

# this file will be included with the scripts so that pyserial doesn't need to be installed
sys.path.append(scriptdir+'pyserial-3.3-py2.py3-none-any.whl')

import serial

from eidolon import *

################################################################################################
### Search for available serial COM ports and add them to `available', assumption is the last one is the RFID reader
################################################################################################

available = []
for i in range(256):
    try:
        with serial.Serial('COM%i'%i) as s:
            available.append('COM%i'%i)
    except serial.SerialException:
        pass

################################################################################################
### Variables
################################################################################################

# name of the port for the RFID reader, if this can't be found replace this with hard coded string, eg. COM3 or COM4
PORT=last(available) 
# PORT='COM4' # try this if the above can't be found

# this setting for the serial port shouldn't need changing
BAUD=115200

def _sortkey(i):
    '''This is used to sort the filenames by timestep since CHeart doesn't include leading zeros in numbers.'''
    return int(re.search('.*Disp-(\d{1,3})',i).group(1))

# name of initial .X file, displacement fields are added to this one
initial=scriptdir+'modeldata/mesh/VP2HF_FE.X'
# name of topology file
topo=scriptdir+'modeldata/mesh/VP2HF_FE.T'

## These two values define the transform applied to rotating the model and rotating the sensor input, 
## they are used if necessary to ensure the model heart matches the physical heart's rotation
modelYaw=0.0 # rotate the model heart to ensure it matches the initial orientation of the phsical heart, 0.0 means RV is on right of screen, math.pi means RV on left
sensorYaw=0.0 # if the sensor is placed in a different orientation in the heart than expected it's transform must be rotated in the yaw axis to match the model

# initial fixing rotation to put the heart in a vertical orientation with RV to the right
initialrotation=rotator(-0.187471734862557,0.384590468636151,0.768019390580495,0.476540382081324)
# multiply the rotator by the model yaw rotator to fix yaw if necessary
initialrotation=rotator(vec3.Z(),modelYaw)*initialrotation 

# names of the 4 meshes to load, everything should be in this order
names=('unpaced', 'anterior','lateral','posterolateral')

#list of loaded representations
reprs=[]

# materials for meshes
mats=[mgr.createMaterial(n) for n in names]
mats[0].setDiffuse(color(1,0,0)) # unpaced color
mats[1].setDiffuse(color(1,1,0)) # anterior paced color
mats[2].setDiffuse(color(0,1,1)) # lateral paced color
mats[3].setDiffuse(color(0,0,1)) # posterolateral paced color
mats[0].setAlpha(0.5) # leave these alone
mats[1].setAlpha(0.5)
mats[2].setAlpha(0.5)
mats[3].setAlpha(0.5)

# list of mesh displacement filenames, ordering is same as 'names'
displaceFilenames=[
    sorted(glob.glob(scriptdir+'modeldata/rsUnpaced/Disp-*.D'),key=_sortkey),
    sorted(glob.glob(scriptdir+'modeldata/rsAnterior/Disp-*.D'),key=_sortkey),
    sorted(glob.glob(scriptdir+'modeldata/rsLateral/Disp-*.D'),key=_sortkey),
    sorted(glob.glob(scriptdir+'modeldata/rsPosterolateral/Disp-*.D'),key=_sortkey),
]

# list of activation map filenames, ordering is same as 'names'
activationMaps=[
    scriptdir+'modeldata/activation_maps/f70_unpaced_point.D',
    scriptdir+'modeldata/activation_maps/f70_anterior_point.D',
    scriptdir+'modeldata/activation_maps/f70_lateral_point.D',
    scriptdir+'modeldata/activation_maps/f70_posterolateral_point.D',
]

################################################################################################
### Load mesh objects
################################################################################################

for n,files,amap,mat in zip(names,displaceFilenames,activationMaps,mats):
    obj=CHeart.loadSceneObject(files[::2],topo,ElemType._Tet1NL,initialXFile=initial,objname=n)
    CHeart.loadDataField(obj,amap,1)
    mgr.addSceneObject(obj)
    
    # center mesh at the origin and rotate to be apex down, RV to the right, and process activation field
    dds=obj.datasets
    df0=first(dds[0].enumDataFields())
    
    center=BoundBox(dds[0].getNodes()).center
    for i,ds in enumerate(dds): 
        i/=float(len(dds)-1)
        
        nodes=ds.getNodes()
        nodes.sub(center)
        nodes.mul(initialrotation)
        
        # subtract the value as i so that the activation time for this dataset is 0 since the isosurface will be plotted at point 0
        df=df0.clone(df0.getName())
        df.sub(lerp(i,0,max(df)))
        ds.setDataField(df)
    
    # create the surface repr
    rep=obj.createRepr(ReprType._volume,0,drawInternal=False,externalOnly=True)
    mgr.addSceneObjectRepr(rep)
    rep.applyMaterial(mat)
    rep.setVisible(False)
    
    # create the isosurface repr and value 0 in the activation field
    rep1=obj.createRepr(ReprType._isosurf,0,drawInternal=True,externalOnly=False,field=df0.getName(),valfunc='', vals='0', maxv=0.171321, numitervals=1,minv=-0.1712)
    mgr.addSceneObjectRepr(rep1)
    rep1.setVisible(False)
    
    reprs.append((rep,rep1)) # add the reprs to the list

reprs[0][0].setVisible(True) # need something visible for setCameraSeeAll() to do anything
mgr.setCameraSeeAll()
mgr.controller.zoom(-200) # zoom closer to mesh a little, might need to adjust this for different screens
mgr.setBackgroundColor(color(0,0,0,1.0))
mgr.setTimeStepsPerSec(30) # this many frames of data are played per elapsed second in real time
mgr.play()

################################################################################################
### Hide the UI
################################################################################################

@mgr.callThreadSafe # comment this line to disable UI hiding
def _hideUI():
    mgr.win.menuBar().setVisible(False)
    mgr.win.interfaceDock.setVisible(False)
    mgr.win.statusBar.setVisible(False)
    mgr.win.timeWidget.setVisible(False)
    mgr.win.setWindowState(Qt.WindowFullScreen)

################################################################################################
### Main event loop
################################################################################################

@asyncfunc
def serialReadLoop():
    '''Loops indefinitely reading the name from the serial device and setting the image visibility as appropriate.'''
    assert PORT, 'Port for serial device not found! Try replacing PORT with hard-coded string.'
    
    baser=rotator(vec3.Z(),sensorYaw)
    
    while(True): # loop forever, attempting to open the port again if it's lost at any time
        try:
            with serial.Serial(PORT,BAUD) as ser:
                printFlush('Starting serial read loop')
                while(True):
                    line=ser.readline().strip()
                    try:
                        x,y,z,w,a,b,c=map(float,line.split())
                        eulers=(baser*rotator(x,y,z,w)).getEulers()
                        #printFlush(x,y,z,w,r)
                        
                        # choose which representation is to be visible based on button presses
                        # 0=unpaced, 1=anterior, 2=lateral, 3=posterolateral 
                        if a and b and c:
                            index=0
                        elif not a:
                            index=1
                        elif not b:
                            index=2
                        elif not c:
                            index=3
                            
                        # set the visibility and rotation of each representation
                        for i,(r1,r2) in enumerate(reprs):
                            r1.setVisible(i==index)
                            r2.setVisible(i==index)
                            r1.setRotation(*eulers)
                            r2.setRotation(*eulers)
                            
                        #mgr.repaint()
                    except Exception as e:
                        printFlush('Cannot read line',repr(line))
                        printFlush(e)
                        if not line:
                            raise
        except:
            pass

################################################################################################                
### Start the read loop, this is the core functionality of this script
################################################################################################
p=serialReadLoop()      
