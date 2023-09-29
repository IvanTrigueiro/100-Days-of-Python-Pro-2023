from tkinter import *


def button_clicked():
    if input.get().replace(".", "").isnumeric():
        value_in_kms = round(float(input.get()) * 1.60934, 2)
    else:
        value_in_kms = 0
    value.config(text=f"{value_in_kms}")


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=100, bg="#856ff8")


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.config(bg="white", fg="#856ff8")

# Miles Label
miles = Label(text="Miles", font=("Courier", 15, "bold"))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=0, bg="#856ff8", fg="white")

# Km label
km = Label(text="Km", font=("Courier", 15, "bold"))
km.grid(column=2, row=1)
km.config(padx=10, pady=0, bg="#856ff8", fg="white")

# is equal to label
is_equal_to = Label(text="is equal to", font=("Courier", 15, "bold"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=0, bg="#856ff8", fg="white")

# value label
value = Label(text="0", font=("Courier", 15, "bold"))
value.grid(column=1, row=1)
value.config(padx=0, pady=0, bg="#856ff8", fg="white")

# Button
button = Button(text="Convert", command=button_clicked, font=("Courier", 10, "bold"))
button.grid(column=1, row=2)
button.config(padx=10, pady=0, bg="#856ff8", fg="white")

window.mainloop()
