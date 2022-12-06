import csv
from scorer import QoSScorer
from score_functions import mean

def simulate_data_streaming(func_to_simulate, row_limit):
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = next(reader)
        n = 0
        for row in reader:
            func_to_simulate(row)
            n += 1
            if n > row_limit:
                break

scorer = QoSScorer(historic_maxlen=3, score_function=mean)
simulate_data_streaming(scorer.run, row_limit=10)