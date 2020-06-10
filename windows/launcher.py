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
        print("")
    else:
        url = "https://github.com/SeaPuppy2006/FruitClicker/raw/master/windows/main.exe"
        r = requests.get(url, allow_redirects=True)
        open("fruitclicker.exe", "wb").write(r.content)
        os.mkdir("images")
        url = "https://raw.githubusercontent.com/SeaPuppy2006/FruitClicker/master/windows/images/apple.ico"
        r = requests.get(url, allow_redirects=True)
        open("images/apple.ico", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/apple.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/apple.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/banana.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/banana.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/blackberry.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/blackberry.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/blueberry.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/blueberry.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/coconut.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/coconut.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/grapes.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/grapes.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/guava.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/guava.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/mango.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/mango.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/orange.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/orange.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/pear.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/pear.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/pineapple.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/pineapple.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/raspberry.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/raspberry.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/strawberry.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/strawberry.png", "wb").write(r.content)
        url = "https://github.com/SeaPuppy2006/FruitClicker/blob/master/windows/images/watermelon.png?raw=true"
        r = requests.get(url, allow_redirects=True)
        open("images/watermelon.png", "wb").write(r.content)
        downloadtextvar.set("Update")

def play():
    if os.path.exists("fruitclicker.exe"):
        root.destroy()
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.call(["fruitclicker.exe"])

downloadtextvar = StringVar()
downloadtextvar.set("Download")
if os.path.exists("fruitclicker.exe"):
    downloadtextvar.set("Update")
Button(root, textvariable=downloadtextvar, command=download, width="20", height="6").pack()
Button(root, text="Play", command=play, width="20", height="6").pack()

root.mainloop()
