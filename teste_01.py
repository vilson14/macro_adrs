
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly

import pandas as pd
import numpy as np

import time
from datetime import datetime
from datetime import date



import streamlit as st
import plotly.express as px

#RUN - NAS PASTA C:\app
#streamlit run .\teste_02.py


fig = make_subplots(rows=5, cols=4, subplot_titles=("VIX", "OURO", "BRENT", "SP500", "WTI", "MINÉRIO DALIAN", "MINÉRIO CME", "EWZ", "SALDO TOTAL", "VALE", "PETRO", "SALDO - mat. básicos", "ITAU", "BRADESCO", "BRASIL", "SALDO - financeiro"),
                    specs=[[{'rowspan':2}, {'rowspan':2}, {}, {'rowspan':2}],
                          [None, None, {}, None],
                          [{}, {}, {}, {'rowspan':2}],
                           [{}, {}, {}, None],
                          [ {}, {}, {}, {}]], print_grid = True,
                    horizontal_spacing = 0.05, vertical_spacing = 0.05)


st.subheader("PRE-MARKET - MACRO + ADRS")
#st.dataframe(iris_df)




fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=1)
fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=2)
fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,2)"), row=1, col=3)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=2, col=1)
fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,3)"), row=2, col=3)
fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(1,4)"), row=1, col=4)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(2,1)"), row=2, col=1)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,1)"), row=3, col=1)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=3, col=2)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=3, col=3)

fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(4,1)"), row=4, col=1)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=4, col=2)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=4, col=3)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=4, col=4)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=5, col=1)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=5, col=2)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=5, col=3)
fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(5,1)"), row=5, col=4)


fig.update_layout(showlegend=False)







st.plotly_chart(fig)
