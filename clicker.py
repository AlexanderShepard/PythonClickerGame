import tkinter as tk

root = tk.Tk()
root.geometry("700x700")
root.title("Juice Adventure")

# GAME VARIABLES -----------------------------------------
score = 0
clickPower = 1
autoClicker = 0
autoClickerPower = 1
# GAME VARIABLES -----------------------------------------

# GAME LOOP -----------------------------------------------
def gameLoop():
    global score
    score = score + (autoClicker * autoClickerPower) # score updater
    var.set(var.get() + (autoClicker * autoClickerPower)) # auto clicker updater
    upgradeClickText.set("Upgrade Click Cost: {}".format(20 * clickPower)) # keep upgrade text up to date
    upgradeClickTenText.set("Upgrade x10 Cost: {}".format(200 * clickPower)) # keep upgrade text up to date
    root.after(1000, gameLoop)
root.after(1000, gameLoop)
# GAME LOOP -----------------------------------------------
def click(): # click to increase score by 1
    var.set(var.get() + (clickPower * 1))
    global score
    score = score + (clickPower * 1)
    print(score)

def clickUpgrade1(): # Upgrade manual clicks
    global score
    global clickPower
    global clickUpgradeCost
    clickUpgradeCost = 20 * clickPower
    if score >= clickUpgradeCost:
        score = score - (20 * clickPower)
        var.set(var.get() - (20 * clickPower))
        clickPower = clickPower + 1
        upgradeClickText.set("Upgrade Click Cost: {}".format(20 * clickPower))
        upgradeClickTenText.set("Upgrade x10 Cost: {}".format(200 * clickPower))
        clickPowerNum.set("Your click power is {}".format(clickPower))
    else:
        print("Insufficient Funds")

def clickUpgrade10(): # Upgrade manual clicks x10
    global score
    global clickPower
    global clickUpgradeCost
    clickUpgradeCost = (200 * clickPower)
    if score >= clickUpgradeCost:
        score = score - (200 * clickPower)
        var.set(var.get() - (200 * clickPower))
        clickPower = clickPower + 10
        clickPowerNum.set("Your click power is {}".format(clickPower))
        upgradeClickText.set("Upgrade Click Cost: {}".format(20 * clickPower))
        upgradeClickTenText.set("Upgrade x10 Cost: {}".format(200 * clickPower))
    else:
        print("Insufficient Funds")
def autoClick(): # Purchase an AutoClicker
    global score
    global autoClicker
    if score >= 10 * (autoClicker + 1):
        score = score - 10 * (autoClicker + 1)
        var.set(var.get() - 10 * (autoClicker + 1))
        autoClicker = autoClicker + 1
        autoClickerNum.set("You have {} Auto Clickers".format(autoClicker))
        autoClickText.set("Purchase Auto Clicker Cost: {}".format(10 * (autoClicker + 1)))
    else:
        print("Insufficient Funds")

def autoClickTen(): # Purchase 10x AutoClickers
    global score
    global autoClicker
    if score >= 100 * (autoClicker + 1):
        score = score - 100 * (autoClicker + 1)
        var.set(var.get() - 100 * (autoClicker + 1))
        autoClicker = autoClicker + 10
        autoClickerNum.set("You have {} Auto Clickers".format(autoClicker))
        autoClickTenText.set("Purchase Auto Clicker Cost: {}".format(100 * (autoClicker + 1)))
    else:
        print("Insufficient Funds")

def autoClickUpgrade(): # Purchase an AutoClicker Upgrade
    global score
    global autoClicker
    if score >= (50* autoClickerPower):
        score = score - (50 * autoClickerPower)
        var.set(var.get() - 50 * autoClickerPower)

var = tk.IntVar()
var.set(0)

# Score Counter
mylabel = tk.Label(root, textvariable=var)
mylabel.pack()

# Purchase Display
autoClickerNum = tk.StringVar()
autoClickerNumLabel = tk.Label(root, textvariable=autoClickerNum)
autoClickerNum.set("You have {} Auto Clickers".format(autoClicker))
autoClickerNumLabel.pack()
autoClickerNumLabel.place(relx = 1.0, rely = 0.0, anchor = 'ne')

clickPowerNum = tk.StringVar()
clickPowerNumLabel = tk.Label(root, textvariable=clickPowerNum)
clickPowerNum.set("Your click power is {}".format(clickPower))
clickPowerNumLabel.pack()
clickPowerNumLabel.place(relx = 0.0, rely = 0.0, anchor = 'nw')

# Click to gain score button
photo = tk.PhotoImage(file = r'C:\Users\Alex\Desktop\images\lemon.gif')
button = tk.Button(root, text = "click here",image = photo, command=click)
button.place(x=320,y=250)

# Upgrade manual click button
upgradeClickText = tk.StringVar()
upgradeClickText.set("Upgrade Click Cost: 20")
upgradeClickTenText = tk.StringVar()
upgradeClickTenText.set("Upgrade x10 Cost: 200")
upgradeClick = tk.Button(root, textvariable=upgradeClickText, command=clickUpgrade1)
upgradeClick.place(x=10,y=100)
upgradeClickTen = tk.Button(root, textvariable=upgradeClickTenText, command=clickUpgrade10)
upgradeClickTen.place(x=10,y=135)

# Purchase auto clicker button
autoClickText = tk.StringVar()
autoClickText.set("Purchase Auto Clicker Cost: 10")
autoClick = tk.Button(root, textvariable=autoClickText, command=autoClick)
autoClick.place(x=520, y=100)

# Purchase 10x auto clicker button
autoClickTenText = tk.StringVar()
autoClickTenText.set("Purchase 10x Auto Clickers Cost: 100")
autoClickTen = tk.Button(root, textvariable=autoClickTenText, command=autoClickTen)
autoClickTen.place(x=490, y=135)

root.mainloop()