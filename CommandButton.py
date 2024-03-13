import tkinter as tk
import pyperclip

class CommandButton(tk.Button):
    def __init__(self, master, text, command_str, *args, **kwargs):
        super().__init__(master, text=text, command=lambda: self.copy_to_clipboard(command_str), *args, **kwargs)

    @staticmethod
    def copy_to_clipboard(command_str):
        pyperclip.copy(command_str)
        print(f"Copied '{command_str}' to clipboard")