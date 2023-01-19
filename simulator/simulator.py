from flask import Flask, request, Response
from collections import deque
import json
from custom_encoder import CustomEncoder
import os
from dotenv import load_dotenv

load_dotenv()

HIST_MAXLEN = 20

app = Flask(__name__)
nodes = dict()
car_x = 0
car_y = 0

def create_new_node():
    return {
        'cpu': deque(maxlen=HIST_MAXLEN),
        'ram': deque(maxlen=HIST_MAXLEN),
        'x': None,
        'y': None,
        'cpu_score_trust': None,
        'ram_score_trust': None,
        'cpu_score_moy'  : None,
        'ram_score_moy'  : None,
        'cpu_score_med'  : None,
        'ram_score_med'  : None,
        'cpu_score_iqv'  : None,
        'ram_score_iqv'  : None,
        'cpu_score_geom'  : None,
        'ram_score_geom'  : None,
        'cpu_score_range'  : None,
        'ram_score_range'  : None,
        'cpu_score_harmonic'  : None,
        'ram_score_harmonic'  : None,
        'cpu_score_lehmer'  : None,
        'ram_score_lehmer'  : None,
        'cpu_score_peer'  : None,
        'ram_score_peer'  : None,
        'score_glob'     : None,
    }


@app.route("/new", methods=['POST'])
def new_input():
    payload = request.get_json()
    for node in payload["nodes"]:
        node_id = node['id']
        if node_id not in nodes:
            nodes[node_id] = create_new_node()

        nodes[node_id]['cpu'].appendleft(node['cpu'])
        nodes[node_id]['ram'].appendleft(node['ram'])
        nodes[node_id]['x'] = node['x']
        nodes[node_id]['y'] = node['y']
    payload["car_x"]
    payload["car_y"]

    return payload


@app.route("/", methods=['GET'])
def get():
    raw = json.dumps(nodes, indent=2, cls=CustomEncoder)
    response = Response(raw, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/update_scores", methods=['POST'])
def update_scores():
    payload = request.get_json()
    for node in payload:
        node_id = int(node)
        if node_id not in nodes:
            print("node " + node_id + " not in list, skipping it")
            continue

        nodes[node_id]["cpu_score_trust"] = round(float(payload[node]["cpu_score_trust"]),2)
        nodes[node_id]["ram_score_trust"] = round(float(payload[node]["ram_score_trust"]),2)
        nodes[node_id]["cpu_score_moy"] = round(float(payload[node]["cpu_score_moy"]),2)
        nodes[node_id]["ram_score_moy"] = round(float(payload[node]["ram_score_moy"]),2)
        nodes[node_id]["cpu_score_med"] = round(float(payload[node]["cpu_score_med"]),2)
        nodes[node_id]["ram_score_med"] = round(float(payload[node]["ram_score_med"]),2)
        nodes[node_id]["cpu_score_iqv"] = round(float(payload[node]["cpu_score_iqv"]),2)
        nodes[node_id]["ram_score_iqv"] = round(float(payload[node]["ram_score_iqv"]),2)

        nodes[node_id]["cpu_score_geom"] = round(float(payload[node]["cpu_score_geom"]),2)
        nodes[node_id]["ram_score_geom"] = round(float(payload[node]["ram_score_geom"]),2)
        nodes[node_id]["cpu_score_range"] = round(float(payload[node]["cpu_score_range"]),2)
        nodes[node_id]["ram_score_range"] = round(float(payload[node]["ram_score_range"]),2)
        nodes[node_id]["cpu_score_harmonic"] = round(float(payload[node]["cpu_score_harmonic"]),2)
        nodes[node_id]["ram_score_harmonic"] = round(float(payload[node]["ram_score_harmonic"]),2)
        nodes[node_id]["cpu_score_lehmer"] = round(float(payload[node]["cpu_score_lehmer"]),2)
        nodes[node_id]["ram_score_lehmer"] = round(float(payload[node]["ram_score_lehmer"]),2)
        nodes[node_id]["cpu_score_peer"] = round(float(payload[node]["cpu_score_peer"]),2)
        nodes[node_id]["ram_score_peer"] = round(float(payload[node]["ram_score_peer"]),2)

        if(payload[node]["score_glob"]!= None) :
            nodes[node_id]["score_glob"] = round(float(payload[node]["score_glob"]),2)


    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['SIMULATOR_PORT'], debug=True)
