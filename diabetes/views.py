from flask import render_template, request, Blueprint
import pickle
import numpy as np
from diabetes import diabetes_bp  # Absolute import assuming 'diabetes' is a sibling directory
# Adjust the import path based on your actual project structure

# Load the diabetes model
with open('diabetes/diabetes.pkl', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

@diabetes_bp.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@diabetes_bp.route('/predict', methods=['POST'])
def predict_diabetes():
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
            ]
            prediction = diabetes_model.predict([data])[0]
            return render_template('afterdiabetes.html', data=prediction)
        except Exception as e:
            return str(e)
