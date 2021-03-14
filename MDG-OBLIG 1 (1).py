import datetime
from tkinter import Tk, N, W, E, S, StringVar, ttk



#title("Kalkulator for beregning av bruktverdi bil")
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
    loss = CarPrice().calculate_loss(self.car_price.get(), self.car_year.get())
    self.value_loss.set(round(loss, 2))
    self.remaining_value.set(round(float(self.car_price.get()) - loss, 2))


class CarPrice:
  def __init__(self):
    self.value_losses = [0.2, 0.14, 0.13, 0.12, 0.11, 0.1]

  def calculate_loss(self, initial_price, year):
    initial_price = float(initial_price)
    price = initial_price
    num_of_years = datetime.datetime.now().year - int(year)

    for i in range(num_of_years):
      if i < len(self.value_losses):
        price = price * (1 - self.value_losses[i])

    return initial_price - price


root = Tk()
CalculatorGUI(root)
root.mainloop()

#Michal Dariusz Grygliki
