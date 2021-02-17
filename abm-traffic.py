# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:26:03 2021

@author: axelb
"""


import pycxsimulator
from pylab import *

width = 50
height = 50
populationSize = 0

free = 0
carrying = 1

garbageProb = 0.8
carSpawnProb = 0.4

stop = 0
go = 1

rd1Xpos = [10,10]
rd1Ypos = [0,50]

red = 0
green = 1

lightXpos = [10, 10, 40, 40]
lightYpos = [10, 40, 10, 40]


def initialize():
    global time, agents, lightAgents, envir, agents1

    time = 0

    agents = []
    for i in range(populationSize):
        newAgent = [randint(width), randint(height), free]
        agents.append(newAgent)
        
    agents1 = []
    newAgent = [rd1Xpos[0], rd1Ypos[0], go]
    agents1.append(newAgent) # Spawn new car
    
    lightAgents = []
    for i in range(len(lightXpos)):
        newAgent = [lightXpos[i], lightYpos[i], red]
        lightAgents.append(newAgent)

    envir = zeros([height, width])
    envir[10,:] = 1
    envir[:,10] = 1
    envir[40,:] = 1
    envir[:,40] = 1
    # for y in range(height):
    #     for x in range(width):
    #         if random() < garbageProb:
    #             state = 1
    #         else:
    #             state = 0
    #         envir[y, x] = state

def observe():
    cla()
    imshow(envir, cmap = cm.Greys, vmin = 0, vmax = 1)
    axis('image')
    x = [ag[0] for ag in agents]
    y = [ag[1] for ag in agents]
    s = [ag[2] for ag in agents]
    xl = [ag[0] for ag in lightAgents]
    yl = [ag[1] for ag in lightAgents]
    sl = [ag[2] for ag in lightAgents]
    x1 = [ag[0] for ag in agents1]
    y1 = [ag[1] for ag in agents1]
    s1 = [ag[2] for ag in agents1]
    scatter(x, y, c = s, cmap = cm.bwr)
    scatter(xl, yl, c = sl, cmap = cm.RdYlGn)
    scatter(x1, y1, c = s1, cmap = cm.cool)
    
    title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def update():
    global time, agents, envir

    time += 1
    
    if (time+3)%25 == 0:
        if lightAgents[0][2] == red:
            lightAgents[0][2] = green
        else:
            lightAgents[0][2] = red
            
    if (time+20)%25 == 0:
        if lightAgents[1][2] == red:
            lightAgents[1][2] = green
        else:
            lightAgents[1][2] = red
    
    if len(agents1)==0 or (agents1[-1][1] != rd1Ypos[0]
                           and random() < carSpawnProb):
        newAgent = [rd1Xpos[0], rd1Ypos[0], go]
        agents1.append(newAgent) # Spawn new car
        
    if agents1[0][1] == rd1Ypos[1]: # Despawn out of bounds car
        agents1.pop(0)
      
    agents1[0][2] = go    
        
    for i in range(len(agents1)-1):
        if (agents1[i][1] - agents1[i+1][1]) < 2:
            agents1[i+1][2] = stop
        else:
            agents1[i+1][2] = go
    
    for i, ag1 in enumerate(agents1):
        if ((ag1[1] == lightYpos[0]-1 and lightAgents[0][2] == red) 
        or (ag1[1] == lightYpos[1]-1 and lightAgents[1][2] == red)):
            ag1[2] = stop # Stop before red lights
        
        
        
    for ag1 in agents1:
        if ag1[2] == go:
            ag1[1] += 1
    
    for ag in agents:

        # simulate random motion
        ag[0] += randint(-1, 2)
        ag[1] += randint(-1, 2)
        ag[0] = clip(ag[0], 0, width - 1)
        ag[1] = clip(ag[1], 0, height - 1)

        # simulate interaction between ants and environment
        if envir[ag[1], ag[0]] > 0:
            if ag[2] == free:
                envir[ag[1], ag[0]] -= 1
                ag[2] = carrying
            else:
                envir[ag[1], ag[0]] += 1
                ag[2] = free

pycxsimulator.GUI().start(func=[initialize, observe, update])
