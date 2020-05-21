#by bidou

import os
from random import randint, sample

os.system("title selecteur de map")

L = ["occasionnel", "wingman" , "course a l'armement" , "sniper volant" , "demolition" , "match a mort" ]
L2 = ["inferno", "overpass", "train" , "cobblestone" , "shortdust" , "lake" , "rialto" , "vertigo", "nuke" ]
L3 = ["Dust II", "Mirage", "Inferno", "Vertigo", "Cobblestone", "cache", "Zoo", "Abbey", "Biome", "Train", "Overpass", "Italy", "Nuke", "Canals", "Militia", "Agency", "Office", "Assault" ]
def replace(a):
    a[0] = a[0].replace("'", "")
    a[0] = a[0].replace("[", "")
    a[0] = a[0].replace("]", "")

    return a

while True:
	alé1 = ""

	choix = input("> ").lower()

	if choix == "":
		alé = sample(L, 1)
		a = alé
		alé = replace(a)
		print(f"le mode de jeu est : {alé[0]}")
		if alé == ["wingman"]:
			alé1 = sample(L2, 1)
			a = alé1
			alé1 = replace(a)
			print(f"la map est : {alé1[0]}")
		if alé == ["occasionnel"]:
			alé1 = sample(L3, 1)
			a = alé1
			alé1 = replace(a)
			print(f"la map est : {alé1[0]}")
	elif choix == "w":
		alé = sample(L2, 1)
		a = alé
		alé = replace(a)
		print(f"la map wingman est : {alé[0]}")
	elif choix == "o":
		alé = sample(L3, 1)
		a = alé
		alé = replace(a)
		print(f"la map occasionnel est : {alé[0]}")
	elif choix == "s":
		break