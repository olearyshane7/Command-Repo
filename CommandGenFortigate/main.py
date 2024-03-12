import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import END
from forticommandGen import forticommandGen

# Create the main window
root = tk.Tk()

# Create an instance of the IMEICommandGenerator class
app = forticommandGen(root)

# Run the Tkinter event loop
root.mainloop()