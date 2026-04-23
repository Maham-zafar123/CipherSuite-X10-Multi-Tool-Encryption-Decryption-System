import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from password_prompt import ToolPasswordPrompt
from password_prompt import Tool1, Tool2, Tool3, Tool4,Tool5, Tool6, Tool7, Tool8, Tool9, Tool10
import subprocess
import os
import sys

# Data for validation (Page 1)
license_data = {
    "52847@#31499Aftrq!": "0111182211",
    "98347$#56201Xbmlp*": "2928273628",
    "629384@75#62Qwert#": "8383747564",
    "4739&201837Plmzx%$": "2937462938",
    "1938475630Asdfg$$": "8374652938",
    "7584932!018Lmnop@": "3748293018",
    "94837$26153Zx&cvb9": "8374652019",
    "6372819#402Qazws^*": "1029384756",
    "4827!365910Edcrf$": "9273847561",
    "20394857$61Vtgbh^": "3749201837",
}

server_data = {
    "192.175.55.33/99!": "P@ssw0rD1234$",
    "172.168.0.1/50#": "S3rVer2024@#",
    "10.0.0.1/8080$": "Adm!nP@ss*2024",
}

user_credentials = {
    "AdminUser1!": "Str0ngP@ssw0rd#123$!1",
    "AdminUser2#": "H@rdToCr@ck$456!X*",
    "AdminUser3@": "S3cure#U$eR#789@!@",
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Application")
        self.geometry("900x650+50+50")
        self.resizable(False, False)
        self.configure(bg="black")
        self.current_frame = None
        self.show_page_1()
        self.show_copyright_notice()
    def show_copyright_notice(self):
        copyright_text = (
            "Copyright © 2024 AJZ - All Rights Reserved\n"
            "This Application is protected by UK and international copyright laws.\n"
            "Reproduction and distribution of the software without written permission is prohibited."
        )
        # Display the copyright notice at the bottom
        copyright_label = tk.Label(self, text=copyright_text, bg="black", fg="white", font=("Arial", 10))
        copyright_label.pack(side="bottom", fill="x")

    def switch_frame(self, frame_class):
        """Destroy the current frame and replace it with a new one."""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack()

    def show_page_1(self):
        self.switch_frame(Page1)

    def show_page_2(self):
        self.switch_frame(Page2)

    def show_page_3(self):
        self.switch_frame(Page3)

    def show_main_page(self):
        self.switch_frame(MainWindow)


class Page1(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        tk.Label(self, text="AJ'Z Server", font=("Arial", 18, "bold"), fg="white", bg="black").pack(pady=10)
        tk.Label(self, text="Machine Code:", font=("Arial", 12), fg="white", bg="black").pack()
        self.machine_code_entry = tk.Entry(self, font=("Arial", 12))
        self.machine_code_entry.pack(pady=5)

        tk.Label(self, text="License Key:", font=("Arial", 12), fg="white", bg="black").pack()
        self.license_key_entry = tk.Entry(self, font=("Arial", 12))
        self.license_key_entry.pack(pady=5)

        self.status_label = tk.Label(
            self, text="Registration: Not Activated", font=("Arial", 12), fg="red", bg="black"
        )
        self.status_label.pack(pady=5)

        tk.Button(
            self,
            text="Register Program",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            command=self.validate_license,
        ).pack(pady=10)

        self.enter_button = tk.Button(
            self,
            text="Enter Program",
            font=("Arial", 12),
            bg="green",
            fg="white",
            command=master.show_page_2,
            state="disabled",
        )
        self.enter_button.pack(pady=10)

        tk.Button(
            self,
            text="Exit Program",
            font=("Arial", 12),
            bg="red",
            fg="white",
            command=master.quit,
        ).pack(pady=5)

        self.failed_attempts = 0  # Track failed attempts

    def validate_license(self):
        if self.failed_attempts >= 3:
            messagebox.showerror("Error", "Too many failed attempts! Program closing...")
            self.master.quit()  # Close after 3 failed attempts
            return
        
        machine_code = self.machine_code_entry.get()
        license_key = self.license_key_entry.get()
        if license_data.get(machine_code) == license_key:
            self.status_label.config(text="Registration: Activated", fg="green")
            self.enter_button.config(state="normal")
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                messagebox.showerror("Error", "Too many failed attempts! Program closing...")
                self.master.quit()  # Close after 3 failed attempts
            else:
                messagebox.showerror("Error", "Invalid Machine Code or License Key Wait for 10 seconds for try again ")
                self.after(10000, self.enable_input_fields)  # Wait 10 seconds before allowing another try
                self.disable_input_fields()  # Disable inputs during wait time

    def disable_input_fields(self):
        self.machine_code_entry.config(state="disabled")
        self.license_key_entry.config(state="disabled")

    def enable_input_fields(self):
        self.machine_code_entry.config(state="normal")
        self.license_key_entry.config(state="normal")

class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        tk.Label(self, text="Server Authentication", font=("Arial", 18, "bold"), fg="white", bg="black").pack(pady=10)
        tk.Label(self, text="Server Code:", font=("Arial", 12), fg="white", bg="black").pack()
        self.server_code_entry = tk.Entry(self, font=("Arial", 12))
        self.server_code_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Arial", 12), fg="white", bg="black").pack()
        self.password_entry = tk.Entry(self, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        self.loading_label = tk.Label(self, text="", font=("Arial", 12), fg="white", bg="black")
        self.loading_label.pack(pady=10)

        self.progress_bar = Progressbar(self, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=5)

        tk.Button(
            self,
            text="Enter Login Stage",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            command=self.validate_server,
        ).pack(pady=10)
        tk.Button(
            self,
            text="Exit Program",
            font=("Arial", 12),
            bg="red",
            fg="white",
            command=master.quit,
        ).pack(pady=5)

        self.failed_attempts = 0  # Track failed attempts

    def validate_server(self):
        if self.failed_attempts >= 3:
            messagebox.showerror("Error", "Too many failed attempts! Program closing...")
            self.master.quit()  # Close after 3 failed attempts
            return
        
        server_code = self.server_code_entry.get()
        password = self.password_entry.get()
        if server_data.get(server_code) == password:
            self.start_loading()
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                messagebox.showerror("Error", "Too many failed attempts! Program closing...")
                self.master.quit()  # Close after 3 failed attempts
            else:
                messagebox.showerror("Error", "Invalid Server Code or Password wait for 10 seconds for try again")
                self.after(10000, self.enable_input_fields)  # Wait 10 seconds before allowing another try
                self.disable_input_fields()  # Disable inputs during wait time

    def start_loading(self):
        for i in range(101):
            self.progress_bar["value"] = i
            self.loading_label.config(text=f"Loading {i}%")
            self.update_idletasks()
            time.sleep(0.05)  # Adjusted for smoother loading
        self.master.show_page_3()

    def disable_input_fields(self):
        self.server_code_entry.config(state="disabled")
        self.password_entry.config(state="disabled")

    def enable_input_fields(self):
        self.server_code_entry.config(state="normal")
        self.password_entry.config(state="normal")



class Page3(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        tk.Label(self, text="Login Stage", font=("Arial", 18, "bold"), fg="white", bg="black").pack(pady=10)
        tk.Label(self, text="Username:", font=("Arial", 12), fg="white", bg="black").pack()
        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Arial", 12), fg="white", bg="black").pack()
        self.password_entry = tk.Entry(self, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        tk.Button(
            self,
            text="Enter Program",
            font=("Arial", 12),
            bg="green",
            fg="white",
            command=self.validate_credentials,
        ).pack(pady=10)
        tk.Button(
            self,
            text="Exit Program",
            font=("Arial", 12),
            bg="red",
            fg="white",
            command=master.quit,
        ).pack(pady=5)

        self.failed_attempts = 0  # Track failed attempts

    def validate_credentials(self):
        if self.failed_attempts >= 3:
            messagebox.showerror("Error", "Too many failed attempts! Program closing...")
            self.master.quit()  # Close after 3 failed attempts
            return
        
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user_credentials.get(username) == password:
            messagebox.showinfo("Success", "Welcome to the Secure System!")
            self.master.show_main_page()
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                messagebox.showerror("Error", "Too many failed attempts! Program closing...")
                self.master.quit()  # Close after 3 failed attempts
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
                self.after(10000, self.enable_input_fields)  # Wait 10 seconds before allowing another try
                self.disable_input_fields()  # Disable inputs during wait time

    def disable_input_fields(self):
        self.username_entry.config(state="disabled")
        self.password_entry.config(state="disabled")

    def enable_input_fields(self):
        self.username_entry.config(state="normal")
        self.password_entry.config(state="normal")



class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        master.title("Program Page - Encryption Tools")
        master.geometry("900x750+50+50")
        master.resizable(False, False) # Increased height to fit all buttons
        master.configure(bg="black")  # Set background to black
        self.open_windows = []  # Keep track of open tool windows

        # Title Label (centered on the window)
        title_label = tk.Label(self, text="Program Page", font=("Arial", 20, "bold"), fg="white", bg="black")
        title_label.pack(pady=20)

        # Tool Buttons (colorful and with "Enter Program")
        tool_names = [f"Tool {i}" for i in range(1, 11)]  # Tool 1 to Tool 10
        colors = ['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'brown', 'violet']

        # Create buttons for each tool
        for i, (tool_name, color) in enumerate(zip(tool_names, colors), start=1):
            button = tk.Button(self, text=f"{tool_name} - Enter Program", font=("Arial", 14), fg="white", bg=color, width=20,
                               command=lambda i=i: self.open_tool(i))
            button.pack(pady=5)



        # Exit Program Button
        exit_button = tk.Button(self, text="Exit Program", font=("Arial", 14), fg="white", bg="red", width=20, command=self.quit_program)
        exit_button.pack(pady=10)


        # Inside your button click handler
    def open_tool(self, tool_num):
        tool_class = globals().get(f'Tool{tool_num}')
        if tool_class:  # Ensure the tool class exists
            tool_window = ToolPasswordPrompt(tool_num, tool_class, master=self)
            tool_window.mainloop()
        else:
            messagebox.showerror("Error", f"Tool {tool_num} not found.")


    def quit_program(self):
        confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm_exit:
            sys.exit()



# Tool Window (Example)
class ToolWindow(tk.Toplevel):
    def __init__(self, tool_num):
        super().__init__()
        self.title(f"Tool {tool_num}")
        self.geometry("400x300")
        self.configure(bg="black")

        # Tool-specific content
        tk.Label(self, text=f"Tool {tool_num} - Encryption/Decryption", font=("Arial", 16), fg="white", bg="black").pack(pady=20)
        tk.Label(self, text="This is the tool's functionality", font=("Arial", 12), fg="white", bg="black").pack(pady=10)

        # Close button for the tool
        close_button = tk.Button(self, text="Close", font=("Arial", 12), fg="white", bg="red", command=self.destroy)
        close_button.pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
