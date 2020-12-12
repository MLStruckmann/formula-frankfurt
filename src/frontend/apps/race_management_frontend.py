import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

def default_layout():

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

def prerace_layout(driver1, driver2):

    text = 'Hallo ihr alten Luschen ' + driver1.driver_name + ' und ' + driver2.driver_name + ' wollt ihr noch ne Runde???'
    start_race_button = dbc.Button("Primary", outline=True, color="primary", className="mr-1", id = 'start-race-button')
    layout = html.Div([html.H1(text),start_race_button])
    return layout

def race_layout():

    layout = ''
    return layout

def postrace_layout():

    layout = ''
    return layout