import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__, use_pages=True)

colors= {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div()


if __name__ == '__main__':
    app.run(debug=True)