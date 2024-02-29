import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
from helpers import generate_config
import command_generator
import command_data
from tkinter import simpledialog




class IMEICommandGenerator:
    def __init__(self, master):
        self.master = master
        master.title("IMEI Command Generator")
        self.imei_input = None  # Initialize imei_input

        # Button to copy the initial command
        ttk.Button(master, text="Get IMEI Command", command=self.copy_initial_command).grid(row=0, column=0,
                                                                                               columnspan=2, pady=10)
        # Test Button
        # Button to copy the initial command
        # ttk.Button(master, text="Test", command=self.test_initial_command).grid(row=0, column=2,
        #                                                                                        columnspan=1, pady=10)        


        # Create input field for IMEI
        ttk.Label(master, text="IMEI:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.imei_frame = ttk.Frame(master, relief="groove", borderwidth=2)
        self.imei_frame.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.imei_entry = ttk.Entry(self.imei_frame, font=("Helvetica", 12), width=17)
        self.imei_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        master.geometry("500x500")  # Set initial window size

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
        
        


        # Create input field for State
        ttk.Label(master, text="VZ-APN State:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.state_entry = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.state_entry.grid(row=self.row_num, column=1, padx=5, pady=5)

        # Button to generate the configuration
        generate_button = ttk.Button(master, text="Generate VZ profile Config", command=lambda: generate_config(self.state_entry))
        generate_button.grid(row=self.row_num + 1, columnspan=2, pady=10)

        # Button to change Wan script
        changeWan_button = ttk.Button(master, text="Change Wan Script", command=self.changeWan_script)
        changeWan_button.grid(row=self.row_num + 2, columnspan=2, pady=10)

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: generate_config(self.state_entry))

        

    # Define copy_initial_command as a method of IMEICommandGenerator
    def copy_initial_command(self):
        initial_command = "show interface lte detail | match IMEI"
        pyperclip.copy(initial_command)
        messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")
    
    def changeWan_script(self):
        imei = self.imei_entry.get()
        gateway = simpledialog.askstring("Input", "Enter the gateway no CIDR:")
        usable_ip = simpledialog.askstring("Input", "Enter the usable IP/CIDR:")
        net_ip = simpledialog.askstring("Input", "Enter the net IP/CIDR:")

        config = f"""
config
interface ip ip-2
ip-addr {usable_ip}
back
-----------------------------------
vrf "public-vrf-2"
ip-route 0.0.0.0/0
gateway "{gateway}"
back
----------------------------------- 
ip-route {net_ip}
interface "ip-2"
back
back
-----------------------------------
applications
hybrid-wan
profile basic
interfaces
wan-port ip-2
gateway-ip {gateway}
commit
        """

        self.copy_command_to_clipboard(config)
        messagebox.showinfo("New Configuration", f"New configuration copied to clipboard:\n\n{config}")

    def copy_command_to_clipboard(self, command):
        pyperclip.copy(command)
    
    # def test_initial_command(self):
    #     #TEST
    #     self.imei_input = self.imei_entry.get()  # Store user input in imei_input
    #     print(f"My name is {self.imei_input}")
