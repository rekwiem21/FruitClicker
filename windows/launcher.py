from tkinter import *
from tkinter import messagebox
import requests
import os
import subprocess

root = Tk()
root.geometry("200x200")
root.title("Fruit Clicker Launcher")

def download():
    if os.path.exists("fruitclicker.exe"):
        messagebox.showerror("Error", "Fruit Clicker is already installed")
    else:
        url = "https://github.com/SeaPuppy2006/FruitClicker/raw/master/windows/main.exe"
        r = requests.get(url, allow_redirects=True)
        open("fruitclicker.exe", "wb").write(r.content)

def play():
    root.destroy()
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call(["fruitclicker.exe"])

Button(root, text="Download", command=download, width="20", height="6").pack()
Button(root, text="Play", command=play, width="20", height="6").pack()

root.mainloop()
