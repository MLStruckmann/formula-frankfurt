import dash_table
import dash_bootstrap_components as dbc
import pandas as pd

def layout(df):
    
    # table = dash_table.DataTable(
    # id='high-score-table',
    # columns=[{"name": i, "id": i} for i in df.columns],
    # data=df.to_dict('records')
    # )

    table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

    return table