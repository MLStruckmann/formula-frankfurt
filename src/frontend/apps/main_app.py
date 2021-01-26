from maindash import app, server
from dash.dependencies import Input, Output

import dash_core_components as dcc
import dash_html_components as html

def layout(video_feed = None, track_vis = None, interval = 1000):
    
    return html.Div([
        video_feed,
        track_vis,
        dcc.Input(id='my-id', value='initial value', type='text'),
        html.Div(id='my-div'),
        dcc.Interval(
        id='interval-component',
        interval= interval, # in milliseconds
        n_intervals=0)
    ])