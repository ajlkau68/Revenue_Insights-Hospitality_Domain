from dash import Dash, html, dcc, Output, Input
from components.ids import CITY_DROPDOWN, MONTH_DROPDOWN
from data.source import DataSource


def create_city_dropdown(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(CITY_DROPDOWN, 'value'),
                  Input(MONTH_DROPDOWN, 'value'))
    def update_platforms(months: list[str]) -> list[str]:
        return source.unique_cities

    return html.Div(
        [
            html.H6('City', style={'textAlign': 'left', 'fontSize':15}),
            dcc.Dropdown(
                id=CITY_DROPDOWN,
                options=[{'label':city, 'value':city} for city in source.unique_cities],
                multi=True,
                clearable=False,
                value=source.unique_cities,
            )
        ]
    )

        