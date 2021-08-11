# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:09:46 2021

@author: Lenovo
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
#model=joblib.load('finalized_model.sav');
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if(output==0):
        return render_template('index.html', prediction_text='No Rain')
        

    return render_template('index.html', prediction_text='It rains')
    #return render_template('index.html', prediction_text='It rains   {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)