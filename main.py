import tkinter as tk
from tkinter import messagebox
import random as rnd
import string

ascii_list = string.ascii_letters + string.digits + string.punctuation

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = rnd.choices(ascii_list, k=10)
    password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    return password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    save_dict = {
        "website": website_entry.get(),
        "email": email_entry.get(),
        "password":password_entry.get(),
    }

    is_ok = messagebox.askokcancel(title=save_dict["website"],
                                   message=f"\nEmail: {save_dict["email"]}\nPassword: {save_dict["password"]}\nOkay to save?")

    if save_dict["website"] == "" or save_dict["email"] == "" or save_dict["password"] == "":
        messagebox.showerror("Error", "Please enter all required fields")
        is_ok = False

    if is_ok:
        with open("data.txt",  'a') as f:
            f.write(save_dict["website"] + ", " + save_dict["email"] + ", " + save_dict["password"] + "\n")
            f.close()
        print("Account data and password saved.")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=400, height=400)
window.configure(padx=20, pady=20, bg="white")

logo = tk.PhotoImage(file="logo.png")

canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tk.Label(window, text="Website:", bg="white", highlightthickness=0)
website_label.grid(row=1, column=0)

website_entry = tk.Entry(window, width=59, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W)

email_label = tk.Label(window, text="Email/Username:", bg="white", highlightthickness=0)
email_label.grid(row=2, column=0)

email_entry = tk.Entry(window, width=59, highlightthickness=0)
email_entry.insert(0, "nanodoc2020@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W)

password_label = tk.Label(window, text="Password:", bg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = tk.Entry(window, width=32, highlightthickness=0)
password_entry.grid(row=3, column=1, sticky=tk.W)

generate_button = tk.Button(text="Generate Password", width=21, command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = tk.Button(text="Add", width=49, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)

window.mainloop()
