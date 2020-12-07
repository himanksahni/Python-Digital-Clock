from digital_clock import *

timerLabel = L(timerTab, font='arial 15 bold', text = 'Timer', bg='#E8D6CF')
timerLabel.pack(anchor = 'center')

timerEntryFrame = F(timerTab)
timerEntryFrame.pack(anchor = 'center')

timerEntryMessage = L(timerEntryFrame, font='arial 15 bold', text = 'Enter time:', bg='#E8D6CF')
timerEntryMessage.pack(side = LEFT)
timerEntry = E(timerEntryFrame, font='arial 15 bold', bg='#FFFFFF')
timerEntry.pack(side = RIGHT)


buttonFrame = F(timerTab)
buttonFrame.pack(anchor = 'center', side = BOTTOM)

timerStartButton = B(buttonFrame, text = 'Start', bg='#E8D6CF')
timerStartButton.pack(side = LEFT)

timerStopButton = B(buttonFrame, text = 'Stop', bg='#E8D6CF', state = 'disabled')
timerStopButton.pack(side = LEFT)

timerResetButton = B(buttonFrame, text = 'Reset', bg='#E8D6CF', state = 'disabled')
timerResetButton.pack(side = LEFT)


clockWindow.mainloop()