import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Coinbase!

""")

tickerSymbol = 'COIN'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2021-4-14', end='2021-5-31')

st.write("""

### Closing Price

""")
st.line_chart(tickerDf.Close)

st.write("""

### Volume

""")
st.line_chart(tickerDf.Volume)