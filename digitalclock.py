import time
from tkinter import *
from tkinter import Label
import time as t

def time_current():
    a = time.strftime("%I::%M::%S %p")
    b = time.asctime()
    time_display.config(text = a)
    time_display.config(text=b)




    time_display.after(1,time_current)


tk_window = Tk()
tk_window.title("DIGITAL CLOCK")
time_display = Label(tk_window,font=("Calibri","60","bold"),
                      bg="yellow",fg="black")
time_display.pack()
time_current()



#wont be able see output without using mainloop function
tk_window.mainloop()
