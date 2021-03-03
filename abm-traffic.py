# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:26:03 2021

@author: axelb
"""


import pycxsimulator
from matplotlib.pylab import *
import matplotlib.cm as cm
from car import Car
from Road import Road


width = 50
height = 50

free = 0 # maurdrit
carrying = 1 # maurdrit

carSpawnProb = 0.4 # chance of spawning car at any given tick

stop = 0 # whether car is stop or go
go = 1 

rd1Xpos = [10,10] # x values are the same as the road is straight
rd1Ypos = [0,50] # y value from 0 to 50 as y = 0 on top, 50 on bottom

red = 0 # color of light
green = 1

lightXpos = [10, 10, 40, 40] # x-position of ligth 1, 2, 3, 4 
lightYpos = [10, 40, 10, 40] # y-position of light 1, 2, 3, 4

def initialize_2():
    global time, agents, lightAgents, envir, agents1

    time = 0
    road_1 = Road(0, 10, 10, 10, 'west')
    car_1 = Car(0, 0, road_1)
    agents1 = [car_1]
    


def initialize():
    global time, agents, lightAgents, envir, agents1

    time = 0

    agents1 = [] # list of cars
    newAgent = [rd1Xpos[0], rd1Ypos[0], go] # create car object
    agents1.append(newAgent) # Spawn new car
    
    lightAgents = [] # list of lights
    for i in range(len(lightXpos)):
        newAgent = [lightXpos[i], lightYpos[i], red] # create light
        lightAgents.append(newAgent) # spawn light

    # Kode som tegner veiene svart
    envir = zeros([height, width])
    envir[10,:] = 1
    envir[:,10] = 1
    envir[40,:] = 1
    envir[:,40] = 1
    

def observe():
    cla() # kanskje clearer drit
    imshow(envir, cmap = cm.Greys, vmin = 0, vmax = 1) # shows ilustration
    axis('image')
    xl = [ag[0] for ag in lightAgents] # x-verdi for alle lyskryss
    yl = [ag[1] for ag in lightAgents] # y-verdi for alle lyskryss
    sl = [ag[2] for ag in lightAgents] # rødt eller grønt
    x1 = [ag[0] for ag in agents1] # x-verdi for alle biler
    y1 = [ag[1] for ag in agents1] # y-verdi for alle lyskryss
    s1 = [ag[2] for ag in agents1] # stop or go
    scatter(xl, yl, c = sl, cmap = cm.RdYlGn) # tegner noe lyskryssdrit
    scatter(x1, y1, c = s1, cmap = cm.cool) # tegner noe bildrit
    
    title('t = ' + str(time)) # D'Tittel da


def update():
    global time, agents, envir

    time += 1
    
    if (time+3)%25 == 0: # for hvert 25. "sekund", flipper lysene for lys 0, med shiftet start
        if lightAgents[0][2] == red:
            lightAgents[0][2] = green
        else:
            lightAgents[0][2] = red
            
    if (time+20)%25 == 0: # for hvert 25. "sekund", flipper lysene for lys 1, med shiftet start
        if lightAgents[1][2] == red:
            lightAgents[1][2] = green
        else:
            lightAgents[1][2] = red
    
    # Hvis liste av biler ikke har biler, eller HVA GJØR EGT AGENTS1[-1][1]?
    if len(agents1)==0 or (agents1[-1][1] != rd1Ypos[0]
                           and random() < carSpawnProb):
        newAgent = [rd1Xpos[0], rd1Ypos[0], go]
        agents1.append(newAgent) # Spawn new car
        
    if agents1[0][1] == rd1Ypos[1]: # Despawn out of bounds car
        agents1.pop(0)
      
    agents1[0][2] = go    # Sets car to go
        
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

pycxsimulator.GUI().start(func=[initialize, observe, update])
