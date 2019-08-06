import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Event
import random
import plotly.plotly as py
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pyrebase

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

X=00.50
wState = DjangoDash('waterstate')

wState.layout = html.Div([
    dcc.Graph(id='waterpie',animate=True),
    dcc.Interval(
        id='waterpieupdate',
        interval=1000
    )
])

@wState.callback(Output('waterpie','figure'),events=[Event('waterpieupdate','interval')])
def stateUpdater():
    global X
    db.child('sence2').child('value').get().val()

    X = X+random.uniform(00.30,00.90)
    labels = ['water','empty']
    values = ['100',X]
    data = go.Pie(labels=labels,values=values)
    return {'data':[data],'layout':go.Layout(autosize=False,height=450,width=500)}

'''
if __name__ == '__main__':
    wState.run_server(debug=True)
'''