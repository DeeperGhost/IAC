# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas as pd
from dash import Dash, html, dcc
from dash import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px



# app = Dash(__name__, external_stylesheets=external_stylesheets)
# app.title = "IAC"
# server = app.server


vpo12022_12 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/1.2.csv"

colors = {
    'background': '#002b36',
    'text': '#7FDBFF'
}

df = pd.read_csv(vpo12022_12, delimiter=";")


vpo2 = html.Div(children=[
    html.H1(children='Информационно-аналитический центр', style={'color': colors['text']}),

])