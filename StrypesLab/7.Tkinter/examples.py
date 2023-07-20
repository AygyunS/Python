from tkinter import *

root = Tk()


def myClick():
    hello = "Hello" + e.get()
    myLabel2 = Label(root, text=hello)
    myLabel2.grid(row=1, column=0, padx=20)

myLabel1 = Label(root, text='Hello World')


myLabel1.grid(row=0, column=0, padx=10)



myButton = Button(root, text="Click me!", command=myClick)
myButton.grid(row=3, column=0, padx=50, pady=50)



e = Entry(root)
e.insert(0, 'Enter your name: ')
e.grid(row=2, column=0)


root.mainloop()
