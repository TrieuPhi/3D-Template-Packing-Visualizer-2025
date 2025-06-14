import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("3D Bin Packing Visualizer")
root.geometry("1100x600")
root.configure(bg="#f6f8fa")

# Sidebar
sidebar = tk.Frame(root, bg="#223366", width=260)
sidebar.pack(side="left", fill="y")

logo = tk.Label(sidebar, text="3D Bin Packing", bg="#223366", fg="white", font=("Segoe UI", 18, "bold"))
logo.pack(pady=(30, 20))

ttk.Label(sidebar, text="Problem Type", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10,0))
problem_type = ttk.Combobox(sidebar, values=["Generated", "Custom"])
problem_type.current(0)
problem_type.pack(padx=20, fill="x")

ttk.Label(sidebar, text="Number of Bins", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(15,0))
bins_slider = ttk.Scale(sidebar, from_=1, to=5, orient="horizontal")
bins_slider.pack(padx=20, fill="x")

ttk.Label(sidebar, text="Bin Dimensions", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(15,0))
bin_dim_frame = tk.Frame(sidebar, bg="#223366")
bin_dim_frame.pack(padx=20, fill="x")
for label in ["L", "W", "H"]:
    tk.Entry(bin_dim_frame, width=4, font=("Segoe UI", 11)).pack(side="left", padx=2)

# Main input area
main_area = tk.Frame(root, bg="#f6f8fa")
main_area.pack(side="left", fill="both", expand=True, padx=10, pady=10)

input_label = tk.Label(main_area, text="Input", font=("Segoe UI", 14, "bold"), bg="#f6f8fa")
input_label.pack(anchor="w", pady=(10, 5))

# Table for input data
columns = ("Case ID", "Quantity", "Length", "Width", "Height")
tree = ttk.Treeview(main_area, columns=columns, show="headings", height=18)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=80, anchor="center")
tree.pack(fill="x", pady=10)

# Dummy data
for i in range(16):
    tree.insert("", "end", values=(i, 1, 10+i, 10+i, 5+i))

# Right panel for info and save
right_panel = tk.Frame(root, bg="#f6f8fa", width=250)
right_panel.pack(side="right", fill="y")

info_label = tk.Label(right_panel, text="Maximum bins: 1\nBin dimensions: 50 * 50 * 50", bg="#f6f8fa", font=("Segoe UI", 11))
info_label.pack(pady=(40, 10))

save_label = tk.Label(right_panel, text="Save Input Data to File", bg="#f6f8fa", font=("Segoe UI", 11))
save_label.pack(pady=(30, 5))
save_entry = tk.Entry(right_panel, font=("Segoe UI", 11))
save_entry.pack(pady=5)
save_btn = ttk.Button(right_panel, text="SAVE")
save_btn.pack(pady=5)

root.mainloop()