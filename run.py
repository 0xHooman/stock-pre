import dash_bootstrap_components as dbc
import dash

app = dash.Dash(__name__)

app.layout = dbc.Row(
    dbc.Col("Column 1", width=4, style={'padding': '0'}),
    dbc.Col("Column 2", width=4, style={'padding': '0'}),
    dbc.Col("Column 3", width=4, style={'padding': '0'}),
)

if __name__ == '__main__':
    app.run_server(debug=True)
