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
assert PORT, 'Port for serial device not found! Try replacing PORT with hard-coded string.'

# this setting for the serial port shouldn't need changing
BAUD=57600

# maps names to the filenames of images to load, expect names to be NORMAL, ATHLETE, HCM, DCM, FONTAN
namedFilenames={
####################################################
### TODO: fill this in to provide images to load ###
####################################################
}

# maps image names to tuples of image objects, keys must match the names emitted by the RFID reader
namedImages={}

# material to apply to all images
mat=mgr.createMaterial('DisplayMat')
mat.setSpectrumData([color(0,0,0),color()],[0,1],[vec3(0,0),vec3(1,1)])

################################################################################################
### Load image objects
################################################################################################

for name,filenames in namedFilenames.items():
    images=[]
    
    for f in filenames:
        obj=Nifti.loadObject(f)
        mgr.addSceneObject(obj)
        rep=obj.createRepr(ReprType._imgtimevolume,imgmat=mat)
        mgr.addSceneObjectRepr(rep)
        images.append(rep)
        rep.setVisible(False)
        
    namedImages[name]=images

################################################################################################
### Hide the UI
################################################################################################

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
p=serialReadLoop()      
