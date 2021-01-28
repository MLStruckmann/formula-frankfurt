from maindash import server

import dash_html_components as html
from stream_analysis.motion_detection.model_dash_integration import Detector, gen
from flask import Response
import os
import numpy as np
import cv2

@server.route('/video_feed')
def video_feed():
    # a = gen(Detector(r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\weights\last.pt", 
    # r"C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg", 
    # r'C:\Users\sdicarrera\Documents\formula-frankfurt\src\stream_analysis\motion_detection\data_new\names.name', 'cpu', '0'))
    
    current_path = str(os.getcwd())
    weights_path = current_path + r'\src\stream_analysis\motion_detection\weights\last.pt'
    model_path = current_path + r'\src\stream_analysis\motion_detection\cfg\yolov3-tiny.cfg'
    names_path = current_path + r'\src\stream_analysis\motion_detection\data_new\names.name'

    a = gen(Detector(weights_path, model_path, names_path, 'cpu', '0'))

    return Response(a, mimetype='multipart/x-mixed-replace; boundary=frame')

def serve_feed():
    return html.Img(src="/video_feed")
