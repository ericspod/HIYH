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
#assert PORT, 'Port for serial device not found! Try replacing PORT with hard-coded string.'

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
                transform(199.0,0.0,10.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(67.0,0.0,8.0,-1.0,1.0,1.0,0.0,0.0,0.0,False),
                transform(600.0,-34.0,123.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False),
                transform(863.0,-34.0,123.0,-1.0,1.0,-1.0,0.0,0.0,0.0,False)
        ),
}

# maps image names to tuples of image objects, keys must match the names emitted by the RFID reader
namedImages={}

# material to apply to all images
mat=mgr.createMaterial('DisplayMat')
mat.setGPUProgram('BaseImage',PT_FRAGMENT)
mat.setSpectrumData([color(0,0,0),color()],[0,1])

matphase=mgr.createMaterial('PhaseMat')
matphase.setGPUProgram('BaseImage',PT_FRAGMENT)
matphase.setSpectrumData([color(0,0,0),color()],[0.2,0.8])

################################################################################################
### Load image objects
################################################################################################

for name,filenames in namedFilenames.items():
    images=[]
    trans=transforms[name] if name in transforms else [transform()]*4
    
    for f,t in zip(filenames,trans):
        obj=MetaImg.loadObject('imagedata/'+f)
        mgr.addSceneObject(obj)
        rep=obj.createRepr(ReprType._imgtimestack,imgmat=matphase if 'phase' in f else mat)
        mgr.addSceneObjectRepr(rep)
        rep.setTransform(t)
        images.append(rep)
        #rep.setVisible(len(namedImages)==0) # for now set the first image series to be visible on startup
        
    namedImages[name]=images

################################################################################################
### Hide the UI
################################################################################################

#reprs[0][0].setVisible(True) # need something visible for setCameraSeeAll() to do anything
mgr.setCameraSeeAll()
#mgr.controller.zoom(-200) # zoom closer to mesh a little, might need to adjust this for different screens
#mgr.setBackgroundColor(color(0,0,0,1.0))
mgr.play()

#@mgr.callThreadSafe
def _hideUI():
    mgr.win.menuBar().setVisible(False)
    mgr.win.interfaceDock.setVisible(False)
    mgr.win.statusBar.setVisible(False)
    mgr.win.setWindowState(Qt.WindowFullScreen)
    mgr.win.timeWidget.setVisible(False)

################################################################################################
### Main event loop
################################################################################################

@asyncfunc
def serialReadLoop():
    '''Loops indefinitely reading the name from the serial device and setting the image visibility as appropriate.'''
    while(True): # loop forever, attempting to open the port again if it's lost at any time
        try:
            with serial.Serial(PORT,BAUD) as ser:
                printFlush('Starting serial read loop')
                while(True):
                    line=ser.readline().strip()
        #            if line[:2]=='\x03\x02': # check the header of each line, if this isn't the check byte pair then skip
                    if line in namedImages:
                        name=line[2:]
                        
                        # loop through all the images and set their visible to True if the name they are under matches the received name
                        for n,imgs in namedImages.items():
                            for i in imgs:
                                i.setVisible(n==name)
                    else:
                        printFlush('Bad name: %r'%line)
                        if not line:
                            raise IOError('Connection lost')
        except:
            pass
                

################################################################################################                
### Start the read loop, this is the core functionality of this script
################################################################################################
#p=serialReadLoop()      
