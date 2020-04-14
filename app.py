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
import dash_bootstrap_components as dbc

exec(open("backend.py").read())
print(solution_df)
pd.options.display.float_format = 'R {:,.2f}'.format

# %% App Layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# %% Parameters

params = [
    'Name', 'Age', 'Salary', 'Interest', 'Rental', 'Capital Gains', 'Local Dividends', 'Foreign Dividends', 'RA Contribution'
]


dt_col_param = []

for col in solution_df.columns:
    dt_col_param.append({"name": str(col), "id": str(col)})


# %% UI Components

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [dbc.Col(
                        dbc.NavbarBrand("B601 Business Tools")
                    ),
                ],
                align="center",
                no_gutters=True,
            )
        )        
    ],         
    color="dark",
    dark=True,
    sticky="top",
)

LEFT_COLUMN = dbc.Jumbotron(
        html.H4(children="Tax Optimization Tool")
)

FAMILY_INPUT = [
    dbc.CardHeader(html.H4(children="Input")),
    dbc.CardBody(
        [
            dbc.Table.from_dataframe(solution_df, id='family_table', striped=True, bordered=True, hover=True)
        ],
        style={"marginTop": 0, "marginBottom": 0},
    ),
]
    
BODY = dbc.Container(
    [
     dbc.Row(
                [
                 dbc.Col(LEFT_COLUMN,width=3),
                 dbc.Col(FAMILY_INPUT,width=9)
                ],
                style={"marginTop": 40}
     ),
     
    ]
)    

# %% App

app.layout = html.Div([NAVBAR, BODY])

# $$ Callbacks



if __name__ == "__main__":
    app.run_server()