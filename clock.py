from digital_clock import *

#Creating clock functionality
timeLabel = L(clockTab, font = 'arial 40 bold', foreground ='black', bg='#E8D6CF')
timeLabel.pack(anchor = 'center')

dateLabel = L(clockTab, font = 'arial 40 bold', foreground = 'black', bg='#E8D6CF')
dateLabel.pack(anchor = 's')

def clockControl():
    dateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time = dateTime.split()
    hourMinSec, amPm = time.split('/')
    hour, min, sec = hourMinSec.split(':')
    if int(hour) > 12 and int(hour) < 24:
        time = str(int(hour) - 12) + ':' + min + ':' + sec + ' ' + str(amPm)
    else:
        time = hourMinSec + ' ' + amPm
    timeLabel.config(text=time)
    dateLabel.config(text=date)
    timeLabel.after(1000, clockControl)

clockControl()