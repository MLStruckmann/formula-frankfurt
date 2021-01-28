from maindash import app, server, get_config

from datetime import datetime
from race_management.data_gathering import read_sensor
from race_management.race_statistics import create_drivers, run_race
from car_steering.voltage_control import send_signal
from azure_dummy.az_storage.cosmos_data import upload_cosmos #TODO use real azure

import random
import string
import serial
import json

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

def rm_form():

    driver1_input = dbc.FormGroup(
        [
            dbc.Label("Driver 1 Name:", html_for="driver-1-name", width=2),
            dbc.Col(
                dbc.Input(
                    type="text", 
                    id="driver-1-name-input", 
                    placeholder="Enter Driver 1 Name"
                ),
            ),
        ],
        row=True,
    )

    driver2_input = dbc.FormGroup(
        [
            dbc.Label("Driver 2 Name:", html_for="driver-2-name", width=2),
            dbc.Col(
                dbc.Input(
                    type="text",
                    id="driver-2-name-input",
                    placeholder="Enter Driver 2 Name"
                ),
            ),
        ],
        row=True,
    )

    start_race_button = dbc.Button("Start Race!", color="primary", className="mr-1", id='start-race-button')
    form = dbc.Form([driver1_input, driver2_input])
    layout = html.Div([form, start_race_button])
    return layout 

# def rm_prerace_layout(driver1, driver2):

#     text = 'Ready to race with ' + driver1.driver_name + ' and ' + driver2.driver_name + '!'
#     start_race_button = dbc.Button("Start Race", outline=True, color="primary", className="mr-1", id = 'start-race-button')
#     layout = html.Div([html.H1(text),start_race_button])
#     return layout

def rm_race_layout(driver_1_name, driver_2_name):

    text = 'Race between ' + driver_1_name + ' and ' + driver_2_name
    layout = html.Div(html.H1(text))
    return layout

def rm_norace_layout():

    layout = html.Div(html.H1('No Race'))
    return layout

@app.callback(Output('race-mgmt-2', 'children'),
              [Input('start-race-button', 'n_clicks')],
              [State('driver-1-name-input', 'value'),
               State('driver-2-name-input', 'value')],
               prevent_initial_call = True) 
def rm2_callback(b1_n_clicks, d1, d2):

    #config = get_config()

    # global driver1, driver2

    return rm_race_layout(d1, d2)

    # button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # print(button_id)

    #return rm_race_layout(), {'display':'none'} #, html.Div(html.H1('whatever'))#driver1, driver2) #json.dumps({'ongoing':'1'})#, driver1.to_dict(as_json = True), driver2.to_dict(as_json = True)

@app.callback(Output('race-mgmt-3', 'children'),
              [Input('race-mgmt-2', 'children')],
              [State('driver-1-name-input', 'value'),
               State('driver-2-name-input', 'value')],
               prevent_initial_call = True) 
def racing_call(n_clicks, driver_1_name, driver_2_name):

    config = get_config()

    lap_number = int(config['lap_number'])
    signal_limit = int(config['signal_limit'])
    buffer_time = int(config['buffer_time'])

    driver1, driver2 = create_drivers(driver_1_name, driver_2_name, config['session_name'])

    auto_driver = "Neither"

    if driver1.driver_name == 'AUTO':
            auto_driver = 'L'
    elif driver2.driver_name == 'AUTO':
            auto_driver = 'R'

    driver1, driver2 = run_race(driver1, driver2, lap_number, auto_driver, signal_limit, buffer_time)

    driver1.calculate_metrics()
    driver2.calculate_metrics()

    print(driver1.driver_name, driver2.driver_name)

    race_data = [driver1.to_dict(for_azure = True),
                 driver2.to_dict(for_azure = True)] #TODO test if this is working

    upload_cosmos(race_data)

    return html.Div(html.H1('Race finished. Driver times: \n {}: {} \n {}. {}'.format(driver1.driver_name,
                                                                                    str(driver1.average_lap * lap_number),
                                                                                    driver2.driver_name,
                                                                                    str(driver2.average_lap * lap_number))))