from tkinter import *

#create window
window = Tk()
window.title("Login App")
window.geometry("400x400")

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulation for you new account!"
    res.insert(END, greet)
    res.insert(END, name)

#create widgets
new_frame = Frame(master=window, height=200, width=360, bg="#ff006f")

LbL1 = Label(new_frame, text="Full Name", bg="green", fg="white", width=12)
LbL2 = Label(new_frame, text="Email ID", bg="green", fg="white", width=12)
LbL3 = Label(new_frame, text="Enter Password", bg="green", fg="white", width=12)

name_entry = Entry(new_frame)
email_entry = Entry(new_frame)
pass_entry = Entry(new_frame)

res = Text(bg="white", fg="black")

btn = Button(text="Create Account", command=display, bg="red", fg="yellow")

#arrange all widgets
new_frame.place(x=20, y=0)

LbL1.place(x=150, y=20)