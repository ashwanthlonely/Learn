# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:19:32 2023

@author: chenn
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:/Users/chenn/Desktop/Deployment/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('C:/Users/chenn/Desktop/Deployment/templates/index.html')

@app.route('/predict', methods=['post'])
def predict():
    """
    for renderinng results on html GUI
    """
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('C:/Users/chenn/Desktop/Deployment/templates/index.html', prediction_text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)