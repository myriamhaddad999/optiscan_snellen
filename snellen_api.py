# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 23:12:21 2025

@author: User-Pc
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoder
model = joblib.load("snellen_model.pkl")
encoder = joblib.load("snellen_label_encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        line = int(data.get("line"))
        mistakes = int(data.get("mistakes"))
        age = int(data.get("age"))

        df = pd.DataFrame([[line, mistakes, age]], columns=["line_read", "mistakes", "age"])
        prediction = model.predict(df)
        label = encoder.inverse_transform(prediction)[0]

        return jsonify({"diagnosis": label})
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"diagnosis": "undefined", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
