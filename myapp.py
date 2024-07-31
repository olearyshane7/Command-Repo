import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
# command_generator.py
from IMEICommandGenerator import IMEICommandGenerator

# def config_button_click():

root = tk.Tk()
app = IMEICommandGenerator(root)
root.mainloop()

# def fg_button_click():

#      # Move the relevant code here 	
#      root = tk.Tk()
#      root.mainloop()    
# Create the main window
# root = tk.Tk()

# Increase the window size
# root.geometry("200x200")

# Create a button with the label "config" that calls the config_button_click function when clicked
# config_button = ttk.Button(root, text="config", command=config_button_click)
# config_button.pack()

# Run the Tkinter event loop
# root.mainloop()

#test IP subnet
#123.123.12.134/24
#255.255.255.252