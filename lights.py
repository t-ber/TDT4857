import itertools
from car import Car



class Traffic_light:
    def __init__(self, x, y, group = 1):
        self.x = x
        self.y = y
        self.group = group
        if group == 1: 
            self.current_state = 'red'
        elif group == 2:
            self.current_state = 'green'

    def is_green(self):
        return self.current_state == 'green'

    def flip_trafic_light_state(self):
        if self.current_state == 'red':
            self.current_state = 'green'
        else:
            self.current_state = 'red'




