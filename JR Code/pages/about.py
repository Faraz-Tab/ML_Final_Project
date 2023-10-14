import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dash.register_page(
    __name__,
    path="/pages/about.py",
    title='About',
    name='About',
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
    'About', className="bg-primary text-white p-2 mb-2 text-center"
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

project = html.Div(
    className='align-center mt-3 p-3',
    children=[
        html.Div(
            [
                html.H3(className='border border-1 border-primary text-center',children='About the project')
            ]
        ),
        html.Div(
            [
                html.P(className='text-wrap', children= [
                    '''
                    The purpose of this project was to create a model that would be able to predict whether 
                    someone has diabetes depending on the test results provided.  To do that the data was analysed
                    to look at how the data was dispursed and then cleaned and processed to prepare it to train the model.
                    to meet bets practices for the medical industry the goal accuracy was expected to be no less than 99%.
                    We did a prelimnary comparison to help determine what type of model would be the most effective and  
                    in the end decided that to use a Random Forest Classifier as it scored the best in preliminary testing.
                    The goal of this project was to be able to get a data set to use and employ our learning from this course
                    and solve a problem using machine learning and other techniques found in this course.
                    '''
                ])
            ]
        )
    ]
)


contributors = html.Div(
    className='align-center mt-3 p-3',
    children=[
        html.Div(
            [
                html.H3(className='border border-1 border-primary text-center',children='Contributors')
            ]
        ),
        html.Div(
            [
                html.P('Faraz Tabatabaei'),
                html.P('Cindy Li'),
                html.P('Kevin Jeong'),
                html.P('Jeffrey Robertson')
            ]
        )
    ]
)

layout = dbc.Container(
    [
        header,
        theme_controls,
        project,
        contributors
    ]
)