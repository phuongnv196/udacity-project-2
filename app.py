from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib

import sklearn.ensemble.GradientBoostingClassifier
import sklearn.preprocessing.StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scale Payload"""

    LOG.info("Scaling Payload: %s", payload)
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home, Welcome to service</h3>"
    return html

# TO DO: Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    try:
        clf = joblib.load("boston_housing_prediction.joblib")
    except Exception as e:
        LOG.error("Model loading error: %s", str(e))
        return "Model not loaded"

    json_payload = request.json
    LOG.info("JSON payload: %s", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("Inference payload DataFrame: %s", inference_payload)
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
