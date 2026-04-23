import tkinter as tk
from tkinter import messagebox
import time
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import pyperclip

# Tool Password Prompt Class
class ToolPasswordPrompt(tk.Toplevel):
    # Password array where the index corresponds to the tool number
    tool_passwords = [
    "T00l1!P@ssw0rd#X8gR3",  # Password for Tool 1
    "T00l2$P@ssw0rd#Zn4*Qk",  # Password for Tool 2
    "T00l3^P@ssw0rd1Dq!A9R",  # Password for Tool 3
    "T00l4&!P@ssw0rdLz$C5t",  # Password for Tool 4
    "T00l5*P@ssw0rdH2n#M8y",  # Password for Tool 5
    "T00l6#P@ssw0rdP7g$W1u",  # Password for Tool 6
    "T00l7!P@ssw0rdTkX9yD5Q",  # Password for Tool 7
    "T00l8*P@ssw0rdD3w@*L2q",  # Password for Tool 8
    "T00l9#P@ssw0rdH4lQ8oM",  # Password for Tool 9
    "T0010$P@ssw0rdVs7NpW6z",  # Password for Tool 10
]
    
    def __init__(self, tool_num, tool_class, master=None):
        super().__init__(master)
        self.tool_num = tool_num
        self.tool_class = tool_class  # The tool class that will be initialized on password success
        self.attempts = 0  # Count wrong password attempts
        self.locked = False  # Lockout state

        self.title(f"Tool {tool_num} - Password")
        self.geometry("300x200")
        self.configure(bg="black")

        tk.Label(self, text=f"Enter Password for Tool {tool_num}", font=("Arial", 12), bg="black", fg="white").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10)

        self.proceed_button = tk.Button(self, text="Proceed", font=("Arial", 12), bg="blue", fg="white", command=self.verify_password)
        self.proceed_button.pack(pady=10)

    def verify_password(self):
        """Verify the password entered by the user."""
        if self.locked:
            return

        correct_password = self.tool_passwords[self.tool_num - 1]  # Retrieve the correct password for this tool
        entered_password = self.password_entry.get()

        if entered_password == correct_password:
            # Password is correct, open the tool
            messagebox.showinfo("Access Granted", f"Password correct! Opening Tool {self.tool_num}.")
            self.destroy()

            # Initialize the tool class passed (e.g., Tool1, Tool2)
            tool_instance = self.tool_class(self.master)  # Create the tool instance
            tool_instance.setup_gui()  # Set up the tool GUI
        else:
            # Incorrect password handling
            self.attempts += 1
            if self.attempts >= 3:
                messagebox.showerror("Access Denied", "Too many failed attempts. Closing program.")
                self.destroy()
                self.master.destroy()  # Close the entire application
            else:
                messagebox.showerror("Access Denied", "Wrong password! Please try again.")
                self.lock_screen(10)  # Lock screen for 10 seconds

    def lock_screen(self, lock_time):
        """Lock the screen for the given time period."""
        self.locked = True
        self.proceed_button.config(state=tk.DISABLED)
        self.update()
        time.sleep(lock_time)  # Lockout for 10 seconds
        self.locked = False
        self.proceed_button.config(state=tk.NORMAL)


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Tool1:
    def __init__(self, master=None):
        self.master = master
        self.key = b'ba8x0eO8@x17!xf2'  # Key must be 16 bytes
        self.cipher = AES.new(self.key, AES.MODE_CBC)
        self.iv = self.cipher.iv  # Initialization vector

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()


    def setup_gui(self):
        """Setup the GUI for Tool1"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 1 - AES Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="Black")

        # Title
        tk.Label(self.window, text="AES Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=470, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            encrypted_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
            self.text_encrypted.set(encrypted_bytes.hex())
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            encrypted_bytes = bytes.fromhex(ciphertext)
            decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
            self.text_decrypted.set(decrypted_bytes.decode())
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")



from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pyperclip

class Tool2:
    def __init__(self, master=None):
        self.master = master
        # RSA Key Setup
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()


    def setup_gui(self):
        """Setup the GUI for Tool2"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 2 - RSA Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="Black")

        # Title
        tk.Label(self.window, text="RSA Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=470, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using RSA"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = PKCS1_OAEP.new(self.public_key)
            encrypted_bytes = cipher.encrypt(plaintext.encode())
            self.text_encrypted.set(encrypted_bytes.hex())
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using RSA"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = PKCS1_OAEP.new(self.private_key)
            encrypted_bytes = bytes.fromhex(ciphertext)
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
            self.text_decrypted.set(decrypted_bytes.decode())
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")

from cryptography.fernet import Fernet
class Tool3:
    def __init__(self, master=None):
        self.master = master
        # Generate Fernet Key
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()


    def setup_gui(self):
        """Setup the GUI for Tool3"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 3 - Fernet Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="Fernet Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using Fernet"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            encrypted_text = self.cipher_suite.encrypt(plaintext.encode()).decode()
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using Fernet"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            decrypted_text = self.cipher_suite.decrypt(ciphertext.encode()).decode()
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")


from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
class Tool4:
    def __init__(self, master=None):
        self.master = master
        # Blowfish Key (Must be between 4 and 56 bytes)
        self.key = b'Se@##@yu@!t$#K%09767@$#*^ey'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()


    def setup_gui(self):
        """Setup the GUI for Tool4"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 4 - Blowfish Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="Blowfish Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using Blowfish"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
            encrypted_text = cipher.encrypt(pad(plaintext.encode(), Blowfish.block_size)).hex()
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using Blowfish"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
            decrypted_text = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), Blowfish.block_size).decode()
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class Tool5:
    def __init__(self, master=None):
        self.master = master
        # DES Key (Must be 8 bytes)
        self.key = b'#ew%were'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()

    def setup_gui(self):
        """Setup the GUI for Tool5"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 5 - DES Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="DES Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using DES"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = DES.new(self.key, DES.MODE_ECB)
            encrypted_text = cipher.encrypt(pad(plaintext.encode(), DES.block_size)).hex()
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using DES"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = DES.new(self.key, DES.MODE_ECB)
            decrypted_text = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), DES.block_size).decode()
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")
        
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
class Tool6:
    def __init__(self, master=None):
        self.master = master
        # 3DES Key (Must be 16 or 24 bytes)
        self.key = b'156756765428078978905734'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()

    def setup_gui(self):
        """Setup the GUI for Tool6"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 6 - Triple DES Implementation")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="Triple DES Implementation Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using 3DES"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = DES3.new(self.key, DES3.MODE_ECB)
            encrypted_text = cipher.encrypt(pad(plaintext.encode(), DES3.block_size)).hex()
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using 3DES"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = DES3.new(self.key, DES3.MODE_ECB)
            decrypted_text = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), DES3.block_size).decode()
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")


from Crypto.Cipher import ChaCha20

class Tool7:
    def __init__(self, master=None):
        self.master = master
        # Generate a Valid 32-Byte Key for ChaCha20
        self.key = b'0xasdfasdfasdfasdfasdfasdfasdfas'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()
    def setup_gui(self):
        """Setup the GUI for Tool7"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 7 - ChaCha20 Encryption Tool")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="ChaCha20 Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using ChaCha20"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = ChaCha20.new(key=self.key)
            ciphertext = cipher.encrypt(plaintext.encode())
            # Combine nonce and ciphertext (separated by ':')
            self.text_encrypted.set(cipher.nonce.hex() + ":" + ciphertext.hex())
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using ChaCha20"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            nonce, encrypted_message = ciphertext.split(":")
            nonce = bytes.fromhex(nonce)
            encrypted_message = bytes.fromhex(encrypted_message)
            cipher = ChaCha20.new(key=self.key, nonce=nonce)
            plaintext = cipher.decrypt(encrypted_message).decode()
            self.text_decrypted.set(plaintext)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
import pyperclip

class Tool8:
    def __init__(self, master=None):
        self.master = master
        
        # Generate ECC Keys
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()

    def setup_gui(self):
        """Setup the GUI for Tool8"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 8 - ECC Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="ECC Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def derive_shared_key(self):
        """Generate the shared key using ECDH and HKDF"""
        shared_key = self.private_key.exchange(ec.ECDH(), self.public_key)
        derived_key = HKDF(algorithm=SHA256(), length=32, salt=None, info=None).derive(shared_key)
        return derived_key

    def encrypt(self):
        """Encrypt the input text"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            shared_key = self.derive_shared_key()
            encrypted_text = "".join(f"{ord(c) ^ shared_key[i % len(shared_key)]}:" for i, c in enumerate(plaintext))[:-1]
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            shared_key = self.derive_shared_key()
            decrypted_text = "".join(
                chr(int(c) ^ shared_key[i % len(shared_key)]) for i, c in enumerate(ciphertext.split(":"))
            )
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")


class Tool9:
    def __init__(self, master=None):
        self.master = master
        
        # RC4 Key (Variable Length)
        self.key = b'#@$56hyert@#'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()

    def rc4_encrypt_decrypt(self, data, key):
        """RC4 Encryption/Decryption function"""
        S = list(range(256))
        j = 0
        out = []

        # Key Scheduling Algorithm (KSA)
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]

        # Pseudo-Random Generation Algorithm (PRGA)
        i = j = 0
        for char in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            out.append(char ^ S[(S[i] + S[j]) % 256])

        return bytes(out)

    def setup_gui(self):
        """Setup the GUI for Tool9"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 9 - RC4 Encryption")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text="RC4 Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using RC4"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            encrypted = self.rc4_encrypt_decrypt(plaintext.encode(), self.key)
            self.text_encrypted.set(encrypted.hex())
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using RC4"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            encrypted_data = bytes.fromhex(ciphertext)
            decrypted = self.rc4_encrypt_decrypt(encrypted_data, self.key)
            self.text_decrypted.set(decrypted.decode())
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")

from hashlib import pbkdf2_hmac

class Tool10:
    def __init__(self, master=None):
        self.master = master
        # DES Key (Must be 8 bytes)
        self.key = b'#gw%were'

        # GUI Variables
        self.text_to_encrypt = tk.StringVar()
        self.text_encrypted = tk.StringVar()
        self.text_to_decrypt = tk.StringVar()
        self.text_decrypted = tk.StringVar()

    def setup_gui(self):
        """Setup the GUI for Tool5"""
        self.window = tk.Toplevel(self.master)
        self.window.title("Tool 10 -  Encryption Tool")
        self.window.geometry("900x650+50+50")
        self.window.resizable(False, False)
        self.window.config(bg="#2B2B2B")

        # Title
        tk.Label(self.window, text=" Encryption Tool", font=("Georgia", 25, "bold"), bg="#2B2B2B", fg="#FFFFFF").pack(pady=20)

        # Encrypt Section
        tk.Label(self.window, text="Enter Text to Encrypt:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=100)
        tk.Entry(self.window, textvariable=self.text_to_encrypt, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=140)
        tk.Label(self.window, text="Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=30, y=200)
        tk.Entry(self.window, textvariable=self.text_encrypted, font=("Helvetica", 15), width=38, bg="#A5A5A5").place(x=7, y=240)
        tk.Button(self.window, text="Encrypt", command=self.encrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=100, y=300, width=150)
        tk.Button(self.window, text="Copy Encrypted", command=self.copy_encrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=270, y=300, width=150)

        # Divider
        tk.Label(self.window, text="", bg="#FFFFFF").place(x=450, y=80, width=2, height=400)

        # Decrypt Section
        tk.Label(self.window, text="Enter Encrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=100)
        tk.Entry(self.window, textvariable=self.text_to_decrypt, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=140)
        tk.Label(self.window, text="Decrypted Text:", font=("Helvetica", 15), bg="#2B2B2B", fg="#FFFFFF").place(x=480, y=200)
        tk.Entry(self.window, textvariable=self.text_decrypted, font=("Helvetica", 15), width=36, bg="#A5A5A5").place(x=480, y=240)
        tk.Button(self.window, text="Decrypt", command=self.decrypt, font=("Helvetica", 15), bg="#4CAF50", fg="#FFFFFF").place(x=550, y=300, width=150)
        tk.Button(self.window, text="Copy Decrypted", command=self.copy_decrypted_text, font=("Helvetica", 15), bg="#007BFF", fg="#FFFFFF").place(x=720, y=300, width=150)

        # Clear Button
        tk.Button(self.window, text="Clear All", command=self.clear_fields, font=("Helvetica", 15), bg="#FF5733", fg="#FFFFFF").place(x=380, y=500, width=150)

    def encrypt(self):
        """Encrypt the input text using DES"""
        plaintext = self.text_to_encrypt.get()
        if not plaintext:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        try:
            cipher = DES.new(self.key, DES.MODE_ECB)
            encrypted_text = cipher.encrypt(pad(plaintext.encode(), DES.block_size)).hex()
            self.text_encrypted.set(encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        """Decrypt the input text using DES"""
        ciphertext = self.text_to_decrypt.get()
        if not ciphertext:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        try:
            cipher = DES.new(self.key, DES.MODE_ECB)
            decrypted_text = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), DES.block_size).decode()
            self.text_decrypted.set(decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def copy_encrypted_text(self):
        """Copy encrypted text to clipboard"""
        text = self.text_encrypted.get()
        if not text:
            messagebox.showinfo("Info", "No encrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Encrypted text copied to clipboard!")

    def copy_decrypted_text(self):
        """Copy decrypted text to clipboard"""
        text = self.text_decrypted.get()
        if not text:
            messagebox.showinfo("Info", "No decrypted text to copy!")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("Info", "Decrypted text copied to clipboard!")

    def clear_fields(self):
        """Clear all input/output fields"""
        self.text_to_encrypt.set("")
        self.text_encrypted.set("")
        self.text_to_decrypt.set("")
        self.text_decrypted.set("")