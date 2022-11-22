
from dash import Dash, html, dcc, dash_table
# from dash import Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# BB сервер
# vpo12022_12 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/1.2.csv"
# vpo12022_211 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/2.1.1.csv"

# Googgle drive
# vpo12022_12 = "https://drive.google.com/file/d/1F5wYeD8Ji13zjImHiZ12nSkUaC_usjco/view?usp=sharing"
# vpo12022_211 = "https://drive.google.com/file/d/1vKZE3_rTTxCR---Oa5ukADlNpPXUOsfm/view?usp=sharing"
# path = 'https://drive.google.com/uc?export=download&id='
# df = pd.read_csv(path+vpo12022_12.split('/')[-2], delimiter=";")
# df1 = pd.read_csv(path+vpo12022_211.split('/')[-2], delimiter=";")

# Local
vpo12022_12 = "H:/IAC/1.2.csv"
vpo12022_211 = "H:/IAC/2.1.1.csv"
df = pd.read_csv(vpo12022_12, delimiter=";")
df1 = pd.read_csv(vpo12022_211, delimiter=";")

df1["УГС"] = df1["НПП"].map(lambda x: x[:2])

df2 = df1[['уровень',
           'Среднее минимальное количество баллов принятых на бюджет',
           'Среднее минимальное количество баллов принятыхна рамках квоты',
           'Среднее минимальное количество баллов с учетом принятых имеющие особое право',
           'Среднее минимальное количество баллов принятых на договор',
           'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых на бюджет',
           'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых  в рамках квоты',
           'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых имеющих особое право',
           'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых на договор'
           ]].groupby('уровень').mean().T
# df = df2.set_index('уровень')
# df2.groups.keys()
from pathlib import Path
filepath = Path('H:/IAC/out.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
# df2.to_csv(filepath,encoding='utf-8')
df3 = pd.read_csv(filepath)



colors = {
    'background': '#002b36',
    'text': '#7FDBFF'
}


# 1.2 образовательные программы
fig12op = px.pie(
    df,
    values='countNPP',
    names='lvl',
    color_discrete_sequence=px.colors.sequential.RdBu,
    # width=500,
    # height=500,
    hole=0.5,
    title='Образовательные программы ДВФУ'
)
fig12op.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
# 1.2 количество студентов
fig12stud = px.pie(
    df,
    values='countStud',
    names='lvl',
    color_discrete_sequence=px.colors.sequential.RdBu,
    # width=500,
    # height=500,
    hole=0.5,
    title='Контингент обучающихся по прогаммам высшего образования ДВФУ'
)

fig12stud.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
# прием по угс
fig211priem = px.bar(df1.sort_values(by=['УГС']),
              x="УГС",
              y="Принято всего",
              color="уровень",
              title="Принято по УГС",
              color_discrete_sequence=px.colors.sequential.RdBu
)

fig211priem.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# средние значения приема бак
fig211mean1 = px.bar(df3,
              # x=df2["уровень"],
              # x='ТИП',
              x=['бакалавриат'],
              color="ТИП",
              title="Баллы приема на бакалавриат",
              color_discrete_sequence=px.colors.sequential.RdBu
)
fig211mean1.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
# средние значения приема спец
fig211mean2 = px.bar(df3,
              # x=df2["уровень"],
              # x='ТИП',
              x=['специалитет'],
              color="ТИП",
              title="Баллы приема на специалитет",
              color_discrete_sequence=px.colors.sequential.RdBu
)
fig211mean2.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
# fig211mean.add_bar(df3,
#               y='специалитет',
#
# )
# fig211mean.add_bar(df2.filter(like='специалитет'),
#               # x="уровень",
#               # x='index',
#               color="уровень",
#               title="Принято по УГС",
#               color_discrete_sequence=px.colors.sequential.RdBu
# )
# fig66 = px.bar()
# fig66.add_trace(px.bar(df2.filter(like='бакалавриат'), color="уровень", title="Принято по УГС", color_discrete_sequence=px.colors.sequential.RdBu))
# fig.add_trace(px.bar(df2.filter(like='специалитет'), color="уровень", title="Принято по УГС", color_discrete_sequence=px.colors.sequential.RdBu))
# fig211Mean = dash_table.DataTable(
#     df2.to_dict('records'),
#     [{"name": i, "id": i} for i in df2.columns]
# )
# fig211Mean = dbc.Container([
#     dbc.Label('Click a cell in the table:'),
#     dash_table.DataTable(df2.to_dict('records'),[{"name": i, "id": i} for i in df2.columns], id='tbl'),
#     dbc.Alert(id='tbl_out'),
# ])


# app.layout = html.Div(children=[
vpo1 = html.Div(children=[
    # 1.2 образовательные программы
    html.Div([
        dcc.Graph(
            id="graph1",
            figure=fig12op,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
# 1.2 количество студентов

    html.Div([
        dcc.Graph(
            id="graph2",
            figure=fig12stud,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
# прием по угс
    html.Div([
        dcc.Graph(
            id='graph3',
            figure=fig211priem,
        )],
        style={'width': '100%', 'display': 'inline-block'}
    ),
# средние значения приема бак
    html.Div([
        dcc.Graph(
            id='graph4',
            figure=fig211mean1,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
# средние значения приема спец
    html.Div([
        dcc.Graph(
            id='graph5',
            figure=fig211mean2,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # html.Div([
    #     dash_table.DataTable(
    #         data=df2.to_dict('records'),
    #         style_cell={  # ensure adequate header width when text is shorter than cell's text
    #             'minWidth': 95, 'maxWidth': 95, 'width': 95
    #         },
    #         style_data={  # overflow cells' content into multiple lines
    #             'whiteSpace': 'normal',
    #             'height': 'auto'
    #         }
    #     )],
    #     style={'width': '50%', 'display': 'inline-block','border': '1px solid grey', 'font-size': '14px', 'background': '#b9c9fe'}
    #
    # ),
    # html.Div([
    #     html.H1(children='75%', className='inside-circle'),
    #     dcc.Markdown('''
    #     #### Dash and Markdown
    #
    #     Dash supports [Markdown](http://commonmark.org/help).
    #
    #     Markdown is a simple way to write and format text.
    #     It includes a syntax for things like **bold text** and *italics*,
    #     [links](http://commonmark.org/help), inline `code` snippets, lists,
    #     quotes, and more.
    #
    #     Markdown is a simple way to write and format text.
    #     It includes a syntax for things like **bold text** and *italics*,
    #     [links](http://commonmark.org/help), inline `code` snippets, lists,
    #     quotes, and more.
    #
    #     Markdown is a simple way to write and format text.
    #     It includes a syntax for things like **bold text** and *italics*,
    #     [links](http://commonmark.org/help), inline `code` snippets, lists,
    #     quotes, and more.
    #
    #     Markdown is a simple way to write and format text.
    #     It includes a syntax for things like **bold text** and *italics*,
    #     [links](http://commonmark.org/help), inline `code` snippets, lists,
    #     quotes, and more.
    #     ''')],
    #     style={'width': '50%', 'display': 'inline-block'}
    # ),


    html.Div(
        children=[
        html.H1(children='75%', className='inside-circle'),
        ], className='header'
    ),

    html.Div([
        dcc.Graph(
        id='graph7',
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
            id='graph8',
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

])
