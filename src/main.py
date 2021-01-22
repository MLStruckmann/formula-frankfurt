import argparse
import json

from flask import Flask, Response, render_template
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from stream_analysis.motion_detection.model_dash_integration import Detector, gen
from azure_.az_storage.cosmos_data import upload_cosmos, download_cosmos
from frontend.apps import high_score_table
from frontend.apps.race_management_frontend import default_layout, prerace_layout, race_layout, postrace_layout

from race_management.race_management import create_drivers, run_race
import random 
import string 

# Read config
with open('src/config.json', 'r') as fp:
    config = json.load(fp)

print('Session Name: ' + config['session_name'])

# Test Data Download
drivers = download_cosmos(config['azure_cosmos_key'])

print(drivers)

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

@server.route('/video_feed')
def video_feed():
    a = gen(Detector(r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\weights\last.pt", 
    r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg", 
    r'C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\data_new\names.name', 'cpu', '0'))
    print(type(a))
    return Response(a, mimetype='multipart/x-mixed-replace; boundary=frame')

# def video_feed():
#     frame, det = gen(Detector(r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\weights\last.pt", 
#     r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg", 
#     r'C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\data_new\names.name', 'cpu', '0'))
#     print(det)
#     return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')

# @server.route('/high_score_table')
# def high_score_table():
#     return high_score_table(download_cosmos())

app.layout = html.Div([
    html.Div(id = 'driver-1-frontend-storage', style = {'display':'none'}),
    html.Div(id = 'driver-2-frontend-storage', style = {'display':'none'}),
    html.H1("Hallo meine lieben Leute"),
    html.Img(src="/video_feed"),
    html.Div(default_layout(), id = 'race-mgmt'),
    html.Div(high_score_table.layout(download_cosmos(config['azure_cosmos_key']))),
    dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
    )
])

@app.callback([Output('race-mgmt', 'children'),
               Output('driver-1-frontend-storage', 'children'),
               Output('driver-2-frontend-storage', 'children')],
              [Input('submit-drivers-button', 'n_clicks')],
              [State('driver-1-name-input', 'value'),
               State('driver-2-name-input', 'value')]) 
def to_prerace(n_clicks, driver_1_name, driver_2_name):

    driver1, driver2 = create_drivers(driver_1_name, driver_2_name, config['session_name'])

    return prerace_layout(driver1, driver2), driver1.to_dict(as_json = True), driver2.to_dict(as_json = True)

# @app.callback(Output('race-mgmt', 'children'), #driver-frontend, children?
#               Input('submit-drivers-button', 'n_clicks'),
#               State('driver-frontend',)) #value/value
# def to_race(n_clicks, driver_1_name, driver_2_name):

#     return race_layout(driver1, driver2), [driver1, driver2]

# def to_postrace(..):

#     # upload_data(driver1, driver2)

#     return postrace_layout(driver1,driver2)

# def to_default(..):

#     # refresh high scores
    
#     return default_layout
    

# @app.callback(Output('tracking-vis', 'children'),
#               Input('interval-component', 'n_intervals'))
# def update_ticker
name_driver1, name_driver2 = ''.join(random.choice(string.ascii_lowercase) for i in range(4)),''.join(random.choice(string.ascii_lowercase) for i in range(4))

driver1, driver2 = create_drivers(name_driver1, name_driver2, config['session_name'])



if __name__ == '__main__':

    # construct the argument parser and parse command line arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--ip", type=str, required=True,
    #     help="ip address of the device")
    # ap.add_argument("-o", "--port", type=int, required=True,
    #     help="ephemeral port number of the server (1024 to 65535)")
    # ap.add_argument("-f", "--frame-count", type=int, default=32,
    #     help="# of frames used to construct the background model")
    # args = vars(ap.parse_args())

    # Run Dashboard
    app.run_server(debug=False)

    print('this runs')