import flask
from flask import Flask, jsonify, request
import json
import pickle
import pandas as pd

app = Flask(__name__)


def load_models():
    request_json = request.get_json()
    file_name = request_json["mdl"]
    with open(file_name, "rb") as file:
        model = pickle.load(file)
    return model


@app.route("/predict", methods=["GET"])
def predict():
    # parse input features from request
    request_json = request.get_json()
    x = pd.read_csv(request_json["input"], index_col=0)

    # load model
    model = load_models()
    prediction = model.predict(x.T)[0]
    response = json.dumps({"response": prediction})
    return response, 200


if __name__ == "__main__":
    application.run(debug=True)
