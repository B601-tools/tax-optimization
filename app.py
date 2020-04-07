# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:39:47 2020

@author: Mutahi.Wachira
"""

# %% Importing
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

# %% App Layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# %% Text Blocks

intro_text = '''
Tax Optimizer 
=========

This is a tool which allows high net worth individuals to withdraw their
income from various funds and trusts in a way which minimizes the overall tax payable.
It is particularly suited to families with access to trusts in common. The software is
compliant with regulations regarding tax and calculates total tax payable according to the law.

'''

# %% Parameters

params = [
    'Name', 'Age', 'Salary', 'Interest', 'Rental', 'Capital Gains', 'Local Dividends', 'Foreign Dividends', 'RA Contribution'
]

# %% UI

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.layout = html.Div(children = [
        html.H1(children = "Tax Minimizer"),
        html.Div(dcc.Markdown(intro_text)),        
        html.Div([
            dash_table.DataTable(
                id='table-editing-simple',
                columns=(
                    [{'id': p, 'name': p} for p in params]
                ),
                data=[
                    dict(Model=i, **{param: 0 for param in params})
                    for i in range(1, 5)
                ],
                editable=True
            )
        ]),
                
        dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'KC'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'ME'},
                    ],
                    'layout': {
                        'title': 'Tax Paid per Trust'
                    }
                }
            ),
        

        ])

if __name__ == '__main__':
    app.run_server()