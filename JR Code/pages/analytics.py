import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('Diabetes/kaggle_diabetes.csv')

columns=list(df.columns)

dash.register_page(
    __name__,
    path = '/analytics-dashboard',
    title = 'Diabetes Analytics Dashboard',
    name= 'Analytics Dashboard'
    )

colors = {
    'background': '0c120c',
    'text': '6d7275'
}

layout = html.Div([
    html.Div([
        dcc.Dropdown(
            columns,
            'Pregnancies',
            id='xaxis_column'
        )
    ], style={
        'width': '48%',
        'display': 'inline-block'
    }),

    html.Div([
        dcc.Dropdown(
            columns,
            "Glucose",
            id='yaxis_column'
        )
    ], style={
        'width': '48%',
        'float': 'right',
        'display': 'inline-block'
    }),

    dcc.Graph(id='indicator_graphic'),

    dcc.Slider(
        df["Outcome"].min(),
        df["Outcome"].max(),
        step=None,
        id='outcome-slider',
        value=df['Outcome'].max(),
        marks={str(outcome): str(outcome) for outcome in df['Outcome'].unique()},
    )
])

@callback(
    Output('indicator_graphic', 'figure'),
    Input('xaxis_column', 'value'),
    Input('yaxis_column', 'value'),
    Input('outcome-slider', 'value')
)

def update_graph(xaxis_column_name, yaxis_column_name, outcome_value):
    dff = df[df['Outcome'] == outcome_value]

    fig = px.scatter(x=dff[xaxis_column_name],y=dff[yaxis_column_name])
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig