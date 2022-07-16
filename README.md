## Zoom AutoRecorder

### Introduction
Zoom Recorder is free and open-source Python based GUI operated screen recorder and scheduler for zoom meetings.
It is complete rewrite of [AutoRecorder](https://github.com/Microsoftlabs/AutoRecorder) with added GUI and reduced bugs.

### Preview
![HomePage](https://github.com/Microsoftlabs/Zoom-AutoRecorder/blob/gh-pages/1.png)
![Service View Page](https://github.com/Microsoftlabs/Zoom-AutoRecorder/blob/gh-pages/2.png)
![Meeting Loading Page](https://github.com/Microsoftlabs/Zoom-AutoRecorder/blob/gh-pages/3.png)


### Requirements
1. [OBS Studio](https://obsproject.com/) installed at default install location.

2. A scene in OBS Studio named "Zoom Meet" with recording set to Zoom Meeting screen with audio source and mic(If required). It is only required only for initial run not regularly. Just User don't have to interfere in "Zoom Meet" Profile afterwards
   
3. [Python v3](https://www.python.org/)

4. Python libraries : datetime, os, errno, sys, tkinter, PIL, time, sqlite3, subprocess, math, platform, webbrowser
  
   (All libraries except PIL are installed by default in Python)
  
   PIL can be installed by using given commands in Terminal/CMD.
   ```markdown
   pip install pillow
   OR
   pip3 install pillow
   ```
  
5. [Zoom Meeting](https://zoom.us/) App Installed

### Notes
- Recording is supported right now only in Linux and Windows
- App hasn't been run on windows PC. So possible error may exists.
- It might be possible that bashCommand in LoadService.launchRecordingbyOBS may give error in terminal. User may need to manually modify it.
- Since recording through Linux is through Software Encoding, users may notice high CPU usage of OBS Studio. To fix it user may follow steps given in comments of main.py file.

### Build an executable
You can build your own executable by using pyinstaller or any other compiler that you like
```markdown
pyinstaller --noconsole --windowed main.py
```

### :warning: Warning
- Since it is in early development phase it might be possible that app may not work at all. Feel free to report any bugs if it exists.
- I admit that UI for loading Service screen is a bit unresponsive on starting service which may be resolved in later updates.

### Roadmap
1. Check if rejoin feature works
2. Debug the app
3. Make app feel more responsive

### Thanks!
