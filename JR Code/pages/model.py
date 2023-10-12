# import dash
# from dash import Dash, html, dcc, callback, Output, Input, clientside_callback, State
# import plotly.express as px
# import pandas as pd
# import dash_bootstrap_components as dbc
# from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
# import dash_ag_grid as dag
# import pickle
# import numpy as np

# filename = 'diabetes-prediction-rfc-model.pkl'
# classifier = pickle.load(open(filename, 'rb'))

# from flask import Flask, render_template, request


# dash.register_page(
#       __name__,
#       path='JR Code/pages/model.py',
#       title= 'model',
# )


# form = dbc.FormFloating(
#       [
#             dbc.Input(id='preg', placeholder="Pregnancies"),
#             dbc.Input(id='gluc', placeholder="Glucose"),
#             dbc.Input(id='bp', placeholder="Blood Pressure"),
#             dbc.Input(id='st', placeholder="Skin Thickness"),
#             dbc.Input(id='bmi', placeholder= "Body Mass Index"),
#             dbc.Input(id='dpf', placeholder="Diabetes Pedigree Funciton"),
#             dbc.Input(id='age', placeholder="Age"),
#       ]
# )

# button = dbc.Button('Submit', n_clicks=0),

# output_container = html.Div(className='mt-4')

# layout= dbc.Container([form,button,output_container], fluid=True)


# @callback(
#       Output(output_container, 'children'),
#       Input(button, 'n_clicks'),
#       State('preg', 'value'),
#       State('gluc', 'value'),
#       State('bp', 'value'),
#       State('st', 'value'),
#       State('bmi', 'value'),
#       State('dpf', 'value'),
#       State('age', 'value'),
#       prevent_initial_call=True,
# )

# def predict(preg, glucose, bp, st, insulin, bmi, dpf, age):
#     filename = 'diabetes-prediction-rfc-model.pkl'
#     classifier = pickle.load(open(filename, 'rb'))
    
#     data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
#     my_prediction = classifier.predict(data)
#     output = my_prediction
#     return f'{output}'


# filename = 'diabetes-prediction-rfc-model.pkl'
# classifier = pickle.load(open(filename, 'rb'))

# # app = Flask(__name__)

# # @app.route('/')
# # def home():
# # 	return render_template('index.html')

# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     if request.method == 'POST':
# #         preg = int(request.form['pregnancies'])
# #         glucose = int(request.form['glucose'])
# #         bp = int(request.form['bloodpressure'])
# #         st = int(request.form['skinthickness'])
# #         insulin = int(request.form['insulin'])
# #         bmi = float(request.form['bmi'])
# #         dpf = float(request.form['dpf'])
# #         age = int(request.form['age'])
        
# #         data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
# #         my_prediction = classifier.predict(data)
# #         output = my_prediction
# #         return render_template('index.html', prediction=my_prediction)

# # if __name__ == '__main__':
# # 	app.run()