import tkinter as tk
from tkinter import ttk

class Sidebar:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#223366", width=260)
        self.frame.pack_propagate(False)
        self._build()

    def _build(self):
        tk.Label(self.frame, text="3D Pallet Packing", bg="#223366", fg="white", font=("Segoe UI", 18, "bold")).pack(pady=(30, 20))
        ttk.Label(self.frame, text="Problem Type", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(10,0))
        self.problem_type = ttk.Combobox(self.frame, values=["Generated", "Custom"])
        self.problem_type.current(0)
        self.problem_type.pack(padx=20, fill="x")
        ttk.Label(self.frame, text="Number of Bins", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(15,0))
        self.bins_slider = ttk.Scale(self.frame, from_=1, to=5, orient="horizontal")
        self.bins_slider.set(1)
        self.bins_slider.pack(padx=20, fill="x")
        ttk.Label(self.frame, text="Bin Dimensions", background="#223366", foreground="white", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=(15,0))
        bin_dim_frame = tk.Frame(self.frame, bg="#223366")
        bin_dim_frame.pack(padx=20, fill="x")
        self.bin_dim_entries = []
        for _ in ["L", "W", "H"]:
            entry = tk.Entry(bin_dim_frame, width=4, font=("Segoe UI", 11))
            entry.insert(0, "50")
            entry.pack(side="left", padx=2)
            self.bin_dim_entries.append(entry)

    def get_problem_type(self):
        return self.problem_type.get()

    def get_number_of_bins(self):
        return int(float(self.bins_slider.get()))

    def get_bin_dimensions(self):
        try:
            return tuple(int(entry.get()) for entry in self.bin_dim_entries)
        except Exception:
            return (0, 0, 0)
