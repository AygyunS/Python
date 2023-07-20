import tkinter as tk

class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")
        master.geometry("400x200")
        master.resizable(False, False)
        self.center_window()
        self.create_widgets()

    def center_window(self):
        screen_height = self.master.winfo_screenheight()
        window_height = self.master.winfo_reqheight()
        y = int((screen_height - window_height) / 2)
        self.master.geometry("+{}+{}".format(200, y-50))

    def create_widgets(self):
        height_label = tk.Label(self.master, text="Height (m):")
        height_label.grid(row=0, column=0, padx=20, pady=20)
        self.height_entry = tk.Entry(self.master)
        self.height_entry.grid(row=0, column=1, padx=5, pady=5)
        weight_label = tk.Label(self.master, text="Weight (kg):")
        weight_label.grid(row=1, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def calculate_bmi(self):
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        bmi = weight / (height ** 2)

        self.result_label.config(text="Your BMI is {:.1f}".format(bmi))

root = tk.Tk()
bmi_calculator = BMICalculator(root)
root.mainloop()
