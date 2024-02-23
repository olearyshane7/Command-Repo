# utils.py
import pyperclip
from tkinter import messagebox

def copy_initial_command():
    initial_command = "show interface lte detail | match IMEI"
    pyperclip.copy(initial_command)
    messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")
