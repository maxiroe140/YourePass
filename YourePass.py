import os
import pyperclip
import time
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox, simpledialog
from threading import Thread


class YourePass:
    def __init__(self, master):
        self.master = master
        self.master.title("YourePass - Secure Password Vault")
        self.master.geometry("800x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#181818")
        self.key = None
        self.file_path = "passwords.dat"
        self.master_key_file = "master.key"
        self.load_key()

        if not self.check_master_key():
            self.master.destroy()
            return

        self.setup_ui()

    def load_key(self):
        if not os.path.exists("key.key"):
            self.key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(self.key)
        else:
            with open("key.key", "rb") as key_file:
                self.key = key_file.read()
        self.fernet = Fernet(self.key)

    def check_master_key(self):
        if not os.path.exists(self.master_key_file):
            return self.set_master_key()
        else:
            return self.authenticate()

    def set_master_key(self):
        set_key_window = tk.Toplevel(self.master)
        set_key_window.title("Set Master Key")
        set_key_window.geometry("400x250")
        set_key_window.configure(bg="#181818")
        set_key_window.transient(self.master)
        set_key_window.grab_set()

        tk.Label(
            set_key_window,
            text="Set Your Master Key",
            font=("Helvetica", 14),
            bg="#181818",
            fg="#FFFFFF",
        ).pack(pady=20)

        master_key_entry = tk.Entry(
            set_key_window,
            show="*",
            font=("Helvetica", 12),
            bg="#262626",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
            width=30,
        )
        master_key_entry.pack(pady=10)

        confirm_key_entry = tk.Entry(
            set_key_window,
            show="*",
            font=("Helvetica", 12),
            bg="#262626",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
            width=30,
        )
        confirm_key_entry.pack(pady=10)

        tk.Label(
            set_key_window,
            text="(Make sure to remember it!)",
            font=("Helvetica", 10),
            bg="#181818",
            fg="#AAAAAA",
        ).pack(pady=5)

        def save_master_key():
            master_key = master_key_entry.get()
            confirm_key = confirm_key_entry.get()
            if not master_key or master_key != confirm_key:
                messagebox.showerror(
                    "Error", "Master Keys do not match or are empty!", parent=set_key_window
                )
                return

            encrypted_key = self.fernet.encrypt(master_key.encode())
            with open(self.master_key_file, "wb") as key_file:
                key_file.write(encrypted_key)
            messagebox.showinfo(
                "Success", "Master Key set successfully!", parent=set_key_window
            )
            set_key_window.destroy()

        tk.Button(
            set_key_window,
            text="Save",
            command=save_master_key,
            bg="#1D3557",
            fg="#FFFFFF",
            activebackground="#457B9D",
            activeforeground="#FFFFFF",
            font=("Helvetica", 12),
            bd=0,
            width=15,
        ).pack(pady=20)

        self.master.wait_window(set_key_window)
        return not set_key_window.winfo_exists()

    def authenticate(self):
        auth_window = tk.Toplevel(self.master)
        auth_window.title("Authentication")
        auth_window.geometry("400x220")
        auth_window.configure(bg="#181818")
        auth_window.transient(self.master)
        auth_window.grab_set()

        tk.Label(
            auth_window,
            text="Enter Master Key",
            font=("Helvetica", 14),
            bg="#181818",
            fg="#FFFFFF",
        ).pack(pady=20)

        master_key_entry = tk.Entry(
            auth_window,
            show="*",
            font=("Helvetica", 12),
            bg="#262626",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
            width=30,
        )
        master_key_entry.pack(pady=10)

        def verify_key():
            master_key = master_key_entry.get()
            with open(self.master_key_file, "rb") as key_file:
                encrypted_key = key_file.read()
            if master_key.encode() == self.fernet.decrypt(encrypted_key):
                auth_window.destroy()
            else:
                messagebox.showerror(
                    "Access Denied", "Invalid Master Key", parent=auth_window
                )

        tk.Button(
            auth_window,
            text="Submit",
            command=verify_key,
            bg="#1D3557",
            fg="#FFFFFF",
            activebackground="#457B9D",
            activeforeground="#FFFFFF",
            font=("Helvetica", 12),
            bd=0,
            width=15,
        ).pack(pady=20)

        self.master.wait_window(auth_window)
        return not auth_window.winfo_exists()

    def setup_ui(self):
        tk.Label(
            self.master,
            text="YourePass",
            font=("Helvetica", 26, "bold"),
            bg="#181818",
            fg="#F4F4F4",
        ).pack(pady=20)

        button_frame = tk.Frame(self.master, bg="#181818")
        button_frame.pack(pady=30)

        tk.Button(
            button_frame,
            text="Add Password",
            command=self.add_password,
            bg="#457B9D",
            fg="#FFFFFF",
            activebackground="#1D3557",
            activeforeground="#FFFFFF",
            font=("Helvetica", 14),
            width=20,
            bd=0,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="View Passwords",
            command=self.view_passwords,
            bg="#457B9D",
            fg="#FFFFFF",
            activebackground="#1D3557",
            activeforeground="#FFFFFF",
            font=("Helvetica", 14),
            width=20,
            bd=0,
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Exit",
            command=self.master.quit,
            bg="#E63946",
            fg="#FFFFFF",
            activebackground="#D62828",
            activeforeground="#FFFFFF",
            font=("Helvetica", 14),
            width=20,
            bd=0,
        ).grid(row=1, column=0, columnspan=2, pady=20)

    def add_password(self):
        service = simpledialog.askstring("Service", "Enter the service name:", parent=self.master)
        if not service:
            return
        username = simpledialog.askstring("Username", "Enter the username:", parent=self.master)
        if not username:
            return
        password = simpledialog.askstring("Password", "Enter the password:", show="*", parent=self.master)
        if not password:
            return
        data = f"{service},{username},{password}\n"
        encrypted_data = self.fernet.encrypt(data.encode())
        with open(self.file_path, "ab") as file:
            file.write(encrypted_data + b"\n")
        messagebox.showinfo("Success", "Password added successfully!", parent=self.master)

    def view_passwords(self):
        if not os.path.exists(self.file_path):
            messagebox.showinfo("No Data", "No passwords saved yet.", parent=self.master)
            return
        with open(self.file_path, "rb") as file:
            lines = file.readlines()
        decrypted_data = []
        for line in lines:
            try:
                decrypted_line = self.fernet.decrypt(line.strip()).decode()
                decrypted_data.append(decrypted_line)
            except:
                continue
        if not decrypted_data:
            messagebox.showinfo("No Data", "No passwords found or file corrupted.", parent=self.master)
            return

        passwords_window = tk.Toplevel(self.master)
        passwords_window.title("Saved Passwords")
        passwords_window.geometry("700x400")
        passwords_window.configure(bg="#181818")

        text_frame = tk.Frame(passwords_window, bg="#181818")
        text_frame.pack(expand=True, fill=tk.BOTH)

        text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Courier", 12),
            bg="#262626",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
        )
        text.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        for entry in decrypted_data:
            service, username, password = entry.split(",")
            text.insert(tk.END, f"Service: {service}\nUsername: {username}\nPassword: {password}\n\n")

        text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = YourePass(root)
    root.mainloop()
