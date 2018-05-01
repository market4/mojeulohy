#-*- coding: utf-8 -*-
from random import randint # randrage viz knihovna, prvni se dělají importy,  druhy definice globalni fuknce

herni_pole = list("-"*10)
delka_pole = len(herni_pole)

def tah_hrace():
	stav = True
	while stav:
		pozice = int(input("Zadej herní pole (0,{}): ".format(delka_pole-1)))
		if pozice >=0 and pozice<delka_pole and herni_pole[pozice] == "-":
			herni_pole[pozice]= "x"
			stav = False # znamena ukonceni a hraje pocitac
			
def tah_pocitace():
	stav = True
	while stav: # je to pravda když stav je 
		pozice = randint(0,delka_pole - 1)  # musime vzit cislo bez 0.
		if herni_pole[pozice] == "-":  # kdyz prazdne pole , da se křížek, jinak nic a obnovuje se ta funkce dokud se to nesplni
			herni_pole[pozice]= "o"
			stav = False
			
def vyhodnot_stav():
	str_herni_pole = "".join(herni_pole)  # prevedeni pole na retezec, pokud to nechame jako pole, diva se na kazdy prvek zvlast tzn.  na kazdy symbol zvlast, coz pri hodnoceni xxx nebo ooo neni dobry
	if "xxx" in str_herni_pole: # potreba upraveneho herniho pole
		print("huraaaa")
		return False # znamena ze hra skoncila
	if "ooo" in str_herni_pole:
		print("smula, zkus to znovu")
		return False
	if "-" not in str_herni_pole:
		print("remiza")
		return False
	else:
		return True
		
stav_hry = True		#  dokud bude stav hry ok (kdyz stav je pravda staci jen if true:), tohle vše proběhne když je to ok
while stav_hry:
    print(herni_pole)
    tah_hrace()
    stav_hry = vyhodnot_stav()
    tah_pocitace()
    stav_hry = vyhodnot_stav()

	
		
	
