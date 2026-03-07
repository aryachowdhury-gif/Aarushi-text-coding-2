from tkinter import *

#create window
window = Tk()
window.title("main")
window.geometry("250x250")

#function to open new (Top Level) window
def topwin():
    top = Toplevel()
    top.geometry("150x150")
    top.title("toplevel")

    #addig a lable widget to Top Window
    L2 = Label(top, text = "This is top level window")
    L2.pack()

    top.mainloop()

#adding a label and button widget to window (Main) window
L = Label(window, text = "This is Main Window")
btn = Button(window, text = "Click here to open top window", command = topwin)

#arrange widgets
L.pack()
btn.pack()

window.mainloop()