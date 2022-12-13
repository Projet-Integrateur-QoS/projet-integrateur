from flask import Flask, request
from collections import deque
import requests
import json
from custom_encoder import CustomEncoder

HIST_MAXLEN = 3

app = Flask(__name__)
nodes = dict()
last_payload = ""


def create_new_node():
    return {
        'cpu': deque(maxlen=HIST_MAXLEN),
        'ram': deque(maxlen=HIST_MAXLEN),
        'x': None,
        'y': None,
        'cpu_score': 0,
        'ram_score': 0,
    }


def calculate_scores():
    for node in nodes:
        response = requests.post(
            f'http://localhost:8001/score',
            data=json.dumps(nodes[node], cls=CustomEncoder),
            headers={'Content-Type': 'application/json'},
        )

        response_json = response.json()

        nodes[node]["cpu_score"] = response_json["cpu_score"]
        nodes[node]["ram_score"] = response_json["ram_score"]


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

    calculate_scores()

    # debug pretty print
    json_formatted_str = json.dumps(nodes, indent=2, cls=CustomEncoder)
    print(json_formatted_str)

    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
