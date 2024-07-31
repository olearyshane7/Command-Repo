import tkinter as tk
from tkinter import messagebox
import pyperclip
import logging
from ipaddress import IPv4Network

class InvalidIPException(Exception):
    pass

def generate_ip_config_tree(usable_ip, gw_ip, subnet_mask):
        
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
exec batch start
config log fortianalyzer setting
unset source-ip 
end
config system interface
edit "wan1"
set mode static
set ip {usable_ip} {subnet_mask}
next
end
config router static
edit 1        
set gateway {gw_ip}
next
edit 9        
set gateway {gw_ip}
next
edit 11
set gateway {gw_ip}
next
edit 14
set gateway {gw_ip}
next
end
config system link-monitor
edit "WAN1"
set gateway-ip {gw_ip}
next
end
exec batch end
"""
        
        pyperclip.copy(config_ip_fortigate_template)

        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")