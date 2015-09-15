#Marvel Heroes Calculator
# Copyright (c) 2015 jpkuo 
import io
import math
from tkinter import *

#Base UI construction
main=PanedWindow()
main.pack(fill=BOTH, expand=1)
sec=PanedWindow(main, orient=VERTICAL)
tri=PanedWindow(main, orient=VERTICAL)

ratings=LabelFrame(main, text="Character Ratings")
ratings.pack()

attributes=LabelFrame(main, text="Character Attributes")
attributes.pack()

synergies=LabelFrame(main, text="Synergies")
synergies.pack()

bonuses=LabelFrame(main, text="Extra Bonuses")
bonuses.pack()

main.add(ratings)
#main.add(attributes)
main.add(sec)
main.add(tri)
sec.add(attributes)
tri.add(synergies)
sec.add(bonuses)

#Character Ratings 
group1toplabel=Label(ratings, text="Enter Values as seen on character info")
group1toplabel.grid(column=1, row=1)
#Damage Ratings
#Base Damage Rating
bdrlab=Label(ratings, text="Base damage rating: ")
bdrlab.grid(column=1, row=2)
basedmg=Entry(ratings, width=10, justify=CENTER)
basedmg.insert(0, "0")
basedmg.grid(column=2, row=2)
#Physical Damage Rating
pdrlab=Label(ratings, text="Physical damage rating: ")
pdrlab.grid( column=1, row=3)
physdmg=Entry(ratings, width=10, justify=CENTER)
physdmg.insert(0, "0")
physdmg.grid(column=2, row=3)
#Energy Damage Rating
edrlab=Label(ratings, text="Energy damage rating: ")
edrlab.grid(column=1, row=4)
nrgdmg=Entry(ratings, width=10, justify=CENTER)
nrgdmg.insert(0, "0")
nrgdmg.grid(column=2, row=4)
#Mental Damage Rating
mdrlab=Label(ratings, text="Mental damage rating: ")
mdrlab.grid(column=1, row=5)
mendmg=Entry(ratings, width=10, justify=CENTER)
mendmg.insert(0, "0")
mendmg.grid(column=2, row=5)
#Area Damage Rating
adrlab=Label(ratings, text="Area damage rating: ")
adrlab.grid(column=1, row=6)
aredmg=Entry(ratings, width=10, justify=CENTER)
aredmg.insert(0, "0")
aredmg.grid(column=2, row=6)
#Melee Damage Rating
mlelab=Label(ratings, text="Melee damage rating: ")
mlelab.grid(column=1, row=7)
mledmg=Entry(ratings, width=10, justify=CENTER)
mledmg.insert(0, "0")
mledmg.grid(column=2, row=7)
#Ranged Damage Rating
rdrlab=Label(ratings, text="Ranged damage rating: ")
rdrlab.grid(column=1, row=8)
randmg=Entry(ratings, width=10, justify=CENTER)
randmg.insert(0, "0")
randmg.grid(column=2, row=8)
#Space Creator
emptyspace=Label(ratings, text=" ")
emptyspace.grid(column=1, row=9)
#Crit Ratings
#Base Critical Rating
bcrlab=Label(ratings, text="Base critical rating: ")
bcrlab.grid(column=1, row=10)
bascrit=Entry(ratings, width=10, justify=CENTER)
bascrit.insert(0, "0")
bascrit.grid(column=2, row=10)
#Melee Crit Rating
mlcrlab=Label(ratings, text="Melee critical rating: ")
mlcrlab.grid(column=1, row=11)
mlecrit=Entry(ratings, width=10, justify=CENTER)
mlecrit.insert(0, "0")
mlecrit.grid(column=2, row=11)
#Ranged Crit Rating
rngcrlab=Label(ratings, text="Ranged critical rating: ")
rngcrlab.grid(column=1, row=12)
rngcrit = Entry(ratings, width=10, justify=CENTER)
rngcrit.insert(0, "0")
rngcrit.grid(column=2, row=12)
#Area Crit Rating
arecrlab=Label(ratings, text="Area critical rating: ")
arecrlab.grid(column=1, row=13)
areacrit=Entry(ratings, width=10, justify=CENTER)
areacrit.insert(0, "0")
areacrit.grid(column=2, row=13)
#Physical Crit Rating
phscrlab=Label(ratings, text="Physical critical rating: ")
phscrlab.grid(column=1, row=14)
physcrit=Entry(ratings, width=10, justify=CENTER)
physcrit.insert(0, "0")
physcrit.grid(column=2, row=14)
#Energy Crit Rating
nrgcrlab=Label(ratings, text="Energy critical rating: ")
nrgcrlab.grid(column=1, row=15)
nrgcrit=Entry(ratings, width=10, justify=CENTER)
nrgcrit.insert(0, "0")
nrgcrit.grid(column=2, row=15)
#Mental Crit Rating
mencrlab=Label(ratings, text="Mental critical rating: ")
mencrlab.grid(column=1, row=16)
mencrit=Entry(ratings, width=10, justify=CENTER)
mencrit.insert(0, "0")
mencrit.grid(column=2, row=16)
#Space Creator
spacecreated=Label(ratings, text=" ")
spacecreated.grid(column=1, row=17)
#Critical and Brutal Damage ratings
#Critical Damage Rating
cdrlab=Label(ratings, text="Critical damage rating: ")
cdrlab.grid(column=1, row=18)
critdmg=Entry(ratings, width=10, justify=CENTER)
critdmg.insert(0, "0")
critdmg.grid(column=2, row=18)
#Brutal Rating
brtlab=Label(ratings, text="Brutal rating: ")
brtlab.grid(column=1, row=19)
bruten=Entry(ratings, width=10, justify=CENTER)
bruten.insert(0, "0")
bruten.grid(column=2, row=19)
#Brutal Damage Rating
brtdmglab=Label(ratings, text="Brutal damage rating: ")
brtdmglab.grid(column=1, row=20)
brutdmgen=Entry(ratings, width=10, justify=CENTER)
brutdmgen.insert(0, "0")
brutdmgen.grid(column=2, row=20)

#Character Attributes
group2toplabel=Label(attributes, text="Enter your Character's Attributes")
group2toplabel.grid(column=1, row=1)
#Durability
durlab=Label(attributes, text="Durability: ")
durlab.grid(column=1, row=2)
durent=Entry(attributes, width=10, justify=CENTER)
durent.insert(0, "0")
durent.grid(column=2, row=2)
#Strength
strlab=Label(attributes, text="Strength: ")
strlab.grid(column=1, row =3)
strent=Entry(attributes, width=10, justify=CENTER)
strent.insert(0, "0")
strent.grid(column=2, row=3)
#Fighting
figlab=Label(attributes, text="Fighting: ")
figlab.grid(column=1, row=4)
figent=Entry(attributes, width=10, justify=CENTER)
figent.insert(0, "0")
figent.grid(column=2, row=4)
#Speed
spelab=Label(attributes, text="Speed: ")
spelab.grid(column=1, row=5)
speent = Entry(attributes, width=10, justify=CENTER)
speent.insert(0, "0")
speent.grid(column=2, row=5)
#Energy
enelab=Label(attributes, text="Energy: ")
enelab.grid(column=1, row=6)
eneent=Entry(attributes, width=10, justify=CENTER)
eneent.insert(0, "0")
eneent.grid(column=2, row=6)
#Intelligence
intlab=Label(attributes, text="Intelligence: ")
intlab.grid(column=1, row=7)
intent=Entry(attributes, width=10, justify=CENTER)
intent.insert(0, "0")
intent.grid(column=2, row=7)

#Synergies
syncounter=0 #used to count the number of synergies activated
#syncounter=0

'''
SYNERGIES = [
    ("1", "antman"),
    ("2", "blackpanther"),
    ("3", "blackwidow"),
    ("4", "cable"),
    ("5", "america"),
    ("6", "colussus"),
    ("7", "cyclops"),
    ("8", "daredevil"),
    ("9", "deadpool"),
    ("10", "strange"),
    ("11", "doom"),
    ("12", "emma"),
    ("13", "gambit"),
    ("14", "ghostrider"),
    ("15", "hawkeye"),
    ("16", "hulk"),
    ("17", "torch"),
    ("18", "iceman"),
    ("19", "suestorm"),
    ("20", "ironman"),
    ("21", "phoenix"),
    ("22", "juggy"),
    ("23", "loki"),
    ("24", "lukecage"),
    ("25", "magneto"),
    ("26", "moonie"),
    ("27", "stretch"), 
    ("28", "carol"),
    ("29", "kurt"),
    ("30", "nova"),
    ("31", "betsy"),
    ("32", "punisher"),
    ("33", "rocket"),
    ("34", "rogue"),
    ("35", "wanda"),
    ("36", "shulk"),
    ("37", "surfer"),
    ("38", "spidey"),
    ("39", "doreen"),
    ("40", "starlord"),
    ("41", "storm"),
    ("42", "tasky"),
    ("43", "thing"),
    ("44", "thor"),
    ("45", "venom"),
    ("46", "vision"),
    ("47", "warmachine"),
    ("48", "bucky"),
    ("49", "logan"),
    ("50", "laura"),
]

def synarraycheck(x):
    print(x)
    for number, button in SYNERGIES:
        if number == x:
            return(button)

def synup(x):
    blurp = x
    global syncounter
    syncounter = syncounter + 1
    blap = synarraycheck(blurp)
    print(blap)
    if syncounter >= 10:
        syncounter = syncounter - 1
'''

def synup(x): #placekeeper
    print(x)

group3toplabel=Label(synergies, text="Please pick only 10")
group3toplabel.grid(column=1, row=1)
#Ant-Man
amsyn=IntVar()
antman=Checkbutton(synergies, text="Ant-Man", variable=amsyn, command=synup(1))
antman.grid(column=1, row=2, sticky=W)
#Black Panther
bpsyn=IntVar()
blackpanther=Checkbutton(synergies, text="Black Panther", variable=bpsyn, command=synup(2))
blackpanther.grid(column=2, row=2, sticky=W)
#Black Widow
bwsyn=IntVar()
blackwidow=Checkbutton(synergies, text="Black Widow", variable=bwsyn, command=synup(3))
blackwidow.grid(column=1, row=3, sticky=W)
#Cable
cblsyn=IntVar()
cable=Checkbutton(synergies, text="Cable", variable=cblsyn, command=synup(4))
cable.grid(column=2, row=3, sticky=W)
#Captain America
cptsyn=IntVar()
america=Checkbutton(synergies, text="Captain America", variable=cptsyn, command=synup(5))
america.grid(column=1, row=4, sticky=W)
#Colossus
colsyn=IntVar()
colossus=Checkbutton(synergies, text="Colossus", variable=colsyn, command=synup(6))
colossus.grid(column=2, row=4, sticky=W)
#cyclops
cycsyn=IntVar()
cyclops=Checkbutton(synergies, text="Cyclops", variable=cycsyn, command=synup(7))
cyclops.grid(column=1, row=5, sticky=W)
#Daredevil
ddsyn=IntVar()
daredevil=Checkbutton(synergies, text="Daredevil", variable=ddsyn, command=synup(8))
daredevil.grid(column=2, row=5, sticky=W)
#Deadpool
dpsyn=IntVar()
deadpool=Checkbutton(synergies, text="Deadpool", variable=dpsyn, command=synup(9))
deadpool.grid(column=1, row=6, sticky=W)
#Doctor Strange
drssyn=IntVar()
strange=Checkbutton(synergies, text="Dr. Strange", variable=drssyn, command=synup(10))
strange.grid(column=2, row=6, sticky=W)
#Dr. Doom
drdsyn=IntVar()
doom=Checkbutton(synergies, text="Dr. Doom", variable=drdsyn, command=synup(11))
doom.grid(column=1, row=7, sticky=W)
#Emma Frost
efsyn=IntVar()
emma=Checkbutton(synergies, text="Emma Frost", variable=efsyn, command=synup(12))
emma.grid(column=2, row=7, sticky=W)
#Gambit
gbtsyn=IntVar()
gambit=Checkbutton(synergies, text="Gambit", variable=gbtsyn, command=synup(13))
gambit.grid(column=1, row=8, sticky=W)
#Ghost Rider
grsyn=IntVar()
ghostrider=Checkbutton(synergies, text="Ghost rider", variable=grsyn, command=synup(14))
ghostrider.grid(column=2, row=8, sticky=W)
#Hawkeye
hawksyn=IntVar()
hawkeye=Checkbutton(synergies, text="Hawkeye", variable=hawksyn, command=synup(15))
hawkeye.grid(column=1, row=9, sticky=W)
#Hulk
hulksyn=IntVar()
hulk=Checkbutton(synergies, text="Hulk", variable=hulksyn, command=synup(16))
hulk.grid(column=2, row=9, sticky=W)
#Human Torch
torchsyn=IntVar()
torch=Checkbutton(synergies, text="Human Torch", variable=torchsyn, command=synup(17))
torch.grid(column=1, row=10, sticky=W)
#Iceman
icesyn=IntVar()
iceman=Checkbutton(synergies, text="Iceman", variable=icesyn, command=synup(18))
iceman.grid(column=2, row=10, sticky=W)
#Invisible Woman
iwsyn=IntVar()
suestorm=Checkbutton(synergies, text="Invisible Woman", variable=iwsyn, command=synup(19))
suestorm.grid(column=1, row=11, sticky=W)
#Iron Man
imsyn=IntVar()
ironman=Checkbutton(synergies, text="Iron Man", variable=imsyn, command=synup(20))
ironman.grid(column=2, row=11, sticky=W)
#Jean Grey
jgsyn=IntVar()
phoenix=Checkbutton(synergies, text="Jean Grey", variable=jgsyn, command=synup(21))
phoenix.grid(column=1, row=12, sticky=W)
#Juggernaut
jugsyn=IntVar()
juggy=Checkbutton(synergies, text="Juggernaut", variable=jugsyn, command=synup(22))
juggy.grid(column=2, row=12, sticky=W)
#Loki
lokisyn=IntVar()
loki=Checkbutton(synergies, text="Loki", variable=lokisyn, command=synup(23))
loki.grid(column=1, row=13, sticky=W)
#Luke Cage
lukesyn=IntVar()
lukecage=Checkbutton(synergies, text="Luke Cage", variable=lukesyn, command=synup(24))
lukecage.grid(column=2, row=13, sticky=W)
#Magneto
magsyn=IntVar()
magneto=Checkbutton(synergies, text="Magneto", variable=magsyn, command=synup(25))
magneto.grid(column=1, row=14, sticky=W)
#Moon Knight
mksyn=IntVar()
moonie=Checkbutton(synergies, text="Moon Knight", variable=mksyn, command=synup(26))
moonie.grid(column=2, row=14, sticky=W)
#Mr. Fantastic
mrfsyn=IntVar()
stretch=Checkbutton(synergies, text="Mr. Fantastic", variable=mrfsyn, command=synup(27))
stretch.grid(column=1, row=15, sticky=W)
#Ms. Marvel
msmsyn=IntVar()
carol=Checkbutton(synergies, text="Ms. Marvel", variable=msmsyn, command=synup(28))
carol.grid(column=2, row=15, sticky=W)
#Nightcrawler
ncsyn=IntVar()
kurt=Checkbutton(synergies, text="Nightcrawler", variable=ncsyn, command=synup(29))
kurt.grid(column=1, row=16, sticky=W)
#Nova
novasyn=IntVar()
nova=Checkbutton(synergies, text="Nova", variable=novasyn, command=synup(30))
nova.grid(column=2, row=16, sticky=W)
#Psylocke
psysyn=IntVar()
betsy=Checkbutton(synergies, text="Psylocke", variable=psysyn, command=synup(31))
betsy.grid(column=1, row=17, sticky=W)
#Punisher
punsyn=IntVar()
punisher=Checkbutton(synergies, text="Punisher", variable=punsyn, command=synup(32))
punisher.grid(column=2, row=17, sticky=W)
#Rocket Raccoon
rrsyn=IntVar()
rocket=Checkbutton(synergies, text="Rocket Raccoon", variable=rrsyn, command=synup(33))
rocket.grid(column=1, row=18, sticky=W)
#Rogue
roguesyn=IntVar()
rogue=Checkbutton(synergies, text="Rogue", variable=roguesyn, command=synup(34))
rogue.grid(column=2, row=18, sticky=W)
#Scarlet Witch
swsyn=IntVar()
wanda=Checkbutton(synergies, text="Scarlet Witch", variable=swsyn, command=synup(35))
wanda.grid(column=1, row=19, sticky=W)
#She-Hulk
shsyn=IntVar()
shulk=Checkbutton(synergies, text="She-Hulk", variable=shsyn, command=synup(36))
shulk.grid(column=2, row=19, sticky=W)
#Silver Surfer
sssyn=IntVar()
surfer=Checkbutton(synergies, text="Silver Surfer", variable=sssyn, command=synup(37))
surfer.grid(column=1, row=20, sticky=W)
#Spider-Man
spideysyn=IntVar()
spidey=Checkbutton(synergies, text="Spider-man", variable=spideysyn, command=synup(38))
spidey.grid(column=2, row=20, sticky=W)
#Squirrel Girl
sqgsyn=IntVar()
doreen=Checkbutton(synergies, text="Squirrel Girl", variable=sqgsyn, command=synup(39))
doreen.grid(column=1, row=21, sticky=W)
#Star-Lord
starsyn=IntVar()
starlord=Checkbutton(synergies, text="Star Lord", variable=starsyn, command=synup(40))
starlord.grid(column=2, row=21, sticky=W)
#Storm
stormsyn=IntVar()
storm=Checkbutton(synergies, text="Storm", variable=stormsyn, command=synup(41))
storm.grid(column=1, row=22, sticky=W)
#Taskmaster
tmsyn=IntVar()
tasky=Checkbutton(synergies, text="Taskmaster", variable=tmsyn, command=synup(42))
tasky.grid(column=2, row=22, sticky=W)
#Thing
thingsyn=IntVar()
thing=Checkbutton(synergies, text="Taskmaster", variable=thingsyn, command=synup(43))
thing.grid(column=1, row=23, sticky=W)
#Thor
thorsyn=IntVar()
thor=Checkbutton(synergies, text="Thor", variable=thorsyn, command=synup(44))
thor.grid(column=2, row=23, sticky=W)
#Venom
venomsyn=IntVar()
venom=Checkbutton(synergies, text="Venom", variable=venomsyn, command=synup(45))
venom.grid(column=1, row=24, sticky=W)
#Vision
visionsyn=IntVar()
vision=Checkbutton(synergies, text="Vision", variable=visionsyn, command=synup(46))
vision.grid(column=2, row=24, sticky=W)
#Warmachine
wmsyn=IntVar()
warmachine=Checkbutton(synergies, text="Warmachine", variable=wmsyn, command=synup(47))
warmachine.grid(column=1, row=25, sticky=W)
#Winter Soldier
wssyn=IntVar()
bucky=Checkbutton(synergies, text="Winter Soldier", variable=wssyn, command=synup(48))
bucky.grid(column=2, row=25, sticky=W)
#Wolverine
wolvsyn=IntVar()
logan=Checkbutton(synergies, text="Wolverine", variable=wolvsyn, command=synup(49))
logan.grid(column=1, row=26, sticky=W)
#X-23
x23syn=IntVar()
laura=Checkbutton(synergies, text="X-23", variable=x23syn, command=synup(50))
laura.grid(column=2, row=26, sticky=W)

#Item Bonuses
group4toplabel = Label( bonuses, text="Triggered Bonuses" )
group4toplabel.pack()


mainloop()

