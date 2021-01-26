import dash
from flask import Flask
import dash_bootstrap_components as dbc
import json

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Recent location storage
recent_locations = [(0,0),(100,100),(200,200),(300,300),(400,400)]

# Read config
def get_config():

    with open('src/config.json', 'r') as fp:
        config = json.load(fp)

    return config