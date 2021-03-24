import itertools
from car import Car



class Traffic_light:
    id = 0
    
    cars_from_south_to_go_north = []
    cars_from_south_to_go_east = []
    cars_from_south_to_go_west = []
    
    cars_from_north_to_go_south = []
    cars_from_north_to_go_east = []
    cars_from_north_to_go_west = []

    cars_from_west_to_go_east = []
    cars_from_west_to_go_north = []
    cars_from_west_to_go_south = []

    cars_from_east_to_go_west = []
    cars_from_east_to_go_north = []
    cars_from_east_to_go_south = []

    ''' 
    def __init__(self, north_south, east_west, speed_limit, traffic_light_north, traffic_light_south, traffic_light_east, traffic_light_west, size):
        self.size = size
        self.north_south = north_south
        self.east_west = east_west
        self.speed_limit = speed_limit
        self.id = Traffic_light.id
        self.current_state = 'red'
        Traffic_light.id += 1
        self.traffic_light_north = traffic_light_north
        self.traffic_light_south = traffic_light_south
        self.traffic_light_east = traffic_light_east
        self.traffic_light_west = traffic_light_west
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = Traffic_light.id
        self.current_state = 'red'
        Traffic_light.id += 1

    def is_green(self):
        pass

    def flip_trafic_light_state(self):
        if self.current_state == 'red':
            self.current_state = 'green'
        else:
            self.current_state = 'red'


    def ticker_based_light_change(self, is_running):
        i = 0
        while is_running:
            if i % 30 == 0:
                # flip lights
                self.flip_trafic_light_state()
                i = 0
            i += 1

# ------------------car arivals-----------------------
    def car_arival(car):
        came_from = car.came_from
        direction = car.traveling_direction

# ---------------------------------------------------


'''
test = Car()

test.set_traveling_direction()
print("going to: " + test.traveling_direction)
print("came from: " + test.came_from)
test.set_traveling_direction()
print("going to: " + test.traveling_direction)
print("came from: " + test.came_from)
test.set_traveling_direction()
print("going to: " + test.traveling_direction)
print("came from: " + test.came_from)
test.set_traveling_direction()
print("going to: " + test.traveling_direction)
print("came from: " + test.came_from)
test.set_traveling_direction()
print("going to: " + test.traveling_direction)
print("came from: " + test.came_from)
'''
