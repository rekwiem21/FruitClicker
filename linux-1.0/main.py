from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame

pygame.init()

money = 10
currentfruit = "Apple"
numOfApples = 0
numOfBananas = 100

def musicselect():
    musicfilename = filedialog.askopenfilename(initialdir = "/",title = "Select MP3 File",filetypes = (("MP3 Files","*.mp3"),("All Files","*.*")))
    pygame.mixer.music.load(musicfilename)
    pygame.mixer.music.play(-1)

def buyapple():
    global money
    global numOfApples
    if money < 1:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 1
        numOfApples = numOfApples + 1
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="175", y="292")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="170", y="292")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="165", y="292")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="315", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="307", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="300", y="0")

def buyapplepack():
    global money
    global numOfApples
    if money < 6:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 6
        numOfApples = numOfApples + 6
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="175", y="292")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="170", y="292")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="165", y="292")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="315", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="307", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="300", y="0")

def buyapplecrate():
    global money
    global numOfApples
    if money < 36:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 36
        numOfApples = numOfApples + 36
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="175", y="292")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="170", y="292")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="165", y="292")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="315", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="307", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="300", y="0")

def clicked():
    global money
    global currentfruit
    global numOfApples
    if currentfruit == "Apple":
        if numOfApples == 0:
            messagebox.showinfo("Error", "You do not have any Apples!")
        else:
            numOfApples = numOfApples - 1
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="175", y="292")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="170", y="292")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="165", y="292")
            money = money + 2
            moneystringvar.set("You have $" + str(money))
            if money < 10:
                moneylabel.place(x="315", y="0")
            if money < 100 and money > 9:
                moneylabel.place(x="307", y="0")
            if money < 1000 and money > 99:
                moneylabel.place(x="300", y="0")

def inventoryOnClose():
    root.deiconify()
    inventorywindow.destroy()

def marketOnClose():
    root.deiconify()
    marketwindow.destroy()
    
def upgradesOnClose():
    root.deiconify()
    upgradeswindow.destroy()
    
def rootOnClose():
    pygame.mixer.music.stop()
    root.destroy()

def inventory():
    global inventorywindow
    root.withdraw()
    inventorywindow = Toplevel()
    inventorywindow.title("Fruit Clicker - Inventory")
    inventorywindow.geometry("400x350+300+100")
    inventorywindow.protocol("WM_DELETE_WINDOW", inventoryOnClose)
    applesinventory = StringVar()
    applesinventory.set("Apples: " + str(numOfApples))
    applesinvlabel = Label(inventorywindow, textvariable=applesinventory)
    applesinvlabel.place(x="0", y="0")
    bananasinventory = StringVar()
    bananasinventory.set("Bananas: " + str(numOfBananas))
    bananasinvlabel = Label(inventorywindow, textvariable=bananasinventory)
    bananasinvlabel.place(x="0", y="20")
    inventorywindow.mainloop()

def market():
    global marketwindow
    root.withdraw()
    marketwindow = Toplevel()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)
    Label(marketwindow, text="Buy\nApple").grid(row="0", column="0")
    Button(marketwindow, text="Buy Apple\n$1", command=buyapple).grid(row="0", column="1")
    Button(marketwindow, text="Buy Pack (6)\n$6", command=buyapplepack).grid(row="0", column="2")
    Button(marketwindow, text="Buy Crate (36)\n$36", command=buyapplecrate).grid(row="0", column="3")
    marketwindow.mainloop()

def upgrades():
    global upgradeswindow
    root.withdraw()
    upgradeswindow = Toplevel()
    upgradeswindow.title("Fruit Clicker - Upgrades")
    upgradeswindow.geometry("400x350+300+100")
    upgradeswindow.protocol("WM_DELETE_WINDOW", upgradesOnClose)
    upgradeswindow.mainloop()

root = Tk()
root.title("Fruit Clicker")
root.geometry("400x350+300+100")

inventorybutton = Button(root, text="Inventory", fg="White", bg="Black", width="6", command=inventory)
inventorybutton.grid(column="0", row="0")

marketbutton = Button(root, text="Market", fg="White", bg="Black", width="6", command=market)
marketbutton.grid(column="0", row="1")

upgradesbutton = Button(root, text="Upgrades", fg="White", bg="Black", width="6", command=upgrades)
upgradesbutton.grid(column="0", row="2")

leftfruitbutton = Button(root, text="<")
leftfruitbutton.place(x="100", y="285")

currentfruitstringvar = StringVar()
if currentfruit == "Apple":  
    currentfruitstringvar.set("Apple x" + str(numOfApples))
    currentfruitlabel = Label(root, textvariable=currentfruitstringvar, fg="White")
    if numOfApples < 10:
        currentfruitlabel.place(x="175", y="292")
    if numOfApples < 100 and numOfApples > 9:
        currentfruitlabel.place(x="170", y="292")
    if numOfApples < 1000 and numOfApples > 99:
        currentfruitlabel.place(x="165", y="292")

rightfruitbutton = Button(root, text=">")
rightfruitbutton.place(x="267", y="285")

moneystringvar = StringVar()
moneystringvar.set("You have $" + str(money))
moneylabel = Label(root, textvariable=moneystringvar)
if money < 10:
    moneylabel.place(x="315", y="0")
if money < 100 and money > 9:
    moneylabel.place(x="307", y="0")
if money < 1000 and money > 99:
    moneylabel.place(x="300", y="0")

clickerphoto = PhotoImage(file = "apple.png")
clickerbutton = Button(root, text="Clicker Button", image=clickerphoto, fg="White", command=clicked)
clickerbutton.place(x="100", y="75")

musicselectbutton = Button(root, text="Music", command=musicselect, bg="Black", fg="White", width="6")
musicselectbutton.grid(row="4", column="0")

root.protocol("WM_DELETE_WINDOW", rootOnClose)
root.mainloop()
