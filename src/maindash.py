import dash
from flask import Flask
import dash_bootstrap_components as dbc
import json

server = Flask(__name__)
app = dash.Dash(__name__, 
                server=server, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)

# Recent location storage
recent_locations = [(0,0,0),
                    (100,100,0),
                    (200,200,1),
                    (300,300,0),
                    (400,400,1),
                    (0,100,1),
                    (100,200,0),
                    (200,390,1),
                    (300,243,0),
                    (400,123,1)]

# Read config
def get_config():

    with open('src/config.json', 'r') as fp:
        config = json.load(fp)

    return config