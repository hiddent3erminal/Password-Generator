import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import hashlib
import pyperclip

# Function to generate passwords
def generate_passwords():
    try:
        length = int(length_var.get())
        count = int(count_var.get())
        hard_spell = hard_var.get()
        
        # Check for valid input values
        if length <= 0 or count <= 0:
            messagebox.showerror("Invalid Input", "Length and Count must be positive integers.")
            return

        passwords = []

        # Define character sets based on difficulty
        easy_chars = string.ascii_lowercase + string.digits
        hard_chars = string.ascii_letters + string.digits + string.punctuation
        char_set = hard_chars if hard_spell else easy_chars

        for _ in range(count):
            password = ''.join(random.choices(char_set, k=length))
            passwords.append(password)

        # Display generated passwords in the text box
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, '\n'.join(passwords))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for length and count.")

# Function to copy generated passwords to clipboard
def copy_to_clipboard():
    passwords = result_text.get(1.0, tk.END).strip()
    if passwords:
        pyperclip.copy(passwords)
        messagebox.showinfo("Copied", "Passwords copied to clipboard!")
    else:
        messagebox.showwarning("No Passwords", "No passwords to copy.")

# Function to hash the generated password using the selected hashing algorithm
def hash_password():
    passwords = result_text.get(1.0, tk.END).strip().split('\n')
    selected_algo = hash_algo_var.get()
    hashed_passwords = []

    if not passwords:
        messagebox.showwarning("No Passwords", "No passwords to hash.")
        return

    try:
        for password in passwords:
            if selected_algo == "SHA-256":
                hashed_passwords.append(hashlib.sha256(password.encode()).hexdigest())
            elif selected_algo == "MD5":
                hashed_passwords.append(hashlib.md5(password.encode()).hexdigest())
            elif selected_algo == "SHA-1":
                hashed_passwords.append(hashlib.sha1(password.encode()).hexdigest())

        # Display hashed passwords in the text box
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, '\n'.join(hashed_passwords))
    except Exception as e:
        messagebox.showerror("Hashing Error", f"Error hashing passwords: {str(e)}")

# Create main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x700")
window.configure(bg="#DCE6F2")

# Title Label
title_label = tk.Label(window, text="Password Generator", font=("Arial", 20, "bold"), bg="#DCE6F2", fg="#333")
title_label.pack(pady=20)

# Frame for input options
input_frame = tk.Frame(window, bg="#DCE6F2")
input_frame.pack(pady=20)

# Length of password
length_label = tk.Label(input_frame, text="Password Length:", font=("Arial", 14), bg="#DCE6F2")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
length_var = tk.StringVar()
length_entry = ttk.Entry(input_frame, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, pady=10)

# Number of passwords
count_label = tk.Label(input_frame, text="Number of Passwords:", font=("Arial", 14), bg="#DCE6F2")
count_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
count_var = tk.StringVar()
count_entry = ttk.Entry(input_frame, textvariable=count_var, width=10)
count_entry.grid(row=1, column=1, pady=10)

# Option for hard-to-spell passwords
hard_var = tk.BooleanVar()
hard_check = ttk.Checkbutton(input_frame, text="Generate Hard-to-Spell Passwords", variable=hard_var)
hard_check.grid(row=2, column=0, columnspan=2, pady=10)

# Generate Password Button
generate_button = ttk.Button(window, text="Generate Passwords", command=generate_passwords)
generate_button.pack(pady=20)

# Text area to display generated passwords
result_text = tk.Text(window, height=15, width=40, font=("Courier", 12))
result_text.pack(pady=20)

# Copy Button
copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Hashing Options
hash_algo_label = tk.Label(window, text="Select Hashing Algorithm:", font=("Arial", 14), bg="#DCE6F2")
hash_algo_label.pack(pady=5)

hash_algo_var = tk.StringVar()
hash_algo_var.set("SHA-256")  # Default hashing algorithm
hash_algo_menu = ttk.OptionMenu(window, hash_algo_var, "SHA-256", "SHA-256", "MD5", "SHA-1")
hash_algo_menu.pack(pady=5)

# Hash Button
hash_button = ttk.Button(window, text="Hash Passwords", command=hash_password)
hash_button.pack(pady=10)

# Run the main event loop
window.mainloop()
