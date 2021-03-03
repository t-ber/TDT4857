import numpy as np
import random

class Car:

    def __init__(self, x, y):#, lane): # Road som f.eks. klasse
        self.go = True
        self.x = x
        self.y = y
        #self.current_lane = lane
        self.traveling_direction = "south" #lane.direction
        self.next_direction = "" #lane.next_direction
        self.directions = ["north", "south", "east", "west"]

    #def spawn_car(self):
        
        # Dette kan løses med liste av mulige spawn locations x og y samt hvor de kan kjøre herfra
        # F.eks. [[x=0, y=0, "south"], [x=0, y=0, "east"], [x=100, y=100, "north"], [x=0, y=0, "west"], etc.]
        # lag deretter en funksjon def random(0 til 1) * lengden på listen av mulige plasser og retninger over
        # , og roof/floor denne
        # Da vil man få en random spawn på ulike plasser

    def _car_ahead(self) -> bool:
        pass

    def _at_intersection(self) -> bool:
        pass


    # def _should_stop(self) -> bool:
    #     if self._car_ahead() or 

    def update_position(self):
        if self.traveling_direction == "north":
            self.y -= 1
        elif self.traveling_direction == "south":
            self.y += 1
        elif self.traveling_direction == "east":
            self.x += 1
        elif self.traveling_direction == "west":
            self.x -= 1

    def get_direction(self):
        return self.traveling_direction
        
    def set_direction(self, direction):
        self.traveling_direction = direction

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_traveling_direction(self):
        traveled_direction = self.traveling_direction
        if traveled_direction == "north": self.came_from = "south"
        if traveled_direction == "south": self.came_from = "north"
        if traveled_direction == "east": self.came_from = "west"
        if traveled_direction == "west": self.came_from = "east"
        possible_directions = self.directions.copy()
        possible_directions.remove(self.came_from)
        self.traveling_direction = possible_directions[random.randint(0,2)]
