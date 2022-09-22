#oppgave 2 oblig 1
import fileinput
#sett element bakerst i koen
def push_back(queue, x):
    queue.append(x)
    return queue

#sett element fremst i koen
def push_front(queue, x):
    queue.insert(0, x)
    return queue

#sett element i midten av koen
def push_middle(queue, x):
    half = (len(queue)+1)//2 #// rounds down
    queue.insert(half, x)  
    return queue

def get(queue, x):
    print(queue[x])

#Lager en tom liste som holder koen
queue = []

#itererer gjennom filen
for line in fileinput.input():
    if line.startswith("push_back"):
        tall = line.split(' ')
        queue = push_back(queue, int(tall[-1]))

    elif line.startswith("push_front"):
        tall = line.split(' ')
        queue = push_front(queue, int(tall[-1]))

    elif line.startswith("push_middle"):
        tall = line.split(' ')
        queue = push_middle(queue, int(tall[-1]))

    elif line.startswith("get"):
        tall = line.split(' ')
        get(queue, int(tall[-1]))