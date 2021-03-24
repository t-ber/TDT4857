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
from lane import Lane


width = 100
height = 100

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
    
    
def initialize_elgeseter():
    global time, envir, lightAgents, cars, roads
    cars = []
    lightAgents = []
    # Kode som tegner veiene svart
    envir = zeros([height, width])


    rngs_lane_1 = Lane(20, 20, 0, 20, "south",envir)
    rngs_lane_2 = Lane(40, 40, 0, 20, "south",envir)
    rngs = [rngs_lane_1, rngs_lane_2]
    road_north_going_south  = Road("south", rngs, [], True)
    
    rmgs_lane_1 = Lane(20, 20, 20, 40, "south",envir)
    rmgs_lane_2 = Lane(40, 40, 20, 40, "south",envir)
    rmgs = [rmgs_lane_1, rmgs_lane_2]
    road_middle_going_south = Road("south", rmgs, [], False)

    rngs_lane_1.connected_roads(road_middle_going_south)
    rngs_lane_2.connected_roads(road_middle_going_south)

    rsmgs_lane_1 = Lane(20, 20, 40, 60, "south",envir)
    rsmgs_lane_2 = Lane(40, 40, 40, 60, "south",envir)
    rsmgs = [rsmgs_lane_1, rsmgs_lane_2]
    road_south_middle_going_south = Road("south", rsmgs, [], False)

    rmgs_lane_1.connected_roads(road_south_middle_going_south)
    rmgs_lane_2.connected_roads(road_south_middle_going_south)
    
    rsgs_lane_1 = Lane(20, 20, 60, 100, "south",envir)
    rsgs_lane_2 = Lane(40, 40, 60, 100, "south",envir)
    rsgs = [rsgs_lane_1, rsgs_lane_2]
    road_south_going_south = Road("south", rsgs, [], False, True)

    rsmgs_lane_1.connected_roads(road_south_going_south)
    rsmgs_lane_2.connected_roads(road_south_going_south)

    traffic_light_rngs_s_1_2 = Traffic_light(30, 20)
    traffic_light_rngs_e_2 = Traffic_light(40, 20)
    traffic_light_rmgs_s_1_2 = Traffic_light(30, 50)
    
    lightAgents.append(traffic_light_rngs_s_1_2)
    lightAgents.append(traffic_light_rngs_e_2)
    lightAgents.append(traffic_light_rmgs_s_1_2)

    rsgn_lane_1 = Lane(60, 60, 100, 80, "north",envir)
    rsgn_lane_2 = Lane(80, 80, 100, 80, "north",envir)
    rsgn = [rsgn_lane_1, rsgn_lane_2]
    road_south_going_north = Road("north", rsgn, [], True)

    traffic_light_rsgn_1_2 = Traffic_light(70, 80)
    lightAgents.append(traffic_light_rsgn_1_2)

    rmgn_lane_1 = Lane(60, 60, 80, 60, "north",envir)
    rmgn_lane_2 = Lane(80, 80, 80, 60, "north",envir)
    rmgn = [rmgn_lane_1, rmgn_lane_2]
    road_middle_going_north = Road("north", rmgn, [], False)
    rsgn_lane_1.connected_roads(road_middle_going_north)
    rsgn_lane_2.connected_roads(road_middle_going_north)

    rsge_lane = Lane(80, 100, 60, 60, "east",envir)
    road_south_going_east = Road("east", [rsge_lane], [], False, True)
    rmgn_lane_2.connected_roads(road_south_going_east)

    rmege_lane = Lane(40, 80, 40, 40, "east",envir)
    road_middle_east_going_east = Road("east", [rmege_lane])
    rmgs_lane_2.connected_roads(road_middle_east_going_east)

    rnege_lane = Lane(80, 100, 40, 40, "east",envir)
    road_north_east_going_east = Road("east", [rnege_lane], [], False, True)
    rmege_lane.connected_roads(road_north_east_going_east)

    rsegw_lane = Lane(100, 30, 50, 50, "west",envir)
    road_south_east_going_west = Road("west", [rsegw_lane], is_spawner=True)
    traffic_light_rsegw = Traffic_light(80, 50)
    lightAgents.append(traffic_light_rsegw)
    rsegw_lane.connected_roads(road_south_going_south)

    rmngn_lane_1 = Lane(60, 60, 60, 40, "north",envir)
    rmngn_lane_2 = Lane(80, 80, 60, 40, "north",envir)
    rmngn = [rmngn_lane_1, rmngn_lane_2]
    road_middle_north_going_north = Road("north", rmngn, [], False, False)
    rmgn_lane_1.connected_roads(road_middle_north_going_north)

    rmnngn_lane_1 = Lane(70, 70, 40, 30, "north", envir)
    road_middle_north_north_going_north = Road("north", [rmnngn_lane_1])
    rmngn_lane_1.connected_roads(road_middle_north_north_going_north)
    rmngn_lane_2.connected_roads(road_middle_north_north_going_north)

    rnegw_lane = Lane(100, 70, 30, 30, "west", envir)
    road_north_east_going_west = Road("west", [rnegw_lane], is_spawner=True)

    rngn_lane = Lane(70, 70, 30, 0, "north",envir)
    road_north_going_north = Road("north", [rngn_lane], is_despawner=True)
    rmnngn_lane_1.connected_roads(road_north_going_north)
    rnegw_lane.connected_roads(road_north_going_north)

    traffic_light_rmngn_1_2 = Traffic_light(70, 30)
    lightAgents.append(traffic_light_rmngn_1_2)






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
    global time, cars, roads, envir

    # Gitt av vi har en list over alle veiene
    for road in roads:
        road.trim_lane_ends()
        new_car = road.spawn_car_cond()
        if new_car != False: # Hvis bil faktisk ble spawnet
            cars.append(new_car)
    
    time += 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for car in cars:
        for lit in range(len(lightXpos)):
            if car.y ==  lightYpos[lit] and car.x ==  lightXpos[lit]: 
                car.set_traveling_direction()

    for car in cars:
        # legg til sjekker om posisjon må stoppes i update_position
        if car.go:
            car.update_position()

pycxsimulator.GUI().start(func=[initialize_elgeseter, observe, update])

#PROBLEM I KODEN!:
'''
ser ut til at når man nå kjører koden, fungerer det meste bra, MEN
Etterhvert er det kun en og en (eller liten gruppe) bil som kan bevege seg, altså ikke alle
'''
