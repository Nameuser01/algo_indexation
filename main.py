#!/usr/bin/env python3

def recherche(nom):
	firstline = open('map.txt', 'r')
	file_content = firstline.readlines()
	firstline.close()
	line_zero = file_content[0]
	i = 0
	path = ""
	for i in range(len(file_content[0])):#De 0 jusqu'à la longueur totale de la ligne. Scan
		if (line_zero[i] == "."):
			path = path + str(i)
		else:
			pass
	print("Le bot",nom,"a trouvé",len(path),"chemins !")
	return path

def chemins_affichage(path):
	i = 0
	printable_path = ""
	for i in range(len(path)):
		printable_path = printable_path + path[i] + " "
	return printable_path

#bot_1
pos_x = 0
pos_y = 0
nom = "searcher"
path = recherche(nom)#Fonction de scan de la première couche
print("effectivement, les chemins",chemins_affichage(path), "sont à explorer")