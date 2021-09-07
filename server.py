import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

# set web title
app.title = 'ASECL'

server = app.server