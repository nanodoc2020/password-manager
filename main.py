import tkinter as tk
from tkinter import messagebox
import random as rnd
import string, json

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
    website = website_entry.get()
    save_dict = {
        website: {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }

    # is_ok = messagebox.askokcancel(title=save_dict["website"],
    #                                message=f"\nEmail: {save_dict["email"]}\nPassword: {save_dict["password"]}\nOkay to save?")

    if website == "" or save_dict[website]["email"] == "" or save_dict[website]["password"] == "":
        messagebox.showerror("Error", "Please enter all required fields")
    #    is_ok = False
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                data.update(save_dict)
        except FileNotFoundError:
            print("...file not found, creating new file...")
            with open('data.json', 'w') as f:
                json.dump(save_dict, f, indent=4)
                #print("Account data and password saved. File created.")
                messagebox.showinfo("Success", "Account data and password saved.\nFile Created")
        else:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
                #print("Account data and password saved. File updated.")
                messagebox.showinfo("Success", f"Account data and password saved.")

        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

    # if is_ok:
    #     with open("data.txt",  'a') as f:
    #         f.write(save_dict["website"] + ", " + save_dict["email"] + ", " + save_dict["password"] + "\n")
    #         f.close()
    #     print("Account data and password saved.")

# ----------------------------SEARCH FUNCTION---------------------------- #
def search_data():
    website = website_entry.get()
    if website == "":
        messagebox.showerror("Error", "Search cannot be empty.")
        return
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            print(data[website])
    except KeyError as key_error:
        messagebox.showerror("Error", f"{key_error} not found in data.json")
    except FileNotFoundError as error:
        messagebox.showerror("Error", f"{error} not found.")
    else:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo("Success", f"Email: {email}\nPassword: {password}")


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

website_entry = tk.Entry(window, width=41, highlightthickness=0)
website_entry.grid(row=1, column=1, sticky=tk.W)

search_button = tk.Button(text="Search", width=17, command=search_data)
search_button.grid(row=1, column=2, sticky='w')

email_label = tk.Label(window, text="Email/Username:", bg="white", highlightthickness=0)
email_label.grid(row=2, column=0)

email_entry = tk.Entry(window, width=61, highlightthickness=0)
email_entry.insert(0, "nanodoc2020@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W)

password_label = tk.Label(window, text="Password:", bg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = tk.Entry(window, width=41, highlightthickness=0)
password_entry.grid(row=3, column=1, sticky=tk.W)

generate_button = tk.Button(text="Generate Password", width=17, command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = tk.Button(text="Add", width=53, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)

window.mainloop()
