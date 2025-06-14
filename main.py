from gui.sidebar import Sidebar
from gui.input_table import InputTable
from gui.right_panel import RightPanel
from gui.style import set_style
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("3D Pallet Packing Visualizer")
    root.geometry("1200x700")
    set_style(root)

    # Sidebar
    sidebar = Sidebar(root)
    sidebar.frame.pack(side="left", fill="y")

    # Main input area
    input_table = InputTable(root)
    input_table.frame.pack(side="left", fill="both", expand=True)

    # Right panel (truyền input_table và sidebar vào)
    right_panel = RightPanel(root, input_table=input_table, sidebar=sidebar)
    right_panel.frame.pack(side="right", fill="y")

    root.mainloop()

if __name__ == "__main__":
    main()
