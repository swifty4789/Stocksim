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


def buy():
   buyroot = tkinter.Tk()
   buyroot.geometry("1000x800")
   buyroot.title("Stocksim")
   Label(buyroot, text="Purchase stuff", font=('Helvetica 17 bold')).pack(pady=20)
   Label(buyroot, text=pformat(SL), font=('Helvetica 17 bold')).pack(pady=50)

inventory()
buy()
