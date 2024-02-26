import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
from helpers import generate_config
import command_generator
import command_data
from UpdateIPConfig import generate_ip_config



class IMEICommandGenerator:
    def __init__(self, master):
        self.master = master
        master.title("IMEI Command Generator")

        # Button to copy the initial command
        ttk.Button(master, text="Get IMEI Command", command=self.copy_initial_command).grid(row=0, column=0,
                                                                                               columnspan=2, pady=10)

        # Create input field for IMEI
        tk.Label(master, text="IMEI:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.imei_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.imei_entry.grid(row=1, column=1, padx=(0, 100), pady=5, sticky="e")

        master.geometry("700x600")  # Set initial window size

        self.row_num = 2

        # Set a pleasing color scheme
        master.configure(bg="#E6E6FA")

        # Adjust column weights to make resizing look better
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        # Define the commands for each action
        self.commands = command_data.commands

        self.row_num = 2

        # Create buttons for each action to generate the command
        for action, command in self.commands.items():
            ttk.Label(master, text=action).grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
            
            ttk.Button(master, text="Generate", command=lambda a=action: command_generator.generate_command(self, a)).grid(row=self.row_num,
                                                                                                          column=1,
                                                                                                          padx=5, pady=5)
            self.row_num += 1

        # Input field for usable CIDR
        ttk.Label(master, text="Usable CIDR:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.usable_in_cidr = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.usable_in_cidr.grid(row=self.row_num, column=1, padx=5, pady=5)
        self.row_num += 1

        # Input field for Gateway IP
        ttk.Label(master, text="Gateway IP:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.gw_ip = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.gw_ip.grid(row=self.row_num, column=1, padx=5, pady=5)
        self.row_num += 1

        # Input field for Network CIDR
        ttk.Label(master, text="Network CIDR:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.network_in_cidr = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.network_in_cidr.grid(row=self.row_num, column=1, padx=5, pady=5)
        self.row_num += 1

        # Create input field for State
        ttk.Label(master, text="VZ-APN State:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.state_entry = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.state_entry.grid(row=self.row_num, column=1, padx=5, pady=5)

        # Button to update the values
        update_button = ttk.Button(master, text="Update IPs", command=lambda: generate_ip_config(self.usable_in_cidr, self.gw_ip, self.network_in_cidr))
        update_button.grid(row=17, column=0, padx=40, pady=5, sticky="w")

        # Button to generate the configuration
        generate_button = ttk.Button(master, text="Generate VZ profile Config", command=lambda: generate_config(self.state_entry))
        generate_button.grid(row=17, column=0, padx=40, pady=5, sticky="e")     

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: generate_config(self.state_entry))

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: generate_ip_config(self.usable_in_cidr, self.gw_ip, self.network_in_cidr))

    # Define copy_initial_command as a method of IMEICommandGenerator
    def copy_initial_command(self):
        initial_command = "show interface lte detail | match IMEI"
        pyperclip.copy(initial_command)
        messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")