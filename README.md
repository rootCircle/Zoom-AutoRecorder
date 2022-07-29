## [Zoom AutoRecorder](https://microsoftlabs.github.io/Zoom-AutoRecorder/)

### Introduction
Zoom Recorder is free and open-source Python based GUI operated screen recorder and scheduler for zoom meetings.
It is complete rewrite of [AutoRecorder](https://github.com/Microsoftlabs/AutoRecorder) with added GUI and reduced bugs.

### Preview
![HomePage](https://raw.githubusercontent.com/Microsoftlabs/Zoom-AutoRecorder/main/docs/1.png)
![Service View Page](https://raw.githubusercontent.com/Microsoftlabs/Zoom-AutoRecorder/main/docs/2.png)
![Meeting Loading Page](https://raw.githubusercontent.com/Microsoftlabs/Zoom-AutoRecorder/main/docs/3.png)

### Download
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white"
     alt="Download from GitHub"
     height="60">](https://github.com/Microsoftlabs/Zoom-AutoRecorder/releases)


### Requirements
1. [OBS Studio](https://obsproject.com/) installed at default install location.

2. A scene in OBS Studio named "Zoom Meet" with recording set to Zoom Meeting screen with audio source and mic(If required). It is only required only for initial run not regularly. Just User don't have to interfere in "Zoom Meet" Profile afterwards
   
3. [Python v3](https://www.python.org/)

4. Python libraries : datetime, os, errno, sys, tkinter, PIL, time, sqlite3, subprocess, math, platform, webbrowser
  
   (All libraries except PIL,ttkthemes are installed by default in Python)
  
   PIL can be installed by using given commands in Terminal/CMD.
   ```markdown
   pip install pillow
   OR
   pip3 install pillow
   
   AND
   
   pip install ttkthemes
   OR
   pip3 install ttkthemes
   ```
  
5. [Zoom Meeting](https://zoom.us/) App Installed with disabled setting for camera on at autojoin and enabled for computer audio on autojoin.

### Notes
- Recording is supported right now only in Linux and Windows
- App hasn't been run on windows PC. So possible error may exists.
- It might be possible that bashCommand in LoadService.launchRecordingbyOBS may give error in terminal. User may need to manually modify it.
- Since recording through Linux is through Software Encoding, users may notice high CPU usage of OBS Studio. To fix it user may follow steps given in comments of main.py file.

### Build an executable
You can build your own executable by using pyinstaller or any other compiler that you like
- UNIX based Systems(Linux,MacOS etc)
```markdown
pyinstaller --noconsole --windowed --add-data "data:data" -i"data/icon.ico" --collect-submodules PIL main.py
```
- Windows
```markdown
pyinstaller --noconsole --windowed --add-data "data;data" -i"data/icon.ico" --collect-submodules PIL main.py
```

### ⚠ Warning
- Since it is in early development phase it might be possible that app may not work at all. Feel free to report any bugs if it exists.
- I admit that UI for loading Service screen is a bit unresponsive on starting service which may be resolved in later updates.

### Roadmap
1. Check if rejoin feature works
2. Debug the app
3. Make app feel more responsive

### Video
[<img src="https://i.ytimg.com/vi/Tu31bdrZyW0/hqdefault.jpg"
     alt="Zoom Recorder | Zoom Meeting Scheduler and Recorder | v0.3Alpha Walk-through | Python"
     height="250">](https://www.youtube.com/watch?v=Tu31bdrZyW0)

### Thanks!
