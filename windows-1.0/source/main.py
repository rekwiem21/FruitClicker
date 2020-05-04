from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame
import os

pygame.init()

munch = 0
money = 10
currentfruit = "Apple"
numOfApples = 0
numOfBananas = 0

def themewindowOnClose():
    root.deiconify()
    themewindow.destroy()
    themeset = themechosen.get()
    if themechosen == "Red":
        root.configure(bg="Red")

def choosetheme():
    global themewindow
    global themechosen
    themewindow = Toplevel()
    root.withdraw()
    themewindow.title("Fruit Clicker - Select Theme")
    themewindow.geometry("400x350+300+100")
    languages = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)]
    themewindow.protocol("WM_DELETE_WINDOW", themewindowOnClose)
    

def save():
    if os.path.exists("save.fcsave") == True:
        if messagebox.askyesno("Save Exists", "A save file already exists.\nWould you still like to save?") == True:
            savedoc = open("save.fcsave", "w+")
            savedoc.write(str(money) + "\n" + str(munch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas))
            messagebox.showinfo("Save", "Your game has been saved!")
        else:
            messagebox.showinfo("Save", "Your game will not be saved")
    else:
        savedoc = open("save.fcsave", "w+")
        savedoc.write(str(money) + "\n" + str(munch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas))
        messagebox.showinfo("Save", "Your game has been saved!")

def load():
    if os.path.exists("save.fcsave") == True:
        loadedfile = open("save.fcsave")
        loadedfilelines = loadedfile.readlines()
        money = loadedfilelines[0]
        moneystringvar.set("You have $" + str(money))
        if int(money) < 10:
            moneylabel.place(x="327", y="0")
        if int(money) < 100 and int(money) > 9:
            moneylabel.place(x="320", y="0")
        if int(money) < 1000 and int(money) > 99:
            moneylabel.place(x="315", y="0")
        munch = loadedfilelines[1]
        munchstringvar.set("Munch: " + str(munch))
        if int(munch) < 10:
            munchlabel.place(x="340", y="20")
        if int(munch) < 100 and int(munch) > 9:
            munchlabel.place(x="335", y="20")
        if int(munch) < 1000 and int(munch) > 99:
            munchlabel.place(x="330", y="20")
        numOfApples = loadedfilelines[2]
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if int(numOfApples) < 10:
            currentfruitlabel.place(x="180", y="290")
        if int(numOfApples) < 100 and int(numOfApples) > 9:
            currentfruitlabel.place(x="175", y="290")
        if int(numOfApples) < 1000 and int(numOfApples) > 99:
            currentfruitlabel.place(x="170", y="290")
        numOfBananas = loadedfilelines[3]
        
    else:
        messagebox.showerror("Error", "Save data not found.")

def switchleft():
    global currentfruit
    global clickerbutton
    if currentfruit == "Banana":
        currentfruit = "Apple"
        clickerbutton.config(image=clickerphoto)
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfBananas > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="170", y="290")

def switchright():
    global currentfruit
    global clickerbutton
    if currentfruit == "Apple":
        currentfruit = "Banana"
        clickerbutton.config(image=clickerphoto2)
        currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="165", y="290")

def musicselect():
    musicfilename = filedialog.askopenfilename(initialdir = "/",title = "Select MP3 File",filetypes = (("MP3 Files","*.mp3"),("WAV Files","*.wav")))
    pygame.mixer.music.load(musicfilename)
    pygame.mixer.music.play(-1)

def buyapple():
    global money
    global numOfApples
    if money < 1:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 1
        numOfApples = numOfApples + 1
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buyapplepack():
    global money
    global numOfApples
    if money < 6:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 6
        numOfApples = numOfApples + 6
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buyapplecrate():
    global money
    global numOfApples
    if money < 36:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 36
        numOfApples = numOfApples + 36
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buybanana():
    global money
    global numOfBananas
    if money < 2:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 2
        numOfBananas = numOfBananas + 1
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
          currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buybananabunch():
    global money
    global numOfBananas
    if money < 10:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 10
        numOfBananas = numOfBananas + 5
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
          currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buybananacrate():
    global money
    global numOfBananas
    if money < 60:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        money = money - 60
        numOfBananas = numOfBananas + 30
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
          currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def clicked():
    global money
    global currentfruit
    global numOfApples
    global numOfBananas
    if currentfruit == "Apple":
        if numOfApples == 0:
            messagebox.showerror("Error", "You do not have any Apples!")
        else:
            numOfApples = numOfApples - 1
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
            money = money + 2
            moneystringvar.set("You have $" + str(money))
            if money < 10:
                moneylabel.place(x="327", y="0")
            if money < 100 and money > 9:
                moneylabel.place(x="320", y="0")
            if money < 1000 and money > 99:
                moneylabel.place(x="315", y="0")
    if currentfruit == "Banana":
        if numOfBananas == 0:
            messagebox.showerror("Error", "You do not have any Bananas!")
        else:
            numOfBananas = numOfBananas - 1
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
            if numOfBananas < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfBananas < 100 and numOfBananas > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfBananas < 1000 and numOfBananas > 99:
                currentfruitlabel.place(x="170", y="290")
            money = money + 4
            moneystringvar.set("You have $" + str(money))
            if money < 10:
                moneylabel.place(x="327", y="0")
            if money < 100 and money > 9:
                moneylabel.place(x="320", y="0")
            if money < 1000 and money > 99:
                moneylabel.place(x="315", y="0")

def inventoryOnClose():
    root.deiconify()
    inventorywindow.destroy()

def marketOnClose():
    root.deiconify()
    marketwindow.destroy()
    
def upgradesOnClose():
    root.deiconify()
    upgradeswindow.destroy()

def inventory():
    global inventorywindow
    global numOfApples
    root.withdraw()
    inventorywindow = Toplevel()
    inventorywindow.title("Fruit Clicker - Inventory")
    inventorywindow.geometry("400x350+300+100")
    inventorywindow.protocol("WM_DELETE_WINDOW", inventoryOnClose)
    applesinventory = StringVar()
    applesinventory.set("Apples: " + str(numOfApples))
    applesinvlabel = Label(inventorywindow, textvariable=applesinventory)
    applesinvlabel.grid(row="0", column="0")
    bananasinventory = StringVar()
    bananasinventory.set("Bananas: " + str(numOfBananas))
    bananasinvlabel = Label(inventorywindow, textvariable=bananasinventory)
    bananasinvlabel.place(x="0", y="20")
    inventorywindow.mainloop()

def market():
    global marketwindow
    global marketapplecount
    root.withdraw()
    marketwindow = Toplevel()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)
    Label(marketwindow, text="Buy\nApple", width="8").grid(row="0", column="0")
    Button(marketwindow, text="Buy Apple\n$1", command=buyapple, width="10").grid(row="0", column="1")
    Button(marketwindow, text="Buy Pack (6)\n$6", command=buyapplepack, width="10").grid(row="0", column="2")
    Button(marketwindow, text="Buy Crate (36)\n$36", command=buyapplecrate, width="10").grid(row="0", column="3")
    Label(marketwindow, text="Buy\nBanana", width="8").grid(row="1", column="0")
    Button(marketwindow, text="Buy Banana\n$2", command=buybanana, width="10").grid(row="1", column="1")
    Button(marketwindow, text="Buy Bunch (5)\n$10", command=buybananabunch, width="10").grid(row="1", column="2")
    Button(marketwindow, text="Buy Crate (30)\n$60", command=buybananacrate, width="10").grid(row="1", column="3")
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

leftfruitbutton = Button(root, text="<", command=switchleft)
leftfruitbutton.place(x="100", y="285")

currentfruitstringvar = StringVar()
if currentfruit == "Apple":  
    currentfruitstringvar.set("Apple x" + str(numOfApples))
    currentfruitlabel = Label(root, textvariable=currentfruitstringvar, fg="Black")
    if numOfApples < 10:
        currentfruitlabel.place(x="180", y="290")
    if numOfApples < 100 and numOfApples > 9:
        currentfruitlabel.place(x="175", y="290")
    if numOfApples < 1000 and numOfApples > 99:
        currentfruitlabel.place(x="170", y="290")

rightfruitbutton = Button(root, text=">", command=switchright)
rightfruitbutton.place(x="287", y="285")

moneystringvar = StringVar()
moneystringvar.set("You have $" + str(money))
moneylabel = Label(root, textvariable=moneystringvar)
if money < 10:
    moneylabel.place(x="327", y="0")
if money < 100 and money > 9:
    moneylabel.place(x="320", y="0")
if money < 1000 and money > 99:
    moneylabel.place(x="315", y="0")

munchstringvar = StringVar()
munchstringvar.set("Munch: " + str(munch))
munchlabel = Label(root, textvariable=munchstringvar)
if munch < 10:
    munchlabel.place(x="340", y="20")
if munch < 100 and munch > 9:
    munchlabel.place(x="335", y="20")
if munch < 1000 and munch > 99:
    munchlabel.place(x="330", y="20")

clickerphoto = PhotoImage(file = "apple.png")
clickerphoto2 = PhotoImage(file = "banana.png")
clickerbutton = Button(root, text="Clicker Button", image=clickerphoto, fg="Black", command=clicked)
clickerbutton.place(x="100", y="75")

musicselectbutton = Button(root, text="Music", command=musicselect, bg="Black", fg="White", width="6")
musicselectbutton.grid(row="4", column="0")

savebutton = Button(root, text="Save", fg="White", bg="Black", width="6", command=save)
savebutton.grid(row="5", column="0")

loadbutton = Button(root, text="Load", fg="White", bg="Black", width="6", command=load)
loadbutton.grid(row="6", column="0")

themesbutton = Button(root, text="Theme", fg="White", bg="Black", width="6", command=choosetheme)
themesbutton.grid(row="7", column="0")
root.mainloop()
