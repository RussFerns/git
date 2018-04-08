from tkinter import *
import tkinter.messagebox as tmb

root = Tk()
root.minsize(400, 200)
root.title("Message Box Demo")

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side': LEFT, 'padx': 4, 'pady': 10}


Label(fr1, text="Demo of tkinter.messagebox").pack()
Button(fr1, text='Hello', command=lambda: tmb.showinfo(
    "Hello", "Hello World!")).pack(opt)
Button(fr1, text='Info', command=lambda: tmb.showinfo(
    "Show Info", "Informational Message")).pack(opt)
Button(fr1, text='Warning', command=lambda: tmb.showwarning(
    "Show Warning", "Warning Message!")).pack(opt)
Button(fr1, text='error', command=lambda: tmb.showerror(
    "Show Error", "Error!!!!!")).pack(opt)
Button(fr1, text='Question', command=lambda: tmb.askquestion(
    "Ask Question", "Can you read this ?")).pack(opt)
Button(fr2, text='OK, Cancel', command=lambda: tmb.askokcancel(
    "Ask OK Cancel", "Say Ok or Cancel?")).pack(opt)
Button(fr2, text='Yes/No', command=lambda: tmb.askyesno(
    "Ask Yes-No", "Say yes or no?")).pack(opt)
Button(fr2, text='Yes/No/Cancel', command=lambda: tmb.askyesnocancel(
    "Yes-No-Cancel", "Say yes no cancel")).pack(opt)
Button(fr2, text='Retry/Cancel', command=lambda: tmb.askretrycancel(
    "Ask Retry Cancel", "Retry or what?")).pack(opt)


fr1.pack()
fr2.pack()

root.mainloop()