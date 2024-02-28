import tkinter as tk
from tkinter import ttk
from IMEICommandGenerator import IMEICommandGenerator

class LHCTool:


    def create_button(self):
        lhc_button = ttk.Button(self.root, text="lhc", command=self.lhc_button_click)
        lhc_button.pack()

    def lhc_button_click(self):
        # Move the relevant code here
        root = tk.Tk()
        app = IMEICommandGenerator(root)
        root.mainloop()