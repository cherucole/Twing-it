import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

df_external_source = FF.create_table(df.head())
py.plot(df_external_source, filename='df-external-source-table')


trace = go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)')
layout = go.Layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

py.plot(fig, filename='apple-stock-prices')