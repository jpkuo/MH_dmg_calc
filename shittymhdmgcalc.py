#Marvel Heroes Calculator
import io
import math
from tkinter import *
import tkinter as tk

root = Tk()

group1 = LabelFrame( root, text="Character Ratings", padx = 5, pady = 5 )
group1.pack( padx = 10, pady = 10 )

group1toplabel = Label( group1, text="Enter Values as seen on character info" )
group1toplabel.pack()

group2 = LabelFrame( root, text="Character Attributes", padx = 5, pady = 5 )
group2.pack( padx = 10, pady = 10 )

group2toplabel = Label( group2, text="Enter your Character's Attributes" )

mainloop()

