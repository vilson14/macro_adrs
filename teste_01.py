
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


import urllib.request


import requests

from urllib.parse import unquote
import json



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType


# @st.cache_resource
# def get_driver():
#     return webdriver.Chrome(
#         service=Service(
#             ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
#         ),
#         options=options,
#     )

# options = Options()
# options.add_argument("--disable-gpu")
# options.add_argument("--headless")

# driver = get_driver()

# driver.get("https://finance.sina.com.cn/futures/quotes/I0.shtml")

# minerio_dalian_preco_01 = driver.find_elements(By.XPATH, '//*[@id="table-box-futures-hq"]/tbody/tr[1]/td[1]/div/span[1]')[0].text

# st.code(minerio_dalian_preco_01)

# driver.close()
# driver.quit()






#RUN - NAS PASTA C:\app
#streamlit run .\teste_02.py



apiurl=r'https://www.barchart.com/proxies/core-api/v1/quotes/get'
getheaders={

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }

getpay={
    'page': 'all'
}



#FUNCAO GET DATA ATIVO------------------------------------------------------------------------------------------------------------------------------
def get_data_ticker(A):
    geturl=r'https://www.barchart.com/stocks/quotes/'+A
    s=requests.Session()
    r=s.get(geturl,params=getpay, headers=getheaders)
    headers={
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': geturl,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'x-xsrf-token': unquote(unquote(s.cookies.get_dict()['XSRF-TOKEN']))
    }
    
    payload={
    "symbol":A,
    'fields': 'symbol,lastPrice,percentChange,percentChangeExt,volume,tradeTime',
    'list': 'futures.contractInRoot',
    'root': A,
    'meta': 'field.shortName,field.type,field.description',
    'hasOptions': 'true',
    'raw': '1'
    }
    
    r=s.get(apiurl,params=payload,headers=headers).json()
    df_data_ticker = pd.DataFrame(r['data']).iloc[:, :-1]
    
    return df_data_ticker












#url = 'https://br.investing.com/equities/vale-s.a.--americ'

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
vix_df = get_data_ticker ("$VIX")
vix_preco_01 = vix_df['lastPrice'].iloc[0]
vix_preco_04 = float(vix_preco_01)

vix_var_01 = vix_df['percentChange'].iloc[0]
vix_var_02 = vix_var_01.replace('%', '')
vix_var_03 = vix_var_02.replace('+', '')
vix_var_07 = float(vix_var_03)*-1



#OURO-------------------------------------------------------------------------------------------------------------------------------------
ouro_df = get_data_ticker ("GC*0")
ouro_preco_01 = ouro_df['lastPrice'].iloc[0]
ouro_preco_02 = ouro_preco_01.replace(',', '')
ouro_preco_05 = float(ouro_preco_02)

ouro_var_01 = ouro_df['percentChange'].iloc[0]
ouro_var_02 = ouro_var_01.replace('%', '')
ouro_var_03 = ouro_var_02.replace('+', '')
ouro_var_07 = float(ouro_var_03)





#BRENT-------------------------------------------------------------------------------------------------------------------------------------
brent_df = get_data_ticker ("QA*0")
brent_preco_01 = brent_df['lastPrice'].iloc[0]
brent_preco_02 = brent_preco_01.replace(',', '')
brent_preco_04 = float(brent_preco_02)

brent_var_01 = brent_df['percentChange'].iloc[0]
brent_var_02 = brent_var_01.replace('%', '')
brent_var_03 = brent_var_02.replace('+', '')
brent_var_07 = float(brent_var_03)


#SP500-------------------------------------------------------------------------------------------------------------------------------------
sp500_df = get_data_ticker ("ES*0")
sp500_preco_01 = sp500_df['lastPrice'].iloc[0]
sp500_preco_02 = sp500_preco_01.replace(',', '')
sp500_preco_05 = float(sp500_preco_02)

sp500_var_01 = sp500_df['percentChange'].iloc[0]
sp500_var_02 = sp500_var_01.replace('%', '')
sp500_var_03 = sp500_var_02.replace('+', '')
sp500_var_07 = float(sp500_var_03)




#WTI-------------------------------------------------------------------------------------------------------------------------------------
wti_df = get_data_ticker ("CL*0")
wti_preco_01 = wti_df['lastPrice'].iloc[0]
wti_preco_02 = wti_preco_01.replace(',', '')
wti_preco_04 = float(wti_preco_02)

wti_var_01 = wti_df['percentChange'].iloc[0]
wti_var_02 = wti_var_01.replace('%', '')
wti_var_03 = wti_var_02.replace('+', '')
wti_var_07 = float(wti_var_03)





#MINERIO DALIAN-------------------------------------------------------------------------------------------------------------------------------------




# print (vix_preco_01)

minerio_dalian_preco_02 = 0


minerio_dalian_var_04 = 0





#MINERIO CME-------------------------------------------------------------------------------------------------------------------------------------
minerio_cme_df = get_data_ticker ("CL*0")
minerio_cme_preco_01 = minerio_cme_df['lastPrice'].iloc[0]
minerio_cme_preco_02 = minerio_cme_preco_01.replace(',', '')
minerio_cme_preco_04 = float(minerio_cme_preco_02)

minerio_cme_var_01 = minerio_cme_df['percentChange'].iloc[0]
minerio_cme_var_02 = minerio_cme_var_01.replace('%', '')
minerio_cme_var_03 = minerio_cme_var_02.replace('+', '')
minerio_cme_var_07 = float(minerio_cme_var_03)




#EWZ-------------------------------------------------------------------------------------------------------------------------------------
ewz_df = get_data_ticker ("EWZ")
ewz_preco_01 = ewz_df['lastPrice'].iloc[0]
ewz_preco_02 = ewz_preco_01.replace(',', '')
ewz_preco_04 = float(ewz_preco_02)

ewz_var_01 = ewz_df['percentChange'].iloc[0]
ewz_var_02 = ewz_var_01.replace('%', '')
ewz_var_03 = ewz_var_02.replace('+', '')
ewz_var_07 = float(ewz_var_03)


url = 'https://br.investing.com/etfs/ishares-brazil-index'
request = urllib.request.Request (url, headers=head)
f = urllib.request.urlopen (request)
html2 = f.read()
soup = BeautifulSoup(html2, "html.parser")

ewz_leilao_08 = float(0)
if soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"}):
    #print ("OK")
    ewz_leilao_01 = soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"})
    ewz_leilao_02 = ewz_leilao_01[1]
    ewz_leilao_03 = ewz_leilao_02.getText()
    ewz_leilao_04 = ewz_leilao_03.replace('(', '')
    ewz_leilao_05 = ewz_leilao_04.replace(')', '')
    ewz_leilao_06 = ewz_leilao_05.replace('%', '')
    ewz_leilao_07 = ewz_leilao_06.replace(',', '.')
    ewz_leilao_08 = float(ewz_leilao_07)
    print (ewz_leilao_08)

if soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"}):
    #print ("BUG")
    ewz_leilao_01 = soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"})
    ewz_leilao_02 = ewz_leilao_01[1]
    ewz_leilao_03 = ewz_leilao_02.getText()
    ewz_leilao_04 = ewz_leilao_03.replace('(', '')
    ewz_leilao_05 = ewz_leilao_04.replace(')', '')
    ewz_leilao_06 = ewz_leilao_05.replace('%', '')
    ewz_leilao_07 = ewz_leilao_06.replace(',', '.')
    ewz_leilao_08 = float(ewz_leilao_07)
    print (ewz_leilao_08)









# time.sleep(3)
# #VALE-------------------------------------------------------------------------------------------------------------------------------------
# url = 'https://br.investing.com/equities/vale-s.a.--americ'
# # req = Request(url, headers=head)
# # html1 = urlopen(req)
# # html2 = html1.read()
# # soup = BeautifulSoup(html2, "html.parser")

# request = urllib.request.Request (url, headers=head)
# f = urllib.request.urlopen (request)
# html2 = f.read()
# soup = BeautifulSoup(html2, "html.parser")

# vale_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
# vale_preco_02 = vale_preco_01.getText()
# vale_preco_03 = vale_preco_02.replace(',', '.')
# vale_preco_04 = float(vale_preco_03)



# vale_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
# vale_var_02 = vale_var_01.getText()
# vale_var_03 = vale_var_02.replace('(', '')
# vale_var_04 = vale_var_03.replace(')', '')
# vale_var_05 = vale_var_04.replace('%', '')
# vale_var_06 = vale_var_05.replace(',', '.')
# vale_var_07 = float(vale_var_06)



# vale_leilao_08 = float(0)


# if soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"}):
#     #print ("OK")
#     vale_leilao_01 = soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"})
#     vale_leilao_02 = vale_leilao_01[1]
#     vale_leilao_03 = vale_leilao_02.getText()
#     vale_leilao_04 = vale_leilao_03.replace('(', '')
#     vale_leilao_05 = vale_leilao_04.replace(')', '')
#     vale_leilao_06 = vale_leilao_05.replace('%', '')
#     vale_leilao_07 = vale_leilao_06.replace(',', '.')
#     vale_leilao_08 = float(vale_leilao_07)
    
    
    


# if soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"}):
#     #print ("BUG")
#     vale_leilao_01 = soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"})
#     vale_leilao_02 = vale_leilao_01[1]
#     vale_leilao_03 = vale_leilao_02.getText()
#     vale_leilao_04 = vale_leilao_03.replace('(', '')
#     vale_leilao_05 = vale_leilao_04.replace(')', '')
#     vale_leilao_06 = vale_leilao_05.replace('%', '')
#     vale_leilao_07 = vale_leilao_06.replace(',', '.')
#     vale_leilao_08 = float(vale_leilao_07)
    






# time.sleep(3)
# #PETRO-------------------------------------------------------------------------------------------------------------------------------------

# url = 'https://br.investing.com/equities/petroleo-bras'
# # req = Request(url, headers=head)
# # html1 = urlopen(req)
# # html2 = html1.read()
# # soup = BeautifulSoup(html2, "html.parser")

# request = urllib.request.Request (url, headers=head)
# f = urllib.request.urlopen (request)
# html2 = f.read()
# soup = BeautifulSoup(html2, "html.parser")

# petro_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
# petro_preco_02 = petro_preco_01.getText()
# petro_preco_03 = petro_preco_02.replace(',', '.')
# petro_preco_04 = float(petro_preco_03)



# petro_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
# petro_var_02 = petro_var_01.getText()
# petro_var_03 = petro_var_02.replace('(', '')
# petro_var_04 = petro_var_03.replace(')', '')
# petro_var_05 = petro_var_04.replace('%', '')
# petro_var_06 = petro_var_05.replace(',', '.')
# petro_var_07 = float(petro_var_06)



# petro_leilao_08 = float(0)

# if soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"}):
#     #print ("OK")
#     petro_leilao_01 = soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"})
#     petro_leilao_02 = petro_leilao_01[1]
#     petro_leilao_03 = petro_leilao_02.getText()
#     petro_leilao_04 = petro_leilao_03.replace('(', '')
#     petro_leilao_05 = petro_leilao_04.replace(')', '')
#     petro_leilao_06 = petro_leilao_05.replace('%', '')
#     petro_leilao_07 = petro_leilao_06.replace(',', '.')
#     petro_leilao_08 = float(petro_leilao_07)
    
    
    


# if soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"}):
#     #print ("BUG")
#     petro_leilao_01 = soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"})
#     petro_leilao_02 = petro_leilao_01[1]
#     petro_leilao_03 = petro_leilao_02.getText()
#     petro_leilao_04 = petro_leilao_03.replace('(', '')
#     petro_leilao_05 = petro_leilao_04.replace(')', '')
#     petro_leilao_06 = petro_leilao_05.replace('%', '')
#     petro_leilao_07 = petro_leilao_06.replace(',', '.')
#     petro_leilao_08 = float(petro_leilao_07)
    



# time.sleep(3)
# #ITAU-------------------------------------------------------------------------------------------------------------------------------------
# url = 'https://br.investing.com/equities/itau-unibanco-holding-sa-adr'
# # req = Request(url, headers=head)
# # html1 = urlopen(req)
# # html2 = html1.read()
# # soup = BeautifulSoup(html2, "html.parser")

# request = urllib.request.Request (url, headers=head)
# f = urllib.request.urlopen (request)
# html2 = f.read()
# soup = BeautifulSoup(html2, "html.parser")

# itau_preco_01 = soup.find('div', {"data-test": "instrument-price-last"})
# itau_preco_02 = itau_preco_01.getText()
# itau_preco_03 = itau_preco_02.replace(',', '.')
# itau_preco_04 = float(itau_preco_03)



# itau_var_01 = soup.find('span', {"data-test": "instrument-price-change-percent"})
# itau_var_02 = itau_var_01.getText()
# itau_var_03 = itau_var_02.replace('(', '')
# itau_var_04 = itau_var_03.replace(')', '')
# itau_var_05 = itau_var_04.replace('%', '')
# itau_var_06 = itau_var_05.replace(',', '.')
# itau_var_07 = float(itau_var_06)


# itau_leilao_08 = float(0)

# if soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"}):
#     #print ("OK")
#     itau_leilao_01 = soup.findAll('span', {"text-positive-main text-base/6 rtl:force-ltr"})
#     itau_leilao_02 = itau_leilao_01[1]
#     itau_leilao_03 = itau_leilao_02.getText()
#     itau_leilao_04 = itau_leilao_03.replace('(', '')
#     itau_leilao_05 = itau_leilao_04.replace(')', '')
#     itau_leilao_06 = itau_leilao_05.replace('%', '')
#     itau_leilao_07 = itau_leilao_06.replace(',', '.')
#     itau_leilao_08 = float(itau_leilao_07)
    
    
    


# if soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"}):
#     #print ("BUG")
#     itau_leilao_01 = soup.findAll('span', {"text-negative-main text-base/6 rtl:force-ltr"})
#     itau_leilao_02 = itau_leilao_01[1]
#     itau_leilao_03 = itau_leilao_02.getText()
#     itau_leilao_04 = itau_leilao_03.replace('(', '')
#     itau_leilao_05 = itau_leilao_04.replace(')', '')
#     itau_leilao_06 = itau_leilao_05.replace('%', '')
#     itau_leilao_07 = itau_leilao_06.replace(',', '.')
#     itau_leilao_08 = float(itau_leilao_07)
    











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


#minerio_dalian-------------------------------------------------------------------------------------------------
ativos_minerio_dalian=['Variação']
y_var_minerio_dalian=[minerio_dalian_var_04]

df_minerio_dalian = pd.DataFrame({
     'Variação':[minerio_dalian_var_04], 
     'Leilão':['Variação']
})

df_minerio_dalian["Color"] = np.where(df_minerio_dalian["Variação"]<0, 'red', 'green')


#minerio_cme-------------------------------------------------------------------------------------------------
ativos_minerio_cme=['Variação']
y_var_minerio_cme=[minerio_cme_var_07]

df_minerio_cme = pd.DataFrame({
     'Variação':[minerio_cme_var_07], 
     'Leilão':['Variação']
})

df_minerio_cme["Color"] = np.where(df_minerio_cme["Variação"]<0, 'red', 'green')



#EWZ-------------------------------------------------------------------------------------------------
ativos_ewz=['Variação']
y_var_ewz=[ewz_var_07]

df_ewz = pd.DataFrame({
     'Variação':[ewz_var_07, ewz_leilao_08], 
     'Leilão':['Variação','Leilão']
})

df_ewz["Color"] = np.where(df_ewz["Variação"]<0, 'red', 'green')


#VALE-------------------------------------------------------------------------------------------------
# df_vale = pd.DataFrame({
#      'Variação':[vale_var_07,vale_leilao_08], 
#      'Leilão':['Variação','Leilão']
# })

# df_vale["Color"] = np.where(df_vale["Variação"]<0, 'red', 'green')


# #PETRO-------------------------------------------------------------------------------------------------
# ativos_petro=['Variação']
# y_var_petro=[petro_var_07]

# df_petro = pd.DataFrame({
#      'Variação':[petro_var_07,petro_leilao_08], 
#      'Leilão':['Variação','Leilão']
# })

# df_petro["Color"] = np.where(df_petro["Variação"]<0, 'red', 'green')


# #SALDO VALE E PETRO-------------------------------------------------------------------------------------------------
# ativos_s_vale_petro=['Variação']
# y_var_s_vale_petro=[petro_var_07]

# df_s_vale_petro = pd.DataFrame({
#      'Variação':[round ((vale_var_07+petro_var_07),2),round ((vale_leilao_08+petro_leilao_08),2)], 
#      'Leilão':['Variação','Leilão']
# })

# df_s_vale_petro["Color"] = np.where(df_s_vale_petro["Variação"]<0, 'red', 'green')



# #ITAU-------------------------------------------------------------------------------------------------
# ativos_itau=['Variação']
# y_var_itau=[itau_var_07]

# df_itau = pd.DataFrame({
#      'Variação':[itau_var_07,itau_leilao_08], 
#      'Leilão':['Variação','Leilão']
# })

# df_itau["Color"] = np.where(df_itau["Variação"]<0, 'red', 'green')







fig = make_subplots(rows=5, cols=4, subplot_titles=("CBOE", "OURO", "BRENT", "SP500", "WTI", "MINÉRIO DALIAN", "MINÉRIO CME", "EWZ", "SALDO TOTAL", "VALE", "PETRO", "SALDO - mat. básicos", "ITAU", "BRADESCO", "BRASIL", "SALDO - financeiro"),
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

#minerio_dalian
fig.add_trace(go.Bar(x=ativos_minerio_dalian, y=df_minerio_dalian['Variação'], marker_color=df_minerio_dalian['Color'], text= [str(i1)+' %' for i1 in df_minerio_dalian['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=3, col=1)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=3, col=1)
fig.add_annotation(x=0, y=((df_minerio_dalian['Variação']/2).iloc[0]),text=str (minerio_dalian_preco_02),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=3, col=1)

#minerio_cme
fig.add_trace(go.Bar(x=ativos_minerio_cme, y=df_minerio_cme['Variação'], marker_color=df_minerio_cme['Color'], text= [str(i1)+' %' for i1 in df_minerio_cme['Variação']], textposition='inside', textfont_color="white", insidetextanchor = "end", width=0.3, marker_line_color='black', marker_line_width=1), row=3, col=2)
fig.add_shape(type='line', x0=-0.5, y0=0, x1=0.5, y1=0, line=dict( color='black', width=5,),row=3, col=2)
fig.add_annotation(x=0, y=((df_minerio_cme['Variação']/2).iloc[0]),text=str (minerio_cme_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=3, col=2)

#EWZ
fig.add_trace(go.Bar(name='Net2', x=df_ewz['Leilão'], y=df_ewz['Variação'], marker_color=df_ewz['Color'], text= [str(i1)+' %' for i1 in df_ewz['Variação']], textposition='inside', width=0.5, marker_line_color='black', marker_line_width=1),row=3, col=3 )
fig.add_shape(type='line', x0=-0.5, y0=0, x1=1.5, y1=0, line=dict( color='black', width=5,),row=3, col=3)
fig.add_annotation(x=0, y=((df_ewz['Variação']/2).iloc[0]),text=str (ewz_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=3, col=3)


#VALE
# fig.add_trace(go.Bar(name='Net2', x=df_vale['Leilão'], y=df_vale['Variação'], marker_color=df_vale['Color'], text= [str(i1)+' %' for i1 in df_vale['Variação']], textposition='inside', width=0.5, marker_line_color='black', marker_line_width=1),row=4, col=1 )
# fig.add_shape(type='line', x0=-0.5, y0=0, x1=1.5, y1=0, line=dict( color='black', width=5,),row=4, col=1)
# fig.add_annotation(x=0, y=((df_vale['Variação']/2).iloc[0]),text=str (vale_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=4, col=1)


#PETRO
# fig.add_trace(go.Bar(name='Net1', x=df_petro['Leilão'], y=df_petro['Variação'], marker_color=df_petro['Color'], text= [str(i1)+' %' for i1 in df_petro['Variação']], textposition='inside', width=0.5, marker_line_color='black', marker_line_width=1),row=4, col=2 )
# fig.add_shape(type='line', x0=-0.5, y0=0, x1=1.5, y1=0, line=dict( color='black', width=5,),row=4, col=2)
# fig.add_annotation(x=0, y=((df_petro['Variação']/2).iloc[0]),text=str (petro_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=4, col=2)

#SALDO VALE + PETRO
# fig.add_trace(go.Bar(name='Net3', x=df_s_vale_petro['Leilão'], y=df_s_vale_petro['Variação'], marker_color=df_s_vale_petro['Color'], text= [str(i1)+' %' for i1 in df_s_vale_petro['Variação']], textposition='inside', width=0.5, marker_line_color='black', marker_line_width=1),row=4, col=3 )
# fig.add_shape(type='line', x0=-0.5, y0=0, x1=1.5, y1=0, line=dict( color='black', width=5,),row=4, col=3)


#ITAU
# fig.add_trace(go.Bar(name='Net3', x=df_itau['Leilão'], y=df_itau['Variação'], marker_color=df_itau['Color'], text= [str(i1)+' %' for i1 in df_itau['Variação']], textposition='inside', width=0.5, marker_line_color='black', marker_line_width=1),row=5, col=1 )
# fig.add_shape(type='line', x0=-0.5, y0=0, x1=1.5, y1=0, line=dict( color='black', width=5,),row=5, col=1)
# fig.add_annotation(x=0, y=((df_itau['Variação']/2).iloc[0]),text=str (itau_preco_04),showarrow=False,yshift=5, font=dict(family="Arial Black",size=16,color="#ffffff"), opacity=0.5, row=5, col=1)




#fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=1)
#fig.add_trace(go.Scatter(x=[4,5], y=[30,30], name="(1,2)"), row=1, col=2)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,2)"), row=1, col=3)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=2, col=1)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(2,3)"), row=2, col=3)
#fig.add_trace(go.Scatter(x=[3,5], y=[5,7], name="(1,4)"), row=1, col=4)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(2,1)"), row=2, col=1)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,1)"), row=3, col=1)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=3, col=2)
#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(3,2)"), row=3, col=3)

#fig.add_trace(go.Scatter(x=[4,5], y=[7,8], name="(4,1)"), row=4, col=1)
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

st.subheader("Desenvolvido por vilson.santosdias@gmail.com")


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
