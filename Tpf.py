from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from threading import Thread
import os
import time
import requests
import load
#API 863726596773166

print("Loading completed.")
if not load.check: exit()

#Main
theme = "darkly"
Window_main = ttk.Window(themename=theme)

style = ttk.Style(theme)

width = 1500
height = 900
check = True
window_width_center = width // 2
window_height_center = height // 2
screen_width_center = Window_main.winfo_screenwidth() // 2
screen_height_center = Window_main.winfo_screenheight() // 2

Window_main.title("Tpf")
Window_main.geometry(f"{width}x{height}+{screen_width_center - window_width_center}+{screen_height_center - window_height_center}")

LeftSide = ttk.Frame(Window_main, width=300, height=900)

TreeView_main = ttk.Treeview(LeftSide, bootstyle=DARK, columns=("Name"), show="tree headings")
TreeView_main.heading("#0", anchor=W)
TreeView_main.heading("Name", text="Name", anchor=W)
TreeView_main.column("#0", width=30, anchor=W)
TreeView_main.column("Name", width=260, anchor=W)
TreeView_main.pack(fill=BOTH, expand=True)

LeftSide.pack(side=LEFT, fill=Y)
LeftSide.pack_propagate(False)

MainArea = ttk.Notebook(Window_main, bootstyle=SUCCESS)

MainArea.pack(side=LEFT, fill=BOTH, expand=True)
MainArea.pack_propagate(False)

Window_main.mainloop()