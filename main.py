from tkinter import *

money = 0
currentfruit = "apple"

def clicked():
    global money
    global currentfruit
    if currentfruit == "apple":
        money = money + 1
    moneystringvar.set("You have $" + str(money))
    if money < 10:
        moneylabel.place(x="315", y="0")
    if money < 100 and money > 9:
        moneylabel.place(x="307", y="0")
    if money < 1000 and money > 99:
        moneylabel.place(x="300", y="0")
    
def marketOnClose():
    root.deiconify()
    marketwindow.destroy()
    
def upgradesOnClose():
    root.deiconify()
    upgradeswindow.destroy()
    
def market():
    global marketwindow
    root.withdraw()
    marketwindow = Tk()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)

def upgrades():
    global upgradeswindow
    root.withdraw()
    upgradeswindow = Tk()
    upgradeswindow.title("Fruit Clicker - Upgrades")
    upgradeswindow.geometry("400x350+300+100")
    upgradeswindow.protocol("WM_DELETE_WINDOW", upgradesOnClose)

root = Tk()
root.title("Fruit Clicker")
root.geometry("400x350+300+100")

marketbutton = Button(root, text="Market", fg="White", bg="Black", width="6", command=market)
marketbutton.grid(column="0", row="0")
upgradesbutton = Button(root, text="Upgrades", fg="White", bg="Black", width="6", command=upgrades)
upgradesbutton.grid(column="0", row="1")

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

upgradeswindow.mainloop()
marketwindow.mainloop()
root.mainloop()