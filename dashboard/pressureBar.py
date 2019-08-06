import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Event,Input
import plotly.plotly as py
import plotly.graph_objs as go
import time
import random
import pyrebase
from django_plotly_dash import DjangoDash
YS = 100
YZ = 100
pressureApp = DjangoDash('underPressure')

pressureApp.layout = html.Div([
    dcc.Graph(id = 'waterPressure'),
    dcc.Interval(id='waterPressureUpdate',
                 interval=1000
                 )
])


@pressureApp.callback(Output('waterPressure','figure'),[Input(component_id='waterPressureUpdate',component_property='n_intervals')])
def pressureUpdater(value):
    global YS
    global YZ
    YS = YS-random.uniform(00.10,00.30)
    YZ = YZ-random.uniform(00.10,00.30)
    data = go.Bar(
        x = ['pressure Sensor 1','pressure Sensor 2'],
        y= [YS,YZ],
        width =[0.8,0.8]
    )
    return {'data':[data],'layout':go.Layout(yaxis={'title':'Pressure(psi)'},
                                             autosize=False,
                                             width=400,
                                             height=500)}

'''
if __name__ == '__main__':
    pressureApp.run_server(debug=True)
'''