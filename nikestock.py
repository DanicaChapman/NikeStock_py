import yfinance as yf
import streamlit as st
from datetime import date, timedelta

st.write("""
# Stock Price of Nike Inc.

Stock Closing Price and Volume for Nike from Jan 2010 til today!
""")



tickerSymbol = 'NKE'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-01-01', end=date.today().strftime("%Y-%m-%d"))


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)