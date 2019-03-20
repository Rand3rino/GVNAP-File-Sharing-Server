from tkinter import *

gui = Tk()

# Window Title
gui.title('GV-NAPSTER Host')

# Labels for first section
Label(gui, text = 'Server Hostname').grid(row=0)
Label(gui, text = 'Username').grid(row=1)
Label(gui, text = 'Port').grid(row=0,column=2)
Label(gui, text = 'Hostname').grid(row=1,column=2)
Label(gui, text = 'Speed').grid(row=2)

# Declare and place textboxes for first section
entryServer = Entry(gui)
entryUsername = Entry(gui)
entryPort = Entry(gui)
entryHostname = Entry(gui)

entryServer.grid(row=0,column=1)
entryUsername.grid(row=1,column=1)
entryPort.grid(row=0,column=3)
entryHostname.grid(row=1,column=3)

# Label for middle section
Label(gui, text = 'Keyword').grid(row=4)
entryKeyword = Entry(gui)
entryKeyword.grid(row=4,column=1,pady=15)


#Label for last section
Label(gui, text = 'Enter Command').grid(row=6)
entryCommand = Entry(gui)
entryCommand.grid(row=6,column=1,pady=15)

# Listbox for speed selection
listboxSpeed = Listbox(gui, height=4)
listboxSpeed.insert(1, 'Modem')
listboxSpeed.insert(2, 'Ethernet')
listboxSpeed.insert(3, 'T1')
listboxSpeed.insert(4, 'T3')
listboxSpeed.grid(row=2,column=1)

# Add Connect Button
buttonConnect = Button(gui, text = 'Connect')
buttonConnect.grid(row=0,column=5)

# Add Go Button
buttonGo = Button(gui, text = 'Go')
buttonGo.grid(row=6, column=2)

gui.mainloop()
