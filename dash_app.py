import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df_tickets = pd.read_csv('/Users/fabriceakalah/Desktop/demandes.csv', encoding = 'macgreek', sep=';')
tickets_place = df_tickets[df_tickets['Produit']=='PLACE']
tickets_mpe = df_tickets[(df_tickets['Produit'] != 'MAXIMILIEN') & (df_tickets['Produit'] != 'PLACE') & (df_tickets['Produit'] != 'TerNum')]


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

##############################################################################################
# APP BODY #

## NAVBAR
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("A propos", href="#")),
    ],
    brand="UTAH ++",
    brand_href="#",
    color="#337ab7",
    dark=True,
)

##NAVBAR END

welcome = html.H2('Bienvenue sur le dashbord d\'utah', style =
                    {
                    "textAlign": 'center',
                    "margin" : '30px',
                    'textTransform' : 'uppercase'
                    }
                )

###### CSV UPLOAD

###### CSV UPLOAD END

######---FIRST ROW OF INFORMATION ---

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Tickets Total", className="card-title"),
            html.H4(f"{df_tickets.shape[0]}"),
        ]
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Tickets Place", className="card-title"),
            html.H4(f"{tickets_place.shape[0]}"),
        ]
    )
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Tickets MPE", className="card-title"),
            html.H4(f"{tickets_mpe.shape[0]}"),
        ]
    )
)


# time_card = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5("Etendue temporel", className="card-title"),
#             html.P(
#                 f"Le plus ancien ticket date du : {df_tickets['Date de création'].min()} "
#             ),
#             html.P(
#                 f"Le plus récent ticket date du : {df_tickets['Date de création'].max()}"
#             ),
#         ]
#     )
# )
cards = dbc.Row([dbc.Col(first_card), dbc.Col(second_card), dbc.Col(third_card)])

######---FIRST ROW END

####################
#### DROPDOWN AND GRAPH

dropdown = html.Div([html.Label('Plateforme'),
dcc.Dropdown(
    options=[
            {'label': 'Tous', 'value': 'df_tickets'},
            {'label': 'Place', 'value': 'tickets_place'},
            {'label': 'Mpe', 'value': 'tickets_mpe'}
        ],
    value=['df_tickets'],
    multi=False
        ),
        ])

#### DROPDOWN END

app.layout = dbc.Container(children = [
                    html.Div(navbar), welcome, cards,
                    html.Br(), dropdown


    # dbc.Row([
    #     html.H2(f"Total tickets : {df.shape[0]-1}"),
    #
    #     html.H2(f"Total agents : {len(df['Agent support en charge'].unique())}"),
    # ])

])




##############################
# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
