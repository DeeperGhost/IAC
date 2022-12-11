
from dash import Dash, html, dcc, dash_table
# from dash import Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import pycountry


# BB сервер
# vpo12022_12 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/1.2.csv"
# vpo12022_211 = "https://bb.dvfu.ru/bbcswebdav/orgs/FUDOOD/%D0%91%D0%94/%D0%98%D0%90%D0%A6/2.1.1.csv"

# Googgle drive
# vpo12022_12 = "https://drive.google.com/file/d/1F5wYeD8Ji13zjImHiZ12nSkUaC_usjco/view?usp=sharing"
# vpo12022_211 = "https://drive.google.com/file/d/1vKZE3_rTTxCR---Oa5ukADlNpPXUOsfm/view?usp=sharing"
# vpo12022_211b = "https://drive.google.com/file/d/1tnHDlfeAIQgxp7B46HevqXIJ0QyKHeiN/view?usp=sharing"
# vpo12022_212 = "https://drive.google.com/file/d/1nC3OXvCDro3NiinZe5KMAIHv6T7JhJBX/view?usp=sharing"
# vpo12022_212b = "https://drive.google.com/file/d/1JVdS0zQob2fU0pd5SE1AKQNdVzGFKczu/view?usp=sharing"
#
# path = 'https://drive.google.com/uc?export=download&id='
# df12 = pd.read_csv(path+vpo12022_12.split('/')[-2], delimiter=";")
# df211 = pd.read_csv(path+vpo12022_211.split('/')[-2], delimiter=";")
# df211b = pd.read_csv(path+vpo12022_211b.split('/')[-2])
# df212b = pd.read_csv(path+vpo12022_212b.split('/')[-2])
# df212 = pd.read_csv(path+vpo12022_212.split('/')[-2], delimiter=";")
# Local


# vpo12022_212b = "H:/IAC/2.1.2b.csv"
path_vpo1 = "H:/IAC/"

df12 = pd.read_csv(path_vpo1+"1.2.csv", delimiter=";")
df211 = pd.read_csv(path_vpo1+"2.1.1.csv", delimiter=";")
df211b = pd.read_csv(path_vpo1+"2.1.1b.csv")
df212 = pd.read_csv(path_vpo1+"2.1.2.csv", delimiter=";")
df212b = pd.read_csv(path_vpo1+"2.1.2b.csv")
df213 = pd.read_csv(path_vpo1 + "2.1.3.csv", delimiter=";")
df2_11 = pd.read_csv(path_vpo1 + "211.csv", dtype={'n-страна': object}, delimiter=";")
df2_12 = pd.read_csv(path_vpo1 + "212.csv", delimiter=";")
df31 = pd.read_csv(path_vpo1 + "31.csv", delimiter=";")

df211["УГС"] = df211["НПП"].map(lambda x: x[:2])


# df.to_csv('H:/IAC/211x.csv',encoding='utf-8')






# df2 = df1[['уровень',
#            'Среднее минимальное количество баллов принятых на бюджет',
#            'Среднее минимальное количество баллов принятыхна рамках квоты',
#            'Среднее минимальное количество баллов с учетом принятых имеющие особое право',
#            'Среднее минимальное количество баллов принятых на договор',
#            'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых на бюджет',
#            'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых  в рамках квоты',
#            'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых имеющих особое право',
#            'Среднее количество баллов ЕГЭ с учетом дополнительных испытаний у принятых на договор'
#            ]].groupby('уровень').mean().T
# df = df2.set_index('уровень')

# df5 = df4.groupby(['уровень', 'форма']).sum().reset_index()
# df5 = df5.assign(lvlform= df5['форма']+' '+df5['уровень'])
# df5 = df5.drop(['уровень', 'форма'], axis=1).T
# df5.to_csv('H:/IAC/out.csv',encoding='utf-8')
df212b['all'] = df212b[['заочная бакалавриат',
                'очная бакалавриат',
                'заочная магистратура',
                'очная магистратура',
                'заочная специалитет',
                'очная специалитет']].sum(axis=1)

df213['выпуск мужчины'] = df213['выпуск всего']-df213['выпуск женщины']

df213b = df213[['выпуск мужчины','выпуск женщины']].sum().reset_index()
# надо переделать по норм
df213 = df213.groupby('форма').sum().reset_index().T
df213 = df213.reset_index().drop(labels=[0, 4, 6], axis=0).reset_index()

df2_11["country"] = df2_11["n-страна"].map(lambda x: pycountry.countries.get(numeric=str(x)).name)
df2_11["iso_alpha"] = df2_11["n-страна"].map(lambda x: pycountry.countries.get(numeric=str(x)).alpha_3)
df2_11 = df2_11.groupby(['country', 'год', 'iso_alpha'], group_keys=False).sum().reset_index()
df2_11 = df2_11[df2_11.iso_alpha != 'RUS']

df2_12['kont_male'] = df2_12['контингент']-df2_12['контингент -женщины']
df2_12['vipusk_male'] = df2_12['выпуск']-df2_12['выпуск - женщины']
df2_12 = df2_12.groupby(['возраст'], group_keys=False).sum().reset_index()
df2_12 = df2_12[df2_12['возраст'] != 'Всего']

print(df31.keys())
print(df31.head())
df31['step'] = df31['доктора наук'] + df31['кандидата наук']
df31['nestep'] = df31['Всего, человек'] - df31['step']
df31a = df31.drop(labels=[0,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,24,25,27,26,28,29,30,31,32,33,34,35],axis=0)
df31b = df31.drop(labels=[0,1,2,3,4,5,6,7,8,9,19,20,21,22,23,24,25,27,26,28,29,30,31,32,33,34,35],axis=0)

print(df31a.keys())
print(df31b)


colors = {
    'background': '#002b36',
    'text': '#7FDBFF'
}

# 1.2 образовательные программы
fig12op = px.pie(
    df12,
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
    df12,
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
fig211priem = px.bar(df211.sort_values(by=['УГС']),
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
fig211mean1 = px.bar(df211b,
              # x=df2["уровень"],
              # x='ТИП',
              x=['бакалавриат'],
              color="ТИП",
              title="Баллы приема на бакалавриат",
              labels={"value": "баллы", "index": "тип"},
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
fig211mean2 = px.bar(df211b,
              # x=df2["уровень"],
              # x='ТИП',
              x=['специалитет'],
              color="ТИП",
              title="Баллы приема на специалитет",
              labels= {"value": "баллы", "index": "тип"},
              color_discrete_sequence=px.colors.sequential.RdBu
)
fig211mean2.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

fig212kont = px.bar(df212b,
                    x=['all'],
                    y='тип',
                    title="Контингент г.Владиаосток по курсам",
                    color='тип',
                    color_discrete_sequence=px.colors.sequential.RdBu
)
fig212kont.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# Контингент 212
fig212kontb = go.Figure()
fig212kontb.add_trace(go.Bar(
  y= df212b['all'],
  x= df212b['тип'],
  name= "всего",
  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig212kontb.add_trace(go.Bar(
  y=df212b['очная бакалавриат'],
  x=df212b['тип'],
  name="очная бакалавриат",
))
fig212kontb.add_trace(go.Bar(
  y= df212b['очная магистратура'],
  x= df212b['тип'],
  name = "очная магистратура",
))
fig212kontb.update_layout(title_text="Multi-category axis")
fig212kontb.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# Выпуск и ожидаемый выпуск
fig213 = go.Figure()
fig213.add_trace(go.Bar(
  y=df213[1][:4],
  x=['всего', 'инв', 'бюджет', 'договор'],
  name="выпуск",
  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig213.add_trace(go.Bar(
  y=df213[1][4:8],
  # x= df213['index'][4:7],
  x=['всего', 'инв', 'бюджет', 'договор'],
  name="ожидаемый",
  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig213.update_layout(title_text="выпуск/ожидаемый выпуск")
fig213.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# 2.13 тетки
fig213b = px.pie(
    df213b,
    values=df213b[0],
    names=df213b['index'],
    color_discrete_sequence=px.colors.sequential.RdBu,
    # width=500,
    # height=500,
    hole=0.5,
    title='выпуск по полам'
)
fig213b.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})





figMAP_priem = px.choropleth(df2_11, locations='iso_alpha', color='Принято – всего', hover_name='country',
                       color_continuous_scale=px.colors.sequential.Reds, projection='equirectangular')
figMAP_priem.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
figMAP_kont = px.choropleth(df2_11, locations='iso_alpha', color='контингент – всего', hover_name='country',
                       color_continuous_scale=px.colors.sequential.Reds, projection='equirectangular')

figMAP_kont.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})



# контингент по полу и возрасту
fig2_12 = go.Figure()
fig2_12.add_trace(go.Bar(
  y=df2_12['kont_male'],
  x=df2_12['возраст'],
  name="муж",

  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig2_12.add_trace(go.Bar(
    y=df2_12['контингент -женщины'],
    x=df2_12['возраст'],
    name="жен",
    # color_discrete_sequence=px.colors.sequential.RdBu
))
fig2_12.update_layout(title_text="контингент по полу и возрасту")
fig2_12.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# выпуск по полу и возрасту
fig2_12b = go.Figure()
fig2_12b.add_trace(go.Bar(
  y=df2_12['vipusk_male'],
  x=df2_12['возраст'],
  name="муж",

  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig2_12b.add_trace(go.Bar(
    y=df2_12['выпуск - женщины'],
    x=df2_12['возраст'],
    name="жен",
    # color_discrete_sequence=px.colors.sequential.RdBu
))
fig2_12b.update_layout(title_text="выпуск по возрасту и полу")
fig2_12b.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})

# 3.1 сотрудники
fig31 = px.pie(
    df31a,
    values=df31a['Всего, человек'],
    names=df31a['Наименование показателей'],
    color_discrete_sequence=px.colors.sequential.RdBu,
    # width=500,
    # height=500,
    hole=0.5,
    title='Персонал'
)
fig31.update_layout({
    'plot_bgcolor': colors['text'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})
# 3.1 остепенненность
fig31c = go.Figure()
fig31c.add_trace(go.Bar(
  y=df31b['nestep'],
  x=df31b['Наименование показателей'],
  name="неостепененный",

  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig31c.add_trace(go.Bar(
    y=df31b['step'],
    x=df31b['Наименование показателей'],
    name="остпененные",
    # color_discrete_sequence=px.colors.sequential.RdBu
))
fig31c.update_layout(title_text="остепененность")
fig31c.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})


# 3.1 Половой состав сотрудников
# выпуск по полу и возрасту
fig31b = go.Figure()
fig31b.add_trace(go.Bar(
  y=df31a['мужчины'],
  x=df31a['Наименование показателей'],
  name="муж",

  # color_discrete_sequence=px.colors.sequential.RdBu
))
fig31b.add_trace(go.Bar(
    y=df31a['женщины'],
    x=df31a['Наименование показателей'],
    name="жен",
    # color_discrete_sequence=px.colors.sequential.RdBu
))
fig31b.update_layout(title_text="персонал и пол")
fig31b.update_layout({
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {
        'color': colors['text']
    }
})



# figMAP_vipusk = px.choropleth(df2_11, locations='iso_alpha', color='Выпуск – всего', hover_name='country',
#                        color_continuous_scale=px.colors.sequential.Plasma, projection='equirectangular')

# figMAP = go.Figure(go.Scattergeo())
# figMAP.update_geos(projection_type="natural earth")
# figMAP.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})


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
        style={'width': '45%', 'display': 'inline-block'}
    ),

# средние значения приема спец
    html.Div([
        dcc.Graph(
            id='graph5',
            figure=fig211mean2,
        )],
        style={'width': '45%', 'display': 'inline-block'}
    ),

# контингент ДВФУ пл годам
    html.Div([
        dcc.Graph(
            id='graph7',
            figure={
                'data': [
                    {'x': [2017, 2018, 2019, 2020, 2021, 2022], 'y': [23347, 22537, 20370, 18174, 17969, 19094],
                     'type': 'bar', 'name': 'Контингент'},
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
        style={'width': '30%', 'display': 'inline-block'}
    ),

# таблица 2.1.2
    html.Div([
        dcc.Graph(
            id='graph6',
            figure=fig212kont,
        )],
        style={'width': '30%', 'display': 'inline-block'}
    ),

# таблица 2.1.2
    html.Div([
        dcc.Graph(
            id='graph66',
            figure=fig212kontb,
        )],
        style={'width': '30%', 'display': 'inline-block'}
    ),

# таблица 2.1.3
    html.Div([
        dcc.Graph(
            id='graph66',
            figure=fig213,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),

# таблица 2.1.3b круг по полам
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig213b,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),

    html.Div([
        dcc.Graph(figure=figMAP_priem)
    ],
    style={'width': '50%', 'display': 'inline-block'}
    ),
    html.Div([
        dcc.Graph(figure=figMAP_kont)
    ],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # контингент по полу и возрасту
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig2_12,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # выпуск по полу и возрасту
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig2_12b,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # 3.1
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig31,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # 3.1с
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig31c,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # 3.1b
    html.Div([
        dcc.Graph(
            # id="graph2",
            figure=fig31b,
        )],
        style={'width': '50%', 'display': 'inline-block'}
    ),
    # html.Div([
    #     dcc.Graph(figure=figMAP_vipusk)
    # ],
    #     style={'width': '33%', 'display': 'inline-block'}
    # ),

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

])
