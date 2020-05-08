from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from numerize import numerize
import pygame
import os
import random


pygame.init()

munch = 0
rawmunch = 0
money = 50
rawmoney = 50
currentfruit = "Apple"
multiconvertlevel = 0
multiconvertcost = 50
numOfApples = 0
numOfBananas = 0
numOfPears = 0
numOfOranges = 0
numOfMangos = 0
numOfStrawberries = 0
numOfBlueberries = 0
numOfBlackberries = 0

def multiconvertbuy():
    global rawmoney
    global multiconvertcost
    global multiconvertlevel
    if multiconvertlevel == 20:
        messagebox.showerror("Error", "Upgrade is MAX Level!")
        return
    if rawmoney < multiconvertcost:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - multiconvertcost
        moneyplace()
        moneystringvar.set("You have $" + str(money))
        multiconvertlevel = multiconvertlevel + 1
        multiconvertcost = multiconvertcost * 2
        if multiconvertlevel == 20:
            multiconverttextvar.set("Multi Convert Lv. MAX") 
        else:
            multiconverttextvar.set("Multi Convert Lv. " + str(multiconvertlevel) + " -> " + str(multiconvertlevel + 1) + " $" + str(multiconvertcost))

def moneyplace():
    global root
    global rawmoney
    global money
    if rawmoney < 10:
        money = rawmoney
        moneylabel.place(x="327", y="0")
    if rawmoney < 100 and rawmoney > 9:
        money = rawmoney
        moneylabel.place(x="320", y="0")
    if rawmoney < 1000 and rawmoney > 99:
        money = rawmoney
        moneylabel.place(x="315", y="0")
    if rawmoney < 10000 and rawmoney > 999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="320", y="0")
    if rawmoney < 100000 and rawmoney > 9999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="315", y="0")
    if rawmoney < 1000000 and rawmoney > 99999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="310", y="0")
    if rawmoney < 10000000 and rawmoney > 999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="320", y="0")
    if rawmoney < 100000000 and rawmoney > 9999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="312", y="0")
    if rawmoney < 1000000000 and rawmoney > 99999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="307", y="0")
    if rawmoney < 10000000000 and rawmoney > 999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="320", y="0")
    if rawmoney < 100000000000 and rawmoney > 9999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="315", y="0")
    if rawmoney < 1000000000000 and rawmoney > 99999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="310", y="0")
    if rawmoney < 10000000000000 and rawmoney > 999999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="320", y="0")
    if rawmoney < 100000000000000 and rawmoney > 9999999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="315", y="0")
    if rawmoney < 1000000000000000 and rawmoney > 99999999999999:
        money = numerize.numerize(rawmoney)
        moneylabel.place(x="310", y="0")
    if rawmoney > 10000000000000000:
        messagebox.showerror("HOw DiD YOu gEt heRE", "YOu hAve ToO MUch mONEy...\nGo gET a lIfE.")
        root.destroy()

def munchplace():
    if munch < 10:
        munchlabel.place(x="340", y="20")
    if munch < 100 and munch > 9:
        munchlabel.place(x="335", y="20")
    if munch < 1000 and munch > 99:
        munchlabel.place(x="330", y="20")
                
def convertmunch():
    global munch
    global rawmoney
    global multiconvertlevel
    if multiconvertlevel == 0:
        if munch < 5:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 5
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 1
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 1:
        if munch < 10:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 10
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 2
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 2:
        if munch < 15:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 15
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 3
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 3:
        if munch < 20:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 20
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 4
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 4:
        if munch < 25:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 25
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 5
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 5:
        if munch < 30:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 30
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 6
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 6:
        if munch < 35:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 35
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 7
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 7:
        if munch < 40:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 40
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 8
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 8:
        if munch < 45:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 45
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 9
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 9:
        if munch < 50:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 50
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 10
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 10:
        if munch < 55:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 55
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 11
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 11:
        if munch < 60:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 60
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 12
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 12:
        if munch < 65:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 65
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 13
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 13:
        if munch < 70:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 70
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 14
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 14:
        if munch < 75:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 75
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 15
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 15:
        if munch < 80:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 80
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 16
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 16:
        if munch < 85:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 85
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 17
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 17:
        if munch < 90:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 90
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 18
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 18:
        if munch < 95:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 95
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 19
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 19:
        if munch < 100:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 100
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 20
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 20:
        if munch < 105:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            munch = munch - 105
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 21
            moneyplace()
            moneystringvar.set("You have $" + str(money))

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
        leftfruitbutton.config(state=DISABLED)
        clickerbutton.config(image=clickerphoto)
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfBananas > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="170", y="290")
    if currentfruit == "Pear":
        currentfruit = "Banana"
        clickerbutton.config(image=clickerphoto2)
        currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Orange":
        currentfruit = "Pear"
        clickerbutton.config(image=clickerphoto3)
        currentfruitstringvar.set("Pear x" + str(numOfPears))
        if numOfPears < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfPears < 100 and numOfPears > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfPears < 1000 and numOfPears > 99:
            currentfruitlabel.place(x="170", y="290")
        return
    if currentfruit == "Mango":
        currentfruit = "Orange"
        clickerbutton.config(image=clickerphoto4)
        currentfruitstringvar.set("Orange x" + str(numOfOranges))
        if numOfOranges < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfOranges < 100 and numOfOranges > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfOranges < 1000 and numOfOranges > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Strawberry":
        currentfruit = "Mango"
        clickerbutton.config(image=clickerphoto5)
        currentfruitstringvar.set("Mango x" + str(numOfMangos))
        if numOfMangos < 10:
            currentfruitlabel.place(x="170", y="290")
        if numOfMangos < 100 and numOfMangos > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfMangos < 1000 and numOfMangos > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Blueberry":
        currentfruit = "Strawberry"
        clickerbutton.config(image=clickerphoto6)
        currentfruitstringvar.set("Strawberry x" + str(numOfStrawberries))
        if numOfStrawberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfStrawberries < 100 and numOfStrawberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfStrawberries < 1000 and numOfStrawberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Blackberry":
        currentfruit = "Blueberry"
        rightfruitbutton.config(state=NORMAL)
        clickerbutton.config(image=clickerphoto7)
        currentfruitstringvar.set("Blueberry x" + str(numOfBlueberries))
        if numOfBlueberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlueberries < 100 and numOfBlueberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlueberries < 1000 and numOfBlueberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return

def switchright():
    global currentfruit
    global clickerbutton
    if currentfruit == "Apple":
        currentfruit = "Banana"
        leftfruitbutton.config(state=NORMAL)
        clickerbutton.config(image=clickerphoto2)
        currentfruitstringvar.set("Banana x" + str(numOfBananas))
        if numOfBananas < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfBananas < 100 and numOfBananas > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfBananas < 1000 and numOfBananas > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Banana":
        currentfruit = "Pear"
        clickerbutton.config(image=clickerphoto3)
        currentfruitstringvar.set("Pear x" + str(numOfPears))
        if numOfPears < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfPears < 100 and numOfPears > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfPears < 1000 and numOfPears > 99:
            currentfruitlabel.place(x="170", y="290")
        return
    if currentfruit == "Pear":
        currentfruit = "Orange"
        clickerbutton.config(image=clickerphoto4)
        currentfruitstringvar.set("Orange x" + str(numOfOranges))
        if numOfOranges < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfOranges < 100 and numOfOranges > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfOranges < 1000 and numOfOranges > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Orange":
        currentfruit = "Mango"
        clickerbutton.config(image=clickerphoto5)
        currentfruitstringvar.set("Mango x" + str(numOfMangos))
        if numOfMangos < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfMangos < 100 and numOfMangos > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfMangos < 1000 and numOfMangos > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Mango":
        currentfruit = "Strawberry"
        clickerbutton.config(image=clickerphoto6)
        currentfruitstringvar.set("Strawberry x" + str(numOfStrawberries))
        if numOfStrawberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfStrawberries < 100 and numOfStrawberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfStrawberries < 1000 and numOfStrawberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Strawberry":
        currentfruit = "Blueberry"
        clickerbutton.config(image=clickerphoto7)
        currentfruitstringvar.set("Blueberry x" + str(numOfBlueberries))
        if numOfBlueberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlueberries < 100 and numOfBlueberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlueberries < 1000 and numOfBlueberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Blueberry":
        currentfruit = "Blackberry"
        rightfruitbutton.config(state=DISABLED)
        clickerbutton.config(image=clickerphoto8)
        currentfruitstringvar.set("Blackberry x" + str(numOfBlackberries))
        if numOfBlackberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlackberries < 100 and numOfBlackberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlackberries < 1000 and numOfBlackberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    
def musicselect():
    musicfilename = filedialog.askopenfilename(initialdir = "/",title = "Select MP3 File",filetypes = (("MP3 Files","*.mp3"),("WAV Files","*.wav")))
    pygame.mixer.music.load(musicfilename)
    pygame.mixer.music.play(-1)

def buyapple():
    global money
    global rawmoney
    global numOfApples
    if rawmoney < 1:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 1
        numOfApples = numOfApples + 1
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyapplepack():
    global money
    global rawmoney
    global numOfApples
    if rawmoney < 6:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 6
        numOfApples = numOfApples + 6
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyapplecrate():
    global money
    global rawmoney
    global numOfApples
    if rawmoney < 36:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 36
        numOfApples = numOfApples + 36
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buybanana():
    global money
    global rawmoney
    global numOfBananas
    if rawmoney < 5:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 5
        numOfBananas = numOfBananas + 1
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
            if numOfBananas < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfBananas < 100 and numOfBananas > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfBananas < 1000 and numOfBananas > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buybananabunch():
    global money
    global rawmoney
    global numOfBananas
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfBananas = numOfBananas + 5
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
            if numOfBananas < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfBananas < 100 and numOfBananas > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfBananas < 1000 and numOfBananas > 99:
             currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buybananacrate():
    global money
    global rawmoney
    global numOfBananas
    if rawmoney < 150:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 150
        numOfBananas = numOfBananas + 30
        if currentfruit == "Banana":
            currentfruitstringvar.set("Banana x" + str(numOfBananas))
            if numOfBananas < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfBananas < 100 and numOfBananas > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfBananas < 1000 and numOfBananas > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buypear():
    global money
    global rawmoney
    global numOfPears
    if rawmoney < 10:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 10
        numOfPears = numOfPears + 1
        if currentfruit == "Pear":
            currentfruitstringvar.set("Pear x" + str(numOfPears))
            if numOfPears < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfPears < 100 and numOfPears > 9:
              currentfruitlabel.place(x="175", y="290")
            if numOfPears < 1000 and numOfPears > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))
        
def buypearpack():
    global money
    global rawmoney
    global numOfPears
    if rawmoney < 30:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 30
        numOfPears = numOfPears + 3
        if currentfruit == "Pear":
            currentfruitstringvar.set("Pear x" + str(numOfPears))
            if numOfPears < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfPears < 100 and numOfPears > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfPears < 1000 and numOfPears > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))


def buypearcrate():
    global money
    global rawmoney
    global numOfPears
    if rawmoney < 250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 250
        numOfPears = numOfPears + 25
        if currentfruit == "Pear":
            currentfruitstringvar.set("Pear x" + str(numOfPears))
            if numOfPears < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfPears < 100 and numOfPears > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfPears < 1000 and numOfPears > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyorange():
    global money
    global rawmoney
    global numOfOranges
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfOranges = numOfOranges + 1
        if currentfruit == "Orange":
            currentfruitstringvar.set("Orange x" + str(numOfOranges))
            if numOfOranges < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfOranges < 100 and numOfOranges > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfOranges < 1000 and numOfOranges > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyorangebag():
    global money
    global rawmoney
    global numOfOranges
    if rawmoney < 80:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 80
        numOfOranges = numOfOranges + 4
        if currentfruit == "Orange":
            currentfruitstringvar.set("Orange x" + str(numOfOranges))
            if numOfOranges < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfOranges < 100 and numOfOranges > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfOranges < 1000 and numOfOranges > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyorangecrate():
    global money
    global rawmoney
    global numOfOranges
    if rawmoney < 400:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 400
        numOfOranges = numOfOranges + 20
        if currentfruit == "Orange":
            currentfruitstringvar.set("Orange x" + str(numOfOranges))
            if numOfOranges < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfOranges < 100 and numOfOranges > 9:
              currentfruitlabel.place(x="170", y="290")
            if numOfOranges < 1000 and numOfOranges > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buymango():
    global money
    global rawmoney
    global numOfMangos
    if rawmoney < 50:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 50
        numOfMangos = numOfMangos + 1
        if currentfruit == "Mango":
            currentfruitstringvar.set("Mango x" + str(numOfMangos))
            if numOfMangos < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfMangos < 100 and numOfMangos > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfMangos < 1000 and numOfMangos > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buymangobag():
    global money
    global rawmoney
    global numOfMangos
    if rawmoney < 100:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 100
        numOfMangos = numOfMangos + 2
        if currentfruit == "Mango":
            currentfruitstringvar.set("Mango x" + str(numOfMangos))
            if numOfMangos < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfMangos < 100 and numOfMangos > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfMangos < 1000 and numOfMangos > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))
        
def buymangocrate():
    global money
    global rawmoney
    global numOfMangos
    if rawmoney < 750:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 750
        numOfMangos = numOfMangos + 25
        if currentfruit == "Mango":
            currentfruitstringvar.set("Mango x" + str(numOfMangos))
            if numOfMangos < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfMangos < 100 and numOfMangos > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfMangos < 1000 and numOfMangos > 99:
                currentfruitlabel.place(x="165", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buystrawberry():
    global money
    global rawmoney
    global numOfStrawberries
    if rawmoney < 10:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 10
        numOfStrawberries = numOfStrawberries + 1
        if currentfruit == "Strawberry":
            currentfruitstringvar.set("Strawberries x" + str(numOfStrawberries))
            if numOfStrawberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfStrawberries < 100 and numOfStrawberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfStrawberries < 1000 and numOfStrawberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buystrawberrybox():
    global money
    global rawmoney
    global numOfStrawberries
    if rawmoney < 250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 250
        numOfStrawberries = numOfStrawberries + 25
        if currentfruit == "Strawberry":
            currentfruitstringvar.set("Strawberries x" + str(numOfStrawberries))
            if numOfStrawberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfStrawberries < 100 and numOfStrawberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfStrawberries < 1000 and numOfStrawberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buystrawberrycrate():
    global money
    global rawmoney
    global numOfStrawberries
    if rawmoney < 7500:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 7500
        numOfStrawberries = numOfStrawberries + 750
        if currentfruit == "Strawberry":
            currentfruitstringvar.set("Strawberries x" + str(numOfStrawberries))
            if numOfStrawberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfStrawberries < 100 and numOfStrawberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfStrawberries < 1000 and numOfStrawberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))
        
def buyblueberry():
    global money
    global rawmoney
    global numOfBlueberries
    if rawmoney < 15:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 15
        numOfBlueberries = numOfBlueberries + 1
        if currentfruit == "Blueberry":
            currentfruitstringvar.set("Blueberries x" + str(numOfBlueberries))
            if numOfBlueberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlueberries < 100 and numOfBlueberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlueberries < 1000 and numOfBlueberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyblueberrybox():
    global money
    global rawmoney
    global numOfBlueberries
    if rawmoney < 375:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 375
        numOfBlueberries = numOfBlueberries + 25
        if currentfruit == "Blueberry":
            currentfruitstringvar.set("Blueberries x" + str(numOfBlueberries))
            if numOfBlueberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlueberries < 100 and numOfBlueberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlueberries < 1000 and numOfBlueberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyblueberrycrate():
    global money
    global rawmoney
    global numOfBlueberries
    if rawmoney < 11250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 11250
        numOfBlueberries = numOfBlueberries + 750
        if currentfruit == "Blueberry":
            currentfruitstringvar.set("Blueberries x" + str(numOfBlueberries))
            if numOfBlueberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlueberries < 100 and numOfBlueberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlueberries < 1000 and numOfBlueberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyblackberry():
    global money
    global rawmoney
    global numOfBlackberries
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfBlackberries = numOfBlackberries + 1
        if currentfruit == "Blackberry":
            currentfruitstringvar.set("Blackberries x" + str(numOfBlackberries))
            if numOfBlackberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlackberries < 100 and numOfBlackberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlackberries < 1000 and numOfBlackberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyblackberrybox():
    global money
    global rawmoney
    global numOfBlackberries
    if rawmoney < 300:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 300
        numOfBlackberries = numOfBlackberries + 15
        if currentfruit == "Blackberry":
            currentfruitstringvar.set("Blackberries x" + str(numOfBlackberries))
            if numOfBlackberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlackberries < 100 and numOfBlackberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlackberries < 1000 and numOfBlackberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))

def buyblackberrycrate():
    global money
    global rawmoney
    global numOfBlackberries
    if rawmoney < 9000:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 9000
        numOfBlackberries = numOfBlackberries + 450
        if currentfruit == "Blackberry":
            currentfruitstringvar.set("Blackberries x" + str(numOfBlackberries))
            if numOfBlackberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlackberries < 100 and numOfBlackberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfBlackberries < 1000 and numOfBlackberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        moneystringvar.set("You have $" + str(money))
            
def clicked():
    global munch
    global currentfruit
    global numOfApples
    global numOfBananas
    global numOfPears
    global numOfOranges
    global numOfMangos
    global numOfStrawberries
    global numOfBlueberries
    global numOfBlackberries
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
            munch = munch + random.randint(5, 10)
            munchstringvar.set("Munch:" + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
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
            munch = munch + random.randint(30, 35)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Pear":
        if numOfPears == 0:
            messagebox.showerror("Error", "You do not have any Pears!")
        else:
            numOfPears = numOfPears - 1
            currentfruitstringvar.set("Pear x" + str(numOfPears))
            if numOfPears < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfPears < 100 and numOfPears > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfPears < 1000 and numOfPears > 99:
                currentfruitlabel.place(x="170", y="290")
            munch = munch + random.randint(60, 75)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Orange":
        if numOfOranges == 0:
            messagebox.showerror("Error", "You do not have any Oranges!")
        else:
            numOfOranges = numOfOranges - 1
            currentfruitstringvar.set("Orange x" + str(numOfOranges))
            if numOfOranges < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfOranges < 100 and numOfOranges > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfOranges < 1000 and numOfOranges > 99:
                currentfruitlabel.place(x="165", y="290")
            munch = munch + random.randint(95, 110)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Mango":
        if numOfMangos == 0:
            messagebox.showerror("Error", "You do not have any Mangoes!")
        else:
            numOfMangos = numOfMangos - 1
            currentfruitstringvar.set("Mango x" + str(numOfMangos))
            if numOfMangos < 10:
                currentfruitlabel.place(x="175", y="290")
            if numOfMangos < 100 and numOfOranges > 9:
                currentfruitlabel.place(x="170", y="290")
            if numOfMangos < 1000 and numOfOranges > 99:
                currentfruitlabel.place(x="165", y="290")
            munch = munch + random.randint(245, 250)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Strawberry":
        if numOfStrawberries == 0:
            messagebox.showerror("Error", "You do not have any Strawberries!")
        else:
            numOfStrawberries = numOfStrawberries - 1
            currentfruitstringvar.set("Strawberries x" + str(numOfStrawberries))
            if numOfStrawberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfStrawberries < 100 and numOfStrawberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfStrawberries < 1000 and numOfStrawberries > 99:
                currentfruitlabel.place(x="155", y="290")
            munch = munch + random.randint(48, 55)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Blueberry":
        if numOfBlueberries == 0:
            messagebox.showerror("Error", "You do not have any Blueberries!")
        else:
            numOfBlueberries = numOfBlueberries - 1
            currentfruitstringvar.set("Blueberries x" + str(numOfBlueberries))
            if numOfBlueberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlueberries < 100 and numOfBlueberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfBlueberries < 1000 and numOfBlueberries > 99:
                currentfruitlabel.place(x="155", y="290")
            munch = munch + random.randint(73, 82)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")
    if currentfruit == "Blackberry":
        if numOfBlackberries == 0:
            messagebox.showerror("Error", "You do not have any Blackberries!")
        else:
            numOfBlackberries = numOfBlackberries - 1
            currentfruitstringvar.set("Blackberries x" + str(numOfBlackberries))
            if numOfBlackberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfBlackberries < 100 and numOfBlackberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfBlackberries < 1000 and numOfBlackberries > 99:
                currentfruitlabel.place(x="155", y="290")
            munch = munch + random.randint(98, 110)
            munchstringvar.set("Munch: " + str(munch))
            if munch < 10:
                munchlabel.place(x="340", y="20")
            if munch < 100 and munch > 9:
                munchlabel.place(x="335", y="20")
            if munch < 1000 and munch > 99:
                munchlabel.place(x="330", y="20")

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
    pearsinventory = StringVar()
    pearsinventory.set("Pears: " + str(numOfPears))
    pearsinvlabel = Label(inventorywindow, textvariable=pearsinventory)
    pearsinvlabel.place(x="0", y="40")
    orangesinventory = StringVar()
    orangesinventory.set("Oranges: " + str(numOfOranges))
    orangesinvlabel = Label(inventorywindow, textvariable=orangesinventory)
    orangesinvlabel.place(x="0", y="60")
    mangosinventory = StringVar()
    mangosinventory.set("Mangoes: " + str(numOfMangos))
    mangosinvlabel = Label(inventorywindow, textvariable=mangosinventory)
    mangosinvlabel.place(x="0", y="80")
    strawberriesinventory = StringVar()
    strawberriesinventory.set("Strawberries: " + str(numOfStrawberries))
    strawberriesinvlabel = Label(inventorywindow, textvariable=strawberriesinventory)
    strawberriesinvlabel.place(x="0", y="100")
    blueberriesinventory = StringVar()
    blueberriesinventory.set("Blueberries: " + str(numOfBlueberries))
    blueberriesinvlabel = Label(inventorywindow, textvariable=blueberriesinventory)
    blueberriesinvlabel.place(x="0", y="120")
    blackberriesinventory = StringVar()
    blackberriesinventory.set("Blackberries: " + str(numOfBlackberries))
    blackberriesinvlabel = Label(inventorywindow, textvariable=blackberriesinventory)
    blackberriesinvlabel.place(x="0", y="140")
    inventorywindow.iconbitmap("images/apple.ico")
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
    Button(marketwindow, text="Buy Apple\n$1", command=buyapple, width="11").grid(row="0", column="1")
    Button(marketwindow, text="Buy Pack (6)\n$6", command=buyapplepack, width="11").grid(row="0", column="2")
    Button(marketwindow, text="Buy Crate (36)\n$36", command=buyapplecrate, width="11").grid(row="0", column="3")
    Label(marketwindow, text="Buy\nBanana", width="8").grid(row="1", column="0")
    Button(marketwindow, text="Buy Banana\n$5", command=buybanana, width="11").grid(row="1", column="1")
    Button(marketwindow, text="Buy Bunch (4)\n$20", command=buybananabunch, width="11").grid(row="1", column="2")
    Button(marketwindow, text="Buy Crate (30)\n$150", command=buybananacrate, width="11").grid(row="1", column="3")
    Label(marketwindow, text="Buy\nPear", width="8").grid(row="2", column="0")
    Button(marketwindow, text="Buy Pear\n$10", command=buypear, width="11").grid(row="2", column="1")
    Button(marketwindow, text="Buy Pack (3)\n$30", command=buypearpack, width="11").grid(row="2", column="2")
    Button(marketwindow, text="Buy Crate (25)\n$250", command=buypearcrate, width="11").grid(row="2", column="3")
    Label(marketwindow, text="Buy\nOrange", width="8").grid(row="3", column="0")
    Button(marketwindow, text="Buy Orange\n$20", command=buyorange, width="11").grid(row="3", column="1")
    Button(marketwindow, text="Buy Bag (4)\n$80", command=buyorangebag, width="11").grid(row="3", column="2")
    Button(marketwindow, text="Buy Crate (20)\n$400", command=buyorangecrate, width="11").grid(row="3", column="3")
    Label(marketwindow, text="Buy\nMango", width="8").grid(row="4", column="0")
    Button(marketwindow, text="Buy Mango\n$50", command=buymango, width="11").grid(row="4", column="1")
    Button(marketwindow, text="Buy Bag (2)\n$100", command=buymangobag, width="11").grid(row="4", column="2")
    Button(marketwindow, text="Buy Crate (15)\n$750", command=buymangocrate, width="11").grid(row="4", column="3")
    Label(marketwindow, text="Buy\nStrawberry", width="8").grid(row="5", column="0")
    Button(marketwindow, text="Buy Strawberry\n$10", command=buystrawberry, width="11").grid(row="5", column="1")
    Button(marketwindow, text="Buy Box (25)\n$250", command=buystrawberrybox, width="11").grid(row="5", column="2")
    Button(marketwindow, text="Buy Crate (750)\n$7500", command=buystrawberrycrate, width="11").grid(row="5", column="3")
    Label(marketwindow, text="Buy\nBlueberry", width="8").grid(row="6", column="0")
    Button(marketwindow, text="Buy Blueberry\n$15", command=buyblueberry, width="11").grid(row="6", column="1")
    Button(marketwindow, text="Buy Box (25)\n$375", command=buyblueberrybox, width="11").grid(row="6", column="2")
    Button(marketwindow, text="Buy Crate (750)\n$11250", command=buyblueberrycrate, width="11").grid(row="6", column="3")
    Label(marketwindow, text="Buy\nBlackberry", width="8").grid(row="7", column="0")
    Button(marketwindow, text="Buy Blackberry\n$20", command=buyblackberry, width="11").grid(row="7", column="1")
    Button(marketwindow, text="Buy Box (15)\n$300", command=buyblackberrybox, width="11").grid(row="7", column="2")
    Button(marketwindow, text="Buy Crate (450)\n$9000", command=buyblackberrycrate, width="11").grid(row="7", column="3")
    marketwindow.iconbitmap("images/apple.ico")
    marketwindow.mainloop()

def upgrades():
    global upgradeswindow
    global multiconverttextvar
    global multiconvertbutton
    root.withdraw()
    upgradeswindow = Toplevel()
    upgradeswindow.title("Fruit Clicker - Upgrades")
    upgradeswindow.geometry("400x350+300+100")
    upgradeswindow.protocol("WM_DELETE_WINDOW", upgradesOnClose)
    upgradeswindow.iconbitmap("images/apple.ico")
    multiconverttextvar = StringVar()
    multiconverttextvar.set("Multi Convert Lv. " + str(multiconvertlevel) + " -> " + str(multiconvertlevel + 1) + " $" + str(multiconvertcost))
    multiconvertbutton = Button(upgradeswindow, textvariable=multiconverttextvar, width="56", command=multiconvertbuy).grid(row="0", column="0")
    upgradeswindow.mainloop()

root = Tk()
root.title("Fruit Clicker")
root.geometry("400x350+300+100")

inventorybutton = Button(root, text="Inventory", fg="White", bg="Black", width="11", command=inventory)
inventorybutton.grid(column="0", row="0")

marketbutton = Button(root, text="Market", fg="White", bg="Black", width="11", command=market)
marketbutton.grid(column="0", row="1")

upgradesbutton = Button(root, text="Upgrades", fg="White", bg="Black", width="11", command=upgrades)
upgradesbutton.grid(column="0", row="2")

leftfruitbutton = Button(root, text="<", command=switchleft, state=DISABLED)
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
moneylabel = Label(root, textvariable=moneystringvar)
moneyplace()
moneystringvar.set("You have $" + str(money))

munchstringvar = StringVar()
munchstringvar.set("Munch: " + str(munch))
munchlabel = Label(root, textvariable=munchstringvar)
if munch < 10:
    munchlabel.place(x="340", y="20")
if munch < 100 and munch > 9:
    munchlabel.place(x="335", y="20")
if munch < 1000 and munch > 99:
    munchlabel.place(x="330", y="20")

clickerphoto = PhotoImage(file = "images/apple.png")
clickerphoto2 = PhotoImage(file = "images/banana.png")
clickerphoto3 = PhotoImage(file = "images/pear.png")
clickerphoto4 = PhotoImage(file = "images/orange.png")
clickerphoto5 = PhotoImage(file = "images/mango.png")
clickerphoto6 = PhotoImage(file = "images/strawberry.png")
clickerphoto7 = PhotoImage(file = "images/blueberry.png")
clickerphoto8 = PhotoImage(file = "images/blackberry.png")
clickerbutton = Button(root, text="Clicker Button", image=clickerphoto, fg="Black", command=clicked)
clickerbutton.place(x="100", y="75")

musicselectbutton = Button(root, text="Music", command=musicselect, bg="Black", fg="White", width="11")
musicselectbutton.grid(row="4", column="0")

savebutton = Button(root, text="Save", fg="White", bg="Black", width="11", command=save)
savebutton.grid(row="5", column="0")

loadbutton = Button(root, text="Load", fg="White", bg="Black", width="11", command=load)
loadbutton.grid(row="6", column="0")

munchconvertbutton = Button(root, text="Convert Munch", fg="White", bg="Black", width="11", command=convertmunch)
munchconvertbutton.grid(row="7", column="0")




root.iconbitmap("images/apple.ico")
root.mainloop()
