from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_site_label = Label(text="Website:")
web_site_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
DOUBLESPANWIDTH = 53
web_site_text = Entry(width=DOUBLESPANWIDTH)
web_site_text.grid(column=1, row=1, columnspan=2)
email_username_text = Entry(width=DOUBLESPANWIDTH)
email_username_text.grid(column=1, row=2, columnspan=2)
password_text = Entry(width=34)
password_text.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=generate_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
