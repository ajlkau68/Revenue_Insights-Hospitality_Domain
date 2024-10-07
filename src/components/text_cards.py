from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from components.ids import REVENUE_CARD, OCCUPANCY_CARD, RATINGS_CARD, BOOKINGS_CARD, CANCEL_CARD
from components.ids import HOTEL_CARD, MONTH_DROPDOWN, CITY_DROPDOWN, TEXT_CARDS
from data.source import DataSource


def create_small_cards(app:Dash, source: DataSource) -> html.Div:

    @app.callback([Output(REVENUE_CARD, 'children'),
                   Output(OCCUPANCY_CARD, 'children'),
                   Output(RATINGS_CARD, 'children'),
                   Output(BOOKINGS_CARD, 'children'),
                   Output(CANCEL_CARD, 'children'),
                   Output(HOTEL_CARD, 'children')],
                   [Input(MONTH_DROPDOWN, 'value'),
                    Input(CITY_DROPDOWN, 'value')])
    def update_text_cards(months: list[str], cities: list[str]) -> html.Div:
        filtered_source = source.filter(months, cities)
        
        if not filtered_source.row_count:
            return ['0', '0', '0', '0', '0', '0']
        else:
            return filtered_source.get_text_data()


    return html.Div(
        [
            dbc.Col([
                dbc.Card([
                    # Revenue Card
                    dbc.CardBody([
                        html.H6('Revenue ($)', style={'fontSize':15}),
                        html.H2(id=REVENUE_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Occupancy %
                    dbc.CardBody([
                        html.H6('Occupancy %', style={'fontSize':15}),
                        html.H2(id=OCCUPANCY_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Average Rating
                    dbc.CardBody([
                        html.H6('Average Rating', style={'fontSize':15}),
                        html.H2(id=RATINGS_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Bookings
                    dbc.CardBody([
                        html.H6('Bookings', style={'fontSize':15}),
                        html.H2(id=BOOKINGS_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Cancellation %
                    dbc.CardBody([
                        html.H6('Cancellation %', style={'fontSize':15}),
                        html.H2(id=CANCEL_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # No. of Hotels
                    dbc.CardBody([
                        html.H6('No. of Hotels', style={'fontSize':15}),
                        html.H2(id=HOTEL_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'skyblue', 'padding':'2px'}),
            ], class_name='two columns'),
        ], className='row ms-0', id=TEXT_CARDS
    )