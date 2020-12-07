from digital_clock import *

def convertToTimeStamp(time):
    hour, min, sec = time.split(':')
    return ((int(hour) * 60) + int(min))* 60 + int(sec)

def timerCounter(timerLabel):
    def count():
        global timerCounterTime
        if timerRunning:
            if timerCounterTime == 0:
                display = 'Time is up'
                timerController('reset')
            else:
                t = datetime.timedelta(seconds = timerCounterTime)
                display = t
            timerLabel.config(text=display)
            timerLabel.after(1000, count)
            timerCounterTime -= 1

        else:
            return
    count()

def timerController(type):
    global timerRunning, timerCounterTime
    if type =='start' or type == 'START':
        timerRunning = True
        timerLabel.config(text='Timer is running')
        timerStartButton.config(state = 'disabled')
        timerStopButton.config(state='normal')
        timerResetButton.config(state='normal')
        timerCounterTime =  convertToTimeStamp(timerEntry.get()) if timerCounterTime == 0 else timerCounterTime
        timerEntry.config(state='disabled')

        timerCounter(timerTimeLable)
    elif type == 'stop':
        timerRunning = False
        timerLabel.config(text = 'Timer stopped')
        timerStartButton.config(state='normal')
        timerStopButton.config(state='disabled')
        timerResetButton.config(state='normal')
        timerEntry.config(state = 'disabled')

    else:
        timerRunning = False
        timerCounterTime = 0
        timeToStart = datetime.timedelta(seconds = 0)

        timerLabel.config(text='Timer')
        timerTimeLable.config(text = timeToStart)
        timerStartButton.config(state='normal')
        timerStopButton.config(state='disabled')
        timerResetButton.config(state='disabled')
        timerEntry.config(state='normal')


timerLabel = L(timerTab, font='arial 15 bold', text = 'Timer', bg='#E8D6CF')
timerLabel.pack(anchor = 'center')

timerEntryFrame = F(timerTab)
timerEntryFrame.pack(anchor = 'center')

timerEntryMessage = L(timerEntryFrame, font='arial 15 bold', text = 'Enter time:', bg='#E8D6CF')
timerEntryMessage.pack(side = LEFT)
timerEntry = E(timerEntryFrame, font='arial 15 bold', bg='#FFFFFF')
timerEntry.pack(side = RIGHT)

timeToStart = datetime.timedelta(seconds = 0)
timerTimeLable = L(timerTab, font='arial 30 bold', text = timeToStart, bg='#E8D6CF')
timerTimeLable.pack(anchor = 'center')


buttonFrame = F(timerTab)
buttonFrame.pack(anchor = 'center')

timerStartButton = B(buttonFrame, text = 'Start', bg='#E8D6CF', command = lambda: timerController('start'))
timerStartButton.pack(side = LEFT)

timerStopButton = B(buttonFrame, text = 'Stop', bg='#E8D6CF', state = 'disabled', command = lambda: timerController('stop'))
timerStopButton.pack(side = LEFT)

timerResetButton = B(buttonFrame, text = 'Reset', bg='#E8D6CF', state = 'disabled', command = lambda: timerController('reset'))
timerResetButton.pack(side = LEFT)


timerCounterTime = 0
timerRunning = False