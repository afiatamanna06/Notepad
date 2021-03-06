from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry("500x600")

def saveFile():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    
def clearFile():
    entry.delete(1.0,END)
    
def openFile():
    file = filedialog.askopenfile(mode='r',filetypes=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        print(content)
    entry.insert(INSERT,content)

button1 = Button(root,text="Save",command=saveFile)
button1.place(x=10,y=10)

button2 = Button(root,text="Clear",command=clearFile)
button2.place(x=70,y=10)

button3 = Button(root,text="Open",command=openFile)
button3.place(x=138,y=10)

entry = Text(root,height=48,width=68,wrap=WORD)
entry.place(x=10,y=50)

mainloop()