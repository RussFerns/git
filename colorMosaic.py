from tkinter import *


def quit_application():
    print("...quiting")
    root.destroy()


root = Tk()
root.title("Color mosaic")
root.minsize(600, 400)


Label(root, text='A beautiful color mosaic using Tkinter').pack()

frame_violet = Frame(root, bg='darkviolet', width=100, height=50).pack(fill=X)
frame_indigo = Frame(root, bg='blue2', width=100, height=50).pack(fill=X)
frame_blue = Frame(root, bg='royalblue1', width=100, height=50).pack(fill=X)
frame_green = Frame(root, bg='seagreen', width=100, height=50).pack(fill=X)
frame_yellow = Frame(root, bg='gold2', width=100, height=50).pack(fill=X)
frame_orange = Frame(root, bg='tomato', width=100, height=50).pack(fill=X)
frame_red = Frame(root, bg='red3', width=100, height=50).pack(fill=X)


quit_button = Button(root, text="Quit", command=quit_application).pack(padx=5, pady=5)

root.mainloop()
