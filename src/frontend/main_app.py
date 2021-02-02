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
    '''
        Takes in the components that make up the main layout, and returns them arranged into a grid
        interval: in ms, refresh time for component that updates the grid
    '''

    center_style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}

    layout = html.Div([
            dbc.Row([ # Title row
                        dbc.Col(html.Div([html.Img(src = 'assets/pwc_logo.png',style={'height':'90%'})], style = {'height':'10vh', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}), width = 4),
                        dbc.Col(html.H2('FS x PwC Carrera Dashboard', style = {'height':'10vh', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'})),
                        dbc.Col(html.Div([html.Img(src = 'assets/fs_logo.png',style={'height':'60%'})], style = {'height':'10vh', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}), width = 4),
                    ]),
            dbc.Row(html.Div(style = {'height':'30px'})),
            dbc.Row([ # Cam and Visualization Row
                        dbc.Col(html.Div(video_feed, style = center_style)),
                        dbc.Col(html.Div(track_vis))
                    ]),
            dbc.Row(html.Div(style = {'height':'30px'})),
            dbc.Row([ # Race Management Row
                        dbc.Col(html.Div(rm_form, id = 'race-mgmt', style = center_style), width = 6),
                        dbc.Col(html.Div(html.H3('No Race Ongoing'), id = 'race-mgmt-2', style = center_style), width = 3),
                        dbc.Col(html.Div(html.H3(''), id = 'race-mgmt-3', style = center_style), width = 3)
                    ]),
            dbc.Row([ # High Score Row
                        dbc.Col(html.H1(''), width=3),
                        dbc.Col([html.H2('High Scores', style = center_style),
                                 html.Div(style = {'height':'10px'}),
                                 html.Div(high_score_table)]),
                        dbc.Col(html.H1(''), width=3)
                    ]),
            dbc.Row([ # Interval Component (Invisible)
                        dbc.Col(dcc.Interval(
                                id='interval-component',
                                interval= interval, # in milliseconds
                                n_intervals=0))
                    ]),     
            ],
            )
    
    return layout