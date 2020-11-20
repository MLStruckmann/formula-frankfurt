import dash_table

def layout(df):
    
    table = dash_table.DataTable(
    id='high-score-table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records')
    )

    return table