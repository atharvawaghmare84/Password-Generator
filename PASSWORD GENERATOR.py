#-------------------------------------------------------------------------------
# Name:       Atharva Waghmare
# Purpose:    TASK 3
# TASK :      Password Generator
# Author:      atharva
# Created:     17-07-2023
# Copyright:   (c) athar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter as tk

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_click():
    global length_entry, password_label  # Declare length_entry and password_label as global variables
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Password length must be greater than zero.")
            return

        password = generate_password(length)
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        password_label.config(text="Invalid input. Please enter a valid integer for the password length.")

def create_password_generator():
    global length_entry, password_label  # Declare length_entry and password_label as global variables
    root = tk.Tk()
    root.title("Password Generator")

    length_label = tk.Label(root, text="Enter password length:")
    length_label.pack()

    length_entry = tk.Entry(root)
    length_entry.pack()

    generate_button = tk.Button(root, text="Generate Password", command=on_generate_click)
    generate_button.pack()

    password_label = tk.Label(root, text="")
    password_label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_password_generator()
