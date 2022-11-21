import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from apps.vpo1 import vpo1
# import plotly.express as px
# import pandas as pd


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets=[dbc.themes.BOOTSTRAP]
# external_stylesheets=[dbc.themes.CYBORG]
# external_stylesheets=[dbc.themes.DARKLY]
external_stylesheets = [dbc.themes.SOLAR]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
app.title = "IAC"
server = app.server

SIDESTYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#222222",
}

CONTSTYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.H2("ИАЦ", className="display-3", style={'color': 'white'}),
            html.Hr(style={'color': 'white'}),
            dbc.Nav(
                [
                    dbc.NavLink("ВПО-1", href="/vpo1", active="exact"),
                    dbc.NavLink("ВПО-2", href="/vpo2", active="exact"),
                    dbc.NavLink("1-Мониторинг", href="/page3", active="exact"),
                ],
                vertical=True, pills=True),
        ],
        style=SIDESTYLE,
    ),
    html.Div(id="page-content", children=[], style=CONTSTYLE)
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def pagecontent(pathname):
    if pathname == "/vpo1":
        return [
            html.Div(
                children=[
                    # html.H1(children='ВПО-1', className='header-title'),
                    # html.P(children='maybe this demo will be useful to someone (:', className='header-description'),
                    html.H1(children='Данные ВПО-1', className='header-title'),
                    vpo1

                ], className='header')
        ]

    elif pathname == "/vpo2":
        return [
            html.Div(
                children=[
                    html.H1(children='ВПО-2', className='header-title'),
                    html.P(children='maybe this demo will be useful to someone (:', className='header-description')
                ], className='header')
        ]
    elif pathname == "/page3":
        return [
            html.Div(
                children=[
                    html.H1(children='1-Мониторинг', className='header-title'),
                ], className='header')
        ]


@app.callback(
    Output(component_id='output_graph', component_property='figure'),
    [Input(component_id='demo_drop', component_property='value')]
)
def update_output(value):
    if value == 'cut':
        pass
        # h = df1.groupby(['cut'], as_index=False, sort=False)['carat'].count()
    elif value == 'clarity':
        pass
        # h = df1.groupby(['clarity'], as_index=False, sort=False)['carat'].count()
    elif value == 'color':
        pass
        # h = df1.groupby(['color'], as_index=False, sort=False)['carat'].count()
    # fig = px.bar(h, x=value, y="carat", labels={"carat": "Count"})
    return 0
    # fig


if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(host='192.168.0.100', port='5000', debug=True)
