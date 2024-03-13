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
from ipaddress import IPv4Network
import webbrowser 
from signalstrength import signalstrength

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

        master.geometry("1000x950")  # Set initial window size

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
        update_button = ttk.Button(master, text="Update WAN IPs", command=lambda: generate_ip_config(self.usable_in_cidr, self.gw_ip, self.network_in_cidr))
        update_button.grid(row=17, column=0, padx=40, pady=5, sticky="e")
        
        # Button to calculate network CIDR
        calculate_button = ttk.Button(master, text="Calculate Network CIDR", command=self.calculate_network_cidr)
        calculate_button.grid(row=17, column=1, padx=40, pady=5, sticky="e")

        # Button to generate the configuration
        generate_button = ttk.Button(master, text="Generate VZ profile Config", command=lambda: generate_config(self.state_entry))
        generate_button.grid(row=18, column=0, padx=40, pady=5, sticky="e")

        # Create input field for foritage ip
        self.usable_in_cidr_fortigate = ttk.Entry(master, font=("Helvetica", 12), width=20)
        self.usable_in_cidr_fortigate.grid(row=20, column=1, padx=5, pady=5)
        
        # Button to generate the foritgate link
        copy_link_button = ttk.Button(master, text="Fortigate Link", command= self.generate_fortigate_link)
        copy_link_button.grid(row=25, column=1, padx=40, pady=5)

        # Create input fields for parameters
        tk.Label(master, text="RSSI (dBm):").grid(row=27, column=0, padx=5, pady=5, sticky="w")
        self.rssi_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.rssi_entry.grid(row=27, column=1, padx=5, pady=5)

        # Create a button to calculate signal strength
        self.calculate_button = ttk.Button(master, text="Calculate RSSI", command= lambda: signalstrength.calculate_rssi_signal_strength(self.rssi_entry))
        self.calculate_button.grid(row=29, columnspan=2, pady=5)

        # Create input fields for parameters
        tk.Label(master, text="SNR (dB):").grid(row=30, column=0, padx=5, pady=5, sticky="w")
        self.snr_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.snr_entry.grid(row=30, column=1, padx=5, pady=5)

        # Create a button to calculate signal strength
        self.calculate_button = ttk.Button(master, text="Calculate SNR", command= lambda: signalstrength.calculate_snr_signal_strength(self.snr_entry))
        self.calculate_button.grid(row=31, columnspan=2, pady=5)

        # Create input fields for parameters
        tk.Label(master, text="RSRQ (dB):").grid(row=32, column=0, padx=5, pady=5, sticky="w")
        self.rsrq_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.rsrq_entry.grid(row=32, column=1, padx=5, pady=5)

        # Create a button to calculate signal strength
        self.calculate_button = ttk.Button(master, text="Calculate RSRQ", command= lambda: signalstrength.calculate_rsrq_signal_strength(self.rsrq_entry))
        self.calculate_button.grid(row=33, columnspan=2, pady=5)

        # Create input fields for parameters
        tk.Label(master, text="RSRP (dBm):").grid(row=34, column=0, padx=5, pady=5, sticky="w")
        self.rsrp_entry = tk.Entry(master, font=("Helvetica", 12), width=20)
        self.rsrp_entry.grid(row=34, column=1, padx=5, pady=5)

        # Create a button to calculate signal strength
        self.calculate_button = ttk.Button(master, text="Calculate RSRP", command= lambda: signalstrength.calculate_rsrp_signal_strength(self.rsrp_entry))
        self.calculate_button.grid(row=35, columnspan=2, pady=5)

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: generate_config(self.state_entry))


    def calculate_network_cidr(self):
        usable_cidr = self.usable_in_cidr.get()
        try:
            network_cidr = IPv4Network(usable_cidr, strict=False)
            host_bits = network_cidr.max_prefixlen - network_cidr.prefixlen
            calculated_cidr = IPv4Network(f"{network_cidr.network_address}/{32 - host_bits}", strict=False)
            self.network_in_cidr.delete(0, tk.END)
            self.network_in_cidr.insert(0, str(calculated_cidr))

        except ValueError:
            messagebox.showerror("Invalid Input", "Usable CIDR must be a valid IPv4 address in the format 192.168.1.1/24") 

    # Opens up the fortigate GUI loging page via usable 
    def generate_fortigate_link(self) :
        usable_in_cidr_fortigate = self.usable_in_cidr_fortigate.get()
        self.open_link(f"https://{usable_in_cidr_fortigate}:60481")
    
    def open_link(usable_in_cidr_fortigate, link):
        webbrowser.open(link)             

    # Define copy_initial_command as a method of IMEICommandGenerator
    def copy_initial_command(self):
        initial_command = "show interface lte detail | match IMEI"
        pyperclip.copy(initial_command)
        messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")