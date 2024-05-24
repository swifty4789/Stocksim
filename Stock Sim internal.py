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

def newgame():
    global playerdict
    
    playerdict= {
        "Name": 'playername',
        "Wallet": 200,
        "Lasttimesaved": datetime.datetime.now(),
        "ownedshares":[]
}
    ngroot = tkinter.Tk()

    label = tkinter.Label(ngroot, text='Name: ')
    label.pack()
    txtbox = tkinter.Text(ngroot)
    txtbox.pack()

    ngroot.bind('<Return>', (lambda event: ngroot.destroy()))
    
    ngroot.mainloop()


    
    

#code start
import tkinter
from tkinter import ttk

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief='flat',
                      background="#000")

btn = ttk.Button(root, text="New", command=newgame)
btn.pack()
btn = ttk.Button(root, text="Load", command=loadgame)
btn.pack()

root.mainloop()







    








