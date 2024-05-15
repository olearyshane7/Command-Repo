import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random
import logging
from tkinter.constants import END
# command_generator.py
from IMEICommandGenerator import IMEICommandGenerator
from FortiGateCheatSheetApp import FortiGateCheatSheetApp

# def lhc_button_click():

root = tk.Tk()
app = IMEICommandGenerator(root)
root.mainloop()

# def fg_button_click():

#      # Move the relevant code here
#      root = tk.Tk()
#      app = FortiGateCheatSheetApp(root)
#      root.mainloop()    
# Create the main window
# root = tk.Tk()

# Increase the window size
# root.geometry("200x200")

# Create a button with the label "lhc" that calls the lhc_button_click function when clicked
# lhc_button = ttk.Button(root, text="lhc", command=lhc_button_click)
# lhc_button.pack()

# fg_button = ttk.Button(root, text="fortigate", command=fg_button_click)
# fg_button.pack()

# Run the Tkinter event loop
# root.mainloop()
