import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from logic.plot3d import draw_boxes
import csv

class RightPanel:
    def __init__(self, master, input_table=None, sidebar=None):
        self.input_table = input_table
        self.sidebar = sidebar
        self.frame = tk.Frame(master, bg="#f6f8fa", width=250)
        self.frame.pack_propagate(False)
        self._build()

    def _build(self):
        self.info_label = tk.Label(self.frame, text="Maximum bins: 1\nBin dimensions: 50 * 50 * 50", bg="#f6f8fa", font=("Segoe UI", 11))
        self.info_label.pack(pady=(40, 10))
        # Nút Load File
        self.load_btn = ttk.Button(self.frame, text="Load File", command=self.on_load_file)
        self.load_btn.pack(pady=5)
        tk.Label(self.frame, text="Save Input Data to File", bg="#f6f8fa", font=("Segoe UI", 11)).pack(pady=(30, 5))
        self.save_entry = tk.Entry(self.frame, font=("Segoe UI", 11))
        self.save_entry.pack(pady=5)
        self.save_btn = ttk.Button(self.frame, text="SAVE", command=self.on_save_file)
        self.save_btn.pack(pady=5)
        # Thêm nút VẼ 3D
        self.draw_btn = ttk.Button(self.frame, text="VẼ 3D", command=self.on_draw)
        self.draw_btn.pack(pady=10)
        # Cập nhật info khi sidebar thay đổi
        if self.sidebar:
            self._update_info()
            if hasattr(self.sidebar, 'bins_slider'):
                self.sidebar.bins_slider.bind('<ButtonRelease-1>', lambda e: self._update_info())
            for entry in getattr(self.sidebar, 'bin_dim_entries', []):
                entry.bind('<FocusOut>', lambda e: self._update_info())
                entry.bind('<Return>', lambda e: self._update_info())

    def _update_info(self):
        if self.sidebar:
            bins = self.sidebar.get_number_of_bins()
            dims = self.sidebar.get_bin_dimensions()
            self.info_label.config(text=f"Maximum bins: {bins}\nBin dimensions: {dims[0]} * {dims[1]} * {dims[2]}")

    def on_draw(self):
        if self.input_table is None:
            return
        data = []
        for row in self.input_table.tree.get_children():
            values = self.input_table.tree.item(row)['values']
            data.append(tuple(int(v) for v in values))
        # Lấy các giá trị từ sidebar
        bins = self.sidebar.get_number_of_bins() if self.sidebar else 1
        dims = self.sidebar.get_bin_dimensions() if self.sidebar else (0, 0, 0)
        problem_type = self.sidebar.get_problem_type() if self.sidebar else "Custom"
        # Truyền các giá trị này vào hàm vẽ hoặc thuật toán nếu cần
        # Ví dụ: draw_boxes(data, bins, dims, problem_type)
        draw_boxes(data)

    def on_load_file(self):
        if self.input_table is None:
            return
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                self.input_table.load_file(file_path)
                messagebox.showinfo("Thành công", f"Đã nạp dữ liệu từ file: {file_path}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể nạp file: {e}")

    def on_save_file(self):
        if self.input_table is None:
            return
        file_path = self.save_entry.get().strip()
        if not file_path:
            messagebox.showwarning("Thiếu tên file", "Vui lòng nhập tên file để lưu.")
            return
        data = []
        for row in self.input_table.tree.get_children():
            values = self.input_table.tree.item(row)['values']
            data.append(values)
        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for row in data:
                    writer.writerow(row)
            messagebox.showinfo("Thành công", f"Đã lưu dữ liệu ra file: {file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")
