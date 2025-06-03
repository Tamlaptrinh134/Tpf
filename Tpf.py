from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from threading import Thread
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import time
#API 863726596773166
def loading() -> None:
    def add_logscreen(text: str, row, col, style) -> None:
        Label_logscreen = ttk.Label(ScrolledFrame_loading.frame, text=text, bootstyle=style)
        Label_logscreen.grid(row=row, column=col, padx=2, pady=5, sticky="w")
    #Check if the file exists
    add_logscreen("Checking for file in source:", 0, 0, INFO)
    files_check = ["source/log.txt", "README.md"]
    step = 100 / len(files_check)
    for index, item in enumerate(files_check):
        add_logscreen(f"{item}.", index + 1, 0, PRIMARY)
        if os.path.exists("source/log.txt"):
            add_logscreen("File found.", index + 1, 1, SUCCESS)
            Progressbar_loading.step(step)
        else:
            add_logscreen("File not found.", index + 1, 1, DANGER)

     
Window_loading = ttk.Window(themename="darkly")

image_loading_screen = Image.open("source/loading_screen.png")
image_loading_screen = ImageTk.PhotoImage(image_loading_screen)
width = 500
height = 300
window_width_center = width // 2
window_height_center = height // 2
screen_width_center = Window_loading.winfo_screenwidth() // 2
screen_height_center = Window_loading.winfo_screenheight() // 2

Window_loading.title("Tpf")
Window_loading.geometry(f"{width}x{height}+{screen_width_center - window_width_center}+{screen_height_center - window_height_center}")
Window_loading.resizable(False, False)
Window_loading.overrideredirect(True)

Label_loading_screen = ttk.Label(Window_loading, image=image_loading_screen)
Label_loading_screen.place(x=0, y=0)

ScrolledFrame_loading = ScrolledFrame(Window_loading, width=300, height=90)
ScrolledFrame_loading.place(x=100, y=105)

Progressbar_loading = ttk.Progressbar(Window_loading, mode="determinate", length=300, bootstyle=INFO)
Progressbar_loading.place(x=100, y=200)
Progressbar_loading.start(0)

Thread(target=loading, daemon=True).start()
Window_loading.mainloop()