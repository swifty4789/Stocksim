import tkinter
from tkinter import ttk

root = ttk
ttk.Style().configure("TButton", padding=60, relief='flat',
                      background="#000")

btn = ttk.Button(root, text="New")
btn.pack()
btn = ttk.Button(root, text="Load")
btn.pack()
