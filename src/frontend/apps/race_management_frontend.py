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

    form = dbc.Form([driver1_input, driver2_input])
    layout = html.Div(form)
    return layout 

def prerace_layout():

    layout = ''
    return layout

def race_layout():

    layout = ''
    return layout

def postrace_layout():

    layout = ''
    return layout