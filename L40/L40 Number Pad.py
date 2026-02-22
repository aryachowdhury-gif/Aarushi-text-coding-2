from tkinter import *

window = Tk()
window.title("Numer Pad")
window.geometry("250x300")

#create the numer grid
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ["#", 0, "*"]]

#configure row and columns to resize window
for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)


for i in range(4):
    for j in range(3):
        new_frame = Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=1,
            bg="purple"
        )

        new_frame.grid(row=i, column=j, sticky="nsew")

        lable2 = Label(master=new_frame, text=nums[i][j], bg="pink", font=("Arial", 18))
        lable2.pack(expand=True, fill="both", padx=5, pady=5)

window.mainloop()