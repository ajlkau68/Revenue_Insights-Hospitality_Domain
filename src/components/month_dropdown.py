from dash import Dash, html, dcc
from components.ids import MONTH_DROPDOWN
from data.source import DataSource



def create_month_dropdown(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        [
            html.H6('Month', style={'textAlign': 'left', 'fontSize':15}),
            dcc.Dropdown(
                id=MONTH_DROPDOWN,
                options=[{'label':month, 'value':month} for month in source.unique_months],
                multi=True,
                clearable=False,
                value=source.unique_months,
            )
        ]
    )
