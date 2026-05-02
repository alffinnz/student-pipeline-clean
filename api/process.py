from flask import Flask, request, Response
import pandas as pd
from io import StringIO
from pipeline import process_data

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.data.decode()
    df = pd.read_csv(StringIO(data))
    df = process_data(df)
    return Response(df.to_csv(index=False), mimetype='text/csv')