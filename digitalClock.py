from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('Digital Clock: Reboot13')


def clock():
    time = strftime('%H:%M:%S %p')
    label.config(text = time)
    label.after(1000, clock)

label = Label(root, font = ('sans', 50), background = 'black', foreground = 'blue')    

label.pack(anchor = 'center')


clock()
mainloop()