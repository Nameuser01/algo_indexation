#!/usr/bin/env python3

import random

def recherche(nom):
	firstline = open('map.txt', 'r')
	file_content = firstline.readlines()
	firstline.close()
	line_zero = file_content[0]
	i = 0
	path = ""
	cpt_path = 0
	for i in range(len(file_content[0])):#De 0 jusqu'à la longueur totale de la ligne. Scan
		if (line_zero[i] == "."):
			path = path + str(i)
			cpt_path += 1
		else:
			pass
	print("Le bot",nom,"a trouvé",len(path),"chemins !")
	return [path, cpt_path]

def chemins_affichage(path):
	i = 0
	printable_path = ""
	if (len(path) > 1):
		for i in range(len(path)):
			if (i == len(path) - 1):
				printable_path = printable_path + path[i]
			else:
				printable_path = printable_path + path[i] + " "
	else:
		printale_path = path
	return printable_path

def map_init():
	x_size = -1#Strictement positif
	y_size = -1#axe ordonnées inversé (vers le bas mais strictement positif)
	while(x_size <= 0 or x_size > 10):
		x_size = int(input("Valeur de x ?\n> "))
	while(y_size <= 0 or y_size > 1000):#Unge!
		y_size = int(input("Valeur de y ?\n> "))
	#print("On va créer une map de x",x_size,"par",y_size)
	map_generation(x_size, y_size)

def map_generation(x, y):
	print("On va créer une map de x",x,"par",y)
	i = 0
	a = 0
	compo_line = ""
	for a in range(y):
		for i in range(x):
			rand_num = random.randrange(0, 100, 1)#Gedanken für Zukunft (Anderen values Bspl)
			print("random number:",rand_num)
			if (rand_num > 50):#Häufigkeit des Auftretens von punkten
				compo_line = compo_line + "."
			else:
				compo_line = compo_line + "*"
		register_line(compo_line, a)
		compo_line = ""

def register_line(compo_line, a):
	if(a == 1):
		file_w = ("foo.txt", "w")
	else:
		file_w = ("foo.txt", "a")
	file_w.write(compo_line)
	file_w.close()

#Map file génération
map_init()


#bot_1 - Searcher
nom = "searcher"
tmp_list_treatment = recherche(nom)#Fonction de scan de la première couche
path = tmp_list_treatment[0]
cpt_path = tmp_list_treatment[1]
print("effectivement, les chemins",chemins_affichage(path), "sont à explorer")

#bot_2 - Explorer
starter_point = 0
cpt_lancement_bots = 0
a = 0
while (a < cpt_path):
	starter_point = path[a]
	print("On lance le bot",starter_point,"dans le x",path[a])
	#launch the fonction [building]
	a += 1