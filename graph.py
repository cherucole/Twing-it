import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd


df = pd.read_csv('redsan1.csv')

data_table = FF.create_table(df.head())
py.plot(data_table, filename='redsan-table')


trace1 = go.Scatter(
                    x=df['date'], y=df['polarity'], # Data
                    mode='lines', name='polarity' # Additional options
                   )
# trace2 = go.Scatter(x=df['date'], y=df['polarity'], mode='lines', name='polarity' )
trace3 = go.Scatter(x=df['date'], y=df['subjectivity'], mode='lines', name='subjectivity')

layout = go.Layout(title='Sentiments About Safaricom with a random sample size of 1000 tweets',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace3], layout=layout)

# Plot data in the notebook
py.plot(fig, filename='simple-plot-from-csv')