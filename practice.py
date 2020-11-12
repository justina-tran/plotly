## First Example

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.title = "Dash tutorial"

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children='Hello World'),

            html.Div(children='''
                Dash: A web application framework for Python.
            ''')
        ], className = "row"),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization',
                            'xaxis' : dict(
                                title = "x-Axis",
                                titlefont = dict(
                                family = "Courier New, monospace",
                                size = 20,
                                color = "black"
                            )),
                            "yaxis" : dict(
                                title = "y-Axis",
                                titlefont = dict(
                                family = "Courier New, monospace",
                                size = 20,
                                color = "black"
                            ))
                        }
                    }
                )
            ], className = "six columns"),
            
            html.Div([
                dcc.Graph(
                    id='example-graph2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization',
                            'xaxis' : dict(
                                title = "x-Axis",
                                titlefont = dict(
                                family = "Courier New, monospace",
                                size = 20,
                                color = "black"
                            )),
                            "yaxis" : dict(
                                title = "y-Axis",
                                titlefont = dict(
                                family = "Courier New, monospace",
                                size = 20,
                                color = "black"
                            ))
                        }
                    }
                )
            ], className = "six columns")
        ], className = "row")
    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)