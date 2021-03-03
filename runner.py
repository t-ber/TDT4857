# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:26:03 2021

@author: axelb
"""


from lights import Traffic_light
import pycxsimulator
from matplotlib.pylab import *
import matplotlib.cm as cm
from car import Car
from road import Road


width = 50
height = 50

free = 0 # maurdrit
carrying = 1 # maurdrit

carSpawnProb = 0.1 # chance of spawning car at any given tick

stop = 0 # whether car is stop or go
go = 1 

rd1Xpos = [10,10] # x values are the same as the road is straight
rd1Ypos = [0,50] # y value from 0 to 50 as y = 0 on top, 50 on bottom

red = 0 # color of light
green = 1

lightXpos = [10, 10, 40, 40] # x-position of ligth 1, 2, 3, 4 
lightYpos = [10, 40, 10, 40] # y-position of light 1, 2, 3, 4

def initialize_2():
    global time, lightAgents, envir, cars

    time = 0
    road_1 = Road(0, 10, 10)
    car_1 = Car(0, 0)
    cars = []


def initialize():
    global time, lightAgents, envir, cars

    time = 0

    cars = [] # list of cars
    car = Car(10, 0) # create car object
    cars.append(car) # Spawn new car
    
    lightAgents = [] # list of lights
    for i in range(len(lightXpos)):
        new_light = Traffic_light(lightXpos[i], lightYpos[i]) #[lightXpos[i], lightYpos[i], red] # create light
        lightAgents.append(new_light) # spawn light

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
    xl = [ag.x for ag in lightAgents] # x-verdi for alle lyskryss
    yl = [ag.y for ag in lightAgents] # y-verdi for alle lyskryss
    sl = [ag.current_state for ag in lightAgents] # rødt eller grønt
    x1 = [car.x for car in cars] # x-verdi for alle biler
    y1 = [car.y for car in cars] # y-verdi for alle lyskryss
    s1 = [car.go for car in cars] # stop or go
    scatter(xl, yl, c = sl, cmap = cm.RdYlGn) # tegner noe lyskryssdrit
    scatter(x1, y1, c = s1, cmap = cm.cool) # tegner noe bildrit
    
    title('t = ' + str(time)) # D'Tittel da


def update():
    global time, cars, envir

    time += 1
    
    if (time+3)%50 == 0: # for hvert 25. "sekund", flipper lysene for lys 0, med shiftet start
        if lightAgents[0].current_state == "red":
            lightAgents[0].current_state = "green"
        else:
            lightAgents[0].current_state = "red"
            
    if (time+20)%50 == 0: # for hvert 25. "sekund", flipper lysene for lys 1, med shiftet start
        if lightAgents[1].current_state == "red":
            lightAgents[1].current_state = "green"
        else:
            lightAgents[1].current_state = "red"
    
    # Hvis liste av biler ikke har biler, eller siste bilen ikke befinner seg på startsted spawn biler
    if len(cars)==0 or (cars[-1].y != rd1Ypos[0]
                           and random() < carSpawnProb):
        car = Car(rd1Xpos[0], rd1Ypos[0]) 
        cars.append(car) # Spawn new car
    
    for car in cars:
        car_pos = (car.x, car.y)
        out_of_bounds = [(0, 10), (0, 40), (40, 0), (50, 10), (50, 40), (40, 50)]
        if car_pos in out_of_bounds: #cars[0].y == rd1Ypos[1] or cars[0].x == rd1Xpos[1]: # Despawn out of bounds car
            cars.remove(car)
      
    cars[0].go = True    # Sets car to go
        
    for i in range(len(cars)-1):
        if (cars[i].y - cars[i+1].y) < 2:
            cars[i+1].go = False
        else:
            cars[i+1].go = True
    
    for i, car in enumerate(cars):
        if ((car.y == lightYpos[0]-1 and lightAgents[0].current_state == "red") 
        or (car.y == lightYpos[1]-1 and lightAgents[1].current_state == "red")):
            car.go = False # Stop before red lights
        
    
    for car in cars:
        for lit in range(len(lightXpos)):
            if car.y ==  lightYpos[lit] and car.x ==  lightXpos[lit]: 
                car.set_traveling_direction()

    for car in cars:
        # legg til sjekker om posisjon må stoppes i update_position
        if car.go:
            car.update_position()

pycxsimulator.GUI().start(func=[initialize, observe, update])

#PROBLEM I KODEN!:
'''
ser ut til at når man nå kjører koden, fungerer det meste bra, MEN
Etterhvert er det kun en og en (eller liten gruppe) bil som kan bevege seg, altså ikke alle
'''
