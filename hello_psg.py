import tkinter
import tkinter as tkMessageBox

top = tkinter.Tk()


def helloCallBack():
    tkMessageBox.showinfo("Welcome Adventurer", "Hello World")


B = tkinter.Button(top, text="TreasureChest", command=helloCallBack)

B.pack()
top.mainloop()
