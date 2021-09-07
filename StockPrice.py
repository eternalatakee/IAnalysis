import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Logo Deplopyment

from PIL import Image
Background = background = Image.open('Ianalysis - Project.png')
st.image(background, width=1000)


# Title
st.write("""

# Welcome Analyst!

Shown are basic information such as **closing prices** and **volume** of selected stock ***IBM***!

""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-1-1', end = '2021-9-5')
# Open  High       Low Close        Volume      Dividends       Stock Splits

st.write("""
## Closing Price

""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price

""")
st.line_chart(tickerDf.Volume)

st.write("""
## Dividends Price

""")
st.line_chart(tickerDf.Dividends)

st.write("""
## Balance Sheets

""")

tickerData.balance_sheet


# alpha vantage title allignment

st.markdown("<h2 style = 'text-align: center; color: Black;' > Fundamental Analysis </h1>" , unsafe_allow_html=True)


st.write("""
## Annual Earnings:
""")

#Deploy API_Key "lOCAL FILE"
key = open('API_KEY.txt').read()

import requests
import json

# ANNUAL EARNINGS

function = 'EARNINGS'
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
call = requests.get(f"https://www.alphavantage.co/query?function={function}&symbol={tickerSymbol}&apikey={key}").text

call = json.loads(call)

call = pd.DataFrame(call['annualEarnings'])
# Annual Earnings Call
call

st.write("""
## Quarterly Earnings:
""")

# QUARTERLY EARNINGS

QE = requests.get(f"https://www.alphavantage.co/query?function={function}&symbol={tickerSymbol}&apikey={key}").text

QE = json.loads(QE)

QE = pd.DataFrame(QE['quarterlyEarnings'])
# Quareterly EARNINGS CALL

QE
