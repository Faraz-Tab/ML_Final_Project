import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url


dash.register_page(
    __name__,
    path='/',
    title='Home',
    name='Home'
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
    'Home', className="bg-primary text-primary p-2 mb-2 text-center"
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



diabetes = html.Div([
    html.H3('What is diabetes'),
    html.P("Diabetes is a disease in which your body either can't produce insulin or can't properly use the insulin it produces. Eleven million Canadians are living with diabetes or prediabetes."),
    html.Footer(
        html.A("-Diabetes Canada", href="https://www.diabetes.ca/about-diabetes/what-is-diabetes", className='pe-auto')
    )
])


type_diabetes = html.Div(
    [
        html.H3("Types of Diabetes"),
        html.H4("Type 1"),
        html.P(className='text-wrap', children=[
            """
            Type 1 diabetes is an autoimmune disease and is also known as insulin-dependent diabetes. People with type 1 diabetes aren't able to produce their own insulin (and can't regulate their blood sugar) because their body is attacking the pancreas. Roughly 10 per cent of people living with diabetes have type 1, insulin-dependent diabetes.

            Type 1 diabetes generally develops in childhood or adolescence, but can also develop in adulthood. People with type 1 need to inject insulin or use an insulin pump to ensure their bodies have the right amount of insulin. 
            """
        ]),
        html.H4('Type 2'),
        html.P(className='text-wrap', children=[
            """
            People with type 2 diabetes can't properly use the insulin made by their bodies, or their bodies aren't able to produce enough insulin. Roughly 90 per cent of people living with diabetes have type 2 diabetes.

            Type 2 diabetes is most commonly developed in adulthood, although it can also occur in childhood. Type 2 diabetes can sometimes be managed with healthy eating and regular exercise alone, but may also require medications or insulin therapy. 

            If you think you or someone you know may have type 2 diabetes, please speak to a doctor or health-care provider.
            """
        ]),
        html.H4("Gestational Diabetes"),
        html.P(className="text-wrap",children=[
            """
            Gestational diabetes is a temporary form of diabetes that occurs during pregnancy. Between three and 20 per cent of pregnant women develop gestational diabetes, depending on their risk factors. A diagnosis of gestational diabetes may increase the risk of developing diabetes later in life for both mother and child. 
            """
        ]),
        html.H4("Prediabetes"),
        html.P(className='text-wrap', children=[
            """
            Prediabetes is a condition where blood sugar levels are higher than normal, but are not yet high enough to be diagnosed as type 2 diabetes. Although not everyone with prediabetes will develop type 2 diabetes, many people will.

            It's important to know if you have prediabetes, because research has shown that some long-term complications associated with diabetes—such as heart disease—may begin during prediabetes. 
            """
        ]),
        html.Footer(
        html.A("-Diabetes Canada", href="https://www.diabetes.ca/about-diabetes/what-is-diabetes", className='pe-auto')
    )
    ]
)


symptoms = html.Div([
    html.P(className='text-wrap', children=[
      html.Li('Frequent urination'),
      html.Li('Weigth change'),
      html.Li('Blurred vision'),
      html.Li('Tingling or numbness in the hands or feet')  
    ])
])


treatment = html.Div([
    html.Li('Dietary adjustments'),
    html.Li('Monitoring blood sugar levels'),
    html.Li('Regular physical activity'),
    html.Li('Taking insulin as reccommended by a physician')
])

accordian = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                diabetes, title = 'What is Diabetes'
            ),
            dbc.AccordionItem(
                type_diabetes, title= "Types of Diabetes"
            ),
            dbc.AccordionItem(
                symptoms, title="Signs and Symptoms"
            ),
            dbc.AccordionItem(
                treatment, title="Treatment"
            )
        ],
        flush=True
    )
)


layout = dbc.Container(
    [
        header,
        dbc.Row([
            theme_controls,
        ]),
        accordian
    ]
)