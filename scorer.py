import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

simulator_url = 'http://simulator:' + os.environ['SIMULATOR_PORT']


while True:
    time.sleep(int(os.environ['SCORER_INTERVAL']))

    payload = {}

    nodes = requests.get(simulator_url).json()
    for node in nodes:
        payload[node] = {}
        cpu_history = [float(cpu) for cpu in nodes[node]["cpu"]]
        ram_history = [float(ram) for ram in nodes[node]["ram"]]
        cpu_score = round(sum(cpu_history) / len(cpu_history), 2)
        ram_score = round(sum(ram_history) / len(ram_history), 2)
        payload[node]["cpu_score"] = cpu_score
        payload[node]["ram_score"] = ram_score

    requests.post(simulator_url + '/update_scores', json=payload)
