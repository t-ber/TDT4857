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
from intersection_manager import IM, IM2


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
    global time, envir, lightAgents, cars, roads, total_traffic, IDIOT_IM, IDIOT_IM2
    time = 0
    cars = []
    lightAgents = []
    roads = []
    # Kode som tegner veiene svart
    envir = zeros([height, width])
    total_traffic = 0

    # RNGS
    
    rngs_lane_1 = Lane(7, 7, 0, 10, "south", envir)
    rngs_lane_2 = Lane(8, 8, 0, 10, "south", envir)
    rngs = [rngs_lane_1, rngs_lane_2]
    rngs_probs = [0.7, 0.3]
    road_north_going_south = Road("south", rngs, rngs_probs, is_spawner=True)
    roads.append(road_north_going_south)

    traffic_light_rngs_s = Traffic_light(7, 11, group=1)
    lightAgents.append(traffic_light_rngs_s)
    rngs_lane_1.add_traffic_light('south', traffic_light_rngs_s)
    rngs_lane_2.add_traffic_light('south', traffic_light_rngs_s)

    traffic_light_rngs_e = Traffic_light(8, 11, group=2)
    lightAgents.append(traffic_light_rngs_e)
    rngs_lane_2.add_traffic_light('east', traffic_light_rngs_e)

    # RNGN

    rngn_lane = Lane(10, 10, 10, 0, "north", envir)
    rngn = [rngn_lane]
    rngn_probs = [1]
    road_north_going_north = Road("north", rngn, rngn_probs, is_despawner=True)
    roads.append(road_north_going_north)

    # RMGN

    rmgn_lane_1 = Lane(10, 10, 24, 14, "north", envir)
    rmgn_lane_2 = Lane(11, 11, 24, 14, "north", envir)
    rmgn = [rmgn_lane_1 ,rmgn_lane_2]
    rmgn_probs = [0.5, 0.5]
    road_middle_going_north = Road("north", rmgn, rmgn_probs)
    roads.append(road_middle_going_north)

    traffic_light_rmgn_n = Traffic_light(10, 13, group=1)
    lightAgents.append(traffic_light_rmgn_n)
    rmgn_lane_1.add_traffic_light('north', traffic_light_rmgn_n)
    rmgn_lane_2.add_traffic_light('north', traffic_light_rmgn_n)

    # RMGS

    rmgs_lane_2 = Lane(8, 8, 14, 24, "south", envir)
    rmgs_lane_1 = Lane(7, 7, 14, 24, "south", envir)
    rmgs = [rmgs_lane_1 ,rmgs_lane_2]
    rmgs_probs = [0.5, 0.5]
    road_middle_going_south = Road("south", rmgs, rmgs_probs)
    roads.append(road_middle_going_south)

    traffic_light_rmgs_s = Traffic_light(7, 25, group=1)
    lightAgents.append(traffic_light_rmgs_s)
    rmgs_lane_1.add_traffic_light('south', traffic_light_rmgs_s)
    rmgs_lane_2.add_traffic_light('south', traffic_light_rmgs_s)

    # RNGW
    rngw_lane = Lane(22, 12, 11, 11, "west", envir)
    rngw = [rngw_lane]
    rngw_probs = [1]
    road_north_going_west = Road("west", rngw, rngw_probs, is_spawner=True, avg_traffic=500)
    roads.append(road_north_going_west)

    rngw_lane.connect_road(road_north_going_north)
    traffic_light_rngw_n = Traffic_light(11, 11, group=2)
    lightAgents.append(traffic_light_rngw_n)
    rngw_lane.add_traffic_light('north', traffic_light_rngw_n)

    # RNGE
    rnge_lane = Lane(12, 22, 13, 13, "east", envir)
    rnge = [rnge_lane]
    rnge_probs = [1]
    road_north_going_east = Road("east", rnge, rnge_probs, is_despawner=True, avg_traffic=200)
    roads.append(road_north_going_east)

    # RSGW
    rsgw_lane = Lane(22, 12, 25, 25, "west", envir)
    rsgw = [rsgw_lane]
    rsgw_probs = [1]
    road_south_going_west = Road("west", rsgw, rsgw_probs, is_spawner=True, avg_traffic=500)
    roads.append(road_south_going_west)

    traffic_light_rsgw_s = Traffic_light(11, 25, group=2)
    lightAgents.append(traffic_light_rsgw_s)
    rsgw_lane.add_traffic_light('south', traffic_light_rsgw_s)

    # RSGE
    rsge_lane = Lane(12, 22, 27, 27, "east", envir)
    rsge = [rsge_lane]
    rsge_probs = [1]
    road_south_going_east = Road("east", rsge, rsge_probs, is_despawner=True, avg_traffic=500)
    roads.append(road_south_going_east)
    
    # RSGS
    rsgs_lane_1 = Lane(7, 7, 28, 38, "south", envir)
    rsgs_lane_2 = Lane(8, 8, 28, 38, "south", envir)
    rsgs = [rsgs_lane_1, rsgs_lane_2]
    rsgs_probs = [0.5, 0.5]
    road_south_going_south = Road("south", rsgs, rsgs_probs, is_despawner=True)
    roads.append(road_south_going_south)

    # RSGN
    rsgn_lane_1 = Lane(10, 10, 38, 28, "north", envir)
    rsgn_lane_2 = Lane(11, 11, 38, 28, "north", envir)
    rsgn = [rsgn_lane_1, rsgn_lane_2]
    rsgn_probs = [0.5, 0.5]
    road_south_going_north = Road("north", rsgn, rsgn_probs, is_spawner=True)
    roads.append(road_south_going_north)
    
    traffic_light_rsgn_n = Traffic_light(10, 27, group=1)
    lightAgents.append(traffic_light_rsgn_n)
    rsgn_lane_1.add_traffic_light('north', traffic_light_rsgn_n)
    rsgn_lane_2.add_traffic_light('north', traffic_light_rsgn_n)
    rsgn_lane_2.add_traffic_light('east', traffic_light_rsgn_n)

    # Connecting lanes to roads
    rngs_lane_1.connect_road(road_middle_going_south)
    rngs_lane_2.connect_road(road_middle_going_south)
    rngs_lane_2.connect_road(road_north_going_east)
    
    rngw_lane.connect_road(road_north_going_north)
    
    rsgn_lane_1.connect_road(road_middle_going_north)
    rsgn_lane_2.connect_road(road_middle_going_north)
    rsgn_lane_2.connect_road(road_south_going_east)
    
    rsgw_lane.connect_road(road_south_going_south)

    rmgs_lane_1.connect_road(road_south_going_south)
    rmgs_lane_2.connect_road(road_south_going_south)

    rmgn_lane_1.connect_road(road_north_going_north)
    rmgn_lane_2.connect_road(road_north_going_north)

    IDIOT_IM = IM()
    IDIOT_IM.add_trafic_light(traffic_light_rngw_n)
    IDIOT_IM.add_trafic_light(traffic_light_rngs_s)
    IDIOT_IM.add_trafic_light(traffic_light_rngs_e)
    IDIOT_IM.add_trafic_light(traffic_light_rmgn_n)

    IDIOT_IM2 = IM()
    IDIOT_IM2.add_trafic_light(traffic_light_rmgs_s)
    IDIOT_IM2.add_trafic_light(traffic_light_rsgw_s)
    IDIOT_IM2.add_trafic_light(traffic_light_rsgn_n)


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
    
    title('Elgseter simulation using identical signals\nt = ' + str(time)+ ' avg traffic = ' + str(int(total_traffic/(time+1)))) # D'Tittel da


def check_if_red_light(car):
    for light in lightAgents:
        xL_dist = abs(car.x - light.x)
        yL_dist = abs(car.y - light.y)
        if np.sqrt(xL_dist**2 + yL_dist**2) -1 == 0 and light.current_state == "red":
            return True
    return False

def get_distance_between_cars(car_1, car_2):
    y_distance = abs(car_1.y - car_2.y)
    x_distance = abs(car_1.x - car_2.x)
    distance = np.sqrt(y_distance**2 + x_distance**2) 
    return distance

def update():
    global time, cars, roads, envir, total_traffic

    # Gitt av vi har en list over alle veiene
    for road in roads:
        popped_cars_list = road.trim_lane_ends()
        for popped_car in popped_cars_list:
            cars.remove(popped_car)
        new_car = road.spawn_car_cond()
        if new_car != False: # Hvis bil faktisk ble spawnet
            cars.append(new_car)
    
    for car in cars:
        car.update()

    IDIOT_IM.update(time)
    IDIOT_IM2.update(time)

    time += 1
    total_traffic += len(cars)
    

pycxsimulator.GUI().start(func=[initialize_elgeseter, observe, update])

#PROBLEM I KODEN!:
'''
ser ut til at når man nå kjører koden, fungerer det meste bra, MEN
Etterhvert er det kun en og en (eller liten gruppe) bil som kan bevege seg, altså ikke alle
'''
