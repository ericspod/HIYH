
Display Instructions
====================

The display machines should be setup to run Eidolon using Anaconda2 4.1.1 with the Arduino drivers. Eidolon and this directory
are checked out from Github using the Github Desktop client, but Anaconda and the drivers must be installed.

Setup procedure (should already be done):
 1. Install Anaconda2 4.1.1 from https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86_64.exe
 2. Install Github Desktop from https://desktop.github.com/
 3. Checkout https://github.com/ericspod/HIYH and https://github.com/ericspod/Eidolon to the desktop
 4. Follow the instructions in HIYH/ArduinoDriversForWin7.zip to install the USB drivers.
    This contains the drivers for getting the Arduino devices recognized as serial devices in
    Windows 7. Extract the directory in this file and run setup.exe if you can't get the scripts to find the serial port.
    Don't worry if Windows complains about the device potentially not being installed properly, just say the device is working fine.

Starting displays:
 There are two .bat files, one for each display, run one of these depending on which machine you're on:
  * Double click on StartImageViewer.bat to start Eidolon with the setup for the image display
  * Double click on StartModelViewer.bat to start with the model display 

These scripts assume the Eidolon directory is found next to the current directory, ie. it tries to run ..\\Eidolon\\run.bat.

*** If Eidolon crashes or otherwise fouls up, close it and restart using the .bat files. ***

When starting the model display, the heart will need to be calibrated. It expects its initial orientation to be upright
and facing the display, hold the heart in this orientation then start the display by double clicking the .bat file.
***More info to follow on this***
