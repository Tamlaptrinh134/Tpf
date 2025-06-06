from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from threading import Thread
import os
import time
import requests
#API 863726596773166
def write_log(text: str) -> None:
    with open("source/log.txt", "a") as log_file:
        time_format = "%Y-%m-%d %H:%M:%S"
        this_time = time.strftime(time_format, time.localtime())
        log_file.write(f"[{this_time}] {text}\n")
def loading() -> None:
    def add_logscreen(text: str, row, col, style) -> None:
        Label_logscreen = ttk.Label(ScrolledFrame_loading, text=text, bootstyle=style)
        Label_logscreen.grid(row=row, column=col, padx=2, pady=5, sticky="w")
        ScrolledFrame_loading.yview_moveto(1.0)

    #Check if the file exists
    add_logscreen("[Task] Checking source:", 0, 0, INFO)
    global check, internet
    tasks = 2
    files_check = ["source/log.txt", "README.md"]
    step = 100 / len(files_check)
    main_step = 100 / tasks
    for index, item in enumerate(files_check):
        add_logscreen(f"{item}.", index + 1, 0, PRIMARY)
        if os.path.exists("source/log.txt"):
            add_logscreen("File found.", index + 1, 1, SUCCESS)
            progressbar_value.set(progressbar_value.get() + step)
        else:
            add_logscreen("File not found.", index + 1, 1, DANGER)
            Progressbar_loading.config(bootstyle=DANGER)
            check = False
    if check:
        add_logscreen("[Task] Done", None, 0, SUCCESS)
        progressbar_value_main.set(progressbar_value_main.get() + main_step)
        add_logscreen("[Task] Checking Internet:", 3, 0, INFO)
        Progressbar_loading.config(mode="indeterminate")
        Progressbar_loading.start(10)
        try:
            response = requests.get("https://remove.bg", timeout=10)
            if response.status_code == 200:
                add_logscreen("Internet connection is available.", None, 0, SUCCESS)
                progressbar_value_main.set(progressbar_value_main.get() + main_step)
            else:
                add_logscreen("Internet connection is not available.", None, 0, DANGER)
                internet = False
        except requests.ConnectionError:
            add_logscreen("Internet connection is not available.", None, 0, DANGER)
        add_logscreen("[Task] Done", None, 0, SUCCESS)
        write_log(f"USER: opened the application")
    else:
        add_logscreen("[Task] Done", None, 0, DANGER)
        add_logscreen("Please check the source files.", None, 0, DANGER)
        write_log("APP: Source files are missing or corrupted.")
    Progressbar_loading.config(mode="determinate")
    Progressbar_loading.config(bootstyle=SUCCESS)
    progressbar_value.set(100)
    Progressbar_loading.stop()
    time.sleep(3)
    Window_loading.after(0, Window_loading.quit)

""""""     
Window_loading = ttk.Window(themename="darkly")

image_loading_screen = Image.open("source/loading_screen.png")
image_loading_screen = ImageTk.PhotoImage(image_loading_screen)
width = 500
height = 300
check = True
internet = True
window_width_center = width // 2
window_height_center = height // 2
screen_width_center = Window_loading.winfo_screenwidth() // 2
screen_height_center = Window_loading.winfo_screenheight() // 2

Window_loading.title("Tpf")
Window_loading.geometry(f"{width}x{height}+{screen_width_center - window_width_center}+{screen_height_center - window_height_center}")
Window_loading.resizable(False, False)
Window_loading.overrideredirect(True)

Label_loading_screen = ttk.Label(Window_loading, image=image_loading_screen)
Label_loading_screen.image = image_loading_screen
Label_loading_screen.place(x=0, y=0)

ScrolledFrame_loading = ScrolledFrame(Window_loading, width=300, height=90)
ScrolledFrame_loading.place(x=100, y=105)

progressbar_value = IntVar(value=0)
Progressbar_loading = ttk.Progressbar(Window_loading, mode="determinate", length=300, variable=progressbar_value, bootstyle=INFO)
Progressbar_loading.place(x=100, y=200)

progressbar_value_main = IntVar(value=0)
Progressbar_loading_main = ttk.Progressbar(Window_loading, mode="determinate", length=300, variable=progressbar_value_main, bootstyle=SUCCESS)
Progressbar_loading_main.place(x=100, y=220)

Thread(target=loading, daemon=True).start()
Window_loading.mainloop()
Window_loading.destroy()