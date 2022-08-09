# Importing the libraries

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Creating the app
app = Dash(__name__)

# importing the dataframe
df = pd.read_csv("C:\\Users\\vijay\\Downloads\\fossil-fuel-co2-emissions-by-nation_csv.csv")

# creating a list of dictionaries :
year_list = []
for i in range(1751, 2015):
    year_dict = {}
    year_dict["label"] = str(i)
    year_dict["value"] = i
    year_list.append(year_dict)

# App layout
app.layout = html.Div([

    html.H1("Total Usage of fossil fuels based on countries", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=year_list,
                 multi=False,
                 value=2014,
                 style={'width': "40%"}
                 ),
    # dcc.Slider(min=1751, max=2014, step=1, value=2014, id='slct_year'),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# App callback
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    container = "The year chosen by user is: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='country names',
        locations='Country',
        scope="world",
        color='Total',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        # labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        # template='plotly_dark'
    )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

