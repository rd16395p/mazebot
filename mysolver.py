import requests
import numpy as np

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

#use a* and solve it
