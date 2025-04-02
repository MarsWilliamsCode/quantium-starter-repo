from click import style
from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('./data/final_daily_sales_data.csv')
fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales by Date', style={'textAlign': 'center'}),
    html.Div([
        html.H3("Filter by Area:"),
        dcc.RadioItems(
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': ''}
            ],
            value='',
            inline=True,
            id='area_radio',
        )
    ], style={'display': 'flex',
              'flex-direction':'row',
              'justify-content': 'center',
              'align-items': 'center',
              'font-family': 'Barlow, serif'}),
    html.Div([
        dcc.Graph(
            id='sales-graph',
     )
    ], style={'width': '80%', 'display': 'inline-block', 'padding-left': '10%'}),

], style = {})
@callback(
    Output('sales-graph', 'figure'),
    Input('area_radio', 'value'))
def update_graph(area_value):
    if area_value != '':
        filtered_df = df[df['region'] == area_value]
        fig = px.line(filtered_df, x="date", y="sales")
    else:
        fig = px.line(df, x="date", y="sales")
    return fig



if __name__ == '__main__':
    app.run(debug=True)