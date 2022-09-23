#pseudokode for treet
#lager liste som holder alle linjene som lister
import fileinput

liste = []
kitten = 0
for line in fileinput.input():
	linje = line.split(" ")
	if int(linje[0])!=-1:
		if (len(linje) == 1):
			kitten = int(line)
		else:
			liste.append(linje)
#funksjon som finner forelder til tall
def find_parent(list, num):
	for sublist in list:
		i = 1
		while i < len(sublist):
			if int(sublist[i]) == num:
				return int(sublist[0])
			i+=1
	return -1
	
path = []

parent = kitten
while parent != -1:
	path.append(parent)
	parent = find_parent(liste, parent)
	

print(*path)