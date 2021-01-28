#from maindash import app, server

#from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def layout(video_feed = None, 
           track_vis = None, 
           high_score_table = None, 
           rm_form = None,
           interval = 1000):

    layout = html.Div([
            dbc.Row([
                        dbc.Col(html.Div(video_feed)),
                        dbc.Col(html.Div(track_vis))
                    ]),
            dbc.Row([
                        dbc.Col(html.Div(rm_form, id = 'race-mgmt')),
                        dbc.Col(html.Div(html.H1('No Race'), id = 'race-mgmt-2')),
                        dbc.Col(html.Div(html.H1(''), id = 'race-mgmt-3')),
                        dbc.Col(html.Div(high_score_table)),
                    ]),
            dbc.Row([
                        dbc.Col(dcc.Interval(
                                id='interval-component',
                                interval= interval, # in milliseconds
                                n_intervals=0)),
                                html.Div(id = 'driver-1-frontend-storage', style = {'display':'none'}),
                                html.Div(id = 'driver-2-frontend-storage', style = {'display':'none'}),
                                html.Div(id = 'race-control', style = {'display':'none'})
                    ])
            ])
    
    return layout