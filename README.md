## [Zoom AutoRecorder](https://microsoftlabs.github.io/Zoom-AutoRecorder/)

### Introduction
Zoom Recorder is a free and open-source Python-based GUI-operated screen recorder and scheduler for Zoom meetings.
It is a complete rewrite of [AutoRecorder](https://github.com/Microsoftlabs/AutoRecorder) with added GUI and reduced bugs, aimed at simplicity and ease of use while requiring minimal user-details and program configuration across all platforms.

### How to Use
1. Download the binary/code from [here](https://github.com/Microsoftlabs/Zoom-AutoRecorder/releases).
2. Run the executable or the main.py file as per the case may be.
3. [Optional] Install the required libraries if you are using source code.
     - Then you can make an executable from the step given [here](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#build-an-executable). Then revert to step 2.
4. Create a service by entering the details in the app's GUI homepage.
     - In case of doubt, you can watch the [walkthrough video](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#video).
5. It is always recommended to test against a [Test Meeting](https://zoom.us/test) before attending a real meeting.
6. Make sure that steps 1,2 & 5 of the [requirements](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#requirements) are fulfilled.
7. In App GUI, click on 'Load Pre-created Service'. It will show all the logs of services created in the past.
8. Then, click 'Autoload Suitable Service'.
9. Finally, click 'Start Service'.

BOOM! You are ready to use this software like a champ!

### Download
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white"
     alt="Download from GitHub"
     height="60">](https://github.com/Microsoftlabs/Zoom-AutoRecorder/releases)


### Requirements
1. [OBS Studio](https://obsproject.com/) is installed at the default installation location.

2. A scene in OBS Studio named "Zoom Meet" with a recording set to Zoom Meeting screen with audio source and mic(If required). It is required only for the initial run, not regularly. Users just don't have to interfere in the "Zoom Meet" Profile afterward.
     - You can do a simple Google Search to find out how to create a scene in OBS Studio.
   
3. [Python v3](https://www.python.org/)

4. Python libraries: datetime, os, errno, sys, tkinter, PIL, time, sqlite3, subprocess, math, platform, webbrowser
 
   (All libraries except PIL and ttkthemes are installed by default in Python)
 
   PIL can be installed by using given commands in Terminal/CMD.
   ```markdown
   pip install pillow ttkthemes
   OR
   pip3 install pillow ttkthemes
   ```
   
5. [Zoom Meeting](https://zoom.us/) App Installed with a disabled setting for the webcam at auto-join and enabled the setting for auto-join computer audio on joining the meeting.

### Notes
- Recording is supported right now only in Linux and Windows.
- The app hasn't been run on Windows OS. So possible errors may exist.
- It might be possible that bashCommand in LoadService.launchRecordingbyOBS may cause an error in the terminal. Users may need to manually modify it.
- Since recording through Linux is through Software Encoding, users may notice high CPU usage of OBS Studio. To fix it, the user may follow the steps given in the comments of the main.py file.

### Build an executable
- You can build your executable by using pyinstaller, Nuitka, or any other [compiler](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_comparisons.html) that you like.
- First, install all the required python libraries as per the 4th point given in the [instructions](https://github.com/Microsoftlabs/Zoom-AutoRecorder/edit/main/README.md#requirements).
- Then install your favorite compiler using their documentation.
     - For pyinstaller, run ```pip3 install pyinstaller``` or ```pip install pyinstaller```
     - For Nuitka, run ```pip3 install nuitka``` or ```pip install nuitka```, and then you need a [C compiler](https://nuitka.net/doc/user-manual.html#requirements) which will be automatically downloaded on the first run, if absent.
- Open the Code directory in the File Explorer and open the Windows PowerShell or terminal at that location and run the given commands.
     - UNIX-based Systems (Linux, macOS, etc.)
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data:data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - Windows
          ```markdown
          pyinstaller --noconsole --windowed --add-data "data;data" -i"data/icon.ico" --collect-submodules PIL main.py
          ```
     - Any OS(es) [Not Recommended to Novice Users]
     {Unstable; Contains Bug}
          ```markdown
          python3 -m nuitka --standalone --nofollow-imports --remove-output --no-pyi-file --include-package=PIL --include-module=ttkthemes --output-dir=app_build --enable-plugin=tk-inter --onefile --include-data-dir=data=data --windows-icon-from-ico=data/icon.ico main.py
          ```
- The Build will be created in the dist directory if using pyinstaller and app_build/main.dist if Nuitka is used.
- Run
     - Nuitka on Windows or pyinstaller: Run main.exe or main
     - Nuitka on Linux-based OS creates a shared-library file named 'main' which can be run by opening the terminal in main.dist and typing ```./main```

### Workaround for Nuitka Build
After building the binary, copy the 'ttkthemes' folder from the site-packages folder (in the lib directory) from your standard python installation location, to remove importing issues.
- To run the binary, open terminal in <Project-location>/app_build/main.dist directory, then type and run main.exe or ./main, depending on your OS.

- Running may cause an error after the app window is closed. (Any Suggestions/Workaround on this is welcome)
     ```
     ............/zoomRecorder/app_build/main.dist/tkinter/__init__.py", line 4025, in __del__
     TypeError: catching classes that do not inherit from BaseException is not allowed
     )
     ```
- Novice users are warned against using the Nuitka build because of its comparatively more complex installation than pyinstaller and increased build size and present bugs in compiling the script on it. (Nuitka builds are faster performance-wise, btw)

### ⚠ Warning
- Since the app is in the early development phase, it might be possible that it may not work at all. Feel free to report any bugs if they exist.
- The UI for loading the Service screen is a bit messy on starting the service, which may be resolved in later updates.

### Roadmap
1. Check if the rejoin feature works.
2. Debug the app.
3. Make the app feel more responsive.
4. Add a properties section to set up the recording service, key functions, etc.
5. Support for integrated screencast, as well as third-party recorders such as OBS and VLC (assistance needed!).
6. Better ease of use.
7. Removal of persistant loading screen Bug.

### Preview
[<img src="https://raw.githubusercontent.com/Microsoftlabs/Zoom-AutoRecorder/main/docs/screenshot_collage.jpg"
alt="Screenshot"
height="500">](https://github.com/Microsoftlabs/Zoom-AutoRecorder/tree/main/docs)
     
### Video
[<img src="https://i.ytimg.com/vi/Tu31bdrZyW0/hqdefault.jpg"
     alt="Zoom Recorder | Zoom Meeting Scheduler and Recorder | v0.3Alpha Walk-through | Python"
     height="250">](https://www.youtube.com/watch?v=Tu31bdrZyW0)
     
### Alternatives
- Warning - User discretion required! I don't take any responsibility for any issues faced while using these alternatives.
  They are just for informative purposes only. I have not tested either of these, except [AutoRecorder](https://github.com/SMazeikis/AutoRecorder).
- I also need to inform user that a few of below mentioned scripts may require sensitive info, including but not limited to, your zoom passwords etc. So proceed at your own risk only!
- It is worth mentioning that some of these alternatives work without using any 3rd party recording software, which is a great feature to look at!
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
