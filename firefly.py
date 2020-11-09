import networkx as nx
import matplotlib.pyplot as plt
import msvcrt,random
from pynput.keyboard import Key, Controller     # used in altTab

### SETUP ###

numNodes = 100          # number of nodes
tau = .25               # tau
speed = .01             # represents how long it takes to update
bumpchange = .005       # how much one flash affects other fireflies
deltaT = .01            # how long one iteration represents
flashVal = .9           # the higher the flashVal, the faster they sync
charges = [random.random() for i in range(numNodes)]    # each firefly's potential
fig = plt.figure()
G = nx.Graph()
nodesDict = {}
for i in range(numNodes):
    nodesDict[i] = (random.random()*1000.0,random.random()*1000.0)
colors = [(0,0,0) for i in range(numNodes)]
sizes = [10 for i in range(numNodes)]

def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret
def altTab():
    plt.draw()
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
            allcharges = [allcharges[k]+bumpchange for k in range(len(allcharges))]
            allcharges[i] = 0
        brightness = 1 if allcharges[i]>1 else allcharges[i]**3
        allcolors[i] = (brightness,brightness,0)
        sizes[i] = allcharges[i]*100
    return allcolors,allcharges

### MAIN ###

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