import dash
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, dbc_css])


nav = html.Nav([
    dbc.Col(className='position-right w-20%', children=[
        html.H1('Menu'),
        dbc.Row([
            dcc.Link(f"{page['name']}", href=page["relative_path"])
            for page in dash.page_registry.values()
    ]),
      
    ]),
])

navigator = dbc.Row(
    [
        dbc.Col(dbc.NavLink("Home", href="/")),
        dbc.Col(dbc.NavLink("About", href="/pages/about.py")),
        dbc.Col(dbc.NavLink("Analysis", href= "/analytics-dashboard"))        
    ]
)
navbar = dbc.NavbarSimple(
    children=[
        navigator,
        ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = dbc.Container([
    navigator,
    dash.page_container    
    ]
)

if __name__ == '__main__':
    app.run(debug=True)