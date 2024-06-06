from pprint import pformat
import tkinter
from tkinter import *
from tkinter import ttk

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

def inventory():
   invroot = tkinter.Tk()
   invroot.geometry("1000x800")
   invroot.title("Stocksim")
   Label(invroot, text="Inventory", font=('Helvetica 17 bold')).pack(pady=20)
   invroot.mainloop()


def buyscreen():
   buyroot = tkinter.Tk()
   buyroot.geometry("1000x800")
   buyroot.title("Stocksim")
   Label(buyroot, text="Purchase stuff", font=('Helvetica 17 bold')).pack(pady=20)

   def buy():# <---purchase function
       global balance
       stockcode = clicked.get()
       price = SL.get(stockcode, 0)
       balance = balance - price
       
       L.config(text = balance)
       label.config(text = clicked.get())
       
   options = list(SL) 
   clicked = StringVar() 
   clicked.set( "Select here" )

   drop = OptionMenu( buyroot , clicked , *options )
   drop.place(x=50, y=100)

   button = Button(buyroot ,text = "PURCHASE" , command = buy).pack() 

   label = Label( buyroot ,text = " ", font=('Helvetica 17 bold')) 
   label.pack()

   L = Label(buyroot, text=balance, font=('Helvetica 17 bold'))
   L.pack()

   buyroot.mainloop() 

inventory()
buy()
