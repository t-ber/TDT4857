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
from intersection_manager import IM


width = 23
height = 38

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
    global time, envir, lightAgents, cars, roads, IDIOT_IM
    time = 0
    cars = []
    lightAgents = []
    roads = []
    # Kode som tegner veiene svart
    envir = zeros([height, width])


    # rngs_lane_1 = Lane(20, 20, 0, 20, "south",envir)
    # rngs_lane_2 = Lane(40, 40, 0, 20, "south",envir)
    # rngs = [rngs_lane_1, rngs_lane_2]
    # road_north_going_south  = Road("south", rngs, [], is_spawner=True)
    # roads.append(road_north_going_south)
    
    # rmgs_lane_1 = Lane(20, 20, 20, 40, "south",envir)
    # rmgs_lane_2 = Lane(40, 40, 20, 40, "south",envir)
    # rmgs = [rmgs_lane_1, rmgs_lane_2]
    # road_middle_going_south = Road("south", rmgs, [], False)
    # roads.append(road_middle_going_south)

    # rngs_lane_1.connect_road(road_middle_going_south)
    # rngs_lane_2.connect_road(road_middle_going_south)

    # rsmgs_lane_1 = Lane(20, 20, 40, 60, "south",envir)
    # rsmgs_lane_2 = Lane(40, 40, 40, 60, "south",envir)
    # rsmgs = [rsmgs_lane_1, rsmgs_lane_2]
    # road_south_middle_going_south = Road("south", rsmgs, [], False)
    # roads.append(road_south_middle_going_south)

    # rmgs_lane_1.connect_road(road_south_middle_going_south)
    # rmgs_lane_2.connect_road(road_south_middle_going_south)
    
    # rsgs_lane_1 = Lane(20, 20, 60, 100, "south",envir)
    # rsgs_lane_2 = Lane(40, 40, 60, 100, "south",envir)
    # rsgs = [rsgs_lane_1, rsgs_lane_2]
    # road_south_going_south = Road("south", rsgs, [], is_spawner=False, is_despawner=True)
    # roads.append(road_south_going_south)

    # rsmgs_lane_1.connect_road(road_south_going_south)
    # rsmgs_lane_2.connect_road(road_south_going_south)

    # traffic_light_rngs_s_1_2 = Traffic_light(30, 20)
    # traffic_light_rngs_e_2 = Traffic_light(40, 20)
    # traffic_light_rmgs_s_1_2 = Traffic_light(30, 50)
    
    # lightAgents.append(traffic_light_rngs_s_1_2)
    # lightAgents.append(traffic_light_rngs_e_2)
    # lightAgents.append(traffic_light_rmgs_s_1_2)

    # rsgn_lane_1 = Lane(60, 60, 100, 80, "north",envir)
    # rsgn_lane_2 = Lane(80, 80, 100, 80, "north",envir)
    # rsgn = [rsgn_lane_1, rsgn_lane_2]
    # road_south_going_north = Road("north", rsgn, [], is_spawner=True)
    # roads.append(road_south_going_north)

    # traffic_light_rsgn_1_2 = Traffic_light(70, 80)
    # lightAgents.append(traffic_light_rsgn_1_2)

    # rmgn_lane_1 = Lane(60, 60, 80, 60, "north",envir)
    # rmgn_lane_2 = Lane(80, 80, 80, 60, "north",envir)
    # rmgn = [rmgn_lane_1, rmgn_lane_2]
    # road_middle_going_north = Road("north", rmgn, [])
    # roads.append(road_middle_going_north)
    # rsgn_lane_1.connect_road(road_middle_going_north)
    # rsgn_lane_2.connect_road(road_middle_going_north)

    # rsge_lane = Lane(80, 100, 60, 60, "east",envir)
    # road_south_going_east = Road("east", [rsge_lane], [], is_despawner=True)
    # roads.append(road_south_going_east)
    # rmgn_lane_2.connect_road(road_south_going_east)

    # rmege_lane = Lane(40, 80, 40, 40, "east",envir)
    # road_middle_east_going_east = Road("east", [rmege_lane])
    # roads.append(road_middle_east_going_east)
    # rmgs_lane_2.connect_road(road_middle_east_going_east)

    # rnege_lane = Lane(80, 100, 40, 40, "east",envir)
    # road_north_east_going_east = Road("east", [rnege_lane], [], is_despawner=True)
    # roads.append(road_north_east_going_east)
    # rmege_lane.connect_road(road_north_east_going_east)

    # rsegw_lane = Lane(100, 30, 50, 50, "west",envir)
    # road_south_east_going_west = Road("west", [rsegw_lane], is_spawner=True)
    # roads.append(road_south_east_going_west)
    # traffic_light_rsegw = Traffic_light(80, 50)
    # lightAgents.append(traffic_light_rsegw)
    # rsegw_lane.connect_road(road_south_going_south)

    # rmngn_lane_1 = Lane(60, 60, 60, 40, "north",envir)
    # rmngn_lane_2 = Lane(80, 80, 60, 40, "north",envir)
    # rmngn = [rmngn_lane_1, rmngn_lane_2]
    # road_middle_north_going_north = Road("north", rmngn, [])
    # road.append(road_middle_north_going_north)
    # rmgn_lane_1.connect_road(road_middle_north_going_north)

    # rmnngn_lane_1 = Lane(70, 70, 40, 30, "north", envir)
    # road_middle_north_north_going_north = Road("north", [rmnngn_lane_1])
    # roads.append(road_middle_north_north_going_north)
    # rmngn_lane_1.connect_road(road_middle_north_north_going_north)
    # rmngn_lane_2.connect_road(road_middle_north_north_going_north)

    # rnegw_lane = Lane(100, 70, 30, 30, "west", envir)
    # road_north_east_going_west = Road("west", [rnegw_lane], is_spawner=True)

    # rngn_lane = Lane(70, 70, 30, 0, "north",envir)
    # road_north_going_north = Road("north", [rngn_lane], is_despawner=True)
    # roads.append(road_middle_going_north)
    # rmnngn_lane_1.connect_road(road_north_going_north)
    # rnegw_lane.connect_road(road_north_going_north)

    # traffic_light_rmngn_1_2 = Traffic_light(70, 30)
    # lightAgents.append(traffic_light_rmngn_1_2)


    # rngs_lane_1 = Lane(7, 7, 0, 10, "south",envir)
    # rngs_lane_2 = Lane(8, 8, 0, 10, "south",envir)
    # rngs = [rngs_lane_1, rngs_lane_2]
    # rngs_probs = [0.5, 0.5]
    # road_north_going_south  = Road("south", rngs, rngs_probs, is_spawner=True)
    # roads.append(road_north_going_south)

    # rmgs_lane_1 = Lane(7, 7, 14, 24, "south",envir)
    # rmgs_lane_2 = Lane(8, 8, 14, 24, "south",envir)
    # rmgs = [rmgs_lane_1, rmgs_lane_2]
    # rmgs_probs = [0.5, 0.5]
    # road_middle_going_south = Road("south", rmgs, rmgs_probs)
    # roads.append(road_middle_going_south)

    # rngs_lane_1.connect_road(road_middle_going_south)
    # rngs_lane_2.connect_road(road_middle_going_south)


    rngn_lane = Lane(10, 10, 10, 0, "north", envir)
    rngn = [rngn_lane]
    rngn_probs = [1]
    road_north_going_north = Road("north", rngn, rngn_probs, is_despawner=True)
    roads.append(road_north_going_north)

    rngw_lane = Lane(22, 12, 11, 11, "west", envir)
    rngw = [rngw_lane]
    rngw_probs = [1]
    road_north_going_west = Road("west", rngw, rngw_probs, is_spawner=True)
    roads.append(road_north_going_west)

    rngw_lane.connect_road(road_north_going_north)
    traffic_light_rngw_n = Traffic_light(11, 11)
    lightAgents.append(traffic_light_rngw_n)
    rngw_lane.add_traffic_light('north', traffic_light_rngw_n)

    IDIOT_IM = IM()
    IDIOT_IM.add_trafic_light(traffic_light_rngw_n)


def observe():
    cla() # kanskje clearer drit
    imshow(envir, cmap = cm.Greys, vmin = 0, vmax = 1) # shows ilustration
    axis('image')
    xl = [ag.x for ag in lightAgents] # x-verdi for alle lyskryss
    yl = [ag.y for ag in lightAgents] # y-verdi for alle lyskryss
    sl = [ag.current_state for ag in lightAgents] # rødt eller grønt
    x1 = [car.x for car in cars] # x-verdi for alle biler
    y1 = [car.y for car in cars] # y-verdi for alle biler
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
        popped_cars_list = road.trim_lane_ends()
        for popped_car in popped_cars_list:
            cars.remove(popped_car)
        new_car = road.spawn_car_cond()
        if new_car != False: # Hvis bil faktisk ble spawnet
            print('Car spawned')
            cars.append(new_car)
    
    for car in cars:
        car.update()

    IDIOT_IM.update(time)

    time += 1
    

pycxsimulator.GUI().start(func=[initialize_elgeseter, observe, update])

#PROBLEM I KODEN!:
'''
ser ut til at når man nå kjører koden, fungerer det meste bra, MEN
Etterhvert er det kun en og en (eller liten gruppe) bil som kan bevege seg, altså ikke alle
'''
