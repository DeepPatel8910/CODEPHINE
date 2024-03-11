import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random
import pyperclip
from PIL import Image, ImageTk

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Password Generator")

        # Load and resize the password image
        password_image = Image.open("password.png")  # Replace "password.png" with your image file
        password_image = password_image.resize((50, 50), Image.LANCZOS)
        password_icon = ImageTk.PhotoImage(password_image)


        # Heading with image
        self.heading_frame = ttk.Frame(master)
        self.heading_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.heading_label = ttk.Label(self.heading_frame, text="Random Password Generator", font=("Helvetica", 20, "bold"))
        self.heading_label.grid(row=0, column=0, padx=5, pady=5)

        self.password_icon_label = ttk.Label(self.heading_frame, image=password_icon)
        self.password_icon_label.grid(row=0, column=1, padx=5, pady=5)
        self.password_icon_label.image = password_icon  # Keep a reference to prevent garbage collection

        # Password Length
        self.length_label = ttk.Label(master, text="Password Length:", font=("Helvetica", 12))
        self.length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.length_entry = ttk.Entry(master, width=10, font=("Helvetica", 12))
        self.length_entry.grid(row=1, column=1, padx=10, pady=5)

        # Character Type Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)  # Default value set to True
        self.uppercase_check = ttk.Checkbutton(master, text="Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.lowercase_var = tk.BooleanVar(value=True)  # Default value set to True
        self.lowercase_check = ttk.Checkbutton(master, text="Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.numbers_var = tk.BooleanVar(value=True)  # Default value set to True
        self.numbers_check = ttk.Checkbutton(master, text="Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.symbols_var = tk.BooleanVar()
        self.symbols_check = ttk.Checkbutton(master, text="Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Generate Password Button
        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Generated Password Entry
        self.password_entry = ttk.Entry(master, width=40, state="readonly", font=("Helvetica", 12))
        self.password_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        # Copy to Clipboard Button
        self.copy_button = ttk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid length.")
            return
        length = int(length)

        if not any([self.uppercase_var.get(), self.lowercase_var.get(), self.numbers_var.get(), self.symbols_var.get()]):
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password generated yet.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
