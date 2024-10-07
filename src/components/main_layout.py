from dash import html, Dash 
import dash_bootstrap_components as dbc 
from components.month_dropdown import create_month_dropdown
from components.city_dropdown import create_city_dropdown
from components.platform_dropdown import create_platfrom_dropdown
from components.status_dropdown import create_status_dropdown
from components.header import create_header
from components.text_cards import create_small_cards
from components.data_table import create_table
from components.revenue_bar_chart import create_revenue_bar_chart
from components.bookings_bar_chart import create_bookings_bar_chart
from components.ratings_bar_chart import create_ratings_bar_chart
from components.daytype_bar_chart import create_day_type_bar_chart
from components.platform_bar_chart import create_platform_bar_chart
from data.source import DataSource



def create_layout(app: Dash, source: DataSource):
    return dbc.Container([
    # Header row
    dbc.Row([
        dbc.Col(create_header(app))
    ],className='mb-3 mt-2', 
    style={'backgroundColor':'skyblue', 'padding':'5px'}),
    # Dropdowns
    dbc.Row([
        dbc.Col([create_city_dropdown(app, source)],width=3),
        dbc.Col([create_platfrom_dropdown(app, source)], width=3),
        dbc.Col([create_status_dropdown(app, source)], width=3),
        dbc.Col([create_month_dropdown(app, source)], width=3)
    ],className='mb-3'),
    # Metrics Cards
    dbc.Row([
        create_small_cards(app, source)
    ],className='mb-3'),
    # Text split by city
    dbc.Row([
        dbc.Col(html.H6('Split by City'))
    ],className='mb-1'),
    # Graphs Split by City
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_revenue_bar_chart(app, source),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_bookings_bar_chart(app, source),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_ratings_bar_chart(app, source),
                ])
            ]),
        ], width=4),
    ],className='mb-3'),
    # Graph
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_day_type_bar_chart(app, source),
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_platform_bar_chart(app, source),
                ])
            ]),
        ], width=6),
        
    ],className='mb-3'),
    # Table and Graph Row
    dbc.Row([
        dbc.Col([
           dbc.Card([
                dbc.CardHeader(html.H6('Property by Key Metrics'), style={'backgroundColor':'white'}),
                html.Div([
                    create_table(app, source)
                    ], style={'backgroundColor':'white'})
                ])
            ], width=12)
        
    ],className='mb-3'),
    
    ], fluid=True)
