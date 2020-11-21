import argparse
import json

from flask import Flask, Response, render_template
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from stream_analysis.motion_detection.model_dash_integration import Detector, gen
from azure_dummy.az_storage.download_cosmos_data import download_cosmos
from frontend.apps import high_score_table

# Read config
# with open('config.json', 'r') as fp:
#     data = json.load(fp)

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
    html.H1("Hallo meine lieben Leute"),
    html.Img(src="/video_feed"),
    html.Div(high_score_table.layout(download_cosmos())),
    # dcc.Interval(
    #         id='interval-component',
    #         interval=5*1000, # in milliseconds
    #         n_intervals=0
    # )
])

# @app.callback(Output('high-score-table', 'children'),
#               Input('interval-component', 'n_intervals'))
# def update_ticker

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
    app.run_server(debug=True)

    print('this runs')