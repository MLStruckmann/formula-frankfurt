from maindash import app, recent_locations
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output



def layout():

    [x, y] = list(map(list, zip(*recent_locations)))

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
    fig.update_xaxes(range=[0, 640])
    fig.update_yaxes(range=[480, 0])
    
    return html.Div([dcc.Graph(figure=fig, id = 'pos-vis')])

@app.callback(Output('pos-vis', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_position_vis(n_intervals):

    [x, y] = list(map(list, zip(*recent_locations)))

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
    fig.update_xaxes(range=[0, 640])
    fig.update_yaxes(range=[480, 0])

    return fig
