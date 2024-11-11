import tkinter as tk
from tkinter import messagebox
import pyperclip
import logging
from ipaddress import IPv4Network

class InvalidIPException(Exception):
    pass

def generate_ip_config2_fortigate(usable_ip, gw_ip, subnet_mask):
        
        usable_ip = usable_ip.get().upper()
        gw_ip = gw_ip.get().upper()
        subnet_mask = subnet_mask.get().upper()

        if not all([usable_ip, gw_ip, subnet_mask]):
            messagebox.showerror("Incomplete Input", "All fields must be filled.")
            logging.debug("Empty Boxes")
            raise InvalidIPException(f"One of the boxes is empty") 
        # usable ip
        try:
            IPv4Network(usable_ip, strict=False)
        except ValueError:
            messagebox.showerror("Invalid Input", "Usable CIDR must be a valid IPv4 address in the format 192.168.1.1/24")
            return
        # gw_ip
        try:
            IPv4Network(gw_ip, strict=False)
        except ValueError:
            messagebox.showerror("Invalid Input", "Gateway must be a valid IPv4 address in the format 192.168.1.1")
            return


        config_ip_fortigate_template = f"""
config system interface
edit port2
unset mode
set ip {usable_ip} {subnet_mask}
set allowaccess ping https ssh fgfm
next
end

config router static
edit 3
unset dynamic-gateway
set device port2
set gateway {gw_ip}
next
end

config sys sdwan
config members
edit 3
set interface port2
set gateway {gw_ip}
next
end
end

config vpn ipsec phase1-interface
edit SDC-21
set interface port2
next

edit NDC-21
set interface port2
next
end
"""
        
        pyperclip.copy(config_ip_fortigate_template)

        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")