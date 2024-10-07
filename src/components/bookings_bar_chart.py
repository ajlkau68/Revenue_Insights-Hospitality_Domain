from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import BOOKINGS_BAR_CHART, MONTH_DROPDOWN
from data.source import DataSource, DataSchema, human_format


def create_bookings_bar_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(BOOKINGS_BAR_CHART, 'children'),
                   Input(MONTH_DROPDOWN, 'value'))
    def update_bar_chart(months: list[str]) -> html.Div:
        filtered_source = source.month_filter(months)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=BOOKINGS_BAR_CHART)

        fig = px.bar(filtered_source.get_city_bookings(), y=DataSchema.CITY, x=DataSchema.BOOKING_ID,
                     title='Bookings by City',
                     labels={
                         DataSchema.CITY: 'City',
                         DataSchema.BOOKING_ID: 'Bookings'},
                         orientation='h',
                         text=[human_format(val) for val in filtered_source.get_city_bookings()[
                             DataSchema.BOOKING_ID]])
        fig.update_traces(marker_color = 'skyblue', textfont=dict(color='white'))
        fig.update_layout(title_font=dict(size=16, family="Arial", color='grey'),
                        xaxis=dict(
                            showgrid=False,
                            showline=False),
                        yaxis=dict(
                            showgrid=False,
                            showline=False)
                            )
        return html.Div(dcc.Graph(figure=fig), id=BOOKINGS_BAR_CHART)

    return html.Div(id=BOOKINGS_BAR_CHART)
