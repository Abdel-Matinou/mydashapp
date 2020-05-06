import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from plotly import graph_objs as go

df_tickets = pd.read_csv('/Users/fabriceakalah/Desktop/demandes.csv', encoding = 'macgreek', sep=';')
tickets_place = df_tickets[df_tickets['Produit']=='PLACE']
tickets_mpe = df_tickets[(df_tickets['Produit'] != 'MAXIMILIEN') & (df_tickets['Produit'] != 'PLACE') & (df_tickets['Produit'] != 'TerNum')]

xx = df_tickets.Produit.value_counts().to_frame()
xx.reset_index(inplace = True)
xx.columns = ['produit', 'total']
top5_produits = xx[:5]

external_stylesheets = [    'https://codepen.io/chriddyp/pen/bWLwgP.css',
                            { 'href' : "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@900&family=Roboto+Mono:wght@300&display=swap",
                             'rel' : "stylesheet"
                            },
                        ]

#external_scripts = [{'src' : "https://unpkg.com/driver.js/dist/driver.min.js"}]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

title = 'dashbord'
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Utah+</title>
        {%favicon%}
        {%scripts%}
        {%css%}
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

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
    html.Div(id = 'idea', children = [
            html.H3('Tickets Total'),
            html.H4(f"{df_tickets.shape[0]}")


            ]),
    html.Div(children= [
            html.H3("Tickets Place"),
            html.H4(id ='x-total', children = f"{tickets_place.shape[0]}")
                ]
            )

    ])



labels = top5_produits.produit
values = top5_produits.total

fig = go.Figure(data=[go.Pie(labels=labels, values=values),]
                             )


right_column = html.Div(className='grid-item right_column', children= [

                    html.Label('PLATEFORME'),
                    dcc.Dropdown( id = 'x-plateforme',
                        options=[
                            {'label': i , 'value': i } for i in df_tickets['Produit'].unique()
                        ],
                        #value= df_tickets['Produit'].unique()[0],
                        placeholder="Choisir une plateforme",
                    ),

                    dcc.Graph(figure = fig)

                ])



app.layout = html.Div(style = basic_style, className = 'grid-Container', children=[
    title, first, left_column, right_column
])


##############################
# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
