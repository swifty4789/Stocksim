
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

# Import module 
from tkinter import *
  
# Create object 
buyroot = Tk() 
  
# Adjust size 
buyroot.geometry( "1000x800" ) 
  
# Change the label text 
def show(): 
    label.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = list(SL)
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Select here" ) 
  
# Create Dropdown menu 
drop = OptionMenu( buyroot , clicked , *options )
drop.pack()
  
# Create button, it will change label text 
button = Button( buyroot , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = Label( buyroot , text = " ", font=('Helvetica 17 bold')) 
label.pack() 
  
# Execute tkinter 
buyroot.mainloop() 
