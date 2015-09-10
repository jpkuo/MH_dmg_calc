#Marvel Heroes Calculator
import io
import math
from tkinter import *
import tkinter as tk

#Base UI construction
main = PanedWindow()
main.pack(fill = BOTH, expand = 1)
sec = PanedWindow(main, orient = VERTICAL )

group1 = LabelFrame( main, text="Character Ratings", padx = 5, pady = 5 )
group1.pack( padx = 10, pady = 10 )

group2 = LabelFrame( main, text="Character Attributes", padx = 5, pady = 5 )
group2.pack( padx = 10, pady = 10 )

group3 = LabelFrame( main, text="Synergies", padx = 5, pady = 5 )
group3.pack( padx = 10, pady = 10 )

group4 = LabelFrame( main, text="Extra Bonuses", padx = 5, pady = 5 )
group4.pack( padx = 10, pady = 10 )

main.add(group1)
main.add(group2)
main.add(sec)
sec.add(group3)
sec.add(group4)

group1toplabel = Label( group1, text="Enter Values as seen on character info" )
group1toplabel.pack()

group2toplabel = Label( group2, text="Enter your Character's Attributes" )
group2toplabel.pack()

group3toplabel = Label( group3, text="Please pick only 10" )
group3toplabel.pack()

group4toplabel = Label( group4, text="Triggered Bonuses" )
group4toplabel.pack()

mainloop()

