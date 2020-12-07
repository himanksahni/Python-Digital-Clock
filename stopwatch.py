from digital_clock import *

stopWatchLabel = L(stopWatchTab, font='arial 30 bold', text = 'Stopwatch', bg='#E8D6CF')
stopWatchLabel.pack(anchor = 'center')

buttonFrame = F(stopWatchTab)
buttonFrame.pack(anchor = 'center')

stopWatchStartButton = B(buttonFrame, text = 'Start', bg='#E8D6CF')
stopWatchStartButton.pack(side = LEFT)

stopWatchStopButton = B(buttonFrame, text = 'Stop', bg='#E8D6CF')
stopWatchStopButton.pack(side = LEFT)

stopWatchResetButton = B(buttonFrame, text = 'Reset', bg='#E8D6CF')
stopWatchResetButton.pack(side = LEFT)

stopWatchCounter = 66600
stopWatchrunning = False