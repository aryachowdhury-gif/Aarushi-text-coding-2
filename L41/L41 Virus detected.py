from tkinter import *
from tkinter import messagebox

#ceate window
window = Tk()
window.title("Virus Detected")
window.geometry("250x250")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found")

#add widgets
btn = Button(window, text="Scan for Virus", command=msg)
btn.place(x=75, y=80)

window.mainloop()