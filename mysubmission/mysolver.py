import requests
import numpy as np

#fix why it cant find the goal and start cords..
#start = 0
#goal = 0
startx = 0
starty = 0
goalx = 0
goaly = 0


def explore(value):
    if value == "X":
        print("A wall!")
    elif value == "A":
        print("Found the start!")
        #startx, starty = np.where(map == "A")
        #start = zip(*np.where(map == "A"))
    elif value == "B":
        print("Found the goal!")
        goalx, goaly = np.where(map == "B")
    else:
        print("Nothing here...")

#thank you to https://stackoverflow.com/questions/36166578/maze-solving-in-python#36166855 for helping me on the righttrack!
#learned a lot from this code!
already_visited=[]
def solve(x,y,matrix):
    #global already_visited
    if x >= len(matrix) or y >= len(matrix[x]):
        return False

    #base cases
    if matrix[x][y] == "B":
        for row in matrix:
            row = str(row)[1:-1]
            #print(row)
            print(matrix)
        return True
    if matrix[x][y] == "*":
        return False
    if matrix[x][y] == "X":
        return False

    matrix[x][y] = "*"

    #---------------------
    if (x,y) in already_visited: #check if we have already been here
        return False

    already_visited.append((x,y)) #add position to list
    #---------------------


    # recursive cases (matrix traversal)
    if (x < len(matrix)-1 and solve(x+1,y,matrix)):
        return True
    elif (y > 0 and solve(x,y-1,matrix)):
        return True
    elif (x > 0 and solve(x-1,y,matrix)):
        return True
    elif (y < len(matrix)-1 and solve(x,y+1,matrix)):
        return True
    else:
        return False

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

startx, starty = np.where(map == "A")
startx = int(startx)
starty = int(starty)
print(startx, starty)
goalx, goaly = np.where(map == "B")
print(goalx, goaly)

print("The solution by hovering and ignoring all walls is " ,int((abs(startx-goalx) + abs(starty-goaly))),  " steps")

matrix = map
solve(startx,starty,matrix)

#use a* and solve it
