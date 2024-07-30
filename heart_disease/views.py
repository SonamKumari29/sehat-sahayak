from flask import render_template, request
import pickle
import numpy as np
from . import heart_bp

# Load the heart disease model
with open('heart_disease/heart.pkl', 'rb') as model_file:
    heart_model = pickle.load(model_file)

@heart_bp.route('/')
def heart_disease():
    return render_template('heartdisease.html')

@heart_bp.route('/predict', methods=['POST'])
def predict_heart_disease():
    if request.method == 'POST':
        try:
            data = [
                int(request.form['a']),
                int(request.form['b']),
                int(request.form['c']),
                int(request.form['d']),
                int(request.form['e']),
                int(request.form['f']),
                int(request.form['g']),
                int(request.form['h']),
                int(request.form['i']),
                float(request.form['j']),
                int(request.form['k']),
                int(request.form['l']),
                int(request.form['m'])
            ]
            prediction = heart_model.predict([data])[0]
            return render_template('afterheart.html', data=prediction)
        except Exception as e:
            return str(e)
