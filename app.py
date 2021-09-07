import dash
import dash_core_components as dcc
import dash_html_components as html
from views.fig_test import figB, figC
import plotly.graph_objs as go

import math
import pandas as pd
import datetime


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ["https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={'backgroundColor': '#000000'},
           #'max-width': '1600px',
           #'margin': '0 auto'},
    children=[
        html.H5(children=f'{datetime.datetime.now().strftime("%Y-%m-%d, %H: %M: %S")}'),
        html.H1(children='A Gapminder Replica with Dash'),

        html.Div(style={'backgroundColor': '#ffffff',
                        'height': '20px',
                        'margin': '0 auto'}),
        dcc.Graph(id='gapminder',
                  animate=True
                  ),

        html.H1(children='A Gapminder Replica with Dash'),
        html.Div(children='Dash: A web application framework for Python.', style={
            'textAlign': 'center',
            'color': '#ffffff'
        }),
        html.Div(className='col-sm-6',
                 children=dcc.Graph(
                     figure=figC
                 ), ),
        html.Div(className='col-sm-6',
                 children=dcc.Graph(
                     figure=figC
                 ), ),
        html.Div(className='col-sm-4',
                 children=dcc.Graph(
                     figure=figB
                 ), ),
        html.Div(className='col-sm-4',
                 children=dcc.Graph(
                     figure=figB
                 ), ),
        html.Div(className='col-sm-4',
                 children=dcc.Graph(
                     figure=figC
                 ), ),
        # dcc.Graph(
        #     figure=figB
        # ),
        # dcc.Graph(
        #     figure=figC
        # ),
        # generate_table(df)

    ])

if __name__ == '__main__':
    app.run_server(debug=True)
