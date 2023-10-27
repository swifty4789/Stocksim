from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os

for f in os.listdir('images/'):
    print(f)
root = Tk()  
canvas = Canvas(root, width = 600, height = 600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("images/fanum.png"))  
canvas.create_image(20, 20, anchor=NW, image=img)

root.mainloop() 

