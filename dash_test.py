import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('../datamembres.csv')
print('dala loaded into dataframe')

app.layout = html.Div(children = [
    html.H1 ('My first dashbord layout'),

    html.Div ('Data from datamembres')

])

if __name__ == '__main__':
    app.run_server(debug=True)
