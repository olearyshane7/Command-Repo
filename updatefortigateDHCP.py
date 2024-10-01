import tkinter as tk
from tkinter import messagebox
import pyperclip
import logging
from ipaddress import IPv4Network

class InvalidIPException(Exception):
    pass

def generate_ip_config2_dhcp_fortigate():
        

        config_ip_fortigate_dhcp_template = f"""
config system interface
edit port2
set priority 10
set dns-server-override disable
next
edit port3
set priority 20
set allowaccess https ping FMG-access
next
end
 
config router static
edit 3
set device port2
next
end
 
config system sdwan
config members
edit 3
set interface port2
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
        
        pyperclip.copy(config_ip_fortigate_dhcp_template)

        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")