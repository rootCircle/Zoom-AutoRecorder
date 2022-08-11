## [Zoom AutoRecorder](https://microsoftlabs.github.io/Zoom-AutoRecorder/)

### Introduction
Zoom Recorder is free and open-source Python based GUI operated screen recorder and scheduler for zoom meetings.
It is complete rewrite of [AutoRecorder](https://github.com/Microsoftlabs/AutoRecorder) with added GUI and reduced bugs.

### How to Use
1. Download the build/code from [here](https://github.com/Microsoftlabs/Zoom-AutoRecorder/releases).
2. Run the executable or the main.py file as per the case may be.
3. Install required libraries if you are using source code.
4. [Optional] Then you may make an excutable from the step given [here](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#build-an-executable).Then revert back to step 2.
5. Create a service by entering the details in app GUI.
     - In case of doubt you can watch the [walkthrough video](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#video). 
6. It is always recommended to test against a [Test Meeting](https://zoom.us/test) before joining a real meeting.
7. Make sure that step 1,2,5 of [requirements](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#requirements) are fulfilled.
8. In App GUI click on Load Service. It will show all the logs of service created in past.
9. Click Autoload Suitable Service.
10. Click Start Service and BOOM! You are ready to use this software like a champ!


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
     - You can do a simple Google Search to know how to create a Scene in OBS Studio.
   
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
- You can build your own executable by using pyinstaller, nuitka or any other [compiler](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_comparisons.html) that you like.
- First install all required python libraries as per fourth point given in the [instructions](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#requirements).
- Then install your favourite compiler using their documentation.
     - For pyinstaller use ```pip3 install pyinstaller``` or ```pip install pyinstaller```
     - For nuitka use ```pip3 install nuitka``` or ```pip install nuitka``` and then you need a [C compiler](https://nuitka.net/doc/user-manual.html#requirements) which is automatically downloaded on first run if absent.
- Open the Code directory in the File Explorer and open window powershell or terminal and run the given commands.
     - UNIX based Systems(Linux,MacOS etc)
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data:data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - Windows
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data;data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - Any OS(es) [Not Recommended to Novice Users] 
     {Unstable;Contains Bug}
          ```markdown
          python3 -m nuitka --standalone --nofollow-imports --remove-output --no-pyi-file --include-package=PIL --include-module=ttkthemes --output-dir=app_build --enable-plugin=tk-inter --onefile --include-data-dir=data=data --windows-icon-from-ico=data/icon.ico main.py
          ```
- Build will be created in dist directory if using pyinstaller and app_build/main.dist if Nuitka is used.
- Run
     - Nuitka on Windows or pyinstaller : Run main.exe or main
     - Nuitka on Linux based OS creates shared-library file named 'main' which can be run by opening the terminal in main.dist and typing ```./main```

### Workaround for Nuitka Build
After building the binary, copy 'ttkthemes' folder from site-packages folder(in lib directory) from your standard python installation location, to remove importing issue.
- To run the binary, open terminal in <Project-location>/app_build/main.dist directory then type and run main.exe or ./main depending on your OS.

- Running may give a error after the app window is closed.(Any Suggestion/Workaround on this are welcome)
     ```
     ............/zoomRecorder/app_build/main.dist/tkinter/__init__.py", line 4025, in __del__
     TypeError: catching classes that do not inherit from BaseException is not allowed
     )
     ```
- Novice Users are warned against using Nuitka build due to its comparatively more complex installation than pyinstaller and increased build size and present bugs in compiling the script on it.(Nuitka builds are performance-wise faster btw)

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
     
### Alternatives
- Warning - User discretion required! I don't any responsibility for any issues faced while using these alternatives.
  They are just for inormative purpose only. I personally haven't tested either of these except [AutoRecorder](https://github.com/SMazeikis/AutoRecorder).
- It is worth mentioning that some of these alternative work without using any 3rd party recording software, which is a really great feature to look on!
- Well Documented Repos
     - [OZ-Automatic-Recorder](https://github.com/tsamouridis/OZ-Automatic-Recorder)
     - [zoom-cli](https://github.com/tmonfre/zoom-cli)
     - [AutoZoomRecorder](https://github.com/Edward11235/AutoZoomRecorder)
     - [classRecorder](https://github.com/empobla/classRecorder)
     - [AutoRecorder](https://github.com/SMazeikis/AutoRecorder)
     - [zoom_recorder](https://github.com/nys99/zoom_recorder)
- Other Repos
     - [automaticZoomRecorder](https://github.com/NKPmedia/automaticZoomRecorder)
     - [zoom-recorder](https://github.com/rabimba/zoom-recorder)
     - [zoom-recorder](https://github.com/aykborstelmann/zoom-recorder)
     - [zoom-recorder](https://github.com/v1nc/zoom-recorder)
     - [ZoomRecorder](https://github.com/pantherman594/ZoomRecorder)
     - [zoom-meeting-recorder](https://github.com/cty012/zoom-meeting-recorder)
     - [automaticZoomRecorder](https://github.com/royjan/automaticZoomRecorder)
     - [Zoom-Meeting-Recorder](https://github.com/MJovanovic40/Zoom-Meeting-Recorder)
### Thanks!
