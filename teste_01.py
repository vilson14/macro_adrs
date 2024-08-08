import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[-1, 6],
        y=[0, 0]
    ))

fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))

fig.show()
