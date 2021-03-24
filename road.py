import random
from lights import Traffic_light
import math

from car import Car
from lane import Lane

class Road:
    def __init__(self, direction, lanes=[], laneprobs=[], is_spawner=False, is_despawner=False, avg_traffic = 10):
        self.lanes = lanes
        self.laneprobs = laneprobs
        self.is_spawner = is_spawner
        self.is_despawner = is_despawner
        self.direction = direction
        self.avg_traffic = avg_traffic
    
    def is_occupied(self) -> bool: # Returns False if at least one of the lanes is free
        for lane in self.lanes:
            if not lane.is_occupied():
                return False
        return True

    def assign_lane(self): # Antar at det i det hele tatt finnes en fil som er ledig
        lane_prob_adj = self.laneprobs.copy() # True/False liste avhengig om filen er ledig
        for idx, lane in enumerate(self.lanes):
            if lane.is_occupied():
                lane_prob_adj[idx] = 0
        return random.choices(self.lanes, weights=lane_prob_adj)[0] # Returnerer fil-objektet som er blitt tildelt
    
    def trim_lane_ends(self): # Fjerner alle biler som er ved slutten av veien hvis veien er en despawner
        popped_cars_list = []
        if self.is_despawner:
            for lane in self.lanes:
                if lane.is_end_occupied():
                    popped_cars_list.append(lane.pop_last_car())
        return popped_cars_list

    def spawn_car(self): # Spawner en bil i assigned lane hvis veien ikke er full
        if self.is_spawner:
            if not self.is_occupied():
                assigned_lane = self.assign_lane()
                spawned_car = Car(assigned_lane.x_start, assigned_lane.y_start, assigned_lane)
                assigned_lane.add_car(spawned_car)
                return spawned_car
        return False

    def spawn_car_cond(self):
        should_spawn_car = True
        return_val = False
        if should_spawn_car:
            return_val = self.spawn_car()
        return return_val # Denne vil være en bil hvis veien er en spawner og den fant plass til den, False ellers---------------------------------------------------s