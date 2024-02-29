from tkinter import messagebox
import pyperclip
import logging
from calculateNetworkIP import calculate_network_ip
from ipaddress import IPv4Network, IPv4Address


class InvalidIPException(Exception):
    pass

def generate_ip_config(ip_interface, usable_in_cidr, vrf_number, gw_ip, network_in_cidr):
    ip_interface = ip_interface.get().upper()
    usable_in_cidr = usable_in_cidr.get().upper()
    vrf_number = int(vrf_number.get().upper())
    gw_ip = gw_ip.get().upper()
    network_in_cidr = network_in_cidr.get().upper()

    if not all([ip_interface, usable_in_cidr, vrf_number, gw_ip, network_in_cidr]):
        messagebox.showerror("Incomplete Input", "All fields must be filled.")
        logging.debug("Empty Boxes")
        raise InvalidIPException(f"One of the boxes is empty")

    # Determine the subnet mask
    if '/' in network_in_cidr:
        # The network is already in CIDR notation
        subnet_cidr = int(network_in_cidr.split('/')[1])
        subnet_mask = IPv4Network(f"0.0.0.0/{subnet_cidr}").netmask
    else:
        # The subnet mask is in dotted decimal notation
        subnet_mask = IPv4Address(network_in_cidr).netmask

    # Calculate the network IP based on the gateway IP and subnet mask
    network_ip = calculate_network_ip(gw_ip, str(subnet_mask))

    config_ip_template = f"""
interface ip {ip_interface}
    ip-addr {usable_in_cidr}/{subnet_mask}
    back

vrf "public-vrf-{vrf_number}"
    ip-route 0.0.0.0/0
        gateway "{gw_ip}"
    back

ip-route {network_ip}/{subnet_mask}
    interface "{ip_interface}"
    back

applications
    hybrid-wan
        profile basic
            interfaces
                wan-port {ip_interface}
                    gateway-ip {gw_ip}
            commit
"""

    pyperclip.copy(config_ip_template)

    messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")

    return config_ip_template