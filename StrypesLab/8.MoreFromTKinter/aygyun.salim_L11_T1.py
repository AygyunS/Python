import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.memory = 0
        self.current_operation = None
        self.current_number = ""

        self.display = tk.Label(master, text="0", font=("Helvetica", 20), anchor="e", width=20)
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.button_1 = tk.Button(master, text="1", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(1))
        self.button_1.grid(row=3, column=0, padx=5, pady=5)

        self.button_2 = tk.Button(master, text="2", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(2))
        self.button_2.grid(row=3, column=1, padx=5, pady=5)

        self.button_3 = tk.Button(master, text="3", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(3))
        self.button_3.grid(row=3, column=2, padx=5, pady=5)

        self.button_4 = tk.Button(master, text="4", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(4))
        self.button_4.grid(row=2, column=0, padx=5, pady=5)

        self.button_5 = tk.Button(master, text="5", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(5))
        self.button_5.grid(row=2, column=1, padx=5, pady=5)

        self.button_6 = tk.Button(master, text="6", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(6))
        self.button_6.grid(row=2, column=2, padx=5, pady=5)

        self.button_7 = tk.Button(master, text="7", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(7))
        self.button_7.grid(row=1, column=0, padx=5, pady=5)

        self.button_8 = tk.Button(master, text="8", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(8))
        self.button_8.grid(row=1, column=1, padx=5, pady=5)

        self.button_9 = tk.Button(master, text="9", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(9))
        self.button_9.grid(row=1, column=2, padx=5, pady=5)

        self.button_0 = tk.Button(master, text="0", font=("Helvetica", 16), padx=10, pady=5,
                                  command=lambda: self.add_number(0))
        self.button_0.grid(row=4, column=1, padx=5, pady=5)

        self.button_point = tk.Button(master, text=".", font=("Helvetica", 16), padx=10, pady=5,
                                      command=lambda: self.add_number("."))
        self.button_point.grid(row=4, column=0, padx=5, pady=5)

        self.button_negative = tk.Button(master, text="+/-", font=("Helvetica", 16), padx=10, pady=5,
                                         command=self.change_sign)
        self.button_negative.grid(row=4, column=2, padx=5, pady=5)

        self.button_add = tk.Button(master, text="+", font=("Helvetica", 16), padx=10, pady=5,
                                    command=lambda: self.set_operation("+"))
        self.button_add.grid(row=1, column=3, padx=5, pady=5)

        self.button_subtract = tk.Button(master, text="-", font=("Helvetica", 16), padx=10, pady=5,
                                         command=lambda: self.set_operation("-"))
        self.button_subtract.grid(row=2, column=3, padx=5, pady=5)

        self.button_multiply = tk.Button(master, text="*", font=("Helvetica", 16), padx=10, pady=5,
                                         command=lambda: self.set_operation("*"))
        self.button_multiply.grid(row=3, column=3, padx=5, pady=5)

        self.button_divide = tk.Button(master, text="/", font=("Helvetica", 16), padx=10, pady=5,
                                       command=lambda: self.set_operation("/"))
        self.button_divide.grid(row=4, column=3, padx=5, pady=5)

        self.button_equals = tk.Button(master, text="=", font=("Helvetica", 16), padx=10, pady=5,
                                       command=self.calculate_result)
        self.button_equals.grid(row=5, column=3, padx=5, pady=5)

        self.button_clear_entry = tk.Button(master, text="CE", font=("Helvetica", 16), padx=10, pady=5,
                                            command=self.clear_entry)
        self.button_clear_entry.grid(row=5, column=0, padx=5, pady=5)

        self.button_all_clear = tk.Button(master, text="AC", font=("Helvetica", 16), padx=10, pady=5,
                                          command=self.all_clear)
        self.button_all_clear.grid(row=5, column=1, padx=5, pady=5)

        self.button_memory_clear = tk.Button(master, text="mc", font=("Helvetica", 16), padx=10, pady=5,
                                             command=self.memory_clear)
        self.button_memory_clear.grid(row=6, column=0, padx=5, pady=5)

        self.button_memory_plus = tk.Button(master, text="m+", font=("Helvetica", 16), padx=10, pady=5,
                                            command=self.memory_plus)
        self.button_memory_plus.grid(row=6, column=1, padx=5, pady=5)

        self.button_memory_minus = tk.Button(master, text="m-", font=("Helvetica", 16), padx=10, pady=5,
                                             command=self.memory_minus)
        self.button_memory_minus.grid(row=6, column=2, padx=5, pady=5)

        self.button_memory_recall = tk.Button(master, text="mr", font=("Helvetica", 16), padx=10, pady=5,
                                              command=self.memory_recall)
        self.button_memory_recall.grid(row=6, column=3, padx=5, pady=5)

        self.button_square_root = tk.Button(master, text="√", font=("Helvetica", 16), padx=10, pady=5,
                                            command=self.square_root)
        self.button_square_root.grid(row=1, column=4, padx=5, pady=5)

        self.button_factorial = tk.Button(master, text="x!", font=("Helvetica", 16), padx=10, pady=5,
                                          command=self.factorial)
        self.button_factorial.grid(row=2, column=4, padx=5, pady=5)

        self.button_power = tk.Button(master, text="^", font=("Helvetica", 16), padx=10, pady=5,
                                      command=lambda: self.set_operation("**"))
        self.button_power.grid(row=3, column=4, padx=5, pady=5)

        self.button_modulus = tk.Button(master, text="%", font=("Helvetica", 16), padx=10, pady=5,
                                        command=lambda: self.set_operation("%"))
        self.button_modulus.grid(row=4, column=4, padx=5, pady=5)


    def add_number(self, number):
        self.current_number += str(number)
        self.update_display()

    def update_display(self):
        if "." in self.current_number:
            result = float(self.current_number)
            if result.is_integer():
                self.display.config(text=str(int(result)))
            else:
                self.display.config(text="{:.3f}".format(result))
        else:
            self.display.config(text=self.current_number)

    def set_operation(self, operation):
        self.current_operation = operation
        self.memory = float(self.current_number)
        self.current_number = ""
        self.update_display()

    def calculate_result(self):
        if self.current_operation == "+":
            result = self.memory + float(self.current_number)
        elif self.current_operation == "-":
            result = self.memory - float(self.current_number)
        elif self.current_operation == "*":
            result = self.memory * float(self.current_number)
        elif self.current_operation == "/":
            result = self.memory / float(self.current_number)
        else:
            result = float(self.current_number)

        self.current_number = str(result)
        self.current_operation = None
        self.update_display()

    def clear_entry(self):
        self.current_number = ""
        self.update_display()

    def all_clear(self):
        self.memory = 0
        self.current_operation = None
        self.current_number = ""
        self.update_display()

    def memory_clear(self):
        self.memory = 0

    def memory_plus(self):
        self.memory += float(self.current_number)

    def memory_minus(self):
        self.memory -= float(self.current_number)

    def memory_recall(self):
        self.current_number = str(self.memory)
        self.update_display()

    def change_sign(self):
        if self.current_number.startswith("-"):
            self.current_number = self.current_number[1:]
        else:
            self.current_number = "-" + self.current_number
        self.update_display()

    def square_root(self):
        self.current_number = str(math.sqrt(float(self.current_number)))
        self.update_display()

    def factorial(self):
        self.current_number = str(math.factorial(int(self.current_number)))
        self.update_display()


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
