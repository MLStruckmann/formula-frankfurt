import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from flask import Flask, Response
import numpy
from cv2 import cv2

import random

class VideoCamera(object):
    def __init__(self):
        print('in')
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        #print(type(image))
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_number(self):
        return random.uniform(-2.0, 2.0)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def number_gen(camera):
    while True:
        number = camera.get_number()
        return number

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

@server.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    number = number_gen(VideoCamera())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Random number: {0:.2f}'.format(number), style=style)
    ]

app.layout = html.Div([
    html.H1("Webcam Test"),
    html.Img(src="/video_feed"),
    html.Div(id='live-update-text'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

print('testing permissions')