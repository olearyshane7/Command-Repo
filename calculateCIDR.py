from ipaddress import IPv4Network, NetmaskValueError
from tkinter import messagebox

def calculate_cidr(subnet_mask_input):
    try:
        cidr = IPv4Network(f"0.0.0.0/{subnet_mask_input}", strict=False).prefixlen
        return cidr
    except NetmaskValueError:
        # Invalid subnet mask
        messagebox.showerror("Invalid Input", "Invalid subnet mask entered.")
        return None
