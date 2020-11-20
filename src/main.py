import argparse
import json

from flask import Flask, Response, render_template
import dash
import dash_html_components as html

from stream_analysis.motion_detection.model_dash_integration import Detector, gen

# Read config
with open('config.json', 'r') as fp:
    data = json.load(fp)

# Start Detector

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

@server.route('/video_feed')
def video_feed():
    return Response(gen(Detector(r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\weights\last.pt", 
                                 r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg", 
                                 r'C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\data_new\names.name', 'cpu', '0')), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# @server.route('/dashboard')
# def dashboard():
# 	return dashboard.layout

app.layout = html.Div([
    html.H1("Wenn das läuft lutsch ich mir selber einen ab"),
    html.Img(src="/video_feed")
])

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