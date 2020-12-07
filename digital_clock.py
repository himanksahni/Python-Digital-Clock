from tkinter import *
from tkinter import Frame as F, Label as L, Entry as E, Button as B
from tkinter.ttk import *
import datetime
import platform
try:
    import winsound
except:
    import os  
# create a 400x200 window
clockWindow = Tk()
clockWindow.title('Digital Clock')
clockWindow.geometry('400x200')
clockWindow.config(bg='#E8D6CF')

# create tabs
tabs = Notebook(clockWindow)
clockTab = F(tabs,width=400, height=200, bg='#E8D6CF')
tabs.add(clockTab,text = 'Clock')

stopWatchTab = F(tabs, bg='#E8D6CF')
tabs.add(stopWatchTab, text = 'Stop Watch')
#
alarmTab = F(tabs, bg='#E8D6CF')
tabs.add(alarmTab, text = 'Alarm')

timerTab = F(tabs, bg='#E8D6CF')
tabs.add(timerTab, text = 'Timer')

tabs.pack(expand=1, fill='both')
#Making clock


