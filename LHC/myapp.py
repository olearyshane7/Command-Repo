import tkinter as tk
from tkinter import messagebox
import pyperclip

# Function to generate and display the command for a specific action
def generate_command(action):
    imei = imei_entry.get()
    command = commands[action]
    
    # Construct the command with the imei
    command_with_imei = command.replace("IMEI", imei)
    
    # Copy the command to the clipboard
    pyperclip.copy(command_with_imei)
    
    # Display the formatted command in a messagebox
    messagebox.showinfo(action, f"Command copied to clipboard:\n\n{command_with_imei}")

# Function to copy the initial command to the clipboard
def copy_initial_command():
    initial_command = "show interface lte detail | match IMEI"
    pyperclip.copy(initial_command)
    messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")

root = tk.Tk()
root.title("IMEI Command Generator")

# Button to copy the initial command
tk.Button(root, text="Get IMEI Command", command=copy_initial_command).grid(row=0, column=0, columnspan=2, pady=10)

# Create input field for IMEI
tk.Label(root, text="IMEI:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
imei_entry = tk.Entry(root)
imei_entry.grid(row=1, column=1, padx=5, pady=5)

# Define the commands for each action
commands = {
    "Swap": "maintenance lte-at IMEI AT!UIMS=1",
    "Check APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT\?",
    "Flush APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT=1",
    "Reboot the LTE Modem": "maintenance lte-at IMEI AT+CFUN=6",
    "Check which sim slot is being used": "maintenance lte-at IMEI AT\!UIMS\?",
    "Run before swapping to TMO": "maintenance lte-at IMEI AT!IMPREF=\"GENERIC\""
}

# Create buttons for each action to generate the command
row_num = 2
for action, command in commands.items():
    tk.Label(root, text=action).grid(row=row_num, column=0, padx=5, pady=5, sticky="w")
    tk.Button(root, text="Generate", command=lambda a=action: generate_command(a)).grid(row=row_num, column=1, padx=5, pady=5)
    row_num += 1

root.mainloop()
