from tkinter import *

money = 0
currentfruit = "Apple"
numOfApples = 654

def clicked():
    global money
    global currentfruit
    if currentfruit == "Apple":
        money = money + 1
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
    root.withdraw()
    inventorywindow = Tk()
    inventorywindow.title("Fruit Clicker - Inventory")
    inventorywindow.geometry("400x350+300+100")
    inventorywindow.protocol("WM_DELETE_WINDOW", inventoryOnClose)
    inventorywindow.mainloop()

def market():
    global marketwindow
    root.withdraw()
    marketwindow = Tk()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)
    marketwindow.mainloop()

def upgrades():
    global upgradeswindow
    root.withdraw()
    upgradeswindow = Tk()
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
    currentfruitlabel = Label(root, textvariable=currentfruitstringvar, fg="Black")
    if numOfApples < 10:
        currentfruitlabel.place(x="180", y="290")
    if numOfApples < 100 and numOfApples > 9:
        currentfruitlabel.place(x="175", y="290")
    if numOfApples < 1000 and numOfApples > 99:
        currentfruitlabel.place(x="170", y="290")

rightfruitbutton = Button(root, text=">")
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

clickerphoto = PhotoImage(file = "apple.png")
clickerbutton = Button(root, text="Clicker Button", image=clickerphoto, fg="Black", command=clicked)
clickerbutton.place(x="100", y="75")

root.mainloop()
