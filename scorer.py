from collections import deque
import json
from pretty_printer import pretty_print

class QoSScorer:
    def __init__(self, historic_maxlen):
        self.historic = {
            "A": {
                "CPU": deque(maxlen=historic_maxlen),
                "RAM": deque(maxlen=historic_maxlen),
            },
            "B": {
                "CPU": deque(maxlen=historic_maxlen),
                "RAM": deque(maxlen=historic_maxlen),
            },
            "C": {
                "CPU": deque(maxlen=historic_maxlen),
                "RAM": deque(maxlen=historic_maxlen),
            },
        }

    def update_historic(self, row):
        lat_a, lat_b, lat_c, cpu_a, ram_a, cpu_b, ram_b, cpu_c, ram_c, x_c, y_c = row
        self.historic["A"]["CPU"].appendleft(float(cpu_a))
        self.historic["A"]["RAM"].appendleft(float(ram_a))
        self.historic["B"]["CPU"].appendleft(float(cpu_b))
        self.historic["B"]["RAM"].appendleft(float(ram_b))
        self.historic["C"]["CPU"].appendleft(float(cpu_c))
        self.historic["C"]["RAM"].appendleft(float(ram_c))

    def calculate_score(self):
        pretty_print(self.historic)

    def run(self, row):
        self.update_historic(row)
        self.calculate_score()
