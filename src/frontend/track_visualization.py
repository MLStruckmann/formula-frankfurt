from maindash import app, recent_locations, get_config
import plotly.graph_objects as go
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def layout(aspect_ratio):

    [x, y, labels] = list(map(list, zip(*recent_locations)))

    layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker = dict(size = 10, color = labels)),
                    layout = layout)
    # normal range would be [0,1280] and [720,0] but margins are added
    fig.update_xaxes(range=[-20, 1300], showgrid = True, gridcolor = 'lightgrey')
    fig.update_yaxes(range=[740, -20], showgrid = True, gridcolor = 'lightgrey')
    
    return html.Div([dcc.Graph(figure=fig, id = 'pos-vis')])

@app.callback(Output('pos-vis', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_position_vis(n_intervals):

    # config = get_config()

    # aspect_ratio = config['camera_aspect_ratio'] #TODO

    [x, y, labels] = list(map(list, zip(*recent_locations)))

    layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker = dict(size = 10, color = labels)),
                    layout = layout)
    # normal range would be [0,1280] and [720,0] but margins are added
    fig.update_xaxes(range=[-20, 1300], showgrid = True, gridcolor = 'lightgrey')
    fig.update_yaxes(range=[740, -20], showgrid = True, gridcolor = 'lightgrey')

    return fig
