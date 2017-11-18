from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import pandas as pd
import time
import os
import base64
import uuid

# HTTP API
app = Flask(__name__)

@app.route('/')
def main():
	return "Flask is running"

@app.route('/carbon', methods=['GET'])
def carbon():
	carbon_emissions = pd.read_excel('flight.xls', sep=',',header=0, skiprows= [0, 1, 2, 3, 4])
	carbon_clean = carbon_emissions.iloc[:, 4:12]
	carbon_clean = carbon_clean.drop(carbon_clean.columns[[5,6]], axis=1) 
	carbon_clean = carbon_clean.sort_values(['GHG QUANTITY (METRIC TONS CO2e)'], ascending=False)
	data = []
	for row in carbon_clean.iterrows():
	    location_json = {"lat": row[1]["LATITUDE"], "lon": row[1]["LONGITUDE"], "co2":row[1]["GHG QUANTITY (METRIC TONS CO2e)"]}
	    data.append(location_json)
	data = str(data)
	return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)    