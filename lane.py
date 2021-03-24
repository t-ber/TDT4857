from lights import Traffic_light
import numpy as np

class Lane:
    def __init__(self, x_start, x_end, y_start, y_end, direction, envir):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.traffic_lights = {} # Kan være greit med en dictionary, traffic_lights[direction] = traffic_light object
        self.cars = []
        self.connected_roads = {} # Også som dict. connected_roads[exit_direction] = road object   
        self.direction = direction
        self.draw_self(envir)
        self.exit_dirs = {}
        self.exit_dirs_probs = {}
        pass

    def is_occupied(self) -> bool:
        if len(self.cars) != 0:
            return self.cars[0].get_position() == (self.x_start, self.y_start) # Sjekker om bilen bakerst i filen ligger bakerst i filen 
        else:
            return False # Filen er ledig hvis det ikke er noen biler på den

    def is_end_occupied(self) -> bool:
        if len(self.cars) != 0:
            return self.cars[-1].get_position() == (self.x_end, self.y_end) # Sjekker om bilen forrerst i filen ligger forrerst i filen 
        else:
            return False # Filen er ledig hvis det ikke er noen biler på den

    def add_traffic_light(self, direction, traffic_light): # Noe kode er blitt fjernet og lagt til her, er ikke som den var
        self.traffic_lights[direction] = traffic_light

    def is_signal_green(self, direction):
        return self.traffic_lights[direction].is_green()

    def add_car(self, car): # Legger til bilen i starten av listen
        self.cars.insert(0, car)
        car.x = self.x_start
        car.y = self.y_start
        car.traveling_direction = self.direction
        car.set_next_direction()

    def remove_car(self, car):
        self.cars.remove(car)

    def pop_last_car(self):
        print('Despawned car')
        return self.cars.pop(-1)

    def trim_end_pos(self):
        if self.is_end_occupied():
            return self.pop_last_car()
        else:
            return False

    def is_first_car(self, asking_car):
        if self.cars.index(asking_car) == len(self.cars)-1:
            return True
        else:
            return False

    def get_distance_to_next_car(self, asking_car):
        asking_index = self.cars.index(asking_car)
        next_car = self.cars[asking_index+1]
        x_dist = np.abs(next_car.x - asking_car.x)
        y_dist = np.abs(next_car.y - asking_car.y)
        return x_dist+y_dist

    def connect_road(self, road):
        self.connected_roads[road.direction] = road 
        self.exit_dirs, self.exit_dirs_probs = self.update_exit_dirs()
    
    def get_connected_roads(self): # Returnerer liste over connected roads
        return list(self.connected_roads.values())

    def update_exit_dirs(self):
        exit_dirs = set()
        exit_dirs_probs = {}
        for road in self.get_connected_roads():
            exit_dirs.add(road.direction)
            exit_dirs_probs[road.direction] = road.avg_traffic
        factor=1.0/sum(exit_dirs_probs.values())
        for direction in exit_dirs_probs:
            exit_dirs_probs[direction] = exit_dirs_probs[direction]*factor # Normaliserer verdier for å gi sannsynligheter
        return exit_dirs, exit_dirs_probs

    def is_end_pos(self, x, y): # For bilens bruk, for å vite om den er ved et lyskryss eller ikke 
        if (x == self.x_end) and (y == self.y_end):
            return True
        else:
            return False
    
    def draw_self(self, envir):
        if self.direction == "north":
            envir[self.y_end:self.y_start+1, self.x_end] = 1
        elif self.direction == "south":
            envir[self.y_start:self.y_end+1, self.x_end] = 1
        elif self.direction == "east":
            envir[self.y_end, self.x_start:self.x_end+1] = 1
        elif self.direction == "west":
            envir[self.y_end, self.x_end:self.x_start+1] = 1
    
            







    # Lyskryss sjekk kode. hvis grønt (ikke nevnt i kode, men er slik, kanskje) -> sjekk om bil er forrerste bil. Er det det, kjør, er det ikke det -> sjekk avstand til bil foran. Er avstanden lang nok -> kjør
    '''
        for car_index, car in enumerate(self.cars):
                if car_index == 0:
                    car.go = True
                else: 
                    prev_car_index = car_index - 1
                    if self.get_distance_to_car(car, self.cars[prev_car_index]) >= 2:
                        car.go = True
    '''
