from tkinter import *


def quit_application():
    root.destroy()


root = Tk()
root.title("Calculator")
root.minsize(150, 330)
root.configure(background='darkorchid3')

# connecting to the external styling optionDB.txt
root.option_readfile('optionDB.txt')

# widget specific styling
text = Text(root, background='black', foreground="white", borderwidth=16, relief='sunken', width=17, height=5)
text.insert(END, "Fern Technologies\n================\nScientific Calc.")
text.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# all the below widgets derive their styling from optionDB.txt file
Button(root, text='*' ).grid(row=1, column=1)
Button(root, text='^' ).grid(row=1, column=2)
Button(root, text='#' ).grid(row=1, column=3)
Button(root, text='<' ).grid(row=2, column=1)
Button(root, text='OK', cursor='target').grid(row=2, column=2)#changing cursor style
Button(root, text='>').grid(row=2, column=3)
Button(root, text='+' ).grid(row=3, column=1)
Button(root, text='v' ).grid(row=3, column=2)
Button(root, text='-' ).grid(row=3, column=3)
for i in range(10):
    Button(root, text=str(i)).grid(column=3 if i%3==0 else (1 if i%3==1 else 2), row= 4 if i<=3  else (5 if i<=6 else 6))

quit_button = Button(root, text="Quit", command=quit_application, padx=5, pady=5).place(x=60, y=300)

root.mainloop()
