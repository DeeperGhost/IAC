
from dash import Dash, html, dcc
from dash import Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px


vpo12022_12 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/1.2.csv"
colors = {
    'background': '#002b36',
    'text': '#7FDBFF'
}

df = pd.read_csv(vpo12022_12, delimiter=";")
fig = px.pie(
    df,
    values='countNPP',
    names='lvl',
    color_discrete_sequence=px.colors.sequential.RdBu,
    # width=500,
    # height=500,
    hole=0.5,
    title='Образовательные программы ДВФУ'
)

fig.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})


# app.layout = html.Div(children=[
vpo1 = html.Div(children=[
    html.Div([
        dcc.Graph(
        id="graph4",
        figure=fig,
        )],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div([
        dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': [2017, 2018, 2019, 2020, 2021, 2022], 'y': [23347, 22537, 20370, 18174, 17969, 19094], 'type': 'bar', 'name': 'Контингент'},
            ],
            'layout': {
                'title': 'Контингент ДВФУ по годам',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        })],
        style= {'width': '25%', 'display': 'inline-block'}
    ),
    html.Div([
        dcc.Graph(
            id='graph2',
            figure={
                'data': [
                    {'x': [2017, 2018, 2019, 2020, 2021, 2022], 'y': [23347, 22537, 20370, 18174, 17969, 19094],
                     'type': 'Pie Chart', 'name': 'Контингент'},
                ],
                'layout': {
                    'title': 'Контингент ДВФУ по годам',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            })],
        style={'width': '25%', 'display': 'inline-block'}
    ),
    html.Div([
        dcc.Graph(
            id='graph3',
            figure={
                'data': [
                    {'x': [2017, 2018, 2019, 2020, 2021, 2022], 'y': [23347, 22537, 20370, 18174, 17969, 19094],
                     'type': 'Pie Chart', 'name': 'Контингент'},
                ],
                'layout': {
                    'title': 'Контингент ДВФУ по годам из отчета ВПО-1',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            })],
        style={'width': '25%', 'display': 'inline-block'}
    ),
])
