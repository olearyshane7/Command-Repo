import tkinter as tk
from tkinter import ttk
from SystemSection import SystemSection
from NetworkSection import NetworkSection
from TrafficProcessingSection import TrafficProcessingSection  # Import the Traffic Processing section
from HighAvailabilitySection import HighAvailabilitySection    # Import the High Availability section

class FortiGateCheatSheetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('FortiGate CLI Cheat Sheet')
        self.create_tabs()

    def create_tabs(self):
        tab_control = ttk.Notebook(self)
        
        # Initialize all Sections
        system_tab = SystemSection(tab_control)
        network_tab = NetworkSection(tab_control)
        traffic_processing_tab = TrafficProcessingSection(tab_control)  # Add Traffic Processing tab
        high_availability_tab = HighAvailabilitySection(tab_control)    # Add High Availability tab
        
        # Add tabs to Notebook
        tab_control.add(system_tab, text='System')
        tab_control.add(network_tab, text='Network')
        tab_control.add(traffic_processing_tab, text='Traffic Processing')  # Add Traffic Processing tab
        tab_control.add(high_availability_tab, text='High Availability')    # Add High Availability tab
        
        tab_control.pack(expand=1, fill='both')

if __name__ == '__main__':
    app = FortiGateCheatSheetApp()
    app.mainloop()