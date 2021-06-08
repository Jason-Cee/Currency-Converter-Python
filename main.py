# All the imports
from tkinter import *
from tkinter import messagebox
import requests

# Let's start with the design of the GUI
root = Tk()
root.title("Currency Conversion")
root.geometry("300x600")
root.config(bg="#6a040f")
root.resizable(False, False)

value = IntVar()

# Retrieving information from external JSON file
info = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
info_json = info.json()

conversion_rate = info_json['conversion_rates']

# label and entry for the results
val_label = Label(root, text="Value", font="50")
val_label.config(bg="#6a040f", fg="#f1e05a")
val_label.place(x=130, y=10)

val_entry = Entry(root, textvariable=value)
val_entry.config(bg="yellow")
val_entry.place(x=70, y=50)

# Creating the FROM (Standard value is USD)
from_label = Label(root, text="From: USD", font="30")
from_label.config(bg="#6a040f", fg="#f1e05a")
from_label.place(x=110, y=100)

# Conversion of the data with the loop
convert = Label(root, text="To:", font="30")
convert.config(bg="#6a040f", fg="#f1e05a")
convert.place(x=140, y=150)

con_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    con_list.insert(END, str(i))
    con_list.config(bg="yellow")
    con_list.place(x=70, y=200)

# Conversion Label
con_label = Label(root, text="Result: ", font="30")
con_label.config(bg="#6a040f", fg="#f1e05a")
con_label.place(x=125, y=400)


# Defining Currency Conversion
def convert_currency():
    num = float(val_entry.get())
    print(info_json['conversion_rates'][con_list.get(ACTIVE)])
    ans = num * info_json['conversion_rates'][con_list.get(ACTIVE)]
    con_label['text'] = ans


# Currency Conversion Button
con_btn = Button(root, command=convert_currency, text="Convert", width=20)
con_btn.config(bg="yellow")
con_btn.place(x=55, y=500)


# Defining Exit Button
def exit_btn():
    messagebox.askyesno("Satisfied ?", "Are You Sure You Want To Exit ?")  # Pop up Exit Box
    root.destroy()


exit_btn = Button(root, command=exit_btn, text="Exit", width=20)
exit_btn.config(bg="yellow")
exit_btn.place(x=55, y=560)

root.mainloop()
