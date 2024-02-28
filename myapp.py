import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
from helpers import generate_config
import command_generator
import command_data
# command_generator.py
from IMEICommandGenerator import IMEICommandGenerator
from MainApp import LHCTool

def lhc_button_click():

    # Move the relevant code here
    root = tk.Tk()
    app = IMEICommandGenerator(root)
    root.mainloop()

# Create the main window
root = tk.Tk()

# Increase the window size
root.geometry("200x200")

# Create a button with the label "lhc" that calls the lhc_button_click function when clicked
lhc_button = ttk.Button(root, text="lhc", command=lhc_button_click)
lhc_button.pack()

# Run the Tkinter event loop
root.mainloop()
