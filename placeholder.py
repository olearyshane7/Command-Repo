import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging   



class Placeholders:

    def on_entry_focus_in(self, event):
        if self.usable_in_cidr_fortigate.get() == self.placeholder_text:
            self.usable_in_cidr_fortigate.delete(0, tk.END)
            self.usable_in_cidr_fortigate.config(foreground='black')  # Optional: Change text color

    def on_entry_focus_out(self, event):
        if not self.usable_in_cidr_fortigate.get():
            self.show_placeholder()

    def show_placeholder(self):
        self.usable_in_cidr_fortigate.insert(0, self.placeholder_text)
        self.usable_in_cidr_fortigate.config(foreground='grey') 


    