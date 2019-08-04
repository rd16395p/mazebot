import requests
import numpy as np

#fix why it cant find the goal and start cords..
start = 0
startx = 0
starty = 0
goalx = 0
goaly = 0


def explore(value):
    if value == "X":
        print("A wall!")
    elif value == "A":
        print("Found the start!")
        startx, starty = np.where(map == "A")
        start = zip(*np.where(map == "A"))
    elif value == "B":
        print("Found the goal!")
        goalx, goaly = np.where(map == "B")
    else:
        print("Nothing here...")

#get map to solve
r = requests.get('https://api.noopschallenge.com/mazebot/random').json()
#print(r.text)
#print(type(r))

maptext = r['map']
#print(maptext)
#print(type(maptext))

#put into array format

map = np.asarray(maptext)
print(map)
print(map.shape)

for n in map:
    for j in n:
        #print("|")
        #print(j)
        explore(j)

print(startx, starty)
print(goalx, goaly)
print(start)

#use a* and solve it
