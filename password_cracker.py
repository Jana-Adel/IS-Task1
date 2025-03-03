import tkinter as tk
from tkinter import messagebox
import itertools
import string

CORRECT_PASSWORD = "abc123"

def dictionary_attack(username, dictionary):
    for password in dictionary:
        if password.strip() == CORRECT_PASSWORD:
            return password
    return None

def brute_force_attack():
    chars = string.ascii_letters  
    for password in map("".join, itertools.product(chars, repeat=5)):
        if password == CORRECT_PASSWORD:
            return password
    return None

def start_attack():
    username = entry_username.get()
    if not username:
        messagebox.showwarning("Warning", "Please enter a username!")
        return
    dictionary = []
    try:
        with open("baby.txt", "r") as file:
            dictionary.extend(file.readlines())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Dictionary file not found!")
    
    try:
        with open("logins.txt", "r") as file:
            dictionary.extend(file.readlines())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Dictionary file not found!")
    
    if not dictionary:
        messagebox.showerror("Error", "No dictionary files found!")
        return
    
    result = dictionary_attack(username, dictionary)
    if result:
        messagebox.showinfo("Success", f"Password found using dictionary attack \nWelcome, {username}!")
    else:
        messagebox.showwarning("Failure", "Dictionary attack failed, starting brute force attack...")
        
        brute_result = brute_force_attack()
        if brute_result:
            messagebox.showinfo("Success!", f"Password found using brute force attack \nWelcome, {username}!")
        else:
            messagebox.showerror("Failure", "Password not found!")

root = tk.Tk()
root.title("Password Cracker")
root.geometry("400x300")

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Start Attack", command=start_attack).pack(pady=20)

root.mainloop()
