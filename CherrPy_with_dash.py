from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash
import cherrypy
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')



class Root(object):

    def index(self):
        output = '''
        "Access the <a href="dash">application</a>"
        '''
        return output

    index.exposed = True

    def dash(self):
        return app

    dash.exposed = True

    def dataexplorer(self):
        raise cherrypy.HTTPRedirect("https://www.google.com")
        # raise cherrypy.HTTPRedirect(cherrypy.url("https://www.google.com"))
    # cherrypy.

    dataexplorer.exposed = True


if __name__ == '__main__':
    # configfile = os.path.join(os.path.dirname(__file__), 'server.conf')
    # cherrypy.quickstart(Root(), script_name='/', config=configfile)
    cherrypy.quickstart(Root(), '/', "app.conf")

