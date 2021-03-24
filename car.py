import numpy as np
import random

class Car:

    def __init__(self, x, y, lane):#, lane): # Road som f.eks. klasse
        self.go = True
        self.lane = lane
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


    def _should_stop(self) -> bool:
        if self.lane.is_first_car(self): # Hvis først, stopp kun hvis du er ved lyskrysset og det er rødt
            if self.lane.is_end_pos(self.x ,self.y):
                if self.lane.is_signal_green(self.next_direction):
                    if self.lane.connected_roads[self.next_direction].is_occupied(): 
                        return True # Hvis den kan kjøre i lyskrysset men det er fullt i veien den skal i
                    else:
                        return False # Hvis den kan kjøre i lyskrysset og det er ledig der den skal
                else:
                    return True # Hvis den er ved enden og det er rødt lys
            else:
                return False # Hvis den er den først bilen og den ikke er ved enden
        else: # Hvis man ikke er den første bilen i filen, stopp kun hvis det er kort til bilen foran
            if self.go:
                if self.lane.get_distance_to_next_car(self) < 2:
                    return True # Beveger på seg og bilen foran er rett foran
            else:
                if self.lane.get_distance_to_next_car(self) < 3:
                    return True # Står stille og bilen foran er nærme
            return False # god avstand til bilen foran
        

    def update_position(self):
        if self.traveling_direction == "north":
            self.y -= 1
        elif self.traveling_direction == "south":
            self.y += 1
        elif self.traveling_direction == "east":
            self.x += 1
        elif self.traveling_direction == "west":
            self.x -= 1

    def move_car_to_new_lane(self, new_lane):
        self.lane.remove_car(self)
        self.lane = new_lane
        self.lane.add_car(self)
    
    def set_next_direction(self):
        if not bool(self.lane.exit_dirs):
            return 'south'
        direction_chances = self.lane.exit_dirs_probs
        chances = list(direction_chances.values())
        self.next_direction = random.choices(list(direction_chances.keys()), weights=chances, k=1)[0] # Returnerer i utgangspunktet en liste selv om det bare er ett objekt

    def choose_new_lane(self):
        new_road = self.lane.connected_roads[self.next_direction]
        new_lane = new_road.assign_lane()
        self.move_car_to_new_lane(new_lane)
        self.set_direction(self.next_direction)


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

    def update(self):
        if self._should_stop():
            self.go = False
            return
        else:
            self.go = True
        
        if self.lane.is_end_pos(self.x, self.y):
            self.choose_new_lane()
            return
        self.update_position()
        