# pylint cleanup stuff
mgr=mgr # pylint:disable=invalid-name,used-before-assignment
scriptdir=scriptdir # pylint:disable=invalid-name,used-before-assignment

import sys

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
BAUD=57600

# maps names to the filenames of images to load, expect names to be NORMAL, ATHLETE, HCM, DCM, FONTAN
namedFilenames={
        'NORMAL':('HEALTHY/sax_slice.mhd','HEALTHY/tags_slice1.mhd','HEALTHY/4dflow_mag_slice.mhd','HEALTHY/4dflow_phase_slice.mhd'),
        'ATHLETE':('ATHLETE/sax_slice.mhd','ATHLETE/tags_slice1.mhd','ATHLETE/4dflow_mag_slice.mhd','ATHLETE/4dflow_phase_slice.mhd'),
        'DCM':('DCM/sax_slice.mhd','DCM/tags_slice1.mhd','DCM/4dflow_mag_slice.mhd','DCM/4dflow_phase_slice.mhd'),
        'FONTAN':('FONTAN/sax_slice.mhd','FONTAN/tags_slice1.mhd'),
        'HCM':('HCM/sax_slice.mhd',)
}

transforms={
        'NORMAL':(
                transform(-217.555986,0.0,200.16079,1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(-232.481062,0.0,200.166145,1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(1020.764664,-0.183632,3730.137349,-1.0,1.0,-1.0,0.0,0.0,0.0,False),
                transform(980.0,-8.313213,1961.7812,-1.0,1.0,-1.0,0.0,0.0,0.0,False)
        ),
        'ATHLETE':(
                transform(-295.0,32.0,884.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(-437.0,32.0,890.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(125.0,-7.0,985.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),
                transform(423.0,-7.0,985.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False)
        ),
        'DCM':(
                transform(-608.0,95.0,593.0,-1.0,1.0,1.0,0.0,0.0,1.570795,False),
                transform(-764.0,96.0,574.0,-1.0,1.0,1.0,0.0,0.0,1.570795,False),
                transform(113.809857,75.748728,1037.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),
                transform(395.0,75.800167,1038.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False)
        ),
        'FONTAN':(
            transform(-538.0,44.0,537.0,1.0,1.0,1.0,0.0,0.0,0.0,False),
            transform(-685.0,44.0,554.0,1.0,1.0,1.0,0.0,0.0,0.0,False)
        ),
        'HCM':(
            transform(-524.0,99.0,601.0,-1.0,1.0,1.0,0.0,0.0,1.57079,False),
        )
}

# maps image names to tuples of image representation objects, keys must match the names emitted by the RFID reader
namedImages={}

# material to apply to all images
mat=mgr.createMaterial('DisplayMat')
mat.setGPUProgram('BaseImage',PT_FRAGMENT)
mat.setSpectrumData([color(0,0,0),color()],[0,1])

matphase=mgr.createMaterial('PhaseMat')
matphase.setGPUProgram('BaseImage',PT_FRAGMENT)
matphase.setSpectrumData([color(0,0,0),color()],[0.2,0.8]) # enhance the contrast by moving the black and white points inwards

################################################################################################
### Load image objects
################################################################################################

for name,filenames in namedFilenames.items():
    trans=transforms[name] if name in transforms else [transform()]*4
    namedImages[name]=[]
    
    for f,t in zip(filenames,trans):
        obj=MetaImg.loadObject('imagedata/'+f)
        mgr.addSceneObject(obj)
        
        rep=obj.createRepr(ReprType._imgtimestack,imgmat=matphase if 'phase' in f else mat)
        mgr.addSceneObjectRepr(rep)
        
        rep.setTransform(t) # set the image's transform as stored above
        rep.setVisible(name=='NORMAL') # make the normal images visible so that setCameraSeeAll works correctly

        namedImages[name].append(rep)        

mgr.setCameraSeeAll()
mgr.controller.zoom(-250) # zoom closer to images a little, might need to adjust this for different screens
mgr.setBackgroundColor(color(0,0,0,1.0))
mgr.play()

################################################################################################
### Hide the UI
################################################################################################

@mgr.callThreadSafe
def _hideUI():
    mgr.win.menuBar().setVisible(False)
    mgr.win.interfaceDock.setVisible(False)
    mgr.win.statusBar.setVisible(False)
    mgr.win.timeWidget.setVisible(False)
    #mgr.win.setWindowState(Qt.WindowFullScreen)

################################################################################################
### Main event loop
################################################################################################

@asyncfunc
def serialReadLoop():
    '''Loops indefinitely reading the name from the serial device and setting the image visibility as appropriate.'''
    assert PORT, 'Port for serial device not found! Try replacing PORT with hard-coded string.'
    
    while(True): # loop forever, attempting to open the port again if it's lost at any time
        try:
            with serial.Serial(PORT,BAUD) as ser: # establish serial connection, this should fail if device not present 
                printFlush('Starting serial read loop')
                
                while(True):
                    name=ser.readline().strip()
                    if name in namedImages:
                        # loop through all the images and set their visible to True if the name they are under matches the received name
                        for n,imgs in namedImages.items():
                            for i in imgs:
                                i.setVisible(n==name)
                    
                            # set the min and max timesteps to match the visible images so that they loop smoothly
                            if n==name:
                                mgr.timestepMin,mgr.timestepMax=minmax((i.getTimestepRange() for i in imgs),ranges=True)
                    else:
                        printFlush('Bad name: %r'%name)
                        if not name:
                            # this will force control flow to the outer loop which will attempt to establish a new connection
                            raise IOError('Connection lost') 
        except:
            pass
                

################################################################################################                
### Start the read loop, this is the core functionality of this script
################################################################################################
#p=serialReadLoop()      

@asyncfunc
def looptest():
    import time
    names=['NORMAL', 'ATHLETE', 'HCM', 'DCM', 'FONTAN']
    while(True):
        for name in names:
            time.sleep(5)
            printFlush(name)
            for n,imgs in namedImages.items():
                for i in imgs:
                    i.setVisible(n==name)
                    
                if n==name:
                    mgr.timestepMin,mgr.timestepMax=minmax((i.getTimestepRange() for i in imgs),ranges=True)
    
p=looptest()
    
        