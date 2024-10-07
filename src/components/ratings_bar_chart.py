from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import RATINGS_BAR_CHART, MONTH_DROPDOWN
from data.source import DataSource, DataSchema


def create_ratings_bar_chart(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(RATINGS_BAR_CHART, 'children'),
                  Input(MONTH_DROPDOWN, 'value'))
    def update_bar_chart(months: list[str]) -> html.Div:
        filtered_source = source.month_filter(months)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=RATINGS_BAR_CHART)

        fig = px.bar(filtered_source.get_city_ratings(), y=DataSchema.CITY, x=DataSchema.RATINGS_GIVEN,
                     title='Average Ratings by City',
                     labels={
                         DataSchema.CITY: 'City',
                         DataSchema.RATINGS_GIVEN: 'Average Rating'},
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
        return html.Div(dcc.Graph(figure=fig), id=RATINGS_BAR_CHART)

    return html.Div(id=RATINGS_BAR_CHART)
