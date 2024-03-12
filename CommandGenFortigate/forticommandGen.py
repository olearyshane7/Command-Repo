import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
import forti_command_data
import fortigenerator

class forticommandGen:
    # Intialize method
    def __init__(self, master):
        self.master = master

        # Create input field for IMEI
        tk.Label(master, text="Fortigate IP:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.forti_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.forti_entry.grid(row=1, column=1, padx=(0, 100), pady=5, sticky="e")

        master.geometry("800x800")  # Set initial window size

        self.row_num = 2

        # Set a pleasing color scheme
        master.configure(bg="#E6E6FA")

        # Adjust column weights to make resizing look better
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        # Define the commands for each action
        self.commands = forti_command_data.commands

        self.row_num = 2

        # Create buttons for each action to generate the command
        for action, command in self.commands.items():
            ttk.Label(master, text=action).grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
            
            ttk.Button(master, text="Generate", command=lambda a=action: fortigenerator.generate_command(self, a)).grid(row=self.row_num,
                                                                                                          column=1,
                                                                                                          padx=5, pady=5)
            self.row_num += 1

