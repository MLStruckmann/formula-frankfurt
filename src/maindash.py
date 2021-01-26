import dash
from flask import Flask

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# Create recent location storage
recent_locations = [(0,0),(100,100),(200,200),(300,300),(400,400)]