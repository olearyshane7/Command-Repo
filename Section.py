from tkinter import ttk

class Section(ttk.Labelframe):
    def __init__(self, master, title, *args, **kwargs):
        super().__init__(master, text=title, *args, **kwargs)