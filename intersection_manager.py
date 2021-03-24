
from lights import Traffic_light


class IM:
    def __init__(self):
        self.traffic_lights = []

    def add_trafic_light(self, trafic_light):
        self.traffic_lights.append(trafic_light)

    def update(self, time):
        for light in self.traffic_lights:
            if time % 25 == 0:
                if light.current_state == 'green':
                    light.current_state = 'red'
                else:
                    light.current_state = 'green'
