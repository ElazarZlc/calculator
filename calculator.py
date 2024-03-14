import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, width=10, command=self.calculate).grid(row=row, column=col, columnspan=2,
                                                                                      padx=5, pady=5)
            else:
                tk.Button(master, text=button, width=5, command=lambda b=button: self.entry.insert(tk.END, b)).grid(
                    row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            messagebox.showinfo("Result", f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
