import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,Event
import plotly
import plotly.graph_objs as go
import pyrebase
from collections import deque
from django_plotly_dash import DjangoDash

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

# firebase connection and auth
config = {
    'apiKey': "AIzaSyDmgvnM0dLfnnJr4jpVvHpTWzDlvxHd8nQ",
    'authDomain': "datastore-8679e.firebaseapp.com",
    'databaseURL': "https://datastore-8679e.firebaseio.com",
    'projectId': "datastore-8679e",
    'storageBucket': "datastore-8679e.appspot.com",
    'messagingSenderId': "827174721908"
}
#databse connection
firebase = pyrebase.initialize_app(config)
db = firebase.database()

external_css = ('https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous')
appB = DjangoDash('sensorBView')

appB.layout = html.Div([
    dcc.Graph(id = 'sensorBGraph',animate=True),
    dcc.Interval(
        id='graph-B-update',
        interval=1*4000
    )
])

@appB.callback(Output('sensorBGraph','figure'),events=[Event('graph-B-update','interval')])
def senceBUpdaeGraph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(db.child('sence3').child('value').get().val())
    #print(db.child('sence1').child('value').get().val())
    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name = 'flow_sensor_A',
        mode = 'lines+markers'
    )
    return {'data':[data],'layout':go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                             yaxis=dict(range=[min(Y),max(Y)]))}


'''if __name__ == '__main__':
    app.run_server(debug=True)
'''