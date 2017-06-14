
Display Instructions
====================

There are two .bat files, one for each display. Double click on StartImageViewer.bat to start Eidolon with the setup for
the image display, and double click on StartModelViewer.bat to start with the model display. 

These scripts assume the Eidolon directory is found next to the current directory, ie. it tries to run ..\\Eidolon\\run.bat.

*** If Eidolon crashes or otherwise fouls up, close it and restart using the .bat files. ***

When starting the model display, the heart will need to be calibrated. It expects its initial orientation to be upright
and facing the display, hold the heart in this orientation then start the display by double clicking the .bat file.

The file ArdruinoDriversForWin7.zip contains the drivers for getting the Ardruino devices recognized as serial devices in
Windows 7. Extract the directory in this file and run setup.exe if you can't get the scripts to find the serial port.