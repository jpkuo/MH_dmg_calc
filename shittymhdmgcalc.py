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
basedmg = Entry( ratings, width = 10, justify = CENTER )
basedmg.insert( 0, "0" )
basedmg.grid( column = 2, row = 2 )
#Physical Damage Rating
pdrlab = Label( ratings, text="Physical damage rating: " )
pdrlab.grid( column = 1, row = 3 )
physdmg = Entry( ratings, width = 10, justify = CENTER )
physdmg.insert( 0, "0" )
physdmg.grid( column = 2, row = 3 )
#Energy Damage Rating
edrlab = Label( ratings, text="Energy damage rating: " )
edrlab.grid( column = 1, row = 4 )
nrgdmg = Entry( ratings, width = 10, justify = CENTER )
nrgdmg.insert( 0, "0" )
nrgdmg.grid( column = 2, row = 4 )
#Mental Damage Rating
mdrlab = Label( ratings, text="Mental damage rating: " )
mdrlab.grid( column = 1, row = 5 )
mendmg = Entry( ratings, width = 10, justify = CENTER )
mendmg.insert( 0, "0" )
mendmg.grid( column = 2, row = 5 )
#Area Damage Rating
adrlab = Label( ratings, text="Area damage rating: " )
adrlab.grid( column = 1, row = 6 )
aredmg = Entry( ratings, width = 10, justify = CENTER )
aredmg.insert( 0, "0" )
aredmg.grid( column = 2, row = 6 )
#Melee Damage Rating
mlelab = Label( ratings, text="Melee damage rating: " )
mlelab.grid( column = 1, row = 7 )
mledmg = Entry( ratings, width = 10, justify = CENTER )
mledmg.insert( 0, "0" )
mledmg.grid( column = 2, row = 7 )
#Ranged Damage Rating
rdrlab = Label( ratings, text="Ranged damage rating: " )
rdrlab.grid( column = 1, row = 8 )
randmg = Entry( ratings, width = 10, justify = CENTER )
randmg.insert( 0, "0" )
randmg.grid( column = 2, row = 8 )
#Space Creator
emptyspace = Label( ratings, text=" " )
emptyspace.grid( column = 1, row = 9 )
#Crit Ratings
#Base Critical Rating
bcrlab = Label( ratings, text="Base critical rating: " )
bcrlab.grid( column = 1, row = 10 )
bascrit = Entry( ratings, width = 10, justify = CENTER )
bascrit.insert( 0, "0" )
bascrit.grid( column = 2, row = 10 )
#Melee Crit Rating
mlcrlab = Label( ratings, text="Melee critical rating: " )
mlcrlab.grid( column = 1, row = 11 )
mlecrit = Entry ( ratings, width = 10, justify = CENTER )
mlecrit.insert( 0, "0" )
mlecrit.grid( column = 2, row = 11 )
#Ranged Crit Rating
rngcrlab = Label( ratings, text="Ranged critical rating: " )
rngcrlab.grid( column = 1, row = 12 )
rngcrit = Entry( ratings, width = 10, justify = CENTER )
rngcrit.insert( 0, "0" )
rngcrit.grid( column = 2, row = 12 )
#Area Crit Rating
arecrlab = Label( ratings, text="Area critical rating: " )
arecrlab.grid( column = 1, row = 13 )
areacrit = Entry( ratings, width = 10, justify = CENTER )
areacrit.insert( 0, "0" )
areacrit.grid( column = 2, row = 13 )
#Physical Crit Rating
phscrlab = Label( ratings, text="Physical critical rating: " )
phscrlab.grid( column = 1, row = 14 )
physcrit = Entry( ratings, width = 10, justify = CENTER )
physcrit.insert( 0, "0" )
physcrit.grid( column = 2, row = 14 )
#Energy Crit Rating
nrgcrlab = Label( ratings, text="Energy critical rating: " )
nrgcrlab.grid( column = 1, row = 15 )
nrgcrit = Entry( ratings, width = 10, justify = CENTER )
nrgcrit.insert( 0, "0" )
nrgcrit.grid( column = 2, row = 15 )
#Mental Crit Rating
mencrlab = Label( ratings, text="Mental critical rating: " )
mencrlab.grid(column = 1, row = 16 )
mencrit = Entry( ratings, width = 10, justify = CENTER )
mencrit.insert( 0, "0" )
mencrit.grid(column = 2, row = 16 )
#Space Creator
spacecreated = Label( ratings, text=" " )
spacecreated.grid( column = 1, row = 17)
#Critical and Brutal Damage ratings
#Critical Damage Rating
cdrlab = Label( ratings, text="Critical damage rating: " )
cdrlab.grid( column = 1, row = 18 )
critdmg = Entry( ratings, width = 10, justify = CENTER )
critdmg.insert( 0, "0" )
critdmg.grid( column = 2, row = 18 )
#Brutal Rating
brtlab = Label( ratings, text="Brutal rating: " )
brtlab.grid( column = 1, row = 19 )
bruten = Entry( ratings, width = 10, justify = CENTER )
bruten.insert( 0, "0" )
bruten.grid( column = 2, row = 19 )
#Brutal Damage Rating
brtdmglab = Label( ratings, text="Brutal damage rating: " )
brtdmglab.grid( column = 1, row = 20 )
brutdmgen = Entry( ratings, width = 10, justify = CENTER )
brutdmgen.insert( 0, "0" )
brutdmgen.grid( column = 2, row = 20 )

group2toplabel = Label( attributes, text="Enter your Character's Attributes" )
group2toplabel.pack()

group3toplabel = Label( synergies, text="Please pick only 10" )
group3toplabel.pack()

group4toplabel = Label( bonuses, text="Triggered Bonuses" )
group4toplabel.pack()

mainloop()

