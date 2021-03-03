from lights import Traffic_light
import numpy as np

class Lane:
    def __init__(self, x_min, x_max, y_min, y_max, direction):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.traffic_lights = []
        self.cars = []
        self.direction = direction
        pass
    
    

    def add_traffic_light(self, traffic_light): # Noe kode er blitt fjernet og lagt til her, er ikke som den var
        self.traffic_lights.append(traffic_light)
        for car_index, car in enumerate(self.cars):
                if car_index == 0:
                    car.go = True
                else: 
                    prev_car_index = car_index - 1
                    if self.get_distance_to_car(car, self.cars[prev_car_index]) >= 2:
                        car.go = True

    def get_distance_to_next_car(self, car1, car2):
        x_distance = car2.x - car1.x
        y_distance = car2.y - car1.y
        distance = np.sqrt(y_distance**2 + x_distance**2)
        return distance

    def get_distance_to_light(car, traffic_light):
        x_light = traffic_light.x
        y_light = traffic_light.y
        x_car = car.x
        y_car = car.y
        return np.sqrt((x_light-x_car)**2 + (y_light-y_car)**2)