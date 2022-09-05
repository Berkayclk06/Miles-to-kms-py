from tkinter import *


def calculate():
    try:
        miles_in = float(entry.get())
        miles_in *= 1.609
        miles_in = round(miles_in, 2)
        result.config(text=miles_in)
    except ValueError:
        result.config(text="Enter a number")


window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=200, height=120)


# Entry
entry = Entry(width=15)
entry.grid(column=1, row=0)

# Labels
mile = Label(text="Miles")
mile.grid(column=2, row=0)
mile.config(padx=20, pady=10)

eq = Label(text="is equal to")
eq.grid(column=0, row=1)
eq.config(padx=20, pady=10)

result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=20, pady=10)

kms = Label(text="Km")
kms.grid(column=2, row=1)
kms.config(padx=20, pady=10)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
