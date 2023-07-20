import tkinter as tk

root = tk.Tk()

def button_clicked():
    button.config(state=tk.DISABLED)

def check_button_state(button):
    if button['state'] == tk.DISABLED:
        button.config(state=tk.NORMAL)

button = tk.Button(root, text="Click me!",
                   command=button_clicked)
button.pack()

button2 = tk.Button(root, text="Check state",
                    command=lambda: check_button_state(button))
button2.pack()

root.mainloop()
