from dash import Dash, html
import dash_bootstrap_components as dbc 


def create_header(app:Dash) -> html.Div:

    return html.Div(
        [
            html.Img(src='assets/Atliq_logo_for_dashboard.png', height='50px'),
            html.Img(src='assets/codebasics_logo_for_dashboard.png', height='50px'),
            html.H3(app.title, style={'textAlign':'center', 'color':'white'}, className='ms-auto'),
            dbc.Button('Learn More', color='secondary', outline=True, className='ms-auto', href='https://ajlkau68.github.io/James_Portfolio/')
        ], className='hstack gap-3'
    )
