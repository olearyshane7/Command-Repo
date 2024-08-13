import tkinter as tk
import pyperclip

# Define initial text options
text_options = {
    "LHC": "Tech: {Tech} \n Call started on time. Tech tested the modem prior to the start of call and got the correct speeds. Moved ahead to connecting the router to the FE. Tested LTE and tech went ahead and worked with LHC rep on the cutover and tested all the equipment on site. TU successful\n Followup: not required.",
    "LHC Failed SIM": "Tech: {Tech} \n Call started on time. Tech tested the modem prior to the start of call and got the correct speeds. Moved ahead to connecting the router to the FE. Tested LTE, but didn't get any solid strong signal for failover. Tech went ahead and worked with LHC rep on the cutover and tested all the equipment on site LTE is pending. TU successful\n Followup: not required.",
    "Hanger success EZ": "Tech: {Tech} \n Call started on time. Confirmed modem worked properly and moved on to the TU. Connected the modem to port 5 on the router and waited for connection to be shown on mist. When we saw connection on the primary we moved on to connecting the switch from port 4 to port 23. Once it was connected and we pulled the switch config successfully, we moved onto the cutover. Powered down their existing equipment and plugged the new Juniper AP into the switch to check connectivity. After AP connection verified and AP upgraded, we swapped the connections over to the new switch. Tech tested all of the equipment and packed up the equipment. TU success.\n No followup required.",
    "Hanger switch issue": "Tech: {Tech} \n Call started on time. Confirmed modem worked properly and moved on to the TU. Confirmed connection to the router via mist. When we saw connection on the router up, we moved on to connecting the switch from port 4 to port 23. The switch wasn't pulling the config so we plugged the router into the management port and configured a dhcp network to pull the new switch config. Once it was connected and we pulled the switch config successfully, we moved onto the cutover. Powered down their existing equipment and plugged the new Juniper AP into the switch to check connectivity. After AP connection verified and AP upgraded, we swapped the connections over to the new switch. Tech tested all of the equipment and packed up the equipment. TU success.\n No followup required.",
    "USPS Fortiswitch 2 switch": "Tech: {Tech} \n Connected circuits to their proper switch ports and moved onto testing speeds on port 2 and port 3 of the switches. TU success\n No followup required",
    "USPS Fortiswitch 1 switch": "Tech: {Tech} \n Connected circuit to the switch on port 1 and moved onto testing speeds on port 2 and port 3 of the switches. TU success\n No followup required"
}

# Function to copy text to clipboard
def copy_text(text):
    pyperclip.copy(text)
    print(f"Copied to clipboard: {text}")

# Function to handle button clicks
def on_button_click(option):
    tech_name = entry.get()
    if not tech_name:
        copy_text("Error: No name entered.")
        return

    text = text_options.get(option, "Option not found.")
    # Substitute {Tech} with the entered name
    text = text.replace("{Tech}", tech_name)
    copy_text(text)

# Create the main application window
root = tk.Tk()
root.title("Text Copier App")
root.geometry("400x400")

# Create an entry widget for the tech name
entry_label = tk.Label(root, text="Enter Tech Name:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add buttons for each option
options = [
    "LHC", 
    "LHC Failed SIM", 
    "Hanger success EZ", 
    "Hanger switch issue", 
    "USPS Fortiswitch 2 switch", 
    "USPS Fortiswitch 1 switch"
]

for option in options:
    button = tk.Button(button_frame, text=option, command=lambda opt=option: on_button_click(opt))
    button.pack(pady=5)

# Run the application
root.mainloop()