import dash
from dash import html, dcc
from selenium.webdriver.chrome.webdriver import WebDriver
from dash import testing


def test_001_header(dash_duo):
    app = dash.Dash()
    app.layout = html.Div(id="header-wrapper", children=[html.H1(children='Pink Morsel Sales by Date', id='header')])
    dash_duo.start_server(app)
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales by Date"
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("test_001_header")

def test_002_radio(dash_duo):
    app = dash.Dash()
    app.layout = html.Div(id="radio_wrapper", children=[dcc.RadioItems(
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
        )])
    dash_duo.start_server(app)
    assert dash_duo.find_element("#area_radio").text == "NorthSouthEastWestAll"

def test_003_visualization(dash_duo):
    app = dash.Dash()
    app.layout = html.Div(id="visualization_wrapper", children=[dcc.Graph(id='sales-graph')])
    dash_duo.start_server(app)
    assert dash_duo.wait_for_element_by_id("sales-graph", timeout=None)

