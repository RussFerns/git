from tkinter import *
from imageDemo import ImageDemo

top = Tk()
app = ImageDemo(top)
label1 = Label(top, text="Demonstrates both bitmapped and PNG images").pack()
top.title("Image Demo")
top.minsize(800, 600)
top.mainloop()
