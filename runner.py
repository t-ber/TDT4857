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


def check_if_red_light(car):
    for light in lightAgents:
        xL_dist = abs(car.x - light.x)
        yL_dist = abs(car.y - light.y)
        if np.sqrt(xL_dist**2 + yL_dist**2) -1 == 0 and light.current_state == "red":
            return True
    return False
    #if ((car.y == lightAgents[0].y-1 and lightAgents[0].current_state == "red") 
    #    or (car.y == lightAgents[1].y-1 and lightAgents[1].current_state == "red")):
    #        return True
    #else:
    #    return False

def get_distance_between_cars(car_1, car_2):
    y_distance = abs(car_1.y - car_2.y)
    x_distance = abs(car_1.x - car_2.x)
    distance = np.sqrt(y_distance**2 + x_distance**2) 
    return distance

def update():
    global time, cars, envir

    time += 1

    for i, light in enumerate(lightAgents):
        if (time+10*i)%50 == 0:
            if light.current_state == "red":
                light.current_state = "green"
            else:
                light.current_state = "red"
    '''
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
    '''
    # Hvis liste av biler ikke har biler, eller siste bilen ikke befinner seg på startsted spawn biler
    if len(cars)==0 or (cars[-1].y != rd1Ypos[0]
                           and random() < carSpawnProb):
        car = Car(rd1Xpos[0], rd1Ypos[0]) 
        cars.append(car) # Spawn new car
    
    for car in cars:
        car_pos = (car.x, car.y)
        out_of_bounds = [(0, 10), (10, -1), (10, 50), (0, 40), (40, 0), (50, 10), (50, 40), (40, 50)]
        if car_pos in out_of_bounds: #cars[0].y == rd1Ypos[1] or cars[0].x == rd1Xpos[1]: # Despawn out of bounds car
            cars.remove(car)
      
    cars[0].go = True    # Sets car to go

    # Controls cars not to collide from behind    
    # Controls cars not to collide from behind    
    for i in range(len(cars)):
        #radiusL1 = math.sqrt((cars[i].y - lightAgents[0].y)**2 + (cars[i].x - lightAgents[0].x)**2) Problem med dette,
        # på vei ut fra lyskryss stopper biler om det blir rødt på vei inn i kryss
        if check_if_red_light(cars[i]):
            cars[i].go = False
        
        else:
            if i > 0:
                dist = get_distance_between_cars(cars[i], cars[i-1]) #funker ikke, neste bil i listen er ikke nødvendigvis i samme lane
                if dist >= 2:
                    cars[i].go = True
                else:
                    cars[i].go = False
            else:
                cars[i].go = True
        """ if i > 0:
                if (cars[i-1].y - cars[i].y) < 2 and cars[i].traveling_direction == cars[i-1].traveling_direction:
                    cars[i].go = False"""
        # setter ikke her at bil 0 kan kjøre.
            #håper det skjer ved grønt lys
    
    """for i, car in enumerate(cars): #lightYpos burde endres til objektet trafficlight og dets  pos
        if ((car.y == lightYpos[0]-1 and lightAgents[0].current_state == "red") 
        or (car.y == lightYpos[1]-1 and lightAgents[1].current_state == "red")):
            car.go = False # Stop before red lights
            
        else:
            if i < len(cars)-1:
                if (cars[i].y - cars[i+1].y) >= 2:
                    car.go = True    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
