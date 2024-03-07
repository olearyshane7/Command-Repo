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
from calculateNetworkIP import calculate_network_ip
from ipaddress import IPv4Network
from calculateCIDR import calculate_cidr





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

        # Create input field for foritage ip
        # self.usable_in_cidr_fortigate = ttk.Entry(master, font=("Helvetica", 12), width=20)
        # self.usable_in_cidr_fortigate.grid(row=20, column=1, padx=5, pady=5)
        
        # Button to generate the foritgate link
        # copy_link_button = ttk.Button(master, text="Fortigate Link", command= self.generate_fortigate_link)
        # copy_link_button.grid(row=25, column=1, padx=40, pady=5)

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: generate_config(self.state_entry))

        

    # Define copy_initial_command as a method of IMEICommandGenerator
    def copy_initial_command(self):
        initial_command = "show interface lte detail | match IMEI"
        pyperclip.copy(initial_command)
        messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")
    
    def changeWan_script(self):
        imei = self.imei_entry.get()
        gateway = simpledialog.askstring("Input", "Enter the gateway (no CIDR):")
        usable_ip = simpledialog.askstring("Input", "Enter the usable (no CIDR):")
        subnet_mask_input = simpledialog.askstring("Input", "Enter the subnet mask:")

        # Calculate CIDR of subnet mask
        cidr = calculate_cidr(subnet_mask_input)

        if cidr is not None:
            # Get usable IP with CIDR
            usable_ip_cidr = f"{usable_ip}/{cidr}"

            # Get gateway IP with CIDR
            gateway_cidr = self.append_cidr_to_ip(gateway)

            # Calculate the network IP based on the gateway IP and subnet mask
            network_ip = calculate_network_ip(gateway, subnet_mask_input)

            # Append CIDR to network IP
            network_ip_cidr = f"{network_ip}/{cidr}"

            config = f"""
        config
        interface ip ip-2
        ip-addr {usable_ip_cidr}
        back
        -----------------------------------
        vrf "public-vrf-2"
        ip-route 0.0.0.0/0
        gateway "{gateway_cidr}"
        back
        ----------------------------------- 
        ip-route {network_ip_cidr}
        interface "ip-2"
        back
        back
        -----------------------------------
        applications
        hybrid-wan
        profile basic
        interfaces
        wan-port ip-2
        gateway-ip {gateway_cidr}
        commit
            """

            self.copy_command_to_clipboard(config)
            messagebox.showinfo("New Configuration", f"New configuration copied to clipboard:\n\n{config}")


    def append_cidr_to_ip(self, ip):
        return ip

    # Opens up the fortigate GUI loging page via usable 
    # def generate_fortigate_link(self) :
    #     usable_in_cidr_fortigate = self.usable_in_cidr_fortigate.get()
    #     self.open_link(f"https://{usable_in_cidr_fortigate}:60481")
    
    # def open_link(usable_in_cidr_fortigate, link):
    #     webbrowser.open(link) 

    def copy_command_to_clipboard(self, command):
        pyperclip.copy(command)
    
    # def test_initial_command(self):
    #     #TEST
    #     self.imei_input = self.imei_entry.get()  # Store user input in imei_input
    #     print(f"My name is {self.imei_input}")
