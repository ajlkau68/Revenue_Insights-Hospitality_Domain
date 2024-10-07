from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import REVENUE_BAR_CHART, MONTH_DROPDOWN
from data.source import DataSource, DataSchema, human_format


px.defaults.template = 'plotly_white'

def create_revenue_bar_chart(app: Dash, source: DataSource) -> html.Div:

    @app.callback(Output(REVENUE_BAR_CHART, 'children'),
                   Input(MONTH_DROPDOWN, 'value'))
    def update_bar_chart(months: list[str]) -> html.Div:
        filtered_source = source.month_filter(months)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=REVENUE_BAR_CHART)

        fig = px.bar(filtered_source.get_city_revenue(), y=DataSchema.CITY, x=DataSchema.REVENUE_REALIZED,
                     title='Revenue by City',
                     labels={
                         DataSchema.CITY: 'City',
                         DataSchema.REVENUE_REALIZED: 'Revenue'},
                         orientation='h',
                         text=[human_format(val) for val in filtered_source.get_city_revenue()[
                             DataSchema.REVENUE_REALIZED]])
        fig.update_traces(marker_color = 'skyblue', textfont=dict(color='white'))
        fig.update_layout(title_font=dict(size=16, family="Arial", color='grey'),
                        xaxis=dict(
                            showgrid=False,
                            showline=False),
                        yaxis=dict(
                            showgrid=False,
                            showline=False)
                            )
        return html.Div(dcc.Graph(figure=fig), id=REVENUE_BAR_CHART)

    return html.Div(id=REVENUE_BAR_CHART)
