#!/usr/bin/env python3

f = open('map.txt','r')
count = 0
Lines = f.readlines()
for line in Lines:
	count += 1
	#print("Line{}: {}".format(count, line.strip()))
	i = 0
	for i in range(len(line.strip())):
		if(line.strip()[i] == "."):
			
		else:
			print("")