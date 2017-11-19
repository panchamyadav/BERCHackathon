from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import pandas as pd

# HTTP API
app = Flask(__name__)
CORS(app)
print("CORS enabled")
@app.route('/')
def main():
	return "Flask is running"

@app.route('/carbon', methods=['GET'])
def carbon():
	centroids = pd.read_csv('centroid.csv')
	centroid_lst = []
	for row in centroids.iterrows():
	    centroid_lst.append({'lat': float(row[1]['lat']), 'lon': float(row[1]['long'])})
	data_json = jsonify({"data": centroid_lst})
	print(data_json)
	return data_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)    