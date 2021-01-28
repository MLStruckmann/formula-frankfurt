from maindash import app, recent_locations, get_config
import plotly.graph_objects as go
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def layout(aspect_ratio):

    config = get_config()

    [x, y, labels] = list(map(list, zip(*recent_locations)))

    # matrix = np.array(dict(config['transformation_matrix'])) #TODO load np array from json
    # shift = np.array([[matrix[0][0], matrix[0][1]],[matrix[1][0], matrix[1][1]]])
    # transpose = np.array([matrix[0][2], matrix[1][2]])

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker = dict(size = 10, color = labels)))
    fig.update_xaxes(range=[0, 1280])
    fig.update_yaxes(range=[720, 0])
    
    return html.Div([dcc.Graph(figure=fig, id = 'pos-vis')])

@app.callback(Output('pos-vis', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_position_vis(n_intervals):

    config = get_config()

    aspect_ratio = config['aspect_ratio'] #TODO

    [x, y, labels] = list(map(list, zip(*recent_locations)))

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker = dict(size = 10, color = labels)))
    fig.update_xaxes(range=[0, 1280])
    fig.update_yaxes(range=[720, 0])

    return fig
