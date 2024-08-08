
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

import selenium
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new") # ocula a janela
#options.add_experimental_option("detach", True) #mantem aberto o browser


options.add_argument("--ignore-certificate-error")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument("--ignore-ssl-errors")
options.add_argument('log-level=3')

#options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options) ## set opcoes definidas








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



#OURO-------------------------------------------------------------------------------------------------------------------------------------
url = 'https://br.investing.com/commodities/gold'
req = Request(url, headers=head)
html1 = urlopen(req)
html2 = html1.read()
soup = BeautifulSoup(html2, "html.parser")

ouro_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
ouro_preco_02 = ouro_preco_01.getText()
ouro_preco_03 = ouro_preco_02.replace('.', '')
ouro_preco_04 = ouro_preco_03.replace(',', '.')
ouro_preco_05 = float(ouro_preco_04)



ouro_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
ouro_var_02 = ouro_var_01.getText()
ouro_var_03 = ouro_var_02.replace('(', '')
ouro_var_04 = ouro_var_03.replace(')', '')
ouro_var_05 = ouro_var_04.replace('%', '')
ouro_var_06 = ouro_var_05.replace(',', '.')
ouro_var_07 = float(ouro_var_06)



#BRENT-------------------------------------------------------------------------------------------------------------------------------------
url = 'https://br.investing.com/commodities/brent-oil'
req = Request(url, headers=head)
html1 = urlopen(req)
html2 = html1.read()
soup = BeautifulSoup(html2, "html.parser")

brent_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
brent_preco_02 = brent_preco_01.getText()
brent_preco_03 = brent_preco_02.replace(',', '.')
brent_preco_04 = float(brent_preco_03)


brent_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
brent_var_02 = brent_var_01.getText()
brent_var_03 = brent_var_02.replace('(', '')
brent_var_04 = brent_var_03.replace(')', '')
brent_var_05 = brent_var_04.replace('%', '')
brent_var_06 = brent_var_05.replace(',', '.')
brent_var_07 = float(brent_var_06)


#SP500-------------------------------------------------------------------------------------------------------------------------------------
url = 'https://br.investing.com/indices/us-spx-500-futures'
req = Request(url, headers=head)
html1 = urlopen(req)
html2 = html1.read()
soup = BeautifulSoup(html2, "html.parser")

sp500_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
sp500_preco_02 = sp500_preco_01.getText()
sp500_preco_03 = sp500_preco_02.replace('.', '')
sp500_preco_04 = sp500_preco_03.replace(',', '.')
sp500_preco_05 = float(sp500_preco_04)



sp500_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
sp500_var_02 = sp500_var_01.getText()
sp500_var_03 = sp500_var_02.replace('(', '')
sp500_var_04 = sp500_var_03.replace(')', '')
sp500_var_05 = sp500_var_04.replace('%', '')
sp500_var_06 = sp500_var_05.replace(',', '.')
sp500_var_07 = float(sp500_var_06)



time.sleep(2)




#WTI-------------------------------------------------------------------------------------------------------------------------------------
url = 'https://br.investing.com/commodities/crude-oil'
req = Request(url, headers=head)
html1 = urlopen(req)
html2 = html1.read()
soup = BeautifulSoup(html2, "html.parser")

wti_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
wti_preco_02 = wti_preco_01.getText()
wti_preco_03 = wti_preco_02.replace(',', '.')
wti_preco_04 = float(wti_preco_03)

wti_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
wti_var_02 = wti_var_01.getText()
wti_var_03 = wti_var_02.replace('(', '')
wti_var_04 = wti_var_03.replace(')', '')
wti_var_05 = wti_var_04.replace('%', '')
wti_var_06 = wti_var_05.replace(',', '.')
wti_var_07 = float(wti_var_06)
print (wti_var_07)








#VIX-------------------------------------------------------------------------------------------------
ativos_vix=['Variação']
y_var_vix=[vix_var_07]

df_vix = pd.DataFrame({
     'Variação':[vix_var_07], 
     'Leilão':['Variação']
})

df_vix["Color"] = np.where(df_vix["Variação"]<0, 'red', 'green')


#OURO-------------------------------------------------------------------------------------------------
ativos_ouro=['Variação']
y_var_ouro=[ouro_var_07]

df_ouro = pd.DataFrame({
     'Variação':[ouro_var_07], 
     'Leilão':['Variação']
})

df_ouro["Color"] = np.where(df_ouro["Variação"]<0, 'red', 'green')


#BRENT-------------------------------------------------------------------------------------------------
ativos_brent=['Variação']
y_var_brent=[brent_var_07]

df_brent = pd.DataFrame({
     'Variação':[brent_var_07], 
     'Leilão':['Variação']
})

df_brent["Color"] = np.where(df_brent["Variação"]<0, 'red', 'green')


#SP500-------------------------------------------------------------------------------------------------
ativos_sp500=['Variação']
y_var_sp500=[sp500_var_07]

df_sp500 = pd.DataFrame({
     'Variação':[sp500_var_07], 
     'Leilão':['Variação']
})

df_sp500["Color"] = np.where(df_sp500["Variação"]<0, 'red', 'green')

#WTI-------------------------------------------------------------------------------------------------
ativos_wti=['Variação']
y_var_wti=[wti_var_07]

df_wti = pd.DataFrame({
     'Variação':[wti_var_07], 
     'Leilão':['Variação']
})

df_wti["Color"] = np.where(df_wti["Variação"]<0, 'red', 'green')







fig = make_subplots(rows=5, cols=4, subplot_titles=("VIX", "OURO", "BRENT", "SP500", "WTI", "MINÉRIO DALIAN", "MINÉRIO CME", "EWZ", "SALDO TOTAL", "VALE", "PETRO", "SALDO - mat. básicos", "ITAU", "BRADESCO", "BRASIL", "SALDO - financeiro"),
                    specs=[[{'rowspan':2}, {'rowspan':2}, {}, {'rowspan':2}],
                          [None, None, {}, None],
                          [{}, {}, {}, {'rowspan':2}],
                           [{}, {}, {}, None],
                          [ {}, {}, {}, {}]], print_grid = True,
                    horizontal_spacing = 0.05, vertical_spacing = 0.05)



#st.dataframe(iris_df)

#VIX
fig.add_trace(go.Bar(x=ativos_vix, y=df_vix['Variação'], marker_color=df_vix['Color'], text= [str(i1)+' %' for i1 in df_vix['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=1, col=1)
fig.add_shape(type='line',x0=-0.5,y0=0,x1=0.5,y1=0,line=dict(color='black',width=5,),row=1, col=1)
#fig.add_trace(go.Scatter(x=[-0.5],y=[df_vix['Variação']/2],mode="markers+text",text=[str (vix_preco_04)],textposition="bottom center"),row=1, col=1)
fig.add_annotation(x=0, y=((df_vix['Variação']/2).iloc[0]),text=str (vix_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=1, col=1)


#OURO
fig.add_trace(go.Bar(x=ativos_ouro, y=df_ouro['Variação'], marker_color=df_ouro['Color'], text= [str(i1)+' %' for i1 in df_ouro['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=1, col=2)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=1, col=2)
fig.add_annotation(x=0, y=((df_ouro['Variação']/2).iloc[0]),text=str (ouro_preco_05),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=1, col=2)


#BRENT
fig.add_trace(go.Bar(x=ativos_brent, y=df_brent['Variação'], marker_color=df_brent['Color'], text= [str(i1)+' %' for i1 in df_brent['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=1, col=3)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=1, col=3)
fig.add_annotation(x=0, y=((df_brent['Variação']/2).iloc[0]),text=str (brent_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=1, col=3)


#SP500
fig.add_trace(go.Bar(x=ativos_sp500, y=df_sp500['Variação'], marker_color=df_sp500['Color'], text= [str(i1)+' %' for i1 in df_sp500['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=1, col=4)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=1, col=4)
fig.add_annotation(x=0, y=((df_sp500['Variação']/2).iloc[0]),text=str (sp500_preco_05),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=1, col=4)

#WTI
fig.add_trace(go.Bar(x=ativos_wti, y=df_wti['Variação'], marker_color=df_wti['Color'], text= [str(i1)+' %' for i1 in df_wti['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=2, col=3)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=2, col=3)
fig.add_annotation(x=0, y=((df_wti['Variação']/2).iloc[0]),text=str (wti_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=2, col=3)




#fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=1)
#fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=2)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,2)"), row=1, col=3)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=2, col=1)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,3)"), row=2, col=3)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(1,4)"), row=1, col=4)
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


#COR DO FUNDO DO GRAFICO INTERNO
fig.update_layout(plot_bgcolor="#c1c1c1")



time_now = datetime.now()
data_hoje = time_now.strftime("%Y.%m.%d")
hora_minutos = time_now.strftime("%H_%M")
data_hoje_min = (data_hoje + " - "+ hora_minutos)






fig.update_layout(height=1100, width=2000) #xaxis_tickfont_size=30

st.subheader("PRE-MARKET - MACRO + ADRS | " + data_hoje)

st.subheader("Vilson Dias")


for i in fig['layout']['annotations']:
    i['font'] = dict(size=18,color='#000000', family="Arial Black")





# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )


#st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.plotly_chart(fig)
