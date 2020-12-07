from digital_clock import *


def stopWatchCounter(label):
    def count():
        if stopWatchRunning:
            global stopWatchCounterTime
            if stopWatchCounterTime == 66600:
                display = 'Starting'
            else:
                t = datetime.datetime.fromtimestamp(stopWatchCounterTime)
                s = t.strftime('%H:%M:%S')
                display = s
            label.config(text = display)
            label.after(1000, count)
            stopWatchCounterTime+=1
    count()

def stopWatchController(type):
    if type =='start' or type == 'START':
        global stopWatchRunning

        stopWatchRunning = True
        stopWatchLabel.config(text='Stopwatch is running')
        stopWatchStartButton.config(state = 'disabled')
        stopWatchStopButton.config(state='normal')
        stopWatchResetButton.config(state='normal')
        stopWatchCounter(stopWatchTimeLable)
    elif type == 'stop':
        stopWatchRunning = False
        stopWatchLabel.config(text = 'Stopwatch stopped')
        stopWatchStartButton.config(state='normal')
        stopWatchStopButton.config(state='disabled')
        stopWatchResetButton.config(state='normal')

    else:
        global stopWatchCounterTime
        stopWatchRunning = False
        stopWatchCounterTime = 66600
        timeToStart = datetime.datetime.fromtimestamp(66600)

        stopWatchLabel.config(text='Stopwatch')
        stopWatchTimeLable.config(text = timeToStart.strftime('%H:%M:%S'))
        stopWatchStartButton.config(state='normal')
        stopWatchStopButton.config(state='disabled')
        stopWatchResetButton.config(state='disabled')





stopWatchLabel = L(stopWatchTab, font='arial 15 bold', text = 'Stopwatch', bg='#E8D6CF')
stopWatchLabel.pack(anchor = 'center')

timeToStart = datetime.datetime.fromtimestamp(66600)
stopWatchTimeLable = L(stopWatchTab, font='arial 30 bold', text = timeToStart.strftime('%H:%M:%S'), bg='#E8D6CF')
stopWatchTimeLable.pack(anchor = 'center')

buttonFrame = F(stopWatchTab)
buttonFrame.pack(anchor = 'center')

stopWatchStartButton = B(buttonFrame, text = 'Start', bg='#E8D6CF', command = lambda: stopWatchController('start'))
stopWatchStartButton.pack(side = LEFT)

stopWatchStopButton = B(buttonFrame, text = 'Stop', bg='#E8D6CF', command = lambda: stopWatchController('stop'))
stopWatchStopButton.pack(side = LEFT)

stopWatchResetButton = B(buttonFrame, text = 'Reset', bg='#E8D6CF', command = lambda: stopWatchController('reset'))
stopWatchResetButton.pack(side = LEFT)

stopWatchCounterTime = 66600
stopWatchRunning = False

