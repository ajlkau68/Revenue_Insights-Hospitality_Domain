from dash import Dash, html, dcc, Output, Input
from components.ids import STATUS_DROPDOWN, MONTH_DROPDOWN, CITY_DROPDOWN, PLATFORM_DROPDOWN
from data.source import DataSource

booking_status = ['Checked Out', 'Cancelled', 'No Show']


def create_status_dropdown(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(STATUS_DROPDOWN, 'value'),
                  [Input(MONTH_DROPDOWN, 'value'),
                   Input(CITY_DROPDOWN, 'value'),
                   Input(PLATFORM_DROPDOWN, 'value')])
    def update_status(months: list[str], cities: list[str], platforms: list[str]) -> list[str]:
        return source.unique_status
    

    return html.Div(
        [
            html.H6('Status', style={'textAlign': 'left', 'fontSize':15}),
            dcc.Dropdown(
                id=STATUS_DROPDOWN,
                options=[{'label':status, 'value':status} for status in booking_status],
                multi=True,
                value=booking_status[0],
            )
        ]
    )

        