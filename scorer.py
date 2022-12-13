from flask import Flask, request


app = Flask(__name__)


@app.route("/score", methods=['POST'])
def calculate_score():
    payload = request.get_json()
    cpu_history = [float(cpu) for cpu in payload["cpu"]]
    ram_history = [float(ram) for ram in payload["ram"]]
    response = {
        "cpu_score": round(sum(cpu_history) / len(cpu_history), 2),
        "ram_score": round(sum(ram_history) / len(ram_history), 2),
    }

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
