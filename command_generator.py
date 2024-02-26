import pyperclip
import logging
from tkinter import messagebox
import random
from errorlogs import ErrorLogging

class InvalidStateException(Exception):
    pass

class InvalidIMEIException(Exception):
    pass

# Define generate_command as a function
def generate_command(self, action):
    imei = self.imei_entry.get()
    # imeiTestVal = 359820329511503
    # print(imeiTestVal)

    # Set the filepath for the error log
    self.error_log_filepath = "error.log"

    # Configure the logging
    logging.basicConfig(filename=self.error_log_filepath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # IMEI code empty error
    if not imei:
        show_random_error(ErrorLogging.error_messages)
        logging.debug(f"An error occurred: Blank box")
        return

    # IMEI code too short
    if len(imei) < 15:
        show_random_short_error(ErrorLogging.short_error_messages)
        logging.debug(f"An error occurred: IMEI too short")
        return

    # IMEI code is too long
    if len(imei) > 15:
        show_random_long_error(ErrorLogging.long_error_messages)
        logging.debug(f"An error occurred: IMEI too long")
        return

    # IMEI code has a letter in it
    if not imei.isdigit():
        show_random_letter_error(ErrorLogging.letter_error_messages)
        logging.debug(f"An error occurred: Includes a letter.")
        return

    command = self.commands[action]

    # Special handling for swap commands to change the last character
    if action.startswith("Swap to"):
        last_char = "1" if action.endswith("2") else "0"
        command = command[:-1] + last_char

    command_with_imei = command.replace("IMEI", imei)   #this is where the IMEI is being replaced

    # Special handling for the last command to ensure correct formatting
    if action == "TMO/ATT Firmware Update" or action == "Verizon Firmware Update":
        command_with_imei = command_with_imei.replace("\\", "\\\\").replace("\"", "\\\"")

    pyperclip.copy(command_with_imei)

    # Display the formatted command in a messagebox
    messagebox.showinfo(action, f"IMEI command copied to clipboard:\n\n{command_with_imei}")

# Define show_random_error as a function
def show_random_error(error_messages):
    random_error = random.choice(error_messages)
    messagebox.showerror("Error", random_error)

# Define show_random_short_error as a function
def show_random_short_error(short_error_messages):
    random_error = random.choice(short_error_messages)
    messagebox.showerror("Error", random_error)

# Define show_random_long_error as a function
def show_random_long_error(long_error_messages):
    random_error = random.choice(long_error_messages)
    messagebox.showerror("Error", random_error)

# Define show_random_letter_error as a function
def show_random_letter_error(letter_error_messages):
    random_error = random.choice(letter_error_messages)
    messagebox.showerror("Error", random_error)
