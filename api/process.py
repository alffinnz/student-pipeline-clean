from flask import Flask, request, Response, send_from_directory
from flask_cors import CORS
import pandas as pd
from io import StringIO
from pipeline import process_data
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory("../public", "index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.data.decode()
        df = pd.read_csv(StringIO(data))

        df = process_data(df)

        return Response(
            df.to_csv(index=False),
            mimetype="text/csv"
        )

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)