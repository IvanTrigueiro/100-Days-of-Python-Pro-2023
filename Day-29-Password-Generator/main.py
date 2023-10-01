from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_text.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_text.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_site = web_site_text.get()
    email_username = email_username_text.get()
    password = password_text.get()

    if len(web_site) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        # Messagebox
        is_ok = messagebox.askokcancel(title=web_site, message=f"These are the details entered: \n"
                                                               f"Email: {email_username} \n"
                                                               f"Password: {password}\n"
                                                               f"Is it ok to save?")
        if is_ok:
            # Save on txt file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web_site} | {email_username} | {password}\n")
            web_site_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_site_label = Label(text="Website:")
web_site_label.grid(column=0, row=1)
web_site_label.config(bg="white", fg="#D4483B", width=20)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_label.config(bg="white", fg="#D4483B", width=20)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(bg="white", fg="#D4483B", width=20)

# Entries
DOUBLESPANWIDTH = 58
web_site_text = Entry(width=DOUBLESPANWIDTH)
web_site_text.grid(column=1, row=1, columnspan=2)
web_site_text.config(fg="#D4483B")
web_site_text.focus()
email_username_text = Entry(width=DOUBLESPANWIDTH)
email_username_text.grid(column=1, row=2, columnspan=2)
email_username_text.config(fg="#D4483B")
email_username_text.insert(0, "mypass@example.com")
password_text = Entry(width=33)
password_text.grid(column=1, row=3)
password_text.config(fg="#D4483B")

generate_password_button = Button(text="Generate Password", width=17, command=generate_password)
generate_password_button.grid(column=2, row=3)
generate_password_button.config(bg="#D4483B", fg="white", font=("Courier", 10, "bold"))

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(bg="#D4483B", fg="white", font=("Courier", 10, "bold"))

window.mainloop()
