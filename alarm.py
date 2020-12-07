from digital_clock import *
# from clock import *


def alarm():
    currTime, currAmPm = datetime.datetime.now().strftime('%H:%M %p').split(' ')
    currHour, currMin = currTime.split(':')

    alarmTime, alarmAmPm = alarmEntry.get().split(' ')
    alarmHour, alarmMin =  alarmTime.split(':')

    if int(currHour) > 12 and int(currHour) < 24:
        currHour = str(int(currHour) - 12)

    if int(currHour) == int(alarmHour) and int(currMin) == int(alarmMin):
        alarmStatusLabel.config(text = 'Alarm is ringing')
        for i in range(5):
            if platform.system() == 'Windows':
                winsound.Beep(5000,1000)
            else:
                os.system('say "Alarm Ringing"')

        alarmEntry.config(state='normal')
        setAlarmButton.config(state='normal')
        alarmEntry.delete(0, END)
        return
    else:
        alarmStatusLabel.config(text = 'Alarm has started')
        alarmEntry.config(state = 'disabled')
        setAlarmButton.config(state = 'disabled')

    alarmStatusLabel.after(1000, alarm)



alarmEntry = E(alarmTab, font = 'arial 20 bold', bg='#E8D6CF')
alarmEntry.pack(anchor = 'center')

alarmLabel = L(alarmTab, font = 'arial 15 bold', text ='Make an alarm', bg='#E8D6CF')
alarmLabel.pack(anchor = 's')

alarmStatusLabel = L(alarmTab, font = 'arial 15 bold', bg='#E8D6CF')
alarmStatusLabel.pack(anchor='s')

setAlarmButton = B(alarmTab, text = 'Set alarm', command = alarm, bg='#E8D6CF')
setAlarmButton.pack(anchor = 's')