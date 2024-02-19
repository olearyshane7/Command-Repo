import tkinter as tk
from tkinter import scrolledtext, messagebox


def generate_values_and_display(group):
    generated_values = generate_values_for_group(group)

    # Combine all values into one string
    result_text = "\n".join([f"{member}: {data}" for member, data in generated_values.items()])

    # Create a new window for displaying values
    display_window = tk.Toplevel()
    display_window.title("Generated Values")

    # Create a scrolled text widget to display values
    text_widget = scrolledtext.ScrolledText(display_window, width=40, height=10, wrap=tk.WORD)
    text_widget.insert(tk.END, result_text)
    text_widget.pack(padx=10, pady=10)

    # Create a button to copy values to the clipboard
    copy_button = tk.Button(display_window, text="Copy to Clipboard", command=lambda: copy_to_clipboard(result_text, display_window))
    copy_button.pack(pady=10)

def copy_to_clipboard(text, window):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    
    # Close the display window and show success message
    window.destroy()
    messagebox.showinfo("Success", "Values copied to clipboard!")

# Function to generate values for the selected group
def generate_values_for_group(group):
    values = {}

    for member in group:
        if member == "LHC Group":
            router_value = "GFLEX-1000-4C8R-LTE"
            access_point_value = None
            switch_value = None
            switch_value2 = None
        elif member == "Western Shamrock":
            router_value = "GFLEX-1000-4C8R-LTE"
            access_point_value = "AP33-US"
            switch_value = "EX2300-C-12P"
            switch_value2 = "EX2300-24P"
        else:
            router_value = None
            access_point_value = None
            switch_value = None
            switch_value2 = None

        values[member] = {
            "Router": router_value,
            "Access Point": access_point_value,
            "Switch": switch_value,
            "Switch2": switch_value2
        }

    return values

# Create the main window
root = tk.Tk()
root.title("Group Selector")
root.geometry("300x200")

# Create buttons for each group
button_lhc = tk.Button(root, text="LHC Group", command=lambda: generate_values_and_display(["LHC Group"]))
button_western_shamrock = tk.Button(root, text="Western Shamrock", command=lambda: generate_values_and_display(["Western Shamrock"]))

# Place the buttons in the main window
button_lhc.pack(pady=10)
button_western_shamrock.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
