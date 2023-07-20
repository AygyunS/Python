import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.memory = 0

        self.display = tk.Entry(master, width=30, justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button(".", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("AC", 5, 0)
        self.create_button("(", 5, 1)
        self.create_button(")", 5, 2)
        self.create_button("DEL", 5, 3)
        self.create_button("CE", 6, 0)
        self.create_button("mc", 6, 1)
        self.create_button("m+", 6, 2)
        self.create_button("m-", 6, 3)
        self.create_button("mr", 7, 1)
        self.create_button("+/-", 4, 0)
        self.create_button("sqrt", 5, 0)
        self.create_button("!", 6, 1)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=10, pady=5, font=("Arial", 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "AC":
            self.display.delete(0, tk.END)
        elif text == "DEL":
            self.display.delete(len(self.display.get())-1, tk.END)
        elif text == "CE":
            self.display.delete(0, tk.END)
        elif text == "mc":
            self.memory = 0
        elif text == "m+":
            self.memory += float(self.display.get())
            self.display.delete(0, tk.END)
        elif text == "m-":
            self.memory -= float(self.display.get())
            self.display.delete(0, tk.END)
        elif text == "mr":
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.memory))
        elif text == "+/-":
            if self.display.get() == "":
                return
            if self.display.get()[0] == "-":
                self.display.delete(0)
            else:
                self.display.insert(0, "-")
        elif text == "sqrt":
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "!":
            try:
                result = math.factorial(int(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

