# Let's start by applying the improvements to the code.

#improved_python_code = """
import datetime
from tkinter import Tk, N, W, E, S, StringVar, ttk
from tkinter import messagebox

# Constants
VALUE_LOSSES = [0.2, 0.14, 0.13, 0.12, 0.11, 0.1]

class CalculatorGUI:
    def __init__(self, root):
        root.title("Ny/Brukt pris kalkulator verdifall")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(root, padding="56 56 56 56")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.draw_inputs()
        self.draw_outputs()

    def draw_inputs(self):
        self.car_price = StringVar()
        self.car_year = StringVar()

        ttk.Label(self.mainframe, text="Nybil pris:").grid(column=1, row=1, sticky=E)
        ttk.Label(self.mainframe, text="kr.").grid(column=3, row=1, sticky=W)
        car_price_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.car_price)
        car_price_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.mainframe, text="Årsmodell:").grid(column=1, row=4, sticky=E)
        ttk.Label(self.mainframe, text=".").grid(column=3, row=4, sticky=W)
        car_year_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.car_year)
        car_year_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Button(self.mainframe, text="Regn ut", command=self.on_calculate).grid(column=3, row=7, sticky=W)

    def draw_outputs(self):
        self.value_loss = StringVar()
        self.remaining_value = StringVar()

        ttk.Label(self.mainframe, textvariable=self.value_loss).grid(column=3, row=5, sticky=(W, E))
        ttk.Label(self.mainframe, text="Verditap:").grid(column=2, row=5, sticky=W)

        ttk.Label(self.mainframe, textvariable=self.remaining_value).grid(column=3, row=6, sticky=(W, E))
        ttk.Label(self.mainframe, text="Restverdi:").grid(column=2, row=6, sticky=W)

    def on_calculate(self):
        try:
            initial_price = float(self.car_price.get())
            year = int(self.car_year.get())
            if initial_price < 0 or year < 0 or year > datetime.datetime.now().year:
                raise ValueError("Invalid input")
        except ValueError as ve:
            messagebox.showerror("Error", "Invalid input: " + str(ve))
            return

        car_price = CarPrice()
        loss = car_price.calculate_loss(initial_price, year)
        self.value_loss.set(round(loss, 2))
        self.remaining_value.set(round(initial_price - loss, 2))


class CarPrice:
    def calculate_loss(self, initial_price, year):
        price = initial_price
        num_of_years = datetime.datetime.now().year - year

        for i, value_loss in enumerate(VALUE_LOSSES):
            if i < num_of_years:
                price *= (1 - value_loss)

        return initial_price - price


def main():
    root = Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# Michal Dariusz Grygliki
#"""

print(improved_python_code)
