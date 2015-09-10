#Marvel Heroes Calculator
import io
import math
from tkinter import *
import tkinter as tk

#Base UI construction
main = PanedWindow()
main.pack(fill = BOTH, expand = 1)
sec = PanedWindow(main, orient = VERTICAL )

ratings = LabelFrame( main, text="Character Ratings", padx = 5, pady = 5 )
ratings.pack( padx = 10, pady = 10 )

attributes = LabelFrame( main, text="Character Attributes", padx = 5, pady = 5 )
attributes.pack( padx = 10, pady = 10 )

synergies = LabelFrame( main, text="Synergies", padx = 5, pady = 5 )
synergies.pack( padx = 10, pady = 10 )

bonuses = LabelFrame( main, text="Extra Bonuses", padx = 5, pady = 5 )
bonuses.pack( padx = 10, pady = 10 )

main.add(ratings)
main.add(attributes)
main.add(sec)
sec.add(synergies)
sec.add(bonuses)

#Character Ratings 
group1toplabel = Label( ratings, text="Enter Values as seen on character info" )
group1toplabel.grid( column = 1, row = 1)
#Damage Ratings
#Base Damage Rating
bdrlab = Label( ratings, text="Base damage rating: " )
bdrlab.grid( column = 1, row = 2 )
basedmg = Entry( ratings, width = 5, justify = CENTER )
basedmg.insert( 0, "0" )
basedmg.grid( column = 2, row = 2 )
#Physical Damage Rating
pdrlab = Label( ratings, text="Physical damage rating: " )
pdrlab.grid( column = 1, row = 3 )
physdmg = Entry( ratings, width = 5, justify = CENTER )
physdmg.insert( 0, "0" )
physdmg.grid( column = 2, row = 3 )
#Energy Damage Rating
edrlab = Label( ratings, text="Energy damage rating: " )
edrlab.grid( column = 1, row = 4 )
nrgdmg = Entry( ratings, width = 5, justify = CENTER )
nrgdmg.insert( 0, "0" )
nrgdmg.grid( column = 2, row = 4 )
#Mental Damage Rating
mdrlab = Label( ratings, text="Mental damage rating: " )
mdrlab.grid( column = 1, row = 5 )
mendmg = Entry( ratings, width = 5, justify = CENTER )
mendmg.insert( 0, "0" )
mendmg.grid( column = 2, row = 5 )
#Area Damage Rating
adrlab = Label( ratings, text="Area damage rating: " )
adrlab.grid( column = 1, row = 6 )
aredmg = Entry( ratings, width = 5, justify = CENTER )
aredmg.insert( 0, "0" )
aredmg.grid( column = 2, row = 6 )
#Melee Damage Rating
mlelab = Label( ratings, text="Melee damage rating: " )
mlelab.grid( column = 1, row = 7 )
mledmg = Entry( ratings, width = 5, justify = CENTER )
mledmg.insert( 0, "0" )
mledmg.grid( column = 2, row = 7 )
#Ranged Damage Rating
rdrlab = Label( ratings, text="Ranged damage rating: " )
rdrlab.grid( column = 1, row = 8 )
randmg = Entry( ratings, width = 5, justify = CENTER )
randmg.insert( 0, "0" )
randmg.grid( column = 2, row = 8 )
#Space Creator
emptyspace = Label( ratings, text=" " )
emptyspace.grid( column = 1, row = 9 )
#Crit Ratings
#Base Critical Rating
bcrlab = Label( ratings, text="Base critical rating: " )
bcrlab.grid( column = 1, row = 10 )
bascrit = Entry( ratings, width = 5, justify = CENTER )
bascrit.insert( 0, "0" )
bascrit.grid( column = 2, row = 10 )
#Melee Crit Rating
mlcrlab = Label( ratings, text="Melee critical rating: " )
mlcrlab.grid( column = 1, row = 11 )
mlecrit = Entry ( ratings, width = 5, justify = CENTER )
mlecrit.insert( 0, "0" )
mlecrit.grid( column = 2, row = 11 )

group2toplabel = Label( attributes, text="Enter your Character's Attributes" )
group2toplabel.pack()

group3toplabel = Label( synergies, text="Please pick only 10" )
group3toplabel.pack()

group4toplabel = Label( bonuses, text="Triggered Bonuses" )
group4toplabel.pack()

mainloop()

