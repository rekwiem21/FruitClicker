from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from numerize import numerize
import pygame
import os
import random
from datetime import datetime
import threading
import time
import requests

pygame.init()

autoeatcost = 50
autoclicklevel = 0
totalfruitclicked = 0
totalfruitbought = 0
wholedate = datetime.date(datetime.now())
date = wholedate.strftime("%d")
month = wholedate.strftime("%m")
year = wholedate.strftime("%Y")
munch = 0
rawmunch = 0
money = 0
rawmoney = 10
currentfruit = "Apple"
multiconvertlevel = 0
fruitupgradelevel = 0
multiconvertcost = 50
marketpage = 1
numOfApples = 0
numOfBananas = 0
numOfPears = 0
numOfOranges = 0
numOfMangos = 0
numOfStrawberries = 0
numOfBlueberries = 0
numOfBlackberries = 0
numOfRaspberries = 0
numOfGrapes = 0
numOfWatermelons = 0
numOfPineapples = 0

def update():
    url = "https://raw.githubusercontent.com/SeaPuppy2006/FruitClicker/master/windows/images/apple.ico"
    r = requests.get(url, allow_redirects=True)
    open("stuff.png", "wb").write(r.content)

def marketplace():
    global marketapplecount
    if marketpage == 1:
        Label(marketwindow, text="Buy\nApple", width="8").grid(row="0", column="0")
        Button(marketwindow, text="Buy Apple\n$1", command=buyapple, width="11").grid(row="0", column="1")
        Button(marketwindow, text="Buy Pack (6)\n$6", command=buyapplepack, width="11").grid(row="0", column="2")
        Button(marketwindow, text="Buy Crate (36)\n$36", command=buyapplecrate, width="11").grid(row="0", column="3")
        marketapplecount = StringVar()
        marketapplecount.set("Current:\n" + str(numOfApples))
        applecountlabel = Label(marketwindow, textvariable=marketapplecount).grid(row="0", column="4")
    if fruitupgradelevel == 1 and marketpage == 1:
        Label(marketwindow, text="Buy\nBanana", width="8").grid(row="1", column="0")
        Button(marketwindow, text="Buy Banana\n$5", command=buybanana, width="11").grid(row="1", column="1")
        Button(marketwindow, text="Buy Bunch (4)\n$20", command=buybananabunch, width="11").grid(row="1", column="2")
        Button(marketwindow, text="Buy Crate (30)\n$150", command=buybananacrate, width="11").grid(row="1", column="3")
    if fruitupgradelevel == 2 and marketpage == 1:
        Label(marketwindow, text="Buy\nBanana", width="8").grid(row="1", column="0")
        Button(marketwindow, text="Buy Banana\n$5", command=buybanana, width="11").grid(row="1", column="1")
        Button(marketwindow, text="Buy Bunch (4)\n$20", command=buybananabunch, width="11").grid(row="1", column="2")
        Button(marketwindow, text="Buy Crate (30)\n$150", command=buybananacrate, width="11").grid(row="1", column="3")
        Label(marketwindow, text="Buy\nPear", width="8").grid(row="2", column="0")
        Button(marketwindow, text="Buy Pear\n$10", command=buypear, width="11").grid(row="2", column="1")
        Button(marketwindow, text="Buy Pack (3)\n$30", command=buypearpack, width="11").grid(row="2", column="2")
        Button(marketwindow, text="Buy Crate (25)\n$250", command=buypearcrate, width="11").grid(row="2", column="3")
    if fruitupgradelevel == 3 and marketpage == 1:
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
    if fruitupgradelevel == 4 and marketpage == 1:
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
    if fruitupgradelevel == 5 and marketpage == 1:
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
    if fruitupgradelevel == 6 and marketpage == 1:
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
    if fruitupgradelevel >= 7 and marketpage == 1:
        bananamarketlabel = Label(marketwindow, text="Buy\nBanana", width="8").grid(row="1", column="0")
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
    if fruitupgradelevel == 8 and marketpage == 2:
        Label(marketwindow, text="Buy\nRaspberry", width="8").grid(row="0", column="0")
        Button(marketwindow, text="Buy Raspberry\n$35", command=buyraspberry, width="11").grid(row="0", column="1")
        Button(marketwindow, text="Buy Box (10)\n$300", command=buyraspberrybox, width="11").grid(row="0", column="2")
        Button(marketwindow, text="Buy Crate (150)\n$4500", command=buyraspberrycrate, width="11").grid(row="0", column="3")
    if fruitupgradelevel == 9 and marketpage == 2:
        Label(marketwindow, text="Buy\nRaspberry", width="8").grid(row="0", column="0")
        Button(marketwindow, text="Buy Raspberry\n$35", command=buyraspberry, width="11").grid(row="0", column="1")
        Button(marketwindow, text="Buy Box (10)\n$300", command=buyraspberrybox, width="11").grid(row="0", column="2")
        Button(marketwindow, text="Buy Crate (150)\n$4500", command=buyraspberrycrate, width="11").grid(row="0", column="3")
        Label(marketwindow, text="Buy\nGrapes", width="8").grid(row="0", column="0")
        Button(marketwindow, text="Buy Grapes\n$10", command=buygrape, width="11").grid(row="0", column="1")
        Button(marketwindow, text="Buy Bag (50)\n$300", command=buygrapebag, width="11").grid(row="0", column="2")
        Button(marketwindow, text="Buy Crate (300)\n$3000", command=buygrapecrate, width="11").grid(row="0", column="3")

def marketpageleft():
    global marketpage
    if not marketpage == 1:
        marketpage = marketpage - 1
        marketplace()

def marketpageright():
    global marketpage
    if not marketpage == 2:
        marketpage = marketpage + 1
        marketplace()

def autoeatbuy():
    global rawmoney
    global autoclicklevel
    global autoeatcost
    if autoclicklevel == 10:
        messagebox.showinfo("Max Level", "Auto Eat is Max Level!")
    else:
        if rawmoney < autoeatcost:
            messagebox.showerror("Error", "Not enough money!")
        else:
            rawmoney = rawmoney - autoeatcost
            moneyplace()
            autoclicklevel = autoclicklevel + 1
            if autoclicklevel == 1:
                autoclick()
            autoeatcost = round(autoeatcost * 3 / 2 + 2)
            if autoclicklevel == 10:
                autoeattextvar.set("Auto Eat (Lv. MAX)")
            else:
                autoeattextvar.set("Auto Eat (Lv. " + str(autoclicklevel) + " -> " + str(autoclicklevel + 1) + ") $" + str(autoeatcost))

def autoclick():
    if autoclicklevel == 1:
        threading.Timer(9.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 2:
        threading.Timer(8.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 3:
        threading.Timer(7.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 4:
        threading.Timer(6.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 5:
        threading.Timer(5.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:            
            clicked()
    if autoclicklevel == 6:
        threading.Timer(4.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 7:
        threading.Timer(3.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 8:
        threading.Timer(2.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 9:
        threading.Timer(1.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
    if autoclicklevel == 10:
        threading.Timer(0.99, autoclick).start()
        if currentfruit == "Apple" and numOfApples > 0 or currentfruit == "Banana" and numOfBananas > 0 or currentfruit == "Pear" and numOfPears > 0 or currentfruit == "Orange" and numOfOranges > 0 or currentfruit == "Mango" and numOfMangos > 0 or currentfruit == "Strawberry" and numOfStrawberries > 0 or currentfruit == "Blueberry" and numOfBlueberries > 0 or currentfruit == "Blackberry" and numOfBlackberries > 0 or currentfruit == "Raspberry" and numOfRaspberries > 0:
            clicked()
        
def rootOnClose():
    root.destroy()    

def fixdate():
    global date
    if date == 1:
        date = "01"
    if date == 2:
        date = "02"
    if date == 3:
        date = "03"
    if date == 4:
        date = "04"
    if date == 5:
        date = "05"
    if date == 6:
        date = "06"
    if date == 7:
        date = "07"
    if date == 8:
        date = "08"
    if date == 9:
        date = "09"

def fixmonth():
    global month
    if month == 1:
        month = "01"
    if month == 2:
        month = "02"
    if month == 3:
        month = "03"
    if month == 4:
        month = "04"
    if month == 5:
        month = "05"
    if month == 6:
        month = "06"
    if month == 7:
        month = "07"
    if month == 8:
        month = "08"
    if month == 9:
        month = "09"
    if month == 10:
        month = "10"
    if month == 11:
        month = "11"
    if month == 12:
        month = "12"

def advancetime():
    global datelabelstringvar
    global date
    global month
    global year
    global calendarthread
    calendarthread = threading.Timer(90.0, advancetime).start()
    if month == "09" or month == "04" or month == "06" or month == "11":
        date = int(date) + 1
        if date > 30:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
        return
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        date = int(date) + 1
        if date > 31:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
        return
    if month == "02":
        date = int(date) + 1
        if date > 31:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
    
def calendarOnClose():
    root.deiconify()
    calendarwindow.destroy()

def calendar():
    global datelabelstringvar
    global calendarwindow
    root.withdraw()
    calendarwindow = Toplevel()
    calendarwindow.title("Calendar")
    calendarwindow.geometry("400x350+300+100")
    calendarwindow.protocol("WM_DELETE_WINDOW", calendarOnClose)
    datelabelstringvar = StringVar()
    datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
    datelabel = Label(calendarwindow, textvariable=datelabelstringvar).grid(row="0", column="0")
    totalfruitclickerstringvar = StringVar()
    totalfruitclickerstringvar.set("Fruit Clicked: " + str(totalfruitclicked))
    Label(calendarwindow, textvariable=totalfruitclickerstringvar).grid(row="2", column="0")

def fruitupgradebuy():
    global fruitupgradelevel
    global rawmoney
    if fruitupgradelevel == 0:
        if rawmoney < 25:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 25
            moneyplace()
            fruitupgradetextvar.set("Market Expansion II (Lv. " + str(fruitupgradelevel + 1) + ") $50")
        return
    if fruitupgradelevel == 1:
        if rawmoney < 50:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 50
            moneyplace()
            fruitupgradetextvar.set("Citrus Stall (Lv. " + str(fruitupgradelevel + 1) + ") $250")
        return
    if fruitupgradelevel == 2:
        if rawmoney < 250:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 250
            moneyplace()
            fruitupgradetextvar.set("Summertime Shop (Lv. " + str(fruitupgradelevel + 1) + ") $1000")
        return
    if fruitupgradelevel == 3:
        if rawmoney < 1000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 1000
            moneyplace()
            fruitupgradetextvar.set("Berry Investment (Lv. " + str(fruitupgradelevel + 1) + ") $5000")
        return
    if fruitupgradelevel == 4:
        if rawmoney < 5000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 5000
            moneyplace()
            fruitupgradetextvar.set("Berry Investment II (Lv. " + str(fruitupgradelevel + 1) + ") $10000")
        return
    if fruitupgradelevel == 5:
        if rawmoney < 10000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 10000
            moneyplace()
            fruitupgradetextvar.set("Berry Investment III (Lv. " + str(fruitupgradelevel + 1) + ") $50000")
        return
    if fruitupgradelevel == 6:
        if rawmoney < 50000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 50000
            moneyplace()
            fruitupgradetextvar.set("Berry Investment IV (Lv. " + str(fruitupgradelevel + 1) + ") $100000")
        return
    if fruitupgradelevel == 7:
        if rawmoney < 100000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 100000
            moneyplace()
            fruitupgradetextvar.set("Market Upgrade Lv. MAX")
        return
    if fruitupgradelevel == 8:
        messagebox.showerror("Error", "Upgrade is MAX Level!")
    
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
    if int(rawmoney) > 999:
        money = numerize.numerize(rawmoney)
    else:
        money = int(rawmoney)
    if len(str(money)) == 1:
        moneylabel.place(x="327", y="0")
    if len(str(money)) == 2:
        moneylabel.place(x="320", y="0")
    if len(str(money)) == 3:
        moneylabel.place(x="315", y="0")
    if len(str(money)) == 4:
        moneylabel.place(x="310", y="0")
    if len(str(money)) == 5:
        moneylabel.place(x="305", y="0")
    if len(str(money)) == 6:
        moneylabel.place(x="300", y="0")
    if len(str(money)) == 7:
        moneylabel.place(x="295", y="0")

def munchplace():
    global root
    global rawmunch
    global munch
    if rawmunch > 999:
        munch = numerize.numerize(rawmunch)
    else:
        munch = rawmunch
    if len(str(munch)) == 1:
        munchlabel.place(x="340", y="20")
    if len(str(munch)) == 2:
        munchlabel.place(x="335", y="20")
    if len(str(munch)) == 3:
        munchlabel.place(x="330", y="20")
    if len(str(munch)) == 4:
        munchlabel.place(x="323", y="20")
    if len(str(munch)) == 5:
        munchlabel.place(x="320", y="20")
    if len(str(munch)) == 6:
        munchlabel.place(x="315", y="20")
    if len(str(munch)) == 7:
        munchlabel.place(x="310", y="20")
                
def convertmunch():
    global munch
    global rawmunch
    global rawmoney
    global multiconvertlevel
    if multiconvertlevel == 0:
        if rawmunch < 5:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 5
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
            rawmoney = rawmoney + 1
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 1:
        if rawmunch < 10:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 10
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
            rawmoney = rawmoney + 2
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 2:
        if rawmunch < 15:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 15
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 3
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 3:
        if rawmunch < 20:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 20
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 4
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 4:
        if rawmunch < 25:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 25
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 5
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 5:
        if rawmunch < 30:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 30
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 6
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 6:
        if rawmunch < 35:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = munch - 35
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 7
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 7:
        if rawmunch < 40:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 40
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 8
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 8:
        if rawmunch < 45:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 45
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 9
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 9:
        if rawmunch < 50:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 50
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 10
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 10:
        if rawmunch < 55:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 55
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 11
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 11:
        if rawmunch < 60:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 60
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 12
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 12:
        if rawmunch < 65:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 65
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 13
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 13:
        if rawmunch < 70:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 70
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 14
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 14:
        if munch < 75:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 75
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 15
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 15:
        if rawmunch < 80:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 80
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 16
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 16:
        if rawmunch < 85:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 85
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 17
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 17:
        if rawmunch < 90:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 90
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 18
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 18:
        if rawmunch < 95:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 95
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 19
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 19:
        if rawmunch < 100:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 100
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 20
            moneyplace()
            moneystringvar.set("You have $" + str(money))
    if multiconvertlevel == 20:
        if rawmunch < 105:
            messagebox.showerror("Error", "Not enough munch!")
        else:
            rawmunch = rawmunch - 105
            munchstringvar.set("Munch: " + str(munch))
            munchplace()
            rawmoney = rawmoney + 21
            moneyplace()
            moneystringvar.set("You have $" + str(money))

def save():
    if os.path.exists("save.fcsave") == True:
        if messagebox.askyesno("Save Exists", "A save file already exists.\nWould you still like to save?") == True:
            savedoc = open("save.fcsave", "w+")
            savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
            messagebox.showinfo("Save", "Your game has been saved!")
        else:
            messagebox.showinfo("Save", "Your game will not be saved")
    else:
        savedoc = open("save.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        messagebox.showinfo("Save", "Your game has been saved!")

def load():
    global rawmoney
    global rawmunch
    global numOfApples
    global numOfBananas
    global numOfPears
    global numOfOranges
    global numOfMangos
    global numOfStrawberries
    global numOfBlueberries
    global numOfBlackberries
    global multiconvertlevel
    global fruitupgradelevel
    global autoclicklevel
    global autoeatcost
    global multiconvertcost
    global wholedate
    if os.path.exists("save.fcsave") == True:
        loadedfile = open("save.fcsave")
        loadedfilelines = loadedfile.readlines()
        rawmoney = str(loadedfilelines[0])
        rawmoney = int(rawmoney)
        moneyplace()
        moneystringvar.set("You have $" + str(money))
        rawmunch = str(loadedfilelines[1])
        rawmunch = int(rawmunch)
        munchplace()
        munchstringvar.set("Munch: " + str(munch))
        numOfApples = int(loadedfilelines[2])
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        numOfBananas = int(loadedfilelines[3])
        numOfPears = int(loadedfilelines[4])
        numOfOranges = int(loadedfilelines[5])
        numOfMangos = int(loadedfilelines[6])
        numOfStrawberries =int(loadedfilelines[7])
        numOfBlueberries = int(loadedfilelines[8])
        numOfBlackberries = int(loadedfilelines[9])
        multiconvertlevel = int(loadedfilelines[10])
        multiconvertcost = int(loadedfilelines[11])
        autoclicklevel = int(loadedfilelines[12])
        autoeatcost = int(loadedfilelines[13])
        fruitupgradelevel = int(loadedfilelines[14])
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
        clickerbutton.config(image=clickerphoto7)
        currentfruitstringvar.set("Blueberry x" + str(numOfBlueberries))
        if numOfBlueberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlueberries < 100 and numOfBlueberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlueberries < 1000 and numOfBlueberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Raspberry":
        currentfruit = "Blackberry"
        rightfruitbutton.config(state=NORMAL)
        clickerbutton.config(image=clickerphoto8)
        currentfruitstringvar.set("Blackberry x" + str(numOfBlackberries))
        if numOfBlackberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlackberries < 100 and numOfBlackberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlackberries < 1000 and numOfBlackberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Grapes":
        currentfruit = "Raspberry"
        clickerbutton.config(image=clickerphoto9)
        currentfruitstringvar.set("Raspberry x" + str(numOfRaspberries))
        if numOfRaspberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfRaspberries < 100 and numOfRaspberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfRaspberries < 1000 and numOfRaspberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Watermelon":
        currentfruit = "Grapes"
        clickerbutton.config(image=clickerphoto10)
        currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
        if numOfGrapes < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfGrapes < 100 and numOfGrapes > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfGrapes < 1000 and numOfGrapes > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Pineapple":
        currentfruit = "Watermelon"
        clickerbutton.config(image=clickerphoto11)
        rightfruitbutton.config(state=NORMAL)
        currentfruitstringvar.set("Watermelon x" + str(numOfWatermelons))
        if numOfWatermelons < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfWatermelons < 100 and numOfWatermelons > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfWatermelons < 1000 and numOfWatermelons > 99:
            currentfruitlabel.place(x="155", y="290")

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
        clickerbutton.config(image=clickerphoto8)
        currentfruitstringvar.set("Blackberry x" + str(numOfBlackberries))
        if numOfBlackberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfBlackberries < 100 and numOfBlackberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfBlackberries < 1000 and numOfBlackberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Blackberry":
        currentfruit = "Raspberry"
        clickerbutton.config(image=clickerphoto9)
        currentfruitstringvar.set("Raspberry x" + str(numOfRaspberries))
        if numOfRaspberries < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfRaspberries < 100 and numOfRaspberries > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfRaspberries < 1000 and numOfRaspberries > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Raspberry":
        currentfruit = "Grapes"
        clickerbutton.config(image=clickerphoto10)
        currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
        if numOfGrapes < 10:
            currentfruitlabel.place(x="175", y="290")
        if numOfGrapes < 100 and numOfGrapes > 9:
            currentfruitlabel.place(x="170", y="290")
        if numOfGrapes < 1000 and numOfGrapes > 99:
            currentfruitlabel.place(x="165", y="290")
        return
    if currentfruit == "Grapes":
        currentfruit = "Watermelon"
        clickerbutton.config(image=clickerphoto11)
        currentfruitstringvar.set("Watermelon x" + str(numOfWatermelons))
        if numOfWatermelons < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfWatermelons < 100 and numOfWatermelons > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfWatermelons < 1000 and numOfWatermelons > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Watermelon":
        currentfruit = "Pineapple"
        rightfruitbutton.config(state=DISABLED)
        clickerbutton.config(image=clickerphoto12)
        currentfruitstringvar.set("Pineapple x" + str(numOfPineapples))
        if numOfPineapples < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfPineapples < 100 and numOfPineapples > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfPineapples < 1000 and numOfPineapples > 99:
            currentfruitlabel.place(x="155", y="290")
    
def musicselect():
    musicfilename = filedialog.askopenfilename(initialdir = "/",title = "Select MP3 File", filetypes=(("MP3 Files","*.mp3"),("WAV Files","*.wav")))
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
        marketapplecount.set("Current:\n" + str(numOfApples))
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketapplecount.set("Current:\n" + str(numOfApples))
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketapplecount.set("Current:\n" + str(numOfApples))
        if currentfruit == "Apple":
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
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
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buyraspberry():
    global money
    global rawmoney
    global numOfRaspberries
    if rawmoney < 35:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 35
        numOfRaspberries = numOfRaspberries + 1
        if currentfruit == "Raspberry":
            currentfruitstringvar.set("Raspberries x" + str(numOfRaspberries))
            if numOfRaspberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfRaspberries < 100 and numOfRaspberries > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfRaspberries < 1000 and numOfRaspberries > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))
            
def clicked():
    global munch
    global rawmunch
    global currentfruit
    global numOfApples
    global numOfBananas
    global numOfPears
    global numOfOranges
    global numOfMangos
    global numOfStrawberries
    global numOfBlueberries
    global numOfBlackberries
    global numOfRaspberries
    global totalfruitclicked
    if currentfruit == "Apple":
        if numOfApples == 0:
            messagebox.showerror("Error", "You do not have any Apples!")
        else:
            totalfruitclicked = totalfruitclicked + 1
            numOfApples = numOfApples - 1
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
            rawmunch = rawmunch + random.randint(5, 10)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(30, 35)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(60, 75)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(95, 110)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(245, 250)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(48, 55)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(73, 82)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
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
            rawmunch = rawmunch + random.randint(98, 110)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
    if currentfruit == "Raspberry":
        if numOfRaspberries == 0:
            messagebox.showerror("Error", "You do not have any Raspberries!")
        else:
            numOfRaspberries = numOfRaspberries - 1
            currentfruitstringvar.set("Raspberries x" + str(numOfRaspberries))
            if numOfRaspberries < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfRaspberries < 100 and numOfRaspberries > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfRaspberries < 1000 and numOfRaspberries > 99:
                currentfruitlabel.place(x="155", y="290")
            rawmunch = rawmunch + random.randint(173, 185)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
            
def inventoryOnClose():
    root.deiconify()
    inventorywindow.destroy()

def marketOnClose():
    root.deiconify()
    marketwindow.destroy()
    
def upgradesOnClose():
    root.deiconify()
    moneyplace()
    upgradeswindow.destroy()

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
    raspberriesinventory = StringVar()
    raspberriesinventory.set("Raspberries: " + str(numOfRaspberries))
    raspberriesinvlabel = Label(inventorywindow, textvariable=raspberriesinventory)
    raspberriesinvlabel.place(x="0", y="140")
    inventorywindow.iconbitmap("images/apple.ico")
    inventorywindow.mainloop()

def market():
    global marketapplecount
    global marketwindow
    global marketmoneylabelstringvar
    global marketleftbutton
    root.withdraw()
    marketwindow = Toplevel()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)
    marketplace()
    marketleftbutton = Button(marketwindow, text="<", width="6", command=marketpageleft)
    marketleftbutton.place(x="0", y="325")
    marketrightbutton = Button(marketwindow, text=">", width="6", command=marketpageright)
    marketrightbutton.place(x="347", y="325")
    marketmoneylabelstringvar = StringVar()
    marketmoneylabelstringvar.set("$" + str(money))
    marketmoneylabel = Label(marketwindow, textvariable=marketmoneylabelstringvar)
    marketmoneylabel.place(x="190", y="330")
    marketwindow.iconbitmap("images/apple.ico")
    marketwindow.mainloop()

def upgrades():
    global upgradeswindow
    global multiconverttextvar
    global multiconvertbutton
    global fruitupgradetextvar
    global autoeattextvar
    root.withdraw()
    upgradeswindow = Toplevel()
    upgradeswindow.title("Fruit Clicker - Upgrades")
    upgradeswindow.geometry("400x350+300+100")
    upgradeswindow.protocol("WM_DELETE_WINDOW", upgradesOnClose)
    upgradeswindow.iconbitmap("images/apple.ico")
    multiconverttextvar = StringVar()
    multiconverttextvar.set("Multi Convert (Lv. " + str(multiconvertlevel) + " -> " + str(multiconvertlevel + 1) + ") $" + str(multiconvertcost))
    multiconvertbutton = Button(upgradeswindow, textvariable=multiconverttextvar, width="56", command=multiconvertbuy).grid(row="0", column="0")
    fruitupgradetextvar = StringVar()
    fruitupgradebutton = Button(upgradeswindow, textvariable=fruitupgradetextvar, width="56", command=fruitupgradebuy).grid(row="1", column="0")
    if fruitupgradelevel == 0:
        fruitupgradetextvar.set("Market Expansion (Lv. " + str(fruitupgradelevel + 1) + ") $25")
    if fruitupgradelevel == 1:
        fruitupgradetextvar.set("Market Expansion II (Lv. " + str(fruitupgradelevel + 1) + ") $50")
    if fruitupgradelevel == 2:
        fruitupgradetextvar.set("Citrus Stall (Lv. " + str(fruitupgradelevel + 1) + ") $250")
    if fruitupgradelevel == 3:
        fruitupgradetextvar.set("Summertime Shop (Lv. " + str(fruitupgradelevel + 1) + ") $1000")
    if fruitupgradelevel == 4:
        fruitupgradetextvar.set("Berry Investment (Lv. " + str(fruitupgradelevel + 1) + ") $5000")
    if fruitupgradelevel == 5:
        fruitupgradetextvar.set("Berry Investment II (Lv. " + str(fruitupgradelevel + 1) + ") $10000")
    if fruitupgradelevel == 6:
        fruitupgradetextvar.set("Berry Investment III (Lv. " + str(fruitupgradelevel + 1) + ") $50000")
    if fruitupgradelevel == 7:
        fruitupgradetextvar.set("Berry Investment IV (Lv. " + str(fruitupgradelevel + 1) + ") $100000")
    if fruitupgradelevel == 8:
        fruitupgradetextvar.set("Market Upgrade Lv. MAX")
    autoeattextvar = StringVar()
    autoeattextvar.set("Auto Eat (Lv. " + str(autoclicklevel) + " -> " + str(autoclicklevel + 1) + ") $" + str(autoeatcost))
    autoeatupgradebutton = Button(upgradeswindow, textvariable=autoeattextvar, width="56", command=autoeatbuy).grid(row="2", column="0")
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
munchlabel = Label(root, textvariable=munchstringvar)
munchplace()
munchstringvar.set("Munch: " + str(munch))

clickerphoto = PhotoImage(file = "images/apple.png")
clickerphoto2 = PhotoImage(file = "images/banana.png")
clickerphoto3 = PhotoImage(file = "images/pear.png")
clickerphoto4 = PhotoImage(file = "images/orange.png")
clickerphoto5 = PhotoImage(file = "images/mango.png")
clickerphoto6 = PhotoImage(file = "images/strawberry.png")
clickerphoto7 = PhotoImage(file = "images/blueberry.png")
clickerphoto8 = PhotoImage(file = "images/blackberry.png")
clickerphoto9 = PhotoImage(file = "images/raspberry.png")
clickerphoto10 = PhotoImage(file = "images/grapes.png")
clickerphoto11 = PhotoImage(file = "images/watermelon.png")
clickerphoto12 = PhotoImage(file = "images/pineapple.png")
clickerphoto13 = PhotoImage(file = "images/coconut.png")
clickerphoto14 = PhotoImage(file = "images/guava.png")
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

calendarbutton = Button(root, text="Calendar", fg="White", bg="Black", width="11", command=calendar)
calendarbutton.grid(row="8", column="0")

Button(root, text="Update", command=update).grid(row="9", column="0")

calendar()
date = int(date) - 1
fixdate()
calendarwindow.destroy()
root.deiconify()
advancetime()

root.iconbitmap("images/apple.ico")
root.protocol("WM_DELETE_WINDOW", rootOnClose)
root.mainloop()
