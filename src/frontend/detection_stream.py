from maindash import server

import dash_html_components as html
from stream_analysis.motion_detection.model_dash_integration import Detector, gen
from flask import Response
import os
import numpy as np
import cv2

@server.route('/video_feed')
def video_feed():
    
    # Find paths to model weights, model, and class names
    current_path = str(os.getcwd())
    weights_path = current_path + r'\src\stream_analysis\motion_detection\weights\last.pt'
    model_path = current_path + r'\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg'
    names_path = current_path + r'\src\stream_analysis\motion_detection\data_new\names.name'

    # Initiate generator
    a = gen(Detector(weights_path, model_path, names_path, 'cpu', '0'))

    # Return Flask response
    return Response(a, mimetype='multipart/x-mixed-replace; boundary=frame')

# Wrap feed into HTML element
def serve_feed():
    return html.Img(src="/video_feed")
