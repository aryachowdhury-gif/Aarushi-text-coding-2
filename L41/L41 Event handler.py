from tkinter import *

#create window
window = Tk()
window.title("Event Handler")
window.geometry("250x250")

#event handler for Keypress
def handler_keypress(event):
    print(event.char)

#bind keypress event to handle_keypress()
window.bind("<Key>", handler_keypress)

#event handler for button click
def handler_click(event):
    print("the button was clicked!")

#add widget
button = Button(text="Click me!")
button.pack()

#bind click event to handler_click()
button.bind("<Button-1>", handler_click)

window.mainloop()