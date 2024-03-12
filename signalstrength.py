import tkinter as tk
from tkinter import ttk, messagebox

class signalstrength:

    def calculate_rssi_signal_strength(rssi_entry):
            rssi = float(rssi_entry.get().upper())

            if rssi >= -65:
                signal_strength = "Excellent"
            elif -65 > rssi >= -75:
                signal_strength = "Good"
            elif -75 > rssi >= -85:
                signal_strength = "Medium"
            elif -85 > rssi >= -95:
                signal_strength = "Weak"
            else:
                signal_strength = "No Signal"

            messagebox.showinfo("Signal Strength", f"Signal Strength: {signal_strength}")

    def calculate_snr_signal_strength(snr_entry):
            snr = float(snr_entry.get().upper())
           
            # Compare SNR value with thresholds and determine signal strength level
            if snr >= 20:
                signal_strength = "Excellent"
            elif 13 <= snr < 20:
                signal_strength = "Good"
            elif 0 <= snr < 13:
                signal_strength = "Weak"
            elif snr < 0:
                signal_strength = "Very Low"
            else:
                signal_strength = "Unknown"
            messagebox.showinfo("Signal Strength", f"Signal Strength: {signal_strength}")

    def calculate_rsrq_signal_strength(rsrq_entry):
            rsrq = float(rsrq_entry.get().upper())
            # Compare RSRQ value with thresholds and determine signal strength level
            if rsrq >= -10:
                signal_strength = "Excellent"
            elif -10 >= rsrq > -15:
                signal_strength = "Good"
            elif -15 >= rsrq > -20:
                signal_strength = "Weak"
            elif rsrq <= -20:
                signal_strength = "Very Low"
            else:
                signal_strength = "Unknown"
            messagebox.showinfo("Signal Strength", f"Signal Strength: {signal_strength}") 

    def calculate_rsrp_signal_strength(rsrp_entry):
    
        rsrp = float(rsrp_entry.get().upper())
            # Compare RSRP value with thresholds and determine signal strength level
        if rsrp >= -80:
            signal_strength = "Excellent"
        elif -80 >= rsrp > -90:
            signal_strength = "Good"
        elif -90 >= rsrp > -100:
            signal_strength = "Weak"
        elif rsrp <= -100:
            signal_strength = "Very Low"
        else:
            signal_strength = "Unknown"
        messagebox.showinfo("Signal Strength", f"Signal Strength: {signal_strength}")
         
