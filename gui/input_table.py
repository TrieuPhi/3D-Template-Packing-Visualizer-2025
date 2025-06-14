import tkinter as tk
from tkinter import ttk, filedialog
import csv

class InputTable:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f6f8fa")
        self._build()
        self._editing = None  # Để theo dõi ô đang sửa

    def _build(self):
        tk.Label(self.frame, text="Input", font=("Segoe UI", 14, "bold"), bg="#f6f8fa").pack(anchor="w", pady=(10, 5))
        self.columns = ("Case ID", "X", "Y", "Z", "Length", "Width", "Height")
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings", height=18)
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80, anchor="center")
        self.tree.pack(fill="x", pady=10)
        # Dummy data: 8 box với vị trí và kích thước khác nhau
        sample_data = [
            (0, 0, 0, 0, 10, 10, 5),
            (1, 10, 0, 0, 10, 10, 5),
            (2, 0, 10, 0, 10, 10, 5),
            (3, 10, 10, 0, 10, 10, 5),
            (4, 0, 0, 5, 10, 10, 5),
            (5, 10, 0, 5, 10, 10, 5),
            (6, 0, 10, 5, 10, 10, 5),
            (7, 10, 10, 5, 10, 10, 5)
        ]
        for row in sample_data:
            self.tree.insert("", "end", values=row)
        # Sửa trực tiếp ô
        self.tree.bind('<Double-1>', self._on_double_click)
        # Thêm nút xoá dòng
        btn_frame = tk.Frame(self.frame, bg="#f6f8fa")
        btn_frame.pack(anchor="w", pady=(0, 5))
        self.delete_btn = tk.Button(btn_frame, text="Xoá dòng", command=self.delete_selected, font=("Segoe UI", 10))
        self.delete_btn.pack(side="left", padx=5)

    def _on_double_click(self, event):
        region = self.tree.identify('region', event.x, event.y)
        if region != 'cell':
            return
        rowid = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)
        col_num = int(col.replace('#', '')) - 1
        x, y, width, height = self.tree.bbox(rowid, col)
        value = self.tree.set(rowid, self.columns[col_num])
        self._editing = (rowid, col_num)
        self.entry = tk.Entry(self.tree, width=8)
        self.entry.place(x=x, y=y, width=width, height=height)
        self.entry.insert(0, value)
        self.entry.focus()
        self.entry.bind('<Return>', self._save_edit)
        self.entry.bind('<FocusOut>', self._save_edit)

    def _save_edit(self, event):
        if not self._editing:
            return
        rowid, col_num = self._editing
        new_value = self.entry.get()
        self.tree.set(rowid, self.columns[col_num], new_value)
        self.entry.destroy()
        self._editing = None

    def delete_selected(self):
        selected = self.tree.selection()
        for item in selected:
            self.tree.delete(item)

    def load_data(self, data):
        # Xóa bảng cũ, nạp dữ liệu mới
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in data:
            self.tree.insert("", "end", values=row)

    def load_file(self, filepath):
        data = []
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 7:
                    data.append(tuple(row))
        self.load_data(data)
