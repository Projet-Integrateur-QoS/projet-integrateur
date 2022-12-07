from collections import deque
from pretty_printer import pretty_print

class QoSScorer:
    def __init__(self, history_maxlen, score_function):
        self.score_function = score_function

        self.last_raw_read = ''

        self.history = {
            "A": deque(maxlen=history_maxlen),
            "B": deque(maxlen=history_maxlen),
            "C": deque(maxlen=history_maxlen),
        }
        self.prediction = {
            "A": (0, 0),
            "B": (0, 0),
            "C": (0, 0),
        }
        self.last_prediction = dict(self.prediction)

    def update_history(self, row):
        self.last_raw_read = row
        lat_a, lat_b, lat_c, cpu_a, ram_a, cpu_b, ram_b, cpu_c, ram_c, x_c, y_c = self.last_raw_read
        self.history["A"].appendleft((float(cpu_a), float(ram_a)))
        self.history["B"].appendleft((float(cpu_b), float(ram_b)))
        self.history["C"].appendleft((float(cpu_c), float(ram_c)))

    def calculate_score(self):
        self.last_prediction = dict(self.prediction)

        for i in self.history:
            self.prediction[i] = self.score_function(list(self.history[i]))

        pretty_print(self.history, self.last_prediction)

    def get_last_processed(self):
        if not self.last_raw_read:
            return {"error": "no data yet"}
        lat_a, lat_b, lat_c, cpu_a, ram_a, cpu_b, ram_b, cpu_c, ram_c, x_c, y_c = self.last_raw_read
        return {
            "lat_a" : lat_a,
            "lat_b" : lat_b,
            "lat_c" : lat_c,
            "cpu_a" : cpu_a,
            "cpu_a_pred" : self.prediction["A"][0],
            "ram_a" : ram_a,
            "ram_a_pred" : self.prediction["A"][1],
            "cpu_b" : cpu_b,
            "cpu_b_pred" : self.prediction["B"][0],
            "ram_b" : ram_b,
            "ram_b_pred" : self.prediction["B"][1],
            "cpu_c" : cpu_c,
            "cpu_c_pred" : self.prediction["C"][0],
            "ram_c" : ram_c,
            "ram_c_pred" : self.prediction["C"][1],
            "x_c" : x_c,
            "y_c" : y_c
        }

    def run(self, row):
        self.update_history(row)
        self.calculate_score()
