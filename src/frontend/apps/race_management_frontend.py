from maindash import app, server, get_config
from race_management.race_management import create_drivers, run_race

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

def rm_default_layout():

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

    submit_drivers_button = dbc.Button("Submit Drivers", color="primary", className="mr-1", id='submit-drivers-button')
    form = dbc.Form([driver1_input, driver2_input])
    layout = html.Div([form, submit_drivers_button])
    return layout 

def rm_prerace_layout(driver1, driver2):

    text = 'Ready to race with ' + driver1.driver_name + ' and ' + driver2.driver_name + '!'
    start_race_button = dbc.Button("Primary", outline=True, color="primary", className="mr-1", id = 'start-race-button')
    layout = html.Div([html.H1(text),start_race_button])
    return layout

def rm_race_layout():

    layout = ''
    return layout

def rm_postrace_layout():

    layout = ''
    return layout


@app.callback(Output('race-mgmt', 'children'),
              [Input('submit-drivers-button', 'n_clicks')],
              [State('driver-1-name-input', 'value'),
               State('driver-2-name-input', 'value')],
               prevent_initial_call = True) 
def to_prerace(n_clicks, driver_1_name, driver_2_name):

    config = get_config()

    global driver1, driver2

    driver1, driver2 = create_drivers(driver_1_name, driver_2_name, config['session_name'])

    return rm_prerace_layout(driver1, driver2)#, driver1.to_dict(as_json = True), driver2.to_dict(as_json = True)

# @app.callback(Output('race-mgmt', 'children'),
#               [Input('start-race-button', 'n_clicks')],
#                prevent_initial_call = True) 
# def to_race(n_clicks):

#     layout = html.H1('Race ongoing!')

#     print(driver1.driver_name)

#     return layout