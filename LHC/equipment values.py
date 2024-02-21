import tkinter as tk
from tkinter import scrolledtext, messagebox
from MainConfig import ConfigTemplate

class GroupSelectorApp(tk.Tk):
    def __init__(self, config_template):
        super().__init__()
        self.title("Group Selector")
        self.geometry("300x200")
        self.config_template = config_template

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)

        self.create_buttons()

    def create_buttons(self):
        for group_name in self.config_template.config_template.keys():
            button = tk.Button(self.button_frame, text=group_name, command=lambda name=group_name: self.generate_and_display_values(name))
            button.pack(side=tk.LEFT, padx=10)

        # Comment for example

    def generate_and_display_values(self, group_name):
        generated_values = self.generate_values_for_group(group_name)

        # Combine all values into one string
        result_text = "\n".join([f"{member}: {data}" for member, data in generated_values.items()])

        # Create a new window for displaying values
        display_window = tk.Toplevel(self)
        display_window.title("Generated Values")

        # Create a scrolled text widget to display values
        text_widget = scrolledtext.ScrolledText(display_window, width=40, height=10, wrap=tk.WORD)
        text_widget.insert(tk.END, result_text)
        text_widget.pack(padx=10, pady=10)

        # Create a button to copy values to the clipboard
        copy_button = tk.Button(display_window, text="Copy to Clipboard", command=lambda: self.copy_to_clipboard(result_text, display_window))
        copy_button.pack(pady=10)

    def copy_to_clipboard(self, text, window):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

        # Close the display window and show success message
        window.destroy()
        messagebox.showinfo("Success", "Values copied to clipboard!")

    def generate_values_for_group(self, group_name):
        return self.config_template.config_template.get(group_name, {})


if __name__ == "__main__":
    config_template = ConfigTemplate()
    app = GroupSelectorApp(config_template)
    app.mainloop()
