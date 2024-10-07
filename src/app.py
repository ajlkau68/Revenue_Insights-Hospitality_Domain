from dash import Dash 
from dash_bootstrap_components.themes import BOOTSTRAP
from components.main_layout import create_layout
from data.loader import load_data
from data.source import DataSource

DATA_PATH = 'full_bookings.csv'

def main() -> None:

    data = load_data(DATA_PATH)
    data = DataSource(data)

    app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
    server = app.server
    app.title = 'AtliQ Grands Dashboard'
    app.layout = create_layout(app, data)
    app.run_server(debug=True)


if __name__ == '__main__':
    main()