"""
Fixed scrolling in linux (cross compatible maybe)

"""

LOG_FILE_FOLDER = "res"
LOG_FILE = ""
"""
Creating Log
"""
try:
    from datetime import datetime, timedelta
    import os
    import errno

    try:
        os.makedirs(LOG_FILE_FOLDER)
    except OSError as er:
        if er.errno != errno.EEXIST:
            print(er)

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    LOG_FILE = os.path.join(LOG_FILE_FOLDER, "log.log")  # Log File init

    print(formatted_date, "============PROGRAM STARTS============", file=open(LOG_FILE, 'a'))
except Exception as e:
    print("ERROR", e)
    import sys

    sys.exit()
"""
Importing various libraries
"""
try:
    import tkinter as tk
    from tkinter import messagebox, Radiobutton, PhotoImage, StringVar, filedialog, ttk, simpledialog
    import tkinter.font as tkFont
    from PIL import Image, ImageTk
    import time
    import sqlite3
    import subprocess
    import math
    import platform
except Exception as ex:
    try:
        os.makedirs(LOG_FILE_FOLDER)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print(e)
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date, "Import Error\t", ex, file=open(LOG_FILE, 'a'))
    import sys

    sys.exit()

"""
Image Files Directories
"""
LOGOImgDir = os.path.join("data", "logonew.png")
DEFAULTIMAGEDir = os.path.join("data", "Additem.png")
HOMEPAGEImgDir = os.path.join("data", "logo.png")

CHOOSENMEETDATA = {}


class Apptools:

    def sqlite3_run(self, *sqlite_query):
        """
        The function will take multiple queries and output the result in
        form of list such that output of Query1 lies at index 0 ,Query2
        at index 1 and so on.
        """
        output = []
        try:
            sqliteConnection = sqlite3.connect("services.db")
            cursor = sqliteConnection.cursor()
            for arguments in sqlite_query:
                if isinstance(arguments, (list, tuple)):
                    if len(arguments) == 2:
                        query, val = arguments
                    else:
                        query = arguments[0]
                        val = ()
                else:
                    query = arguments
                    val = ()
                cursor.execute(query, tuple(val))
                sqliteConnection.commit()
                output.append(cursor.fetchall())
            cursor.close()
            return output
        except sqlite3.Error as error:
            print(error)
            messagebox.showwarning("Error", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()

    def image_Show(self, Dir, xrow, ycolumn, width, height, mode="grid", rspan=1, cspan=1, px=0, py=0):
        try:
            Photo = Image.open(Dir)
        except Exception as e:
            Apptools.writeLog(e)
            Photo = Image.open(DEFAULTIMAGEDir)
        Photo = Photo.resize((width, height))
        render = ImageTk.PhotoImage(Photo)
        img = tk.Label(self, image=render)
        img.image = render
        if mode == 'grid':
            img.grid(row=xrow, column=ycolumn, rowspan=rspan, columnspan=cspan, padx=px, pady=py, sticky="ns")
        else:
            img.place(x=xrow, y=ycolumn, relx=0, rely=0)

    def is_not_null(*text):
        if len(text) != 0:
            for msg in text:
                if msg == "" or (isinstance(msg, str) and msg.strip() == ""):
                    return False
            return True
        else:
            return False

    def check_digit(*text):
        try:
            for i in text:
                x = float(i)
            return True
        except Exception as e:
            return False

    def writeLog(msg):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        try:
            os.makedirs(LOG_FILE_FOLDER)
        except OSError as e:
            if e.errno != errno.EEXIST:
                Apptools.writeLog(e)
        f = open(LOG_FILE, 'a')
        print(formatted_date, msg, file=f)
        f.flush()
        f.close()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(CreateService)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class ScrollableFrame(ttk.Frame):

    def __init__(self, container, cw=775, ch=500, showscrlbar=True, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg="#333333", highlightthickness=0)
        self.canvas.config(scrollregion=(0, 0, 900, 1000))
        if showscrlbar:
            vscrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
            hscrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)

        s = ttk.Style()
        s.configure('TFrame', background='#333333')

        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self._canvasWidth = cw
        self._canvasHeight = ch
        self.canvas.config(width=self._canvasWidth, height=self._canvasHeight,
                           scrollregion=(0, 0, self._canvasWidth, self._canvasHeight))
        if showscrlbar:
            self.canvas.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)

        self.canvas.grid(row=0, column=0)
        if showscrlbar:
            vscrollbar.grid(row=0, column=1, rowspan=2, sticky='nse')
            hscrollbar.grid(row=1, column=0, sticky='wse')

            self.canvas.bind('<Enter>', self._bound_to_mousewheel)
            self.canvas.bind('<Leave>', self._unbound_to_mousewheel)

        return None

    def _bound_to_mousewheel(self, event):
        globals()['count'] = 0
        self.canvas.bind("<MouseWheel>", self.MouseWheelHandler)
        self.canvas.bind("<Button-4>", self.MouseWheelHandler)
        self.canvas.bind("<Button-5>", self.MouseWheelHandler)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind("<MouseWheel>")
        self.canvas.unbind("<Button-4>")
        self.canvas.unbind("<Button-5>")

    def MouseWheelHandler(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
            return
        self.canvas.yview_scroll(-1, "units")



class CreateService(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#333333")
        self.makeWidgets(master)

    def makeWidgets(self, master):
        Apptools.image_Show(self, HOMEPAGEImgDir, 0, 0, 300, 450, rspan=14)

        lbl = tk.Label(self, text="Zoom Auto Recorder")
        lbl.config(font=("Segoe UI", 30), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=1, column=1, columnspan=4, sticky='ew')

        lbl = tk.Label(self, text="Enter Details")
        lbl.config(font=("Segoe UI", 18), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=2, column=1, columnspan=4, pady=20, sticky='ew')

        lbl = tk.Label(self, text="Nickname")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=3, column=1, sticky='ew', pady=5, padx=5)

        nickname = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        nickname.grid(row=3, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Meeting ID")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=4, column=1, sticky='ew', pady=5, padx=5)

        meetID = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        meetID.grid(row=4, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Meeting Password")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=5, column=1, padx=5, sticky='ew', pady=5)

        meetPassword = tk.Entry(self, show="●", fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        meetPassword.grid(row=5, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Starting time\nhh:mm")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=6, column=1, sticky='ew', padx=5, pady=5)

        startTimeHour = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey', width=10)
        startTimeHour.grid(row=6, column=2, sticky='ew', padx=3)

        startTimeMinute = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey', width=10)
        startTimeMinute.grid(row=6, column=3, sticky='ew')

        lbl = tk.Label(self, text="Rejoin Time\nin min\n(If free user)")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=7, column=1, sticky='ew', padx=5, pady=5)

        rejoinInterval = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        rejoinInterval.grid(row=7, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Update frequency\nin min")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=8, column=1, sticky='ew', padx=5, pady=5)

        updateFrequency = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        updateFrequency.grid(row=8, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Warmup duration\nin min")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=9, column=1, sticky='ew', padx=5, pady=5)

        warmUpDuration = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        warmUpDuration.grid(row=9, column=2, sticky='ew', columnspan=2)

        lbl = tk.Label(self, text="Meeting Length\nin min")
        lbl.config(font=("Segoe UI", 12), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=10, column=1, sticky='ew', padx=5, pady=5)

        meetLength = tk.Entry(self, fg="#E8E8E8", bg="#333333", highlightcolor='grey')
        meetLength.grid(row=10, column=2, sticky='ew', columnspan=2)

        btn = tk.Button(self, text="Create Service",
                        command=lambda: self.createService(master, data={'nickname': nickname.get(),
                                                                         'meetID': meetID.get(),
                                                                         'meetPassword': meetPassword.get(),
                                                                         'startTimeHour': startTimeHour.get(),
                                                                         'startTimeMinute': startTimeMinute.get(),
                                                                         'rejoinInterval': rejoinInterval.get(),
                                                                         'updateFrequency': updateFrequency.get(),
                                                                         'warmUpDuration': warmUpDuration.get(),
                                                                         'meetLength': meetLength.get()}))
        btn.config(bg="#1F8EE7", padx=7, pady=3, fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=11, column=4, padx=15, pady=15, sticky='nw')

        btn = tk.Button(self, text="Create Service & Load",
                        command=lambda: self.createAndLoadService(master, data={'nickname': nickname.get(),
                                                                                'meetID': meetID.get(),
                                                                                'meetPassword': meetPassword.get(),
                                                                                'startTimeHour': startTimeHour.get(),
                                                                                'startTimeMinute': startTimeMinute.get(),
                                                                                'rejoinInterval': rejoinInterval.get(),
                                                                                'updateFrequency': updateFrequency.get(),
                                                                                'warmUpDuration': warmUpDuration.get(),
                                                                                'meetLength': meetLength.get()}))
        btn.config(bg="#1F8EE7", padx=7, pady=3, fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=12, column=1, columnspan=4, padx=15, pady=15, sticky='nsew')

        btn = tk.Button(self, text="Load Pre-created Services",
                        command=lambda: master.switch_frame(ViewService))
        btn.config(bg="#1F8EE7", padx=7, pady=3, fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=13, column=1, columnspan=4, padx=15, pady=15, sticky='nsew')

    def createService(self, master, data):
        isValidData = self.validateData(data)
        if isValidData == 1:
            if data["rejoinInterval"] is None:
                data["rejoinInterval"] = "0"
            if self.writeDataToStorage(master, data) is not None:
                messagebox.showinfo("Success", "Services created successfully!")
                return True

        else:
            if isValidData == 0:
                messagebox.showwarning("Warning", "Fill all the forms correctly")
            elif isValidData == -1:
                messagebox.showwarning("Warning", "Please enter valid numeral value")
            elif isValidData == -2:
                messagebox.showwarning("Warning", "Please enter valid time range")
            elif isValidData == -3:
                messagebox.showwarning("Warning", "Update frequency should be less than warmup time.")
            elif isValidData == -4:
                messagebox.showwarning("Warning", "Update frequency should be non zero.")
            elif isValidData == -5:
                messagebox.showwarning("Warning", "Invalid Meeting Length.")

    def validateData(self, data):
        for key in data.keys():
            if not (data[key] and Apptools.is_not_null(data[key])) and key != 'rejoinInterval':
                return 0
            elif (key not in ['meetPassword', 'nickname'] and not (data[key].isdigit())):
                if key == 'rejoinInterval' and not(data[key]):
                    continue
                return -1

        else:
            if not (0 <= int(data['startTimeHour']) < 24):
                return -2
            if not (0 <= int(data['startTimeMinute']) < 60):
                return -2
            if int(data['updateFrequency']) >= int(data['warmUpDuration']):
                return -3
            if int(data['updateFrequency']) == 0:
                return -4
            if int(data['meetLength']) <= 0:
                return -5
        return 1

    def writeDataToStorage(self, master, data):
        DEFAULTQUERY = "CREATE TABLE IF NOT EXISTS SERVICES(" \
                       "nickname TEXT NOT NULL," \
                       " meetID TEXT NOT NULL PRIMARY KEY," \
                       " meetPassword TEXT NOT NULL," \
                       " startTimeHour INT NOT NULL," \
                       " startTimeMinute INT Not Null," \
                       " rejoinInterval INTEGER NOT NULL," \
                       " updateFrequency INTEGER NOT NULL," \
                       " warmUpDuration INTEGER NOT NULL," \
                       " meetLength INTEGER NOT NULL);"

        QUERYF1 = "select meetID from SERVICES where meetID = ?;"
        out = Apptools.sqlite3_run(self, DEFAULTQUERY, (QUERYF1, (data['meetID'],)))
        if out is not None:
            if out[1] == []:
                QUERYF2 = "Insert into SERVICES (nickname, meetID, meetPassword, " \
                          "startTimeHour, startTimeMinute, rejoinInterval,updateFrequency," \
                          "warmUpDuration,meetLength) values(?,?,?,?,?,?,?,?,?);"
                return Apptools.sqlite3_run(self, (QUERYF2, data.values()))
            elif out[1]:
                messagebox.showwarning("Warning", "Duplicate Meeting ID!")

    def createAndLoadService(self, master, data):
        if self.createService(master, data):
            globals()['CHOOSENMEETDATA'] = data
            master.switch_frame(LoadService)


class ViewService(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#333333")
        self.makeWidgets(master)

    def makeWidgets(self, master):
        Apptools.image_Show(self, HOMEPAGEImgDir, 0, 0, 300, 450, rspan=10)

        lbl = tk.Label(self, text="Active Services")
        lbl.config(font=("Segoe UI", 30), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=0, column=1, sticky='ew')

        sep = ttk.Separator(self, orient='horizontal')
        sep.grid(row=1, column=1, sticky="ew")

        frame = ScrollableFrame(self, cw=400, ch=300)
        out = self.getDataFromStorage()
        if out:
            r = 0
            for data in out:
                mappedData = {'nickname': data[0],
                              'meetID': data[1],
                              'meetPassword': data[2],
                              'startTimeHour': data[3],
                              'startTimeMinute': data[4],
                              'rejoinInterval': data[5],
                              'updateFrequency': data[6],
                              'warmUpDuration': data[7],
                              'meetLength': data[8]}

                txt = "Nickname : " + mappedData['nickname'].title().strip()
                txt += "\nMeeting ID : " + mappedData['meetID']
                txt += "\nStarting Time : {0}:{1} Local Time".format(mappedData['startTimeHour'],
                                                                     mappedData['startTimeMinute'])
                txt += "\nMeeting Length : {0} min".format(mappedData['meetLength'])

                btn = tk.Button(frame.scrollable_frame, text=txt)
                btn.config(bg="#1F8EE7", padx=3, fg="#E8E8E8", bd=0, justify=tk.LEFT)
                btn.config(activebackground="#3297E9", font=("Segoe Print", 15))
                btn.grid(row=r, column=0, padx=10, pady=10, sticky="w")

                btn.config(command=lambda x=mappedData: self.framechange(master, x))
                r += 1

        else:
            lbl = tk.Label(frame.scrollable_frame, text="No Entry Found :-(")
            lbl.config(font=("Segoe Print", 30), fg="#E8E8E8", bg="#333333")
            lbl.grid(row=0, column=2, columnspan=4, padx=50, pady=50)

        frame.grid(row=2, column=1)

        btn = tk.Button(self, text="AutoLoad Suitable Service",
                        command=lambda: self.autoload(master, out))
        btn.config(bg="#1F8EE7", fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=3, column=1, padx=5, pady=10)

        lbl = tk.Label(self, text="Create Service")
        lbl.config(font=("Segoe UI", 15), fg="#E8E8E8", bg="#333333")
        lbl.config(cursor="hand2")
        lbl.bind("<Button-1>", lambda e: master.switch_frame(CreateService))
        lbl.grid(row=4, column=1, sticky="ew", pady=10)

    def autoload(self, master, out):
        if out:
            earliestCall = out[0]
            currentTime = datetime.now().time().hour * 60 + datetime.now().time().minute
            for data in out:
                startTimeData = int(data[3]) * 60 + int(data[4])
                endTimeData = startTimeData +int(data[8])

                startTimeEarliestCall = int(earliestCall[3]) * 60 + int(earliestCall[4])
                endTimeEarliestCall = startTimeEarliestCall + int(earliestCall[8])

                if endTimeData >= currentTime:
                    earliestCall = earliestCall if currentTime <= endTimeEarliestCall and \
                                                   startTimeEarliestCall < startTimeData else data

            endTimeEarliestCall = int(earliestCall[3]) * 60 + int(earliestCall[4]) + int(earliestCall[8])
            if endTimeEarliestCall >= currentTime:
                mappedData = {'nickname': earliestCall[0],
                              'meetID': earliestCall[1],
                              'meetPassword': earliestCall[2],
                              'startTimeHour': earliestCall[3],
                              'startTimeMinute': earliestCall[4],
                              'rejoinInterval': earliestCall[5],
                              'updateFrequency': earliestCall[6],
                              'warmUpDuration': earliestCall[7],
                              'meetLength': earliestCall[8]}
                globals()['CHOOSENMEETDATA'] = mappedData
                master.switch_frame(LoadService)
            else:
                messagebox.showinfo("Warning", "Services Expired\nCome tomorrow or create one!")
        else:
            messagebox.showwarning("Warning", "No Service Exists\nCreate One!")

    def getDataFromStorage(self):
        DEFAULTQUERY = "CREATE TABLE IF NOT EXISTS SERVICES(" \
                       "nickname TEXT NOT NULL," \
                       " meetID TEXT NOT NULL PRIMARY KEY," \
                       " meetPassword TEXT NOT NULL," \
                       " startTimeHour INT NOT NULL," \
                       " startTimeMinute INT Not Null," \
                       " rejoinInterval INTEGER NOT NULL," \
                       " updateFrequency INTEGER NOT NULL," \
                       " warmUpDuration INTEGER NOT NULL," \
                       " meetLength INTEGER NOT NULL);"

        QUERYF1 = "select * from SERVICES;"
        out = Apptools.sqlite3_run(self, DEFAULTQUERY, QUERYF1)
        if out is not None:
            return out[1]

    def framechange(self, master, data):
        globals()['CHOOSENMEETDATA'] = data
        master.switch_frame(LoadService)


class LoadService(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#333333")
        self.makeWidgets(master)

    def makeWidgets(self, master):
        lbl = tk.Label(self, text="Loading Meeting...")
        lbl.config(font=("Segoe UI", 30), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=0, column=0, sticky='ew')

        sep = ttk.Separator(self, orient='horizontal')
        sep.grid(row=1, column=1, sticky="ew")

        consoleText = "Initialising..."

        console = tk.Label(self, text=consoleText)
        console.config(font=("Segoe UI", 8), fg="#E8E8E8", bg="#333333")
        console.grid(row=2, column=0, sticky='nsew')

        lbl = tk.Label(self, text="Waiting for the meeting to start at time {0}:{1} LST .. ".
                       format(CHOOSENMEETDATA['startTimeHour'], CHOOSENMEETDATA['startTimeMinute']))
        lbl.config(font=("Segoe UI", 15), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=3, column=0, sticky='ew')

        txt = "Nickname : " + CHOOSENMEETDATA['nickname'].title().strip()
        txt += "\nMeeting ID : " + CHOOSENMEETDATA['meetID']
        txt += "\nStarting Time : {0}:{1} Local Time".format(CHOOSENMEETDATA['startTimeHour'],
                                                             CHOOSENMEETDATA['startTimeMinute'])
        txt += "\nMeeting Length : {0} min".format(CHOOSENMEETDATA['meetLength'])

        btn = tk.Button(self, text="Meeting Details:\n" + txt)
        btn.config(font=("Segoe UI", 15), fg="#E8E8E8", bg="#333333")
        btn.grid(row=5, column=0, sticky='ew')

        consoleText += "\n[Loading 10%] Create Zoom Link"
        console.config(text=consoleText)

        MeetLink = self.createMeetLink(CHOOSENMEETDATA['meetID'], CHOOSENMEETDATA['meetPassword'])
        if MeetLink:
            consoleText += "\n[Loading 20%] Zoom Link Created\n"+MeetLink
            console.config(text=consoleText)

            consoleText += "\n[Loading 30%] Computing Time Ranges for triggering Response"
            console.config(text=consoleText)

            timeRange = self.checkTimeRange(CHOOSENMEETDATA)

            if timeRange:
                consoleText += "\n[Loading 40%] Time Range Generated"
                console.config(text=consoleText)

                consoleText += "\n[Loading 50%] Validating Inputted Data"
                console.config(text=consoleText)

                consoleText += "\n[Loading 100%] Initialised Successfully\nClick Start Service!"
                console.config(text=consoleText)

            else:
                consoleText += "\n[Loading 30%] Oops Error Occurred while creating time range\nRetry Later"
                console.config(text=consoleText)
        else:
            consoleText += "\n[Loading 10%] Oops Error Occurred while creating Meet link\nRetry Later"
            console.config(text=consoleText)

        btn = tk.Button(self, text="Start Service",
                        command=lambda: self.service(MeetLink, timeRange, console, consoleText))
        btn.config(bg="#1F8EE7", fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=6, column=0, padx=5, pady=10)

        btn = tk.Button(self, text="Reload Page",
                        command=lambda: master.switch_frame(LoadService))
        btn.config(bg="#1F8EE7", fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=7, column=0, padx=5, pady=10)

        btn = tk.Button(self, text="Go to Home",
                        command=lambda: master.switch_frame(CreateService))
        btn.config(bg="#1F8EE7", fg="#E8E8E8", bd=0, activebackground="#3297E9")
        btn.grid(row=8, column=0, padx=5, pady=10)

    def service(self, MeetLink, timeRange, console, consoleText):
        if MeetLink and timeRange:
            consoleText += "\nInitialising Service"
            console.config(text=consoleText)
            currentTime = datetime.now().time().hour * 60 + datetime.now().time().minute
            while currentTime <= timeRange[0][1]:
                if currentTime >= timeRange[0][0]:
                    if self.launchMeeting(MeetLink, timeRange):
                        rejoinInterval = CHOOSENMEETDATA['rejoinInterval']
                        sleepDuration = int(rejoinInterval) \
                            if Apptools.check_digit(rejoinInterval) and int(rejoinInterval) >0 \
                            else int(CHOOSENMEETDATA['meetLength'])

                        time.sleep(sleepDuration * 60)
                    else:
                        updateFrequency = int(CHOOSENMEETDATA['updateFrequency'])
                        consoleText += "\nError! Retrying after some time" \
                                       "\nSleeping for another {} minutes".format(updateFrequency)
                        console.config(text=consoleText)
                        time.sleep(updateFrequency * 60)
                    currentTime = datetime.now().time().hour * 60 + datetime.now().time().minute
                    endTime = timeRange[0][1]
                    if currentTime >= endTime:
                        # os.system("taskkill /F /IM obs64.exe")
                        break
                else:
                    updateFrequency = int(CHOOSENMEETDATA['updateFrequency'])
                    consoleText += "\n Sleeping for another {} minutes".format(updateFrequency)
                    console.config(text=consoleText)
                    time.sleep(updateFrequency*60)
            else:
                consoleText += "\nOut of Service\nIf that's a possible error retry after some time"
                console.config(text=consoleText)

    def createMeetLink(self, meetID, meetPassword = ""):
        # Creates zoommtg link doesn't require browser permission (more safe.Hope so!)
        if isinstance(meetID, int) or (isinstance(meetID, str) and meetID.isdigit()):
            pass_param = "&pwd={}".format(meetPassword) if (meetPassword) else ""
            meeting_link = "zoommtg://zoom.us/join?action=join&confno={0}{1}".format(meetID, pass_param)
            return meeting_link

    # Adopted from: https://github.com/tmonfre/zoom-cli/blob/main/zoom_cli/utils.py
    def launchZoommtgUrl(self, url):
        command = ""
        if platform.system() == 'Darwin':
            command = "open"
        elif platform.system() == 'Linux':
            command = "xdg-open"
        elif platform.system() == 'Windows':
            command = "cmd /c start" #Not Sure About This Need Checking
            #If error replace command with 'start' and retry or use webbrowser one
        else:
            try:
                import webbrowser
                webbrowser.open(url)
            except:
                pass
            return
        os.system('{} "{}"'.format(command, url))

    def checkTimeRange(self, data):
        # Creates Possible time to trigger checking for Loading meeting
        startTimeHour = int(data['startTimeHour'])
        startTimeMinute = int(data['startTimeMinute'])
        rejoinInterval = int(data['rejoinInterval']) if Apptools.check_digit(data['rejoinInterval']) else 0
        warmUpDuration = int(data['warmUpDuration'])
        meetLength = int(data['meetLength'])

        startTime = startTimeHour*60 + startTimeMinute

        currentTime = datetime.now().time().hour * 60 + datetime.now().time().minute
        scriptStartTime = max(startTime - warmUpDuration, currentTime)

        EndTime = startTime + meetLength + warmUpDuration
        IdealStartTime = startTime - warmUpDuration
        checkAtTime = [[IdealStartTime, EndTime],
                       [(scriptStartTime // 60, scriptStartTime % 60)]]
        if rejoinInterval > 0:
            numberOfMeet = math.ceil(meetLength/int(rejoinInterval))
            for i in range(numberOfMeet):
                thatTime = startTime + (i+1)*rejoinInterval
                checkAtTime[1].append((thatTime // 60, thatTime % 60))

        return checkAtTime

    def launchMeeting(self, MeetLink, timeRange):
        consoleText = "Initialising Launch Service"
        serviceConsole = tk.Label(self, text=consoleText)
        serviceConsole.config(font=("Segoe UI", 8), fg="#E8E8E8", bg="#333333")
        serviceConsole.grid(row=3, column=0, sticky='nsew')

        currentTime = datetime.now().time().hour * 60 + datetime.now().time().minute
        if currentTime in range(timeRange[0][0] - 1, timeRange[0][1] + 1):
            consoleText += "\n Launching Meeting"
            serviceConsole.config(text=consoleText)
            self.launchZoommtgUrl(MeetLink)
            self.launchRecordingbyOBS()
            return True
        return False

    def launchRecordingbyOBS(self):
        lbl = tk.Label(self, text="Launching Recording...")
        lbl.config(font=("Segoe UI", 15), fg="#E8E8E8", bg="#333333")
        lbl.grid(row=3, column=0, sticky='ew')
        try:
            if platform.system() == 'Linux':
                bashCommand = 'env LIBGL_ALWAYS_SOFTWARE=1 obs --startrecording --multi --scene "Zoom Meet" --minimize-to-tray'
            elif platform.system() == 'Windows':
                bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording --multi --scene "Zoom Meet"'
            else:
                raise "Unsupported OS"
            os.system(bashCommand)
        except Exception as e:
            messagebox.showerror("Error",e)


# Main Program
if __name__ == "__main__":
    app = App()
    app.title("Kans:Your Shopping Partner")
    app.resizable(0, 0)
    app.update_idletasks()
    x_Left = int(app.winfo_screenwidth() / 4)
    app.geometry("+{}+{}".format(x_Left, 100))
    try:
        Icon = PhotoImage(file=LOGOImgDir)
        app.iconphoto(False, Icon)
    except Exception as e:
        Apptools.writeLog(e)
        Icon = PhotoImage(file=DEFAULTIMAGEDir)
        app.iconphoto(False, Icon)
    app.mainloop()