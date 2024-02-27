import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yahooquery as yq
# import pprint
import random
from datetime import datetime
import mplfinance as mpf

st.title('Stock Analysis App')
st.title('_Stock_ is :blue[cool] :sunglasses:')

st.header('Trend Chart', divider='rainbow')
st.header('_Trend_ is :blue[true] :sparkles:')

stockCode = st.text_input('Stock Code', '5947')
symbols = stockCode + '.T'
tickers = yq.Ticker(symbols,asynchronous=True,backoff_factor=1,formatted=True,progress=True,retry=3)

# @st.cache_data
df=tickers.history(period='12mo', interval='1d')

#ローソク足
# dg = df.loc[symbols].copy()

# dh = dg.reset_index()
# dh.rename(columns=str.capitalize, inplace=True)
# dh['Date'] = pd.to_datetime(dh['Date'])

# di = dh.reset_index()
# di.set_index('Date', inplace=True)

# print(di.columns)
# di.drop('Adjclose', axis=1, inplace=True) #日足未満ではAdjclose存在しない

# mpf.plot(di, type='candle')
# mpf.show()

st.divider()

#ローソク足
dg = df.loc[symbols].copy()

dh = dg.reset_index()
dh.rename(columns=str.capitalize, inplace=True)
dh['Date'] = pd.to_datetime(dh['Date'])

di = dh.reset_index()
di.set_index('Date', inplace=True)

# mplfinanceのプロットをストリームリットで表示する
fig, ax = mpf.plot(di, type='candle', returnfig=True, mav=(5, 20, 60))
st.pyplot(fig)

# data 表示
st.dataframe(df)