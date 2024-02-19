import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging


class InvalidStateException(Exception):
    pass

class InvalidIMEIException(Exception):
    pass

class IMEICommandGenerator:
    def __init__(self, master):
        self.master = master
        master.title("IMEI Command Generator")

        # Button to copy the initial command
        ttk.Button(master, text="Get IMEI Command", command=self.copy_initial_command).grid(row=0, column=0, columnspan=2, pady=10)

        # Create input field for IMEI
        ttk.Label(master, text="IMEI:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.imei_frame = ttk.Frame(master, relief="groove", borderwidth=2)
        self.imei_frame.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.imei_entry = ttk.Entry(self.imei_frame, font=("Helvetica", 12), width=17)
        self.imei_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        master.geometry("500x500")  # Set initial window size

        self.row_num = 2

        # Set a pleasing color scheme
        master.configure(bg="#E6E6FA")

        # Adjust column weights to make resizing look better
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

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

        self.row_num = 2

        # Create buttons for each action to generate the command
        for action, command in self.commands.items():
            ttk.Label(master, text=action).grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
            ttk.Button(master, text="Generate", command=lambda a=action: self.generate_command(a)).grid(row=self.row_num, column=1, padx=5, pady=5)
            self.row_num += 1

        # Create input field for State
        ttk.Label(master, text="VZ-APN State:").grid(row=self.row_num, column=0, padx=5, pady=5, sticky="w")
        self.state_entry = ttk.Entry(master, font=("Helvetica", 12), width=20) 
        self.state_entry.grid(row=self.row_num, column=1, padx=5, pady=5)

        # Button to generate the configuration
        generate_button = ttk.Button(master, text="Generate VZ profile Config", command=self.generate_config)
        generate_button.grid(row=self.row_num + 1, columnspan=2, pady=10)

        # Bind the <Return> key to the generate_config function
        self.state_entry.bind("<Return>", lambda event: self.generate_config())

    # Function to generate and copy the configuration for changing to the proper region based on the state input
    def generate_config(self):
        state = self.state_entry.get().upper()

        # Set the filepath for the error log
        self.error_log_filepath = "error.log"

        # Configure the logging
        logging.basicConfig(filename=self.error_log_filepath, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        
        valid_states = ['AK', 'WA', 'MT', 'OR', 'ID', 'WY', 'NV', 'CA', 'AZ', 'NM',
                        'TX', 'OK', 'AR', 'LA', 'MS', 'TN', 'AL', 'GA', 'SC', 'NC', 'FL',
                        'ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'MI', 'IN', 'IL', 'KY', 'OH', 'PA', 'WV',
                        'ME', 'VT', 'NH', 'MA', 'CT', 'RI', 'NY', 'PA', 'NJ', 'DE', 'DC', 'MD', 'VA']
        try:
            if state not in valid_states:
                raise InvalidStateException(f"Invalid state entered: {state}")
        except InvalidStateException as e:
            messagebox.showerror("Error", str(e))
            logging.debug(str(e)) 
            return    
        
        apn_mappings = {
            "Region1": ['AK', 'WA', 'MT', 'OR', 'ID', 'WY', 'NV', 'CA'],
            "Region2": ['AZ', 'NM', 'TX', 'OK', 'AR', 'LA', 'MS', 'TN', 'AL', 'GA', 'SC', 'NC', 'FL'],
            "Region3": ['ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'MI', 'IN', 'IL', 'KY', 'OH', 'PA', 'WV'],
            "Region4": ['ME', 'VT', 'NH', 'MA', 'CT', 'RI', 'NY', 'PA', 'NJ', 'DE', 'DC', 'MD', 'VA']
        }

        # Define the APN mappings for each region
        apn_mappings = {
            'WE': ['WE01.VZWSTATIC'],
            'MW': ['MW01.VZWSTATIC'],
            'SO': ['SO01.VZWSTATIC'],
            'NE': ['NE01.VZWSTATIC']
        }

        # Update the APN lists for each region
        apn_mappings['WE'].extend(['AK', 'WA', 'MT', 'OR', 'ID', 'WY', 'NV', 'CA', 'AZ', 'NM'])
        apn_mappings['SO'].extend(['TX', 'OK', 'AR', 'LA', 'MS', 'TN', 'AL', 'GA', 'SC', 'NC', 'FL'])
        apn_mappings['MW'].extend(['ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'MI', 'IN', 'IL', 'KY', 'OH', 'PA', 'WV'])
        apn_mappings['NE'].extend(['ME', 'VT', 'NH', 'MA', 'CT', 'RI', 'NY', 'PA', 'NJ', 'DE', 'DC', 'MD', 'VA'])

        for region, states in apn_mappings.items():
            if state in states:
                regional_apn = states[0]
                break

        config_template = f"""
configure
    pdp-profile "VZ-Static"
        apn-id "1"
            apn {regional_apn}
            back
        mobile-country-code "311"
        mobile-network-code "480"
        back
    commit
main"""
        pyperclip.copy(config_template)
        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")
            

    def generate_command(self, action):
        imei = self.imei_entry.get()

        # Set the filepath for the error log
        self.error_log_filepath = "error.log"

        # Configure the logging
        logging.basicConfig(filename=self.error_log_filepath, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
            "Please delete any letters"
           
        ]
        

        # IMEI code empty error
        if not imei:
            self.show_random_error()
            logging.debug(f"An error occurred: Blank box")
            return  
        
        # IMEI code too short
        if len(imei) < 15:
            self.show_random_short_error()
            logging.debug(f"An error occurred: IMEI too short")
            return
        
        # IMEI code is too long  
        if len(imei) > 15:
            self.show_random_long_error()
            logging.debug(f"An error occurred: IMEI too long")
            return

        # IMEI code has a letter in it
        if not imei.isdigit():
            self.show_random_letter_error()
            logging.debug(f"An error occurred: Includes a letter.")
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
        messagebox.showinfo(action, f"IMEI command copied to clipboard:\n\n{command_with_imei}")

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
