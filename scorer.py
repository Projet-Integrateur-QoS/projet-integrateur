import os
import requests
import time
import alternate_scorers
from plot import plot
from dotenv import load_dotenv

load_dotenv()

simulator_url = 'http://localhost:' + '8000'


while True:
    time.sleep(int(os.environ['SCORER_INTERVAL']))

    payload = {}

    nodes = requests.get(simulator_url).json()

    scorePrio = {
        " -1" : 1,
        "1-2" : 0.5,
        "2- " : 0.2
    }

    payload = alternate_scorers.peerTrust(nodes,scoreTimePriority=scorePrio)

    plot(payload,"peerTrust/ram",nodes,"ram_score")
    plot(payload,"peerTrust/cpu",nodes,"cpu_score")



    requests.post(simulator_url + '/update_scores', json=payload)
