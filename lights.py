import itertools

class traffic_light:
    id_iter = itertools.count()

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


    def __init__(self, north_south, east_west, speed_limit, traffic_light_north, traffic_light_south, traffic_light_east, traffic_light_west, size):
        self.size = size
        self.north_south = north_south
        self.east_west = east_west
        self.speed_limit = speed_limit
        self.id = next(traffic_light.id_iter)
        self.traffic_light_north = traffic_light_north
        self.traffic_light_south = traffic_light_south
        self.traffic_light_east = traffic_light_east
        self.traffic_light_west = traffic_light_west

    def ticker_based_light_change(self, is_running):
        i = 0
        while is_running:
            if i % 30:
                # flip lights
                i = 0
            i += 1


# ------------------car arivals-----------------------
    def car_arival_south_going_north(self, car):
        self.cars_from_south_to_go_north.append(car)
    
    def car_arival_south_going_east(self, car):
        self.cars_from_south_to_go_east.append(car)

    def car_arival_south_going_west(self, car):
        self.cars_from_south_to_go_west.append(car)

   
    def car_arival_north_going_south(self, car):
        self.cars_from_north_to_go_south.append(car)
    
    def car_arival_north_going_east(self, car):
        self.cars_from_north_to_go_east.append(car)

    def car_arival_north_going_west(self, car):
        self.cars_from_north_to_go_west.append(car)


    def car_arival_west_going_east(self, car):
        self.cars_from_west_to_go_east.append(car)
    
    def car_arival_west_going_north(self, car):
        self.cars_from_west_to_go_north.append(car)
    
    def car_arival_west_going_south(self, car):
        self.cars_from_west_to_go_south.append(car)


    def car_arival_east_going_west(self, car):
        self.cars_from_east_to_go_west.append(car)

    def car_arival_east_going_north(self, car):
        self.cars_from_east_to_go_north.append(car)

    def car_arival_east_going_south(self, car):
        self.cars_from_east_to_go_south.append(car)

# ---------------------------------------------------

class car:
    speed_limit = 60
    acceleration = 2


    def __init__(self, traffic_light):
        self.speed_limit = traffic_light.speed_limit