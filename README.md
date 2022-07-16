Zoom Recorder is free and open-source Python based GUI operated screen recorder and scheduler for zoom meetings.

# Requirements
1> OBS Studio at default install position

2> A scene in OBS named "Zoom Meet" with recording set to zoom screen with audio source and mic(if required)
   It is only required only for initial run not regularly.
   Just User don't have to interfere in "Zoom Meet" Profile afterwards
   
3> Python v3

4> Python libraries : datetime, os, errno, sys, tkinter, PIL, time, sqlite3, subprocess, math, platform, webbrowser
  (All libraries except PIL are installed by default in Python)
  PIL can be installed by
  pip install pillow
  OR
  pip3 install pillow
  in Terminal/CMD
  
5> Zoom meeting Installed

# Notes
1> Recording is supported right now only in linux

2> App hasn't been run on windows PC. So possible error may exists

3> It might be possible that bashCommand in LoadService.launchRecordingbyOBS 
   may give error in terminal. User may need to manually modify it.

# Build an executable
You can build your own executable by using pyinstaller or any other compiler that you like

# ⚠Warning
Since it is in early development phase it might be possible that app may not work at all. Feel free to report any bugs if it exists.

I admit that UI for loading Service screen is a bit unresponsive on starting service which may be resolved in later updates.

# Roadmap
1> Check if rejoin feature works
2> Debug the app
3> Make app feel more responsive

## Thanks!
