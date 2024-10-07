from dash import Dash, html, dcc, Output, Input
from components.ids import PLATFORM_DROPDOWN, MONTH_DROPDOWN, CITY_DROPDOWN
from data.source import DataSource


def create_platfrom_dropdown(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(PLATFORM_DROPDOWN, 'value'),
                  [Input(MONTH_DROPDOWN, 'value'),
                  Input(CITY_DROPDOWN, 'value'),])
    def update_platforms(months: list[str], cities: list[str]) -> list[str]:
        return source.unique_platforms

    return html.Div(
        [
            html.H6('Platfrom', style={'textAlign': 'left', 'fontSize':15}),
            dcc.Dropdown(
                id=PLATFORM_DROPDOWN,
                options=[{'label':platform, 'value':platform} for platform in source.unique_platforms],
                multi=True,
                value=source.unique_platforms[0],
            )
        ]
    )

        