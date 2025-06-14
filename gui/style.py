from tkinter import ttk

def set_style(root):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Segoe UI', 11), padding=6)
    style.configure('TLabel', font=('Segoe UI', 11), background="#f6f8fa")
    style.configure('TFrame', background="#f6f8fa")
    root.configure(bg="#f6f8fa")
