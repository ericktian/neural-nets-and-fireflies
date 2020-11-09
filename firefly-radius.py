import networkx as nx
import matplotlib.pyplot as plt
import msvcrt,random
from pynput.keyboard import Key, Controller     # used in altTab
from math import pi,acos,sin,cos

numNodes = 100
tau = .25
speed = .01             # represents how long it takes to update
bumpchange = .005
deltaT = .005
blastRadius = 500
flashVal = .99           # the higher the flashVal, the faster they sync
charges = [random.random() for i in range(numNodes)]
# plt.figure(figsize=(10, 6))
fig = plt.figure()
G = nx.Graph()
nodesDict = {}
for i in range(numNodes):
    nodesDict[i] = (random.random()*1000.0,random.random()*1000.0)
colors = [(0,0,0) for i in range(numNodes)]
sizes = [10 for i in range(numNodes)]

def calcd(index1,index2):
    y1 = nodesDict[index1][1]
    x1 = nodesDict[index1][0]
    y2 = nodesDict[index2][1]
    x2 = nodesDict[index2][0]
    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    R  = 6371#3958.76 # miles = 6371 km
    y1 *= pi/180.0
    x1 *= pi/180.0
    y2 *= pi/180.0
    x2 *= pi/180.0
    # print( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) )
    return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
def altTab():
    plt.draw()
    # SIMULATE KEYPRESS
    keyboard = Controller()
    plt.pause(.01)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
def update(allcolors,allcharges):
    allcharges = [allcharges[k]+deltaT*(1-allcharges[k])/tau for k in range(len(allcharges))]
    for i in range(len(allcharges)):
        if allcharges[i]>flashVal:
            allcharges = [allcharges[k]+bumpchange if i!=k and calcd(i,k)<blastRadius
                          else allcharges[k] for k in range(len(allcharges))]
            allcharges[i] = 0
        brightness = 1 if allcharges[i]>1 else allcharges[i]**3
        allcolors[i] = (brightness,brightness,0)
        sizes[i] = allcharges[i]*100
    return allcolors,allcharges


altTab()
while True:
    if kbfunc():
        break
    G.add_nodes_from(nodesDict)
    nx.draw(G, nodesDict, node_size=sizes, node_color=colors, with_labels=False)
    fig.set_facecolor("#000000")
    plt.draw()
    plt.pause(speed)
    colors,charges=update(colors,charges)
    plt.clf()
    G.clear()