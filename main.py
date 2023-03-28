import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passowrd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    #Automtically copies the password
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data =  {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 and len(password) ==0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_files:
                # json.dump(new_data, data_files, indent=4)
                #Reading old data
                data = json.load(data_files)

        except FileNotFoundError:
            with open("data.json", "w") as data_files:
                json.dump(new_data, data_files, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_files:
                #Saving updated data
                json.dump(data, data_files, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_files:
            json_data = json.load(data_files)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in json_data:
            messagebox.showinfo(title=website, message=f"Email: {json_data[website]['email']}\nPassword: {json_data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password GUI app remake")
window.config(padx=20, pady=20)

#Canvas
canvas = Canvas(width=200, height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "angela@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

#Buttons
generate_pass_button = Button(text="Generate Password", command=generate_passowrd)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=17, command=search)
search_button.grid(row=1, column=2)

window.mainloop()