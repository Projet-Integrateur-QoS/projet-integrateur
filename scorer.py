from collections import deque
from pretty_printer import pretty_print

class QoSScorer:
    def __init__(self, historic_maxlen, score_function):
        self.score_function = score_function

        self.historic = {
            "A_CPU": deque(maxlen=historic_maxlen),
            "A_RAM": deque(maxlen=historic_maxlen),
            "B_CPU": deque(maxlen=historic_maxlen),
            "B_RAM": deque(maxlen=historic_maxlen),
            "C_CPU": deque(maxlen=historic_maxlen),
            "C_RAM": deque(maxlen=historic_maxlen),
        }
        self.predicted = {
            "A_CPU": 0,
            "A_RAM": 0,
            "B_CPU": 0,
            "B_RAM": 0,
            "C_CPU": 0,
            "C_RAM": 0,
        }

    def update_historic(self, row):
        lat_a, lat_b, lat_c, cpu_a, ram_a, cpu_b, ram_b, cpu_c, ram_c, x_c, y_c = row
        self.historic["A_CPU"].appendleft(float(cpu_a))
        self.historic["A_RAM"].appendleft(float(ram_a))
        self.historic["B_CPU"].appendleft(float(cpu_b))
        self.historic["B_RAM"].appendleft(float(ram_b))
        self.historic["C_CPU"].appendleft(float(cpu_c))
        self.historic["C_RAM"].appendleft(float(ram_c))

    def calculate_score(self):
        for i in self.historic:
            self.predicted[i] = self.score_function(list(self.historic[i]))

        pretty_print(self.historic, self.predicted)

    def run(self, row):
        self.update_historic(row)
        self.calculate_score()
