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


def create_new_node():
    return {
        'cpu': deque(maxlen=HIST_MAXLEN),
        'ram': deque(maxlen=HIST_MAXLEN),
        'x': None,
        'y': None,
        'cpu_score': None,
        'ram_score': None,
    }


@app.route("/new", methods=['POST'])
def new_input():
    payload = request.get_json()
    for node in payload:
        node_id = node['id']
        if node_id not in nodes:
            nodes[node_id] = create_new_node()

        nodes[node_id]['cpu'].appendleft(node['cpu'])
        nodes[node_id]['ram'].appendleft(node['ram'])
        nodes[node_id]['x'] = node['x']
        nodes[node_id]['y'] = node['y']

    return payload


@app.route("/", methods=['GET'])
def get():
    raw = json.dumps(nodes, indent=2, cls=CustomEncoder)
    return Response(raw, mimetype='application/json')

@app.route("/update_scores", methods=['POST'])
def update_scores():
    payload = request.get_json()
    for node in payload:
        node_id = int(node)
        if node_id not in nodes:
            print("node " + node_id + " not in list, skipping it")
            continue

        nodes[node_id]["cpu_score"] = float(payload[node]["cpu_score"])
        nodes[node_id]["ram_score"] = float(payload[node]["ram_score"])

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['SIMULATOR_PORT'], debug=True)
