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
def find_parent(num, list):
	for sublist in list:
		i = 1
		while i < len(sublist):
			if int(sublist[i]) is num:
				return list[0]
			i+=1
	
path = [kitten]

parent = 0
while parent != -1:
	parent = find_parent(path, kitten)
	path.append(parent)

print(*path)