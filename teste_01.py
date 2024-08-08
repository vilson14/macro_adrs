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

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#RUN - NAS PASTA C:\app
#streamlit run .\teste_02.py





url = 'https://br.investing.com/equities/vale-s.a.--americ'

head = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': 'https://br.investing.com/equities/vale-s.a.--americ',
  'cookie': """your cookie value ( you can get that from your web page) """
}



#VIX-------------------------------------------------------------------------------------------------------------------------------------
url = 'https://br.investing.com/indices/volatility-s-p-500'
req = Request(url, headers=head)
html1 = urlopen(req)
html2 = html1.read()
soup = BeautifulSoup(html2, "html.parser")

vix_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
vix_preco_02 = vix_preco_01.getText()
vix_preco_03 = vix_preco_02.replace(',', '.')
vix_preco_04 = float(vix_preco_03)


vix_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
vix_var_02 = vix_var_01.getText()
vix_var_03 = vix_var_02.replace('(', '')
vix_var_04 = vix_var_03.replace(')', '')
vix_var_05 = vix_var_04.replace('%', '')
vix_var_06 = vix_var_05.replace(',', '.')
vix_var_07 = float(vix_var_06)




fig = make_subplots(rows=5, cols=4, subplot_titles=("VIX", "OURO", "BRENT", "SP500", "WTI", "MINÉRIO DALIAN", "MINÉRIO CME", "EWZ", "SALDO TOTAL", "VALE", "PETRO", "SALDO - mat. básicos", "ITAU", "BRADESCO", "BRASIL", "SALDO - financeiro"),
                    specs=[[{'rowspan':2}, {'rowspan':2}, {}, {'rowspan':2}],
                          [None, None, {}, None],
                          [{}, {}, {}, {'rowspan':2}],
                           [{}, {}, {}, None],
                          [ {}, {}, {}, {}]], print_grid = True,
                    horizontal_spacing = 0.05, vertical_spacing = 0.05)


st.subheader("PRE-MARKET - MACRO + ADRS " + vix_var_06)
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
