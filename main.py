# All the imports
from tkinter import *
import requests

# Let's start with the design of the GUI
root = Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.config(bg="#5bc0de")

value = IntVar()

# Retrieving information from external JSON file
info = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
info_json = info.json()

conversion_rate = info_json['conversion_rates']


# label and entry for the results
val_label = Label(root, text="Value", font="30")
val_label.config(bg="#5bc0de")
val_label.pack()

val_entry = Entry(root, textvariable=value)
val_entry.config(bg="yellow")
val_entry.pack()

# Creating the FROM (Standard value is USD)
from_label = Label(root, text="From: USD", font="30")
from_label.config(bg="#5bc0de")
from_label.pack()

# Conversion of the data with the loop
convert = Label(root, text="To:", font="30")
convert.config(bg="#5bc0de")
convert.pack()

con_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    con_list.insert(END, str(i))
    con_list.config(bg="yellow")
    con_list.pack()

con_label = Label(root, text="Converted to: ", font="30")
con_label.config(bg="#5bc0de")
con_label.place(x=195, y=280)


def convert_currency():
    num = float(val_entry.get())
    print(info_json['conversion_rates'][con_list.get(ACTIVE)])
    ans = num * info_json['conversion_rates'][con_list.get(ACTIVE)]
    con_label['text'] = ans


con_btn = Button(root, command=convert_currency, text="Convert", width=20)
con_btn.config(bg="yellow")
con_btn.place(x=160, y=350)

root.mainloop()
