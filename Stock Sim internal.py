import datetime
import random
import time
import json

SL =   {
    'SKB': 100,
    'FRT': 100,
    'AMG': 100,
    'DFT': 100,
    'MOG': 250,
    'MEW': 250,
    'LMX': 250,
    'OHO': 250,
    'EDG': 500,
    'GNG': 500,
    'GYT': 500,
    'SGA': 500,
    'CNT': 1000,
    'LGR': 1000,
    'FNM': 1000,
    'RIZ': 1000,
    'DDN': 1000
}


    
def purchase():
    setprice = 0
    marketmult = 0
    finalprice = 0
    purchaseUI = 1

    while purchaseUI == 1:
        a = input("""Please enter desired stocks and amount to purchase (example: ABC 123)\n
Type 'x' to return to menu: """)
        if a in ['x']:
            #replace with list of stocks and buttons to choose each share option
            words = a.split()
            #Check if input from player is valid and correct syntax
            if len(words) == 2:
                requestint = (words[1])
                requeststr = (words[0])

                if requestint.isdigit():
                    requestint = int(words[1])
                    requeststr = str(words[0])
                        
                    if requeststr in SL:
                        setprice = (list(SL.keys())[list(SL.values()).index(requeststr)])
                        marketmult = marketsim()
                            
                        if setprice >= requestint:
                            confirm = input("Confirm purchase of "+ str(a))
                            #confirm purchase

                            if confirm in ['y','Y','Yes','yes','Confirm','confirm','c','C']:
                               
                               time.sleep(1)
                               print('Purchase Successful')
                               time.sleep(1)
                               purchaseUI = purchaseUI - 1
                               
                            else:
                               print('Transaction Cancelled')
                               time.sleep(1)
                                    
                        else:
                            print("Request Invalid")

                    else:
                        print("Request Invalid")

                else:
                    print("Request Invalid")

            else:
                print("Request Invalid")
##########################################################################
                
def savegame(playerdict):
    outfile = open('playersave', 'w')
    json.dump(playerdict, outfile)
    outfile.close()

def loadgame():
    global playerdict
    infile = open('playersave', 'r')
    result = json.load(infile)
    infile.close()
    playerdict = result
    gameloop()

def newgame():
    global playerdict

    playerdict= {
        "Name": 'playername',
        "wallet": 200,
        "Lasttimesaved": str(datetime.datetime.now()),
        "ownedshares":[]
}
    ngroot = tkinter.Tk()
    ngroot.geometry("1000x800")
    label = tkinter.Label(ngroot, text='Name: ')
    label.pack()
    txtbox = tkinter.Text(ngroot)
    txtbox.pack()

    def getuser(event = None):
        global playerdict
        playerdict["Name"] = txtbox.get("1.0", "end").strip()
        savegame(playerdict)
        ngroot.destroy()
        gameloop()
        
    ngroot.bind('<Return>', getuser)

    btn = ttk.Button(ngroot, text="Save", command=getuser)
    btn.pack()

    ngroot.mainloop()


def buyscreen():
    global playerdict
    buyroot = tkinter.Tk()
    buyroot.geometry("1000x800")
    buyroot.title("Stocksim")
    Label(buyroot, text="Purchase stuff", font=('Helvetica 17 bold')).pack(pady=20)

    def buy():# <---purchase function
        global playerdict
        stockcode = clicked.get()
        price = SL.get(stockcode, 0)
        if playerdict["wallet"] >= price:
            playerdict["wallet"] = playerdict["wallet"] - price
            playerdict["ownedshares"].append(stockcode)
            savegame(playerdict)
        
        L.config(text = str(playerdict["wallet"]))
        label.config(text = clicked.get())
        
    options = list(SL) 
    clicked = StringVar() 
    clicked.set( "Select here" )

    drop = OptionMenu( buyroot , clicked , *options )
    drop.place(x=50, y=100)

    button = Button(buyroot ,text = "PURCHASE" , command = buy).pack() 

    label = Label( buyroot ,text = " ", font=('Helvetica 17 bold')) 
    label.pack()

    L = Label(buyroot, text=str(playerdict["wallet"]), font=('Helvetica 17 bold'))
    L.pack()

    buyroot.mainloop() 

    
###############################################################################

def startup():
    startroot = tkinter.Tk()
    startroot.geometry("1000x800")
    startroot.resizable(False, False)

    def loadclose():
        startroot.destroy()
        loadgame()

    def newclose():
        startroot.destroy()
        newgame()
        
    btn = Button(startroot, text = 'Load', height= 5, width=25, command = loadclose)
    btn.place(x=360, y=250)

    btn = Button(startroot, text = 'New', height= 5, width=25, command = newclose)
    btn.place(x=360, y=370)

    startroot.mainloop()
    
def gameloop():
    mainroot = Tk()
    mainroot.geometry("1000x800")
    mainroot.title("Stocksim")
    
    buybtn = Button(mainroot, text  = 'Purchase Stocks', height=5, width=25, command = buyscreen)
    buybtn.place(x=360, y=250)

    mainroot.mainloop()
    
    
    

#code start
import tkinter
from tkinter import ttk
from tkinter import *


startup()







