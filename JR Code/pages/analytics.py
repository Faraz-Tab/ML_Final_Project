import dash
from dash import Dash, html, dcc, callback, Output, Input, clientside_callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
import dash_ag_grid as dag

df = pd.read_csv('Diabetes/kaggle_diabetes.csv')

df2 = df.drop(columns='Outcome')
columns=list(df.columns)

dash.register_page(
    __name__,
    path = '/analytics-dashboard',
    title = 'Diabetes Analytics Dashboard',
    name= 'Analytics Dashboard',
    )
color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

theme_controls = html.Div(
    [ThemeChangerAIO(aio_id="theme"), color_mode_switch],
    className="hstack gap-3 mt-2"
)

header = html.H4(
    "Analyisis of Data", className="bg-primary text-white p-2 mb-2 text-center"
)

grid = dag.AgGrid(
    id="grid",
    columnDefs=[{"field": i} for i in df.columns],
    rowData=df.to_dict("records"),
    defaultColDef={"flex": 1, "minWidth": 120, "sortable": True, "resizable": True, "filter": True},
    dashGridOptions={"rowSelection":"multiple"},
)

xDropdown = html.Div(
    [
        dbc.Label("X Axis Drop Down"),
        dcc.Dropdown(
            columns,
            'Pregnancies',
            id='xaxis_column',
            clearable=False
        )
    ],
    className="mb-4",
)

yDropDown =  html.Div(
    [
        dbc.Label("Y Axis Drop Down"),
        dcc.Dropdown(
            columns,
            'Pregnancies',
            id='yaxis_column',
            clearable=False
        )
    ],
    className="mb-4",
)

theme_colors = [
    "primary",
    "secondary",
    "success",
    "warning",
    "danger",
    "info",
    "light",
    "dark",
    "link",
]
colors = html.Div(
    [dbc.Button(f"{color}", color=f"{color}", size="sm") for color in theme_colors]
)
colors = html.Div(["Theme Colors:", colors], className="mt-2")

controls = dbc.Card(
    [xDropdown, yDropDown],
    body=True,
)

tab1 = dbc.Tab([dcc.Graph(id='scatter-chart', figure=px.scatter(template='bootstrap'))], label="Scatter Chart")
tab2 = dbc.Tab([dcc.Graph(id='hist-chart',figure=px.histogram(template='bootstrap'))], label="Histogram")

tabs = dbc.Card(dbc.Tabs([tab1,tab2]))

layout = dbc.Container(
    [
        header,
        dbc.Row([
            dbc.Col([
                controls,
                # ************************************
                # Uncomment line below when running locally!
                # ************************************
                theme_controls
            ],  width=4),
            dbc.Col([tabs, colors], width=8),
        ]),
    ],
    fluid=True,
    className="dbc dbc-ag-grid",
)

@callback(
        Output('scatter-chart', 'figure'),
        Output('hist-chart', 'figure'),
        Input('xaxis_column', 'value'),
        Input('yaxis_column', 'value'),
        Input(ThemeChangerAIO.ids.radio("theme"), "value"),
        Input("switch", "value"),
)



def update(xaxis_column, yaxis_column, theme, color_mode_switch_on):
    if xaxis_column is None or yaxis_column is None:
        return {},{},[]
    
    theme_name = template_from_url(theme)

    template_name = theme_name if color_mode_switch_on else theme_name + "_dark"

    fig_scatter = px.scatter(
        df,
        x= xaxis_column,
        y= yaxis_column,
        color='Outcome',
        template=template_name,
        title= f'{xaxis_column} versus {yaxis_column}'
    )
    fig_scatter.update_layout(showlegend=False)

    return fig_scatter


clientside_callback(
    """
    switchOn => {       
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)
