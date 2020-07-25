from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry("500x600")

def saveFile():
    print(" ")
    
def clearFile():
    print(" ")

button1 = Button(root,text="Save",command=saveFile)
button1.place(x=10,y=10)

button2 = Button(root,text="Clear",command=clearFile)
button2.place(x=70,y=10)

mainloop()