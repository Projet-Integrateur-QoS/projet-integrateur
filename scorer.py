import os
import requests
import time
import trustman
import maths_scorer as ms
from plot import plot
from plot import remove_file
from dotenv import load_dotenv
from vizu import figure

remove_file("plot")

load_dotenv()

simulator_url = 'http://simulator:' + os.environ['SIMULATOR_PORT']

figure()

while True:
    time.sleep(int(os.environ['SCORER_INTERVAL']))

    payload = {}

    nodes = requests.get(simulator_url).json()

    payload = ms.maths(nodes)[0]
    plot(payload, "moyenne/cpu", nodes, "cpu_score_moy")
    plot(payload, "moyenne/ram", nodes, "ram_score_moy")

    payload = ms.maths(nodes)[1]
    plot(payload, "mediane/cpu", nodes, "cpu_score_med")
    plot(payload, "mediane/ram", nodes, "ram_score_med")

    payload = ms.maths(nodes)[2]
    plot(payload, "iqv/cpu", nodes, "cpu_score_iqv")
    plot(payload, "iqv/ram", nodes, "ram_score_iqv")

    payload = trustman.Trustman_Scorer(nodes)
    plot(payload, "trustman/cpu", nodes, "cpu_score")
    plot(payload, "trustman/ram", nodes, "ram_score")

    requests.post(simulator_url + '/update_scores', json=payload)
