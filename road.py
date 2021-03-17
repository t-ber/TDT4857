from pygame import gfxdraw
from lights import Traffic_light
import math

class Road:

    def __init__(self, lanes=[], laneprobs=[], is_spawner=False):
        self.lanes = lanes
        self.laneprobs = laneprobs
        self.is_spawner = is_spawner
    
    def is_occupied(self) -> bool: # Returns False if at least one of the lanes is free
        for lane in self.lanes:
            if not lane.occupied:
                return False
        return True

    def assign_lane(self):
        pass