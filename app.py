from scorer import QoSScorer
from score_functions import mean
from flask import Flask

app = Flask(__name__)
scorer = QoSScorer(history_maxlen=3, score_function=mean)


@app.route("/new/<payload>", methods = ['POST'])
def new_input(payload):
    scorer.run(payload.split(';'))
    return payload

@app.route("/history")
def get_history():
    return scorer.get_last_processed()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
