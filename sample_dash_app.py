
import dash
import flask
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id="url"),
    html.H1("My Dash App"),
    html.Div(id='cookie-value-output')
])

@app.callback(
    Output('cookie-value-output', 'children'),
    Input('url', 'pathname')
)
def display_cookie_value(pathname):
    # print(flask.Request.cookies)
    print("session id is" + flask.request.cookies.get("session_id"))
    # dash.callback_context
    cookies = dash.callback_context.request.cookies
    print(cookies)
    my_cookie_value = cookies.get('sessionid', 'No cookie found')
    return f"Value of my_cookie: {my_cookie_value}"

if __name__ == '__main__':
    app.run_server(debug=True)