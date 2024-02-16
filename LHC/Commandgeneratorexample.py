import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import logging

class IMEICommandGenerator:
    def __init__(self, master):
        self.master = master
        master.title("IMEI Command Generator")

        # Button to copy the initial command
        tk.Button(master, text="Get IMEI Command", command=self.copy_initial_command).grid(row=0, column=0, columnspan=2, pady=10)

        # Create input field for IMEI
        tk.Label(master, text="IMEI:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.imei_entry = tk.Entry(master)
        self.imei_entry.grid(row=1, column=1, padx=5, pady=5)

        # Define the commands for each action
        self.commands = {
            "Swap to Port 1": "maintenance lte-at IMEI AT!UIMS=0",
            "Swap to Port 2": "maintenance lte-at IMEI AT!UIMS=1",
            "Check APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT\?",
            "Flush APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT=1",
            "Reboot the LTE Modem": "maintenance lte-at IMEI AT+CFUN=6",
            "Check which sim slot is being used": "maintenance lte-at IMEI AT\!UIMS\?",
            "TMO/ATT Firmware Update": "maintenance lte-at IMEI AT!IMPREF=\"GENERIC\"",
            "Verizon Firmware Update": "maintenance lte-at IMEI AT!IMPREF=\"VERIZON\""
        }

        # Create buttons for each action to generate the command
        row_num = 2
        for action, command in self.commands.items():
            tk.Label(master, text=action).grid(row=row_num, column=0, padx=5, pady=5, sticky="w")
            tk.Button(master, text="Generate", command=lambda a=action: self.generate_command(a)).grid(row=row_num, column=1, padx=5, pady=5)
            row_num += 1

    def generate_command(self, action):
        imei = self.imei_entry.get()

        # Array of randomly generated error messages
        # Commented error messages are passive aggressive statements. 
        # Only activate commented error messages if you have a strong heart and mind.

        # IMEI is blank
        self.error_messages = [
            # "I can't even with you right now.",
            # "Do you not know how to copy and paste properly?",
            # "Arthas did nothing wrong",
            # "You're wasting your time. Populate the IMEI properly.",
            # "What is your IQ?",
            # "Just have somebody else swap for you.."
            "It's Blank.",
            "Please, Populate the field",
            "You forgot to type in the IMEI",
            "Boss Ahead",
            "NANI???"
        ]
        
        # IMEI is short
        self.short_error_messages = [
            # "I'm being as lazy as you are with these error messages",
            # "Did you not learn how to use a computer as a child?",
            # "Are you blind?",
            # "Can you do anything right?",
            # "What came first, the messed up IMEI command or the failed SIM Swap?"
            "The Etruscan shrew is the smallest mammal on earth, much like the IMEI input",
            "The IMEI is too short.",
            "Try again, it's too short",
            "Generally the playoff run of the Toronto Maple Leafs."
        ]

        # IMEI is long
        self.long_error_messages = [
            # "Your power level is clearly under 9000.",
            # "Fact: That input was trash."
            "The IMEI is too long.",
            "Try again, it's too long.",
            "It's an IMEI number not a python. Shorten it to 15 integers",
            "I always got yelled at for keeping the fridge open too long."
        ]

        # IMEI has a letter
        self.letter_error_messages = [
            # "Failure ahead...",
            # "It's alright. It's been a long day.",
            # "If you input the IMEI properly next time, you'll successfully complete the sim swap.",
            # "Did you input it correctly?",
            # "Try again!"
            "Check for letters.",
            "The IMEI can only be integers",
            "Please delete any letters",
            ""
        ]

        # Configure the logging
        logging.basicConfig(filename='error.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


        # IMEI code empty error
        if not imei:
            self.show_random_error()
            logging.debug("An error occurred: Blank box", self) 
            return
        
        # IMEI code too short
        if len(imei) < 15:
            self.show_random_short_error()
            logging.debug("An error occurred: Too short", self) 
            return
        
        # IMEI code is too long  
        if len(imei) > 15:
            self.show_random_long_error()
            logging.debug("An error occurred: too long", self)
            return

        # IMEI code has a letter in it
        if not imei.isdigit():
            self.show_random_letter_error()
            logging.debug("An error occurred: contains a letter", self) 
            return
        
        command = self.commands[action]
        
        # Special handling for swap commands to change the last character
        if action.startswith("Swap to"):
            last_char = "1" if action.endswith("2") else "0"
            command = command[:-1] + last_char
        
        command_with_imei = command.replace("IMEI", imei)
        
        # Special handling for the last command to ensure correct formatting
        if action == "TMO/ATT Firmware Update" or action == "Verizon Firmware Update":
            command_with_imei = command_with_imei.replace("\\", "\\\\").replace("\"", "\\\"")
        
        pyperclip.copy(command_with_imei)
        
        # Display the formatted command in a messagebox
        messagebox.showinfo(action, f"Congratulations! You know how to copy and paste!\n\n{command_with_imei}")

    def copy_initial_command(self):
        initial_command = "show interface lte detail | match IMEI"
        pyperclip.copy(initial_command)
        messagebox.showinfo("IMEI Command", f"IMEI command copied to clipboard:\n\n{initial_command}")


    def show_random_error(self):
        random_error = random.choice(self.error_messages)      
        messagebox.showerror("Error", random_error) 

    # IMEI Short Error messages
    def show_random_short_error(self):
        random_error = random.choice(self.short_error_messages)
        messagebox.showerror("Error", random_error) 
    
    # IMEI Long Error messages
    def show_random_long_error(self):
        random_error = random.choice(self.long_error_messages)
        messagebox.showerror("Error", random_error) 

    # IMEI String error messages
    def show_random_letter_error(self):
        random_error = random.choice(self.letter_error_messages)
        messagebox.showerror("Error", random_error)         

# Create the main window
root = tk.Tk()

# Create an instance of the IMEICommandGenerator class
app = IMEICommandGenerator(root)

# Run the Tkinter event loop
root.mainloop()

