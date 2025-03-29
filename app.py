
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('./data/final_daily_sales_data.csv')

fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales by Date', style={'textAlign': 'center'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)