import tkinter as tk
from tkinter import messagebox
import pyperclip
import logging
from ipaddress import IPv4Network

class InvalidIPException(Exception):
    pass

def generate_ip_config( usable_in_cidr, gw_ip, network_in_cidr):
        
        usable_in_cidr = usable_in_cidr.get().upper()
        gw_ip = gw_ip.get().upper()
        network_in_cidr = network_in_cidr.get().upper()

        if not all([usable_in_cidr, gw_ip, network_in_cidr]):
            messagebox.showerror("Incomplete Input", "All fields must be filled.")
            logging.debug("Empty Boxes")
            raise InvalidIPException(f"One of the boxes is empty") 
        # usable ip
        try:
            IPv4Network(usable_in_cidr, strict=False)
        except ValueError:
            messagebox.showerror("Invalid Input", "Usable CIDR must be a valid IPv4 address in the format 192.168.1.1/24")
            return
        # gw_ip
        try:
            IPv4Network(gw_ip, strict=False)
        except ValueError:
            messagebox.showerror("Invalid Input", "Gateway must be a valid IPv4 address in the format 192.168.1.1/24")
            return

        #  Netowrk cidr
        try:
            IPv4Network(network_in_cidr, strict=False)
        except ValueError:
            messagebox.showerror("Invalid Input", "Network cidr must be a valid IPv4 address in the format 192.168.1.1/24")
            return

        config_ip_template = f"""
interface ip ip-2
ip-addr {usable_in_cidr}
back
--------------------------------------
vrf "public-vrf-2"
ip-route 0.0.0.0/0
gateway "{gw_ip}"
back
--------------------------------------
ip-route {network_in_cidr}
interface "ip-2"
back
--------------------------------------
applications
hybrid-wan
profile basic
interfaces
wan-port ip-2
gateway-ip {gw_ip}
commit
"""
        
        pyperclip.copy(config_ip_template)

        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")

