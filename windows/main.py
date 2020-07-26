from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from numerize import numerize
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
from datetime import datetime
import threading
import time
import requests
import subprocess

pygame.init()

saveopen = 0
appleprice = 1
applesboughttoday = 0
bananaprice = 5
bananasboughttoday = 0
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
numOfCoconuts = 0

def marketplace():
    global marketapplecount
    global marketbananacount
    global marketpearcount
    global marketorangecount
    global marketmangocount
    global marketstrawberrycount
    global marketblueberrycount
    global marketblackberrycount
    global marketraspberrycount
    global marketgrapescount
    global marketmeloncount
    global bananalabel
    global bananabutton1
    global bananabutton2
    global bananabutton3
    global bananacountlabel
    global pearlabel
    global pearbutton1
    global pearbutton2
    global pearbutton3
    global pearcountlabel
    global orangelabel
    global orangebutton1
    global orangebutton2
    global orangebutton3
    global orangecountlabel
    global mangolabel
    global mangobutton1
    global mangobutton2
    global mangobutton3
    global mangocountlabel
    global strawberrylabel
    global strawberrybutton1
    global strawberrybutton2
    global strawberrybutton3
    global strawberrycountlabel
    global blueberrylabel
    global blueberrybutton1
    global blueberrybutton2
    global blueberrybutton3
    global blueberrycountlabel
    global blackberrylabel
    global blackberrybutton1
    global blackberrybutton2
    global blackberrybutton3
    global blackberrycountlabel
    if marketpage == 1:
        Label(marketwindow, text="Buy\nApple", width="8").grid(row="0", column="0")
        Button(marketwindow, text="Buy Apple\n$" + numerize.numerize(appleprice), command=buyapple, width="11").grid(row="0", column="1")
        Button(marketwindow, text="Buy Pack (6)\n$" + numerize.numerize(appleprice * 6), command=buyapplepack, width="11").grid(row="0", column="2")
        Button(marketwindow, text="Buy Crate (36)\n$" + numerize.numerize(appleprice * 36), command=buyapplecrate, width="11").grid(row="0", column="3")
        marketapplecount = StringVar()
        marketapplecount.set("Current:\n" + str(numOfApples))
        applecountlabel = Label(marketwindow, textvariable=marketapplecount).grid(row="0", column="4")
    if fruitupgradelevel >= 1 and marketpage == 1:
        bananalabel = Label(marketwindow, text="Buy\nBanana", width="8")
        bananalabel.grid(row="1", column="0")
        bananabutton1 = Button(marketwindow, text="Buy Banana\n$" + numerize.numerize(bananaprice), command=buybanana, width="11")
        bananabutton1.grid(row="1", column="1")
        bananabutton2 = Button(marketwindow, text="Buy Bunch (4)\n$" + numerize.numerize(bananaprice * 4), command=buybananabunch, width="11")
        bananabutton2.grid(row="1", column="2")
        bananabutton3 = Button(marketwindow, text="Buy Crate (30)\n$" + numerize.numerize(bananaprice * 30), command=buybananacrate, width="11")
        bananabutton3.grid(row="1", column="3")
        marketbananacount = StringVar()
        marketbananacount.set("Current:\n" + str(numOfBananas))
        bananacountlabel = Label(marketwindow, textvariable=marketbananacount)
        bananacountlabel.grid(row="1", column="4")
    if fruitupgradelevel >= 2 and marketpage == 1:
        pearlabel = Label(marketwindow, text="Buy\nPear", width="8")
        pearlabel.grid(row="2", column="0")
        pearbutton1 = Button(marketwindow, text="Buy Pear\n$10", command=buypear, width="11")
        pearbutton1.grid(row="2", column="1")
        pearbutton2 = Button(marketwindow, text="Buy Pack (3)\n$30", command=buypearpack, width="11")
        pearbutton2.grid(row="2", column="2")
        pearbutton3 = Button(marketwindow, text="Buy Crate (25)\n$250", command=buypearcrate, width="11")
        pearbutton3.grid(row="2", column="3")
        marketpearcount = StringVar()
        marketpearcount.set("Current:\n" + str(numOfPears))
        pearcountlabel = Label(marketwindow, textvariable=marketpearcount)
        pearcountlabel.grid(row="2", column="4")
    if fruitupgradelevel >= 3 and marketpage == 1:
        orangelabel = Label(marketwindow, text="Buy\nOrange", width="8")
        orangelabel.grid(row="3", column="0")
        orangebutton1 = Button(marketwindow, text="Buy Orange\n$20", command=buyorange, width="11")
        orangebutton1.grid(row="3", column="1")
        orangebutton2 = Button(marketwindow, text="Buy Bag (4)\n$80", command=buyorangebag, width="11")
        orangebutton2.grid(row="3", column="2")
        orangebutton3 = Button(marketwindow, text="Buy Crate (20)\n$400", command=buyorangecrate, width="11")
        orangebutton3.grid(row="3", column="3")
        marketorangecount = StringVar()
        marketorangecount.set("Current:\n" + str(numOfOranges))
        orangecountlabel = Label(marketwindow, textvariable=marketorangecount)
        orangecountlabel.grid(row="3", column="4")
    if fruitupgradelevel >= 4 and marketpage == 1:
        mangolabel = Label(marketwindow, text="Buy\nMango", width="8")
        mangolabel.grid(row="4", column="0")
        mangobutton1 = Button(marketwindow, text="Buy Mango\n$50", command=buymango, width="11")
        mangobutton1.grid(row="4", column="1")
        mangobutton2 = Button(marketwindow, text="Buy Bag (2)\n$100", command=buymangobag, width="11")
        mangobutton2.grid(row="4", column="2")
        mangobutton3 = Button(marketwindow, text="Buy Crate (15)\n$750", command=buymangocrate, width="11")
        mangobutton3.grid(row="4", column="3")
        marketmangocount = StringVar()
        marketmangocount.set("Current:\n" + str(numOfMangos))
        mangocountlabel = Label(marketwindow, textvariable=marketmangocount)
        mangocountlabel.grid(row="4", column="4")
    if fruitupgradelevel >= 5 and marketpage == 1:
        strawberrylabel = Label(marketwindow, text="Buy\nStrawberry", width="8")
        strawberrylabel.grid(row="5", column="0")
        strawberrybutton1 = Button(marketwindow, text="Buy Strawberry\n$10", command=buystrawberry, width="11")
        strawberrybutton1.grid(row="5", column="1")
        strawberrybutton2 = Button(marketwindow, text="Buy Box (25)\n$250", command=buystrawberrybox, width="11")
        strawberrybutton2.grid(row="5", column="2")
        strawberrybutton3 = Button(marketwindow, text="Buy Crate (750)\n$7500", command=buystrawberrycrate, width="11")
        strawberrybutton3.grid(row="5", column="3")
        marketstrawberrycount = StringVar()
        marketstrawberrycount.set("Current:\n" + str(numOfStrawberries))
        strawberrycountlabel = Label(marketwindow, textvariable=marketstrawberrycount)
        strawberrycountlabel.grid(row="5", column="4")
    if fruitupgradelevel >= 6 and marketpage == 1:
        blueberrylabel = Label(marketwindow, text="Buy\nBlueberry", width="8")
        blueberrylabel.grid(row="6", column="0")
        blueberrybutton1 = Button(marketwindow, text="Buy Blueberry\n$15", command=buyblueberry, width="11")
        blueberrybutton1.grid(row="6", column="1")
        blueberrybutton2 = Button(marketwindow, text="Buy Box (25)\n$375", command=buyblueberrybox, width="11")
        blueberrybutton2.grid(row="6", column="2")
        blueberrybutton3 = Button(marketwindow, text="Buy Crate (750)\n$11250", command=buyblueberrycrate, width="11")
        blueberrybutton3.grid(row="6", column="3")
        marketblueberrycount = StringVar()
        marketblueberrycount.set("Current:\n" + str(numOfBlueberries))
        blueberrycountlabel = Label(marketwindow, textvariable=marketblueberrycount)
        blueberrycountlabel.grid(row="6", column="4")
    if fruitupgradelevel >= 7 and marketpage == 1:
        blackberrylabel = Label(marketwindow, text="Buy\nBlackberry", width="8")
        blackberrylabel.grid(row="7", column="0")
        blackberrybutton1 = Button(marketwindow, text="Buy Blackberry\n$20", command=buyblackberry, width="11")
        blackberrybutton1.grid(row="7", column="1")
        blackberrybutton2 = Button(marketwindow, text="Buy Box (15)\n$300", command=buyblackberrybox, width="11")
        blackberrybutton2.grid(row="7", column="2")
        blackberrybutton3 = Button(marketwindow, text="Buy Crate (450)\n$9000", command=buyblackberrycrate, width="11")
        blackberrybutton3.grid(row="7", column="3")
        marketblackberrycount = StringVar()
        marketblackberrycount.set("Current:\n" + str(numOfBlackberries))
        blackberrycountlabel = Label(marketwindow, textvariable=marketblackberrycount)
        blackberrycountlabel.grid(row="7", column="4")
    if fruitupgradelevel >= 8 and marketpage == 2:
        bananalabel.grid_forget()
        bananabutton1.grid_forget()
        bananabutton2.grid_forget()
        bananabutton3.grid_forget()
        bananacountlabel.grid_forget()
        pearlabel.grid_forget()
        pearbutton1.grid_forget()
        pearbutton2.grid_forget()
        pearbutton3.grid_forget()
        pearcountlabel.grid_forget()
        orangelabel.grid_forget()
        orangebutton1.grid_forget()
        orangebutton2.grid_forget()
        orangebutton3.grid_forget()
        orangecountlabel.grid_forget()
        mangolabel.grid_forget()
        mangobutton1.grid_forget()
        mangobutton2.grid_forget()
        mangobutton3.grid_forget()
        mangocountlabel.grid_forget()
        strawberrylabel.grid_forget()
        strawberrybutton1.grid_forget()
        strawberrybutton2.grid_forget()
        strawberrybutton3.grid_forget()
        strawberrycountlabel.grid_forget()
        blueberrylabel.grid_forget()
        blueberrybutton1.grid_forget()
        blueberrybutton2.grid_forget()
        blueberrybutton3.grid_forget()
        blueberrycountlabel.grid_forget()
        blackberrylabel.grid_forget()
        blackberrybutton1.grid_forget()
        blackberrybutton2.grid_forget()
        blackberrybutton3.grid_forget()
        blackberrycountlabel.grid_forget()
        raspberrylabel = Label(marketwindow, text="Buy\nRaspberry", width="8")
        raspberrylabel.grid(row="0", column="0")
        raspberrybutton1 = Button(marketwindow, text="Buy Raspberry\n$35", command=buyraspberry, width="11")
        raspberrybutton1.grid(row="0", column="1")
        raspberrybutton2 = Button(marketwindow, text="Buy Box (10)\n$300", command=buyraspberrybox, width="11")
        raspberrybutton2.grid(row="0", column="2")
        raspberrybutton3 = Button(marketwindow, text="Buy Crate (150)\n$4500", command=buyraspberrycrate, width="11")
        raspberrybutton3.grid(row="0", column="3")
        marketraspberrycount = StringVar()
        marketraspberrycount.set("Current:\n" + str(numOfRaspberries))
        raspberrycountlabel = Label(marketwindow, textvariable=marketraspberrycount)
        raspberrycountlabel.grid(row="0", column="4")
    if fruitupgradelevel >= 9 and marketpage == 2:
        grapeslabel = Label(marketwindow, text="Buy\nGrapes", width="8")
        grapeslabel.grid(row="1", column="0")
        grapesbutton1 = Button(marketwindow, text="Buy Grapes\n$100", command=buygrape, width="11")
        grapesbutton1.grid(row="1", column="1")
        grapesbutton2 = Button(marketwindow, text="Buy Bag (3)\n$300", command=buygrapebag, width="11")
        grapesbutton2.grid(row="1", column="2")
        grapesbutton3 = Button(marketwindow, text="Buy Crate (18)\n$1800", command=buygrapecrate, width="11")
        grapesbutton3.grid(row="1", column="3")
        marketgrapescount = StringVar()
        marketgrapescount.set("Current:\n" + str(numOfGrapes))
        grapescountlabel = Label(marketwindow, textvariable=marketgrapescount)
        grapescountlabel.grid(row="1", column="4")
    if fruitupgradelevel >= 10 and marketpage == 2:
        melonlabel = Label(marketwindow, text="Buy\nMelon", width="8")
        melonlabel.grid(row="2", column="0")
        melonbutton1 = Button(marketwindow, text="Buy Melon\n$1000", command=buymelon, width="11")
        melonbutton1.grid(row="2", column="1")
        melonbutton2 = Button(marketwindow, text="Buy Box (4)\n$4000", command=buymelonbox, width="11")
        melonbutton2.grid(row="2", column="2")
        melonbutton3 = Button(marketwindow, text="Buy Crate (7)\n$7000", command=buymeloncrate, width="11")
        melonbutton3.grid(row="2", column="3")
        marketmeloncount = StringVar()
        marketmeloncount.set("Current:\n" + str(numOfWatermelons))
        meloncountlabel = Label(marketwindow, textvariable=marketmeloncount)
        meloncountlabel.grid(row="2", column="4")

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
    main.deiconify()

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

def stockchange():
    return
    
def advancetime():
    global datelabelstringvar
    global date
    global month
    global year
    global calendarthread
    calendarthread = threading.Timer(90.0, advancetime)
    calendarthread.setDaemon=(True)
    print(calendarthread.isDaemon())
    calendarthread.start()
    stockchange()
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
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Market Expansion II (Lv. " + str(fruitupgradelevel + 1) + ") $50")
        return
    if fruitupgradelevel == 1:
        if rawmoney < 50:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 50
            moneyplace()
            rightfruitbutton.config(state=NORMAL)                
            fruitupgradetextvar.set("Citrus Stall (Lv. " + str(fruitupgradelevel + 1) + ") $250")
        return
    if fruitupgradelevel == 2:
        if rawmoney < 250:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 250
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Summertime Shop (Lv. " + str(fruitupgradelevel + 1) + ") $1K")
        return
    if fruitupgradelevel == 3:
        if rawmoney < 1000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 1000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Berry Investment (Lv. " + str(fruitupgradelevel + 1) + ") $5K")
        return
    if fruitupgradelevel == 4:
        if rawmoney < 5000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 5000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Berry Investment II (Lv. " + str(fruitupgradelevel + 1) + ") $10K")
        return
    if fruitupgradelevel == 5:
        if rawmoney < 10000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 10000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Berry Investment III (Lv. " + str(fruitupgradelevel + 1) + ") $50K")
        return
    if fruitupgradelevel == 6:
        if rawmoney < 50000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 50000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Berry Investment IV (Lv. " + str(fruitupgradelevel + 1) + ") $100K")
        return
    if fruitupgradelevel == 7:
        if rawmoney < 100000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 100000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Berry Investment V (Lv. " + str(fruitupgradelevel + 1) + ") $350K")
        return
    if fruitupgradelevel == 8:
        if rawmoney < 350000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 350000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Melon Fever (Lv. " + str(fruitupgradelevel + 1) + ") $1M")
        return
    if fruitupgradelevel == 9:
        if rawmoney < 1000000:
            messagebox.showerror("Error", "You do not have enough money!")
        else:
            fruitupgradelevel = fruitupgradelevel + 1
            rawmoney = rawmoney - 1000000
            moneyplace()
            rightfruitbutton.config(state=NORMAL)
            fruitupgradetextvar.set("Upgrade is MAX Level!")
        return
    if fruitupgradelevel == 10:
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
    global saveopen
    if saveopen == 1:
        savedoc = open("saves/save1.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        messagebox.showinfo("Info", "Game Saved!")
    if saveopen == 2:
        savedoc = open("saves/save2.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        messagebox.showinfo("Info", "Game Saved!")
    if saveopen == 3:
        savedoc = open("saves/save3.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        messagebox.showinfo("Info", "Game Saved!")
        
def switchleft():
    global currentfruit
    global clickerbutton
    if currentfruit == "Banana":
        currentfruit = "Apple"
        leftfruitbutton.config(state=DISABLED)
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
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
        rightfruitbutton.config(state=NORMAL)
        clickerbutton.config(image=clickerphoto11)
        currentfruitstringvar.set("Watermelon x" + str(numOfWatermelons))
        if numOfWatermelons < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfWatermelons < 100 and numOfWatermelons > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfWatermelons < 1000 and numOfWatermelons > 99:
            currentfruitlabel.place(x="155", y="290")
    if currentfruit == "Coconut":
        currentfruit = "Pineapple"
        clickerbutton.config(image=clickerphoto12)
        rightfruitbutton.config(state=NORMAL)
        currentfruitstringvar.set("Pineapple x" + str(numOfPineapples))
        if numOfPineapples < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfPineapples < 100 and numOfPineapples > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfPineapples < 1000 and numOfPineapples > 99:
            currentfruitlabel.place(x="155", y="290")
    
def switchright():
    global currentfruit
    global clickerbutton
    if fruitupgradelevel == 0:
        rightfruitbutton.config(state=DISABLED)
        return
    if currentfruit == "Apple":
        currentfruit = "Banana"
        leftfruitbutton.config(state=NORMAL)
        if fruitupgradelevel == 1:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 2:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 3:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 4:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 5:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 6:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 7:
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
    if currentfruit == "Blackberry":
        currentfruit = "Raspberry"
        if fruitupgradelevel == 8:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 9:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 10:
            rightfruitbutton.config(state=DISABLED)
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
        if fruitupgradelevel == 11:
            rightfruitbutton.config(state=DISABLED)
        clickerbutton.config(image=clickerphoto12)
        currentfruitstringvar.set("Pineapple x" + str(numOfPineapples))
        if numOfPineapples < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfPineapples < 100 and numOfPineapples > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfPineapples < 1000 and numOfPineapples > 99:
            currentfruitlabel.place(x="155", y="290")
        return
    if currentfruit == "Pineapple":
        currentfruit = "Coconut"
        if fruitupgradelevel == 12:
            rightfruitbutton.config(state=DISABLED)
        rightfruitbutton.config(state=DISABLED)
        clickerbutton.config(image=clickerphoto13)
        currentfruitstringvar.set("Coconuts x" + str(numOfCoconuts))
        if numOfCoconuts < 10:
            currentfruitlabel.place(x="165", y="290")
        if numOfCoconuts < 100 and numOfCoconuts > 9:
            currentfruitlabel.place(x="160", y="290")
        if numOfCoconuts < 1000 and numOfCoconuts > 99:
            currentfruitlabel.place(x="155", y="290")
    
def musicselect():
    musicfilename = filedialog.askopenfilename(initialdir = "/",title = "Select MP3 File", filetypes=(("MP3 Files","*.mp3"),("WAV Files","*.wav")))
    pygame.mixer.music.load(musicfilename)
    pygame.mixer.music.play(-1)

def buyapple():
    global appleprice
    global applesboughttoday
    global money
    global rawmoney
    global numOfApples
    global currentfruitstringvar
    if rawmoney < appleprice:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - appleprice
        applesboughttoday = applesboughttoday + 1
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
    global appleprice
    global applesboughttoday
    global money
    global rawmoney
    global numOfApples
    global currentfruitstringvar
    if rawmoney < appleprice * 6:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 6
        applesboughttoday = applesboughttoday + 6
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
    global appleprice
    global applesboughttoday
    global money
    global rawmoney
    global numOfApples
    if rawmoney < appleprice * 36:
        messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - appleprice * 36
        applesboughttoday = applesboughttoday + 36
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
    global currentfruitstringvar
    if rawmoney < 5:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 5
        numOfBananas = numOfBananas + 1
        marketbananacount.set("Current:\n" + str(numOfBananas))
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
    global currentfruitstringvar
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfBananas = numOfBananas + 5
        marketbananacount.set("Current:\n" + str(numOfBananas))
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
    global currentfruitstringvar
    if rawmoney < 150:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 150
        numOfBananas = numOfBananas + 30
        marketbananacount.set("Current:\n" + str(numOfBananas))
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
    global currentfruitstringvar
    if rawmoney < 10:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 10
        numOfPears = numOfPears + 1
        marketpearcount.set("Current:\n" + str(numOfPears))
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
    global currentfruitstringvar
    if rawmoney < 30:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 30
        numOfPears = numOfPears + 3
        marketpearcount.set("Current:\n" + str(numOfPears))
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
    global currentfruitstringvar
    if rawmoney < 250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 250
        numOfPears = numOfPears + 25
        marketpearcount.set("Current:\n" + str(numOfPears))
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
    global currentfruitstringvar
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfOranges = numOfOranges + 1
        marketorangecount.set("Current:\n" + str(numOfOranges))
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
    global currentfruitstringvar
    if rawmoney < 80:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 80
        numOfOranges = numOfOranges + 4
        marketorangecount.set("Current:\n" + str(numOfOranges))
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
    global currentfruitstringvar
    if rawmoney < 400:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 400
        numOfOranges = numOfOranges + 20
        marketorangecount.set("Current:\n" + str(numOfOranges))
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
    global currentfruitstringvar
    if rawmoney < 50:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 50
        numOfMangos = numOfMangos + 1
        marketmangocount.set("Current:\n" + str(numOfMangos))
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
    global currentfruitstringvar
    if rawmoney < 100:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 100
        numOfMangos = numOfMangos + 2
        marketmangocount.set("Current:\n" + str(numOfMangos))
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
    global currentfruitstringvar
    if rawmoney < 750:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 750
        numOfMangos = numOfMangos + 25
        marketmangocount.set("Current:\n" + str(numOfMangos))
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
    global currentfruitstringvar
    if rawmoney < 10:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 10
        numOfStrawberries = numOfStrawberries + 1
        marketstrawberrycount.set("Current:\n" + str(numOfStrawberries))
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
    global currentfruitstringvar
    if rawmoney < 250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 250
        numOfStrawberries = numOfStrawberries + 25
        marketstrawberrycount.set("Current:\n" + str(numOfStrawberries))
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
    global currentfruitstringvar
    if rawmoney < 7500:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 7500
        numOfStrawberries = numOfStrawberries + 750
        marketstrawberrycount.set("Current:\n" + str(numOfStrawberries))
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
    global currentfruitstringvar
    if rawmoney < 15:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 15
        numOfBlueberries = numOfBlueberries + 1
        marketblueberrycount.set("Current:\n" + str(numOfBlueberries))
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
    global currentfruitstringvar
    if rawmoney < 375:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 375
        numOfBlueberries = numOfBlueberries + 25
        marketblueberrycount.set("Current:\n" + str(numOfBlueberries))
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
    global currentfruitstringvar
    if rawmoney < 11250:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 11250
        numOfBlueberries = numOfBlueberries + 750
        marketblueberrycount.set("Current:\n" + str(numOfBlueberries))
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
    global currentfruitstringvar
    if rawmoney < 20:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 20
        numOfBlackberries = numOfBlackberries + 1
        marketblackberrycount.set("Current:\n" + str(numOfBlackberries))
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
    global currentfruitstringvar
    if rawmoney < 300:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 300
        numOfBlackberries = numOfBlackberries + 15
        marketblackberrycount.set("Current:\n" + str(numOfBlackberries))
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
    global currentfruitstringvar
    if rawmoney < 9000:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 9000
        numOfBlackberries = numOfBlackberries + 450
        marketblackberrycount.set("Current:\n" + str(numOfBlackberries))
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
    global currentfruitstringvar
    if rawmoney < 35:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 35
        numOfRaspberries = numOfRaspberries + 1
        marketraspberrycount.set("Current:\n" + str(numOfRaspberries))
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

def buyraspberrybox():
    global money
    global rawmoney
    global numOfRaspberries
    global currentfruitstringvar
    if rawmoney < 300:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 300
        numOfRaspberries = numOfRaspberries + 10
        marketraspberrycount.set("Current:\n" + str(numOfRaspberries))
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

def buyraspberrycrate():
    global money
    global rawmoney
    global numOfRaspberries
    global currentfruitstringvar
    if rawmoney < 4500:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 4500
        numOfRaspberries = numOfRaspberries + 150
        marketraspberrycount.set("Current:\n" + str(numOfRaspberries))
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

def buygrape():
    global money
    global rawmoney
    global numOfGrapes
    global currentfruitstringvar
    if rawmoney < 100:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 100
        numOfGrapes = numOfGrapes + 1
        marketgrapescount.set("Current:\n" + str(numOfGrapes))
        if currentfruit == "Grapes":
            currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
            if numOfGrapes < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfGrapes < 100 and numOfGrapes > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfGrapes < 1000 and numOfGrapes > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buygrapebag():
    global money
    global rawmoney
    global numOfGrapes
    global currentfruitstringvar
    if rawmoney < 300:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 300
        numOfGrapes = numOfGrapes + 3
        marketgrapescount.set("Current:\n" + str(numOfGrapes))
        if currentfruit == "Grapes":
            currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
            if numOfGrapes < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfGrapes < 100 and numOfGrapes > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfGrapes < 1000 and numOfGrapes > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buygrapecrate():
    global money
    global rawmoney
    global numOfGrapes
    global currentfruitstringvar
    if rawmoney < 1800:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 1800
        numOfGrapes = numOfGrapes + 18
        marketgrapescount.set("Current:\n" + str(numOfGrapes))
        if currentfruit == "Grapes":
            currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
            if numOfGrapes < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfGrapes < 100 and numOfGrapes > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfGrapes < 1000 and numOfGrapes > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buymelon():
    global money
    global rawmoney
    global numOfWatermelons
    global currentfruitstringvar
    if rawmoney < 1000:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 1000
        numOfWatermelons = numOfWatermelons + 1
        marketmeloncount.set("Current:\n" + str(numOfWatermelons))
        if currentfruit == "Watermelon":
            currentfruitstringvar.set("Watermelon x" + str(numOfWatermelon))
            if numOfWatermelons < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfWatermelons < 100 and numOfWatermelons > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfWatermelons < 1000 and numOfWatermelons > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buymelonbox():
    global money
    global rawmoney
    global numOfWatermelons
    global currentfruitstringvar
    if rawmoney < 4000:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 4000
        numOfWatermelons = numOfWatermelons + 4
        marketmeloncount.set("Current:\n" + str(numOfWatermelons))
        if currentfruit == "Watermelon":
            currentfruitstringvar.set("Watermelon x" + str(numOfWatermelon))
            if numOfWatermelons < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfWatermelons < 100 and numOfWatermelons > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfWatermelons < 1000 and numOfWatermelons > 99:
                currentfruitlabel.place(x="155", y="290")
        moneyplace()
        marketmoneylabelstringvar.set("$" + str(money))
        moneystringvar.set("You have $" + str(money))

def buymeloncrate():
    global money
    global rawmoney
    global numOfWatermelons
    global currentfruitstringvar
    if rawmoney < 7000:
       messagebox.showerror("Error", "You do not have enough money!")
    else:
        rawmoney = rawmoney - 7000
        numOfWatermelons = numOfWatermelons + 7
        marketmeloncount.set("Current:\n" + str(numOfWatermelons))
        if currentfruit == "Watermelon":
            currentfruitstringvar.set("Watermelon x" + str(numOfWatermelon))
            if numOfWatermelons < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfWatermelons < 100 and numOfWatermelons > 9:
              currentfruitlabel.place(x="160", y="290")
            if numOfWatermelons < 1000 and numOfWatermelons > 99:
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
    global numOfGrapes
    global numOfWatermelons
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
    if currentfruit == "Grapes":
        if numOfGrapes == 0:
            messagebox.showerror("Error", "You do not have any Grapes!")
        else:
            numOfGrapes = numOfGrapes - 1
            currentfruitstringvar.set("Grapes x" + str(numOfGrapes))
            if numOfGrapes < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfGrapes < 100 and numOfGrapes > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfGrapes < 1000 and numOfGrapes > 99:
                currentfruitlabel.place(x="155", y="290")
            rawmunch = rawmunch + random.randint(495, 520)
            munchplace()
            munchstringvar.set("Munch: " + str(munch))
    if currentfruit == "Watermelon":
        if numOfWatermelons == 0:
            messagebox.showerror("Error", "You do not have any Watermelons!")
        else:
            numOfWatermelons = numOfWatermelons - 1
            currentfruitstringvar.set("Watermelon x" + str(numOfWatermelons))
            if numOfWatermelons < 10:
                currentfruitlabel.place(x="165", y="290")
            if numOfWatermelons < 100 and numOfWatermelons > 9:
                currentfruitlabel.place(x="160", y="290")
            if numOfWatermelons < 1000 and numOfWatermelons > 99:
                currentfruitlabel.place(x="155", y="290")
            rawmunch = rawmunch + random.randint(4900, 5100)
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
    upgradeswindow.destroy()

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
        fruitupgradetextvar.set("Summertime Shop (Lv. " + str(fruitupgradelevel + 1) + ") $1K")
    if fruitupgradelevel == 4:
        fruitupgradetextvar.set("Berry Investment (Lv. " + str(fruitupgradelevel + 1) + ") $5K")
    if fruitupgradelevel == 5:
        fruitupgradetextvar.set("Berry Investment II (Lv. " + str(fruitupgradelevel + 1) + ") $10K")
    if fruitupgradelevel == 6:
        fruitupgradetextvar.set("Berry Investment III (Lv. " + str(fruitupgradelevel + 1) + ") $50K")
    if fruitupgradelevel == 7:
        fruitupgradetextvar.set("Berry Investment IV (Lv. " + str(fruitupgradelevel + 1) + ") $100K")
    if fruitupgradelevel == 8:
        fruitupgradetextvar.set("Berry Investment V (Lv. " + str(fruitupgradelevel + 1) + ") $350K")
    if fruitupgradelevel == 9:
        fruitupgradetextvar.set("Melon Fever (Lv. " + str(fruitupgradelevel + 1) + ") $1M")
    if fruitupgradelevel == 10:
        fruitupgradetextvar.set("Upgrade Lv. MAX")
    autoeattextvar = StringVar()
    autoeattextvar.set("Auto Eat (Lv. " + str(autoclicklevel) + " -> " + str(autoclicklevel + 1) + ") $" + str(autoeatcost))
    autoeatupgradebutton = Button(upgradeswindow, textvariable=autoeattextvar, width="56", command=autoeatbuy).grid(row="2", column="0")
    upgradeswindow.mainloop()

def achievementsmenu():
    return

def rootopen():
    global root
    global moneylabel
    global munchlabel
    global date
    global month
    global year
    global currentfruitstringvar
    global currentfruitlabel
    global moneystringvar
    global leftfruitbutton
    global rightfruitbutton
    global munchstringvar
    global clickerbutton
    global clickerphoto
    global clickerphoto2
    global clickerphoto3
    global clickerphoto4
    global clickerphoto5
    global clickerphoto6
    global clickerphoto7
    global clickerphoto8
    global clickerphoto9
    global clickerphoto10
    global clickerphoto11
    global clickerphoto12
    global clickerphoto13
    global clickerphoto14
    root = Toplevel()
    main.withdraw()
    root.title("Fruit Clicker")
    root.geometry("400x350+300+100")
    marketbutton = Button(root, text="Market", fg="White", bg="Black", width="11", command=market)
    marketbutton.grid(column="0", row="0")
    upgradesbutton = Button(root, text="Upgrades", fg="White", bg="Black", width="11", command=upgrades)
    upgradesbutton.grid(column="0", row="1")
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
    rightfruitbutton = Button(root, text=">", command=switchright, state=DISABLED)
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
    musicselectbutton.grid(row="2", column="0")
    savebutton = Button(root, text="Save", fg="White", bg="Black", width="11", command=save)
    savebutton.grid(row="3", column="0")
    munchconvertbutton = Button(root, text="Convert Munch", fg="White", bg="Black", width="11", command=convertmunch)
    munchconvertbutton.grid(row="4", column="0")
    calendarbutton = Button(root, text="Calendar", fg="White", bg="Black", width="11", command=calendar)
    calendarbutton.grid(row="5", column="0")
    menubutton = Button(root, text="Main Menu", fg="White", bg="Black", width="11", command=mainmenu)
    menubutton.grid(row="6", column="0")
    achievementsbutton = Button(root, text="Achievements", fg="White", bg="Black", width="11", command=achievementsmenu)
    achievementsbutton.grid(row="7", column="0")
    pygame.mixer.music.load("audio/theme.wav")
    pygame.mixer.music.play(-1)
    calendar()
    date = int(date) - 1
    fixdate()
    calendarwindow.destroy()
    root.deiconify()
    advancetime()
    root.iconbitmap("images/apple.ico")
    root.protocol("WM_DELETE_WINDOW", rootOnClose)

def loadsave1():
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
    global numOfRaspberries
    global numOfGrapes
    global numOfWatermelons
    global multiconvertlevel
    global fruitupgradelevel
    global autoclicklevel
    global autoeatcost
    global multiconvertcost
    global wholedate
    global saveopen
    saveopen = 1
    startscreenback()
    rootopen()
    if os.path.exists("saves/save1.fcsave") == True:
        print("Save 1 Load")
        loadedfile = open("saves/save1.fcsave")
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
        numOfRaspberries = int(loadedfilelines[10])
        numOfGrapes = int(loadedfilelines[11])
        numOfWatermelons = int(loadedfilelines[12])
        multiconvertlevel = int(loadedfilelines[13])
        multiconvertcost = int(loadedfilelines[14])
        autoclicklevel = int(loadedfilelines[15])
        autoeatcost = int(loadedfilelines[16])
        fruitupgradelevel = int(loadedfilelines[17])
        print("Loaded")
    else:
        print("Save 1 Create")
        messagebox.showinfo("Info", "Save data not found.\nStarting new save!")
        savedoc = open("saves/save1.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        startscreenback()
        rootopen()

def loadsave2():
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
    global numOfRaspberries
    global numOfGrapes
    global numOfWatermelons
    global multiconvertlevel
    global fruitupgradelevel
    global autoclicklevel
    global autoeatcost
    global multiconvertcost
    global wholedate
    global saveopen
    saveopen = 2
    if os.path.exists("saves/save2.fcsave") == True:
        print("Save 2 Load")
        startscreenback()
        rootopen()
        loadedfile = open("saves/save2.fcsave")
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
        numOfRaspberries = int(loadedfilelines[10])
        numOfGrapes = int(loadedfilelines[11])
        numOfWatermelons = int(loadedfilelines[12])
        multiconvertlevel = int(loadedfilelines[13])
        multiconvertcost = int(loadedfilelines[14])
        autoclicklevel = int(loadedfilelines[15])
        autoeatcost = int(loadedfilelines[16])
        fruitupgradelevel = int(loadedfilelines[17])
    else:
        print("Save 2 Create")
        messagebox.showinfo("Info", "Save data not found.\nStarting new save!")
        savedoc = open("saves/save2.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        startscreenback()
        rootopen()

def loadsave3():
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
    global numOfRaspberries
    global numOfGrapes
    global numOfWatermelons
    global multiconvertlevel
    global fruitupgradelevel
    global autoclicklevel
    global autoeatcost
    global multiconvertcost
    global wholedate
    global saveopen
    saveopen = 3
    if os.path.exists("saves/save3.fcsave") == True:
        print("Save 3 Load")
        startscreenback()
        rootopen()
        loadedfile = open("saves/save3.fcsave")
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
        numOfRaspberries = int(loadedfilelines[10])
        numOfGrapes = int(loadedfilelines[11])
        numOfWatermelons = int(loadedfilelines[12])
        multiconvertlevel = int(loadedfilelines[13])
        multiconvertcost = int(loadedfilelines[14])
        autoclicklevel = int(loadedfilelines[15])
        autoeatcost = int(loadedfilelines[16])
        fruitupgradelevel = int(loadedfilelines[17])
    else:
        print("Save 3 Create")
        messagebox.showinfo("Info", "Save data not found.\nStarting new save!")
        savedoc = open("saves/save3.fcsave", "w+")
        savedoc.write(str(rawmoney) + "\n" + str(rawmunch) + "\n" + str(numOfApples) + "\n" + str(numOfBananas) + "\n" + str(numOfPears) + "\n" + str(numOfOranges) + "\n" + str(numOfMangos) + "\n" + str(numOfStrawberries) + "\n" + str(numOfBlueberries) + "\n" + str(numOfBlackberries) + "\n" + str(numOfRaspberries) + "\n" + str(numOfGrapes) + "\n" + str(numOfWatermelons) + "\n" + str(multiconvertlevel) + "\n" + str(multiconvertcost) + "\n" + str(autoclicklevel) + "\n" + str(autoeatcost) + "\n" + str(fruitupgradelevel))
        savedoc.flush()
        savedoc.close()
        startscreenback()
        rootopen() 

def savefiles():
    global backbutton
    global save1button
    global save2button
    global save3button
    global creditslabel
    global creditslabel1
    global creditslabel2
    global creditslabel3
    global creditslabel4
    global creditslabel5
    global creditslabel6
    global creditslabel7
    global companylogolabel
    global copyrightlabel
    playbutton.pack_forget()
    quitbutton.pack_forget()
    backbutton = Button(main, text="Back", width ="56", command=startscreenback)
    backbutton.grid(row="0", column="0")
    save1button = Button(main, text="Save 1", width ="56", command=loadsave1)
    save1button.grid(row="1", column="0")
    save2button = Button(main, text="Save 2", width ="56", command=loadsave2)
    save2button.grid(row="2", column="0")
    save3button = Button(main, text="Save 3", width ="56", command=loadsave3)
    save3button.grid(row="3", column="0")
    creditslabel = Label(main, text="Credits")
    creditslabel.place(x="175", y="110")
    creditslabel1 = Label(main, text="Lead Programmer:\nJayden Collis")
    creditslabel1.place(x="10", y="130")
    creditslabel2 = Label(main, text="Lead Artist:\nEmily Tatlock")
    creditslabel2.place(x="25", y="170")
    creditslabel3 = Label(main, text="Lead Composer:\nWilliam Burgess")
    creditslabel3.place(x="20", y="210")
    creditslabel4 = Label(main, text="Kickstarters:\nAlison Collis\nJordan Silva\nSarah Kim\nMadison Golik\nJayden Golik")
    creditslabel4.place(x="20", y="250")
    creditslabel5 = Label(main, text="Glen Kerr\nRudra Labh\nAurora D'Rozario\nJasmine Walmsley\nMarc Cowan\nJoey Chen")
    creditslabel5.place(x="135", y="130")
    creditslabel6 = Label(main, text="Special Thanks:\nLisa Rodgers\nLeanne Hall\nStacey Collis\nAshton Grant\nStephanie Stellas\nStephen Collis")
    creditslabel6.place(x="140", y="230")
    creditslabel7 = Label(main, text="Jaide Knaus-Petrie\nScott Hackett\nKaylee Hatcher\nKoby Marshall\nEzekiel Swinn\nGeorge *****\nMason Colbran\nNadia *****")
    creditslabel7.place(x="260", y="130")
    companylogo = PhotoImage(file="images/company-logo.png")
    companylogolabel = Label(main, image=companylogo)
    companylogolabel.img = companylogo
    companylogolabel.place(x="280", y="260")
    copyrightlabel = Label(main, text="(c) SeaPuppy Studios 2020")
    copyrightlabel.place(x="240", y="320")

def mainmenu():
    save()
    root.destroy()
    calendarthread.join()
    main.deiconify()

def startscreenback():
    backbutton.grid_forget()
    save1button.grid_forget()
    save2button.grid_forget()
    save3button.grid_forget()
    playbutton.grid(row="0", column="0")
    quitbutton.grid(row="1", column="0")
    creditslabel.place_forget()
    creditslabel1.place_forget()
    creditslabel2.place_forget()
    creditslabel3.place_forget()
    creditslabel4.place_forget()
    creditslabel5.place_forget()
    creditslabel6.place_forget()
    creditslabel7.place_forget()
    companylogolabel.place_forget()
    copyrightlabel.place_forget()
    
main = Tk()
main.title("Fruit Clicker")
main.geometry("400x350+300+100")
playbutton = Button(main, text="Play", width="56", command=savefiles)
playbutton.grid(row="0", column="0")
quitbutton = Button(main, text="Quit Game", width="56", command=main.destroy)
quitbutton.grid(row="1", column="0")
main.iconbitmap("images/apple.ico")
main.mainloop()
