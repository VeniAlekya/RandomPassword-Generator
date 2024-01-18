import tkinter as tk
from tkinter import StringVar
import random
import string
#logic of the password generator
def generate_password(length,usenumbers=True,useuppercase=True,uselowercase=True,use_specialcharacters=True):
    characters = ''
    if usenumbers:
        characters += string.digits
    if useuppercase:
        characters += string.ascii_uppercase
    if uselowercase:
        characters += string.ascii_lowercase
    if use_specialcharacters:
        characters += string.punctuation
    if not characters:
        return "Please select at least one type of character."
    if usenumbers and useuppercase and uselowercase and use_specialcharacters:
        generated_password = (
            random.choice(string.digits) +
            random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_lowercase) +
            ''.join(random.choice(characters) for _ in range(length - 3))
        )
    else:
        generated_password=''.join(random.choice(characters) for _ in range(length))
    password_list=list(generated_password)
    random.shuffle(password_list)
    return ''.join(password_list)
#gui programming with logic
def generate_password_from_gui():
    length=int(length2.get())
    usenumbers=numbers.get() == 1
    useuppercase=uppercase.get() == 1
    uselowercase=lowercase.get() == 1
    usespecialcharacters=specialcharacters.get() == 1
    password=generate_password(length, usenumbers, useuppercase, uselowercase, usespecialcharacters)
    result.set("Generated Password: " + password)
root=tk.Tk()
root.title("Random Password Generator")
length2=StringVar()
numbers=tk.IntVar()
uppercase=tk.IntVar()
lowercase=tk.IntVar()
specialcharacters=tk.IntVar()
result=StringVar()
length_label=tk.Label(root, text="Length:")
length_entry=tk.Entry(root, textvariable=length2)
numbers_check=tk.Checkbutton(root, text="Numbers", variable=numbers)
uppercase_check=tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase)
lowercase_check=tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase)
special_chars_check=tk.Checkbutton(root, text="Special Characters", variable=specialcharacters)
generate_button=tk.Button(root, text="Generate Password", command=generate_password_from_gui)
result_label=tk.Label(root, textvariable=result)
length_label.grid(row=0, column=0, sticky="w")
length_entry.grid(row=0, column=1)
numbers_check.grid(row=1, column=0, columnspan=2, sticky="w")
uppercase_check.grid(row=2, column=0, columnspan=2, sticky="w")
lowercase_check.grid(row=3, column=0, columnspan=2, sticky="w")
special_chars_check.grid(row=4, column=0, columnspan=2, sticky="w")
generate_button.grid(row=5, column=0, columnspan=2, pady=10)
result_label.grid(row=6, column=0, columnspan=2)
root.mainloop()
