import tkinter as tk
from tkinter import messagebox, ttk
import requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to get connected devices
def get_connected_devices():
    try:
        url = f"https://{fortigate_ip}/api/v2/monitor/firewall/user/device"
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers, verify=True)  # Ensure SSL verification
        response.raise_for_status()
        devices = response.json().get('results', [])
        display_devices(devices)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve devices: {e}")
        messagebox.showerror("Error", f"Failed to retrieve devices: {e}")


# Function to display the connected devices in the treeview
def display_devices(devices):
    for row in tree.get_children():
        tree.delete(row)
    for device in devices:
        tree.insert("", "end", values=(device['mac'], device['ip'], device['hostname'], device['type']))


# Function to remove a device
def remove_device():
    mac_address = mac_entry.get()

    if not mac_address:
        messagebox.showwarning("Input Error", "Please enter the MAC address to remove")
        return

    try:
        url = f"https://{fortigate_ip}/api/v2/monitor/firewall/user/device/{mac_address}"
        headers = {
            "Authorization": f"Bearer {api_token}",
        }
        response = requests.delete(url, headers=headers, verify=True)  # Ensure SSL verification
        response.raise_for_status()
        messagebox.showinfo("Success", "Device removed successfully")
        get_connected_devices()  # Refresh the device list
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to remove device: {e}")
        messagebox.showerror("Error", "Failed to remove device")


# Function to assign a static IP to a device
def assign_static_ip():
    mac_address = mac_entry.get()
    static_ip = static_ip_entry.get()

    if not mac_address or not static_ip:
        messagebox.showwarning("Input Error", "Please enter both MAC address and Static IP")
        return

    try:
        url = f"https://{fortigate_ip}/api/v2/monitor/firewall/user/device/{mac_address}"
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "ip": static_ip
        }
        response = requests.put(url, headers=headers, json=payload, verify=True)  # Ensure SSL verification
        response.raise_for_status()
        messagebox.showinfo("Success", "Static IP assigned successfully")
        get_connected_devices()  # Refresh the device list
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to assign static IP: {e}")
        messagebox.showerror("Error", "Failed to assign static IP")


# Function to connect to the FortiGate device
def connect():
    global fortigate_ip, api_token
    fortigate_ip = fortigate_ip_entry.get()
    api_token = api_token_entry.get()

    if not fortigate_ip or not api_token:
        messagebox.showwarning("Input Error", "Please enter both FortiGate IP and API Token")
        return

    get_connected_devices()


# GUI Setup
root = tk.Tk()
root.title("FortiGate Device Monitoring")

# Frame for FortiGate connection details
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="FortiGate IP:").grid(row=0, column=0, padx=5, pady=5)
fortigate_ip_entry = tk.Entry(frame)
fortigate_ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="API Token:").grid(row=1, column=0, padx=5, pady=5)
api_token_entry = tk.Entry(frame, show="*")
api_token_entry.grid(row=1, column=1, padx=5, pady=5)

connect_button = tk.Button(frame, text="Connect", command=connect)
connect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Frame for device details
device_frame = tk.Frame(root)
device_frame.pack(pady=10)

tk.Label(device_frame, text="MAC Address:").grid(row=0, column=0, padx=5, pady=5)
mac_entry = tk.Entry(device_frame)
mac_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(device_frame, text="Static IP:").grid(row=1, column=0, padx=5, pady=5)
static_ip_entry = tk.Entry(device_frame)
static_ip_entry.grid(row=1, column=1, padx=5, pady=5)

remove_button = tk.Button(device_frame, text="Remove Device", command=remove_device)
remove_button.grid(row=2, column=0, pady=10)

assign_button = tk.Button(device_frame, text="Assign Static IP", command=assign_static_ip)
assign_button.grid(row=2, column=1, pady=10)

# Treeview for displaying connected devices
columns = ("MAC Address", "IP Address", "Hostname", "Device Type")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("MAC Address", text="MAC Address")
tree.heading("IP Address", text="IP Address")
tree.heading("Hostname", text="Hostname")
tree.heading("Device Type", text="Device Type")
tree.pack(pady=10)

# Main loop
root.mainloop()
