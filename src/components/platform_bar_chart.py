from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import PLATFORM_BAR_CHART, MONTH_DROPDOWN
from data.source import DataSource, DataSchema


def create_platform_bar_chart(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(PLATFORM_BAR_CHART, 'children'),
                   Input(MONTH_DROPDOWN, 'value'))
    def update_bar_chart(months: list[str]) -> html.Div:
        filtered_source = source.month_filter(months)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=PLATFORM_BAR_CHART)

        fig = px.bar(filtered_source.get_booking_platform(), y=DataSchema.BOOKING_PLATFORM, x=DataSchema.PROPORTION,
                     title='Bookings per Platform',
                     labels={
                         DataSchema.BOOKING_PLATFORM: 'Platform',
                         DataSchema.PROPORTION: 'Percentage'},
                         orientation='h',
                         text_auto=True)
        fig.update_traces(marker_color = 'skyblue', textfont=dict(color='white'))
        fig.update_layout(title_font=dict(size=16, family="Arial", color='grey'),
                        xaxis=dict(
                            showgrid=False,
                            showline=False),
                        yaxis=dict(
                            showgrid=False,
                            showline=False)
                            )
        return html.Div(dcc.Graph(figure=fig), id=PLATFORM_BAR_CHART)

    return html.Div(id=PLATFORM_BAR_CHART)
