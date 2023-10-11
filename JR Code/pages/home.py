import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

colors = {
    'background': '0C120C',
    'text': '6D7275'
}

dash.register_page(
    __name__,
    path='/',
    title='Home',
    name='Home'
    )
markdown_text = '''
# What is diabetes?
---
Diabetes is a disease in which your body either can't produce insulin or can't properly use the insulin it produces.
Eleven million Canadians are living with diabetes or prediabetes. [Diabetes Canada](https://www.diabetes.ca/about-diabetes/what-is-diabetes)

# Types of Diabetes
## Type 1
**Type 1 Diabetes** is an autoimmune disease known as insulin-dependant diabetes.
People with **Type 1 Diabetes** are unable to produce
their own insulin.  It affects roughly *10%* of all diabetic patients

## Type 2
People with **Type 2 Diabetes** cannot properly use the insulin that their own body creates/  It affects roughly *90%* of all patients.
'''

symptoms = '''
# Signs and Symptoms
[Signs and Symptoms](https://www.diabetes.ca/en-CA/about-diabetes)
Some common symptoms include:
* Frequent urination
* Weight change
* Blurred vision
* Tingling or numbness in the hands or feet
'''

treatment = '''
Most treatment includes:
* Dietary adjustments
* Monitoring blood sugar levels
* Taking insulin as reccommended
'''

layout = html.Div(children=[
    html.Div([dcc.Markdown(children=markdown_text)]),
    html.Div([dcc.Markdown(children=symptoms)]),
    html.Div([dcc.Markdown(children=treatment)])]
)
