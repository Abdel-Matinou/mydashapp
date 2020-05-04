import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from plotly import graph_objs as go

df_tickets = pd.read_csv('/Users/fabriceakalah/Desktop/demandes.csv', encoding = 'macgreek', sep=';')
tickets_place = df_tickets[df_tickets['Produit']=='PLACE']
tickets_mpe = df_tickets[(df_tickets['Produit'] != 'MAXIMILIEN') & (df_tickets['Produit'] != 'PLACE') & (df_tickets['Produit'] != 'TerNum')]



external_stylesheets = [
                            { 'rel' :"stylesheet",
                            'href' : "https://unpkg.com/driver.js/dist/driver.min.css"
                            },
                            { 'href' : "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@900&family=Roboto+Mono:wght@300&display=swap",
                             'rel' : "stylesheet"
                            },
                        ]

external_scripts = [{'src' : "https://unpkg.com/driver.js/dist/driver.min.js"}]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts = external_scripts )

##############################################################################################
# APP BODY #
basic_style = {
    'display':'grid',
    'backgroundColor':'black',
    'text': '#7FDBFF',
}

title = html.Nav(className='grid-item title', children='UTAH ++')
first = html.P(className='grid-item item2', children='Bienvenue sur le dashbord Utah')
left_column = html.Div(className='grid-item left_column', children= [
    html.Div(children = [
            html.H3('Tickets Total'),
            html.Strong(f"{df_tickets.shape[0]}")


            ]),
    html.Div(children= [
            html.H3("Tickets Place"),
            html.Strong(f"{tickets_place.shape[0]}")
                ]
            )

    ])
right_column = html.Div(className='grid-item right_column', children='right_column Here')



app.layout = html.Div(style = basic_style, className = 'grid-Container', children=[
    title, first, left_column, right_column
])


##############################
# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
