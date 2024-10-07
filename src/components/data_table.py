from dash import html, dash_table, Dash, Input, Output
from data.source import DataSource
from components.ids import DATA_TABLE, MONTH_DROPDOWN


# Create the layout to display the dataset in a table
def create_table(app:Dash, source: DataSource) -> html.Div:

    @app.callback(Output(DATA_TABLE, 'children'),
                  Input(MONTH_DROPDOWN, 'value'))
    def update_table(months: list[str]) -> html.Div:
        filtered_source = source.month_filter(months)
        
        if not filtered_source.row_count:
            return html.Div('No data selected', id=DATA_TABLE)
        
        return dash_table.DataTable(
                            data=filtered_source.get_table_data().to_dict('records'),
                            page_size=10,
                            style_cell={'background-color': 'white', 'border': 'solid 1px lightgrey',
                                        'color': 'black', 'font-size': '12px', 'text-align': 'left'},
                            style_header={'background-color': 'white', 'font-weight': 'bold',
                                        'color': 'black', 'padding': '2px', 'font-size': '15px'},
                            style_table={'minWidth': '100%'}
            )
        
    return html.Div(id=DATA_TABLE)
