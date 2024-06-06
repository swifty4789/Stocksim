import datetime
import random
import time
import json
import tkinter
from tkinter import ttk
from tkinter import *
from pprint import pformat



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

    buyroot = tkinter.Tk()
    buyroot.geometry("1000x800")
    buyroot.title("Stocksim")
    Label(buyroot, text="Purchase stuff", font=('Helvetica 17 bold')).pack(pady=20)

    Label.config( text = clicked.get() ) 
  
    # Dropdown menu options 
    options = [ 
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
    ] 
      
    # datatype of menu text 
    clicked = StringVar() 
      
    # initial menu text 
    clicked.set( "Monday" ) 
      
    # Create Dropdown menu 
    drop = OptionMenu( buyroot , clicked , *options ) 
    drop.pack() 
      
    # Create button, it will change label text 
    button = Button( buyroot , text = "click Me" , command = show ).pack() 
      
    # Create Label 
    label = Label( buyroot , text = " " ) 
    label.pack() 
      
    # Execute tkinter 
    buyroot.mainloop() 

purchase()




