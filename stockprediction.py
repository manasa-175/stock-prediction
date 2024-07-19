import streamlit as st # type: ignore
import yfinance as yf # type: ignore
import pandas as pd # type: ignore

st.title('List Finance Dashboard')

tickers = ('TSLA', 'AAPL', 'MSFT', 'GOOG')

dropdown = st.multiselect('Pick your assets', tickers)

def get_ticker(name):
    ticker = yf.Ticker(name)
    return ticker

c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")
c4 = get_ticker("GOOG")

apple = yf.download("AAPL", start="2022-11-2", end="2022-11-11")
microsoft = yf.download("MSFT", start="2022-11-2", end="2022-11-11")
tesla = yf.download("TSLA", start="2022-11-2", end="2022-11-11")
google = yf.download("GOOG", start="2022-11-2", end="2022-11-11")

data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c3.history(period="3mo")
data4 = c4.history(period="3mo")

if len(dropdown) > 0:
    df = yf.download(dropdown)['Adj Close']
    st.line_chart(df)

    if "AAPL" in dropdown:
        st.header("Apple")
        st.write("### Stock prediction")
        st.write(apple)
        st.sidebar.header("High and Low Prices of Apple")
        st.sidebar.write("High:", apple['High'].max())
        st.sidebar.write("Low:", apple['Low'].min())

    if "MSFT" in dropdown:
        st.header("Microsoft")
        st.write("### Stock prediction")
        st.write(microsoft)
        st.sidebar.header("High and Low Prices of Microsoft")
        st.sidebar.write("High:", microsoft['High'].max())
        st.sidebar.write("Low:", microsoft['Low'].min())

    if "TSLA" in dropdown:
        st.header("Tesla")
        st.write("### Stock prediction")
        st.write(tesla)
        st.sidebar.header("High and Low Prices of Tesla")
        st.sidebar.write("High:", tesla['High'].max())
        st.sidebar.write("Low:", tesla['Low'].min())

    if "GOOG" in dropdown:
        st.header("Google")
        st.write("### Stock prediction")
        st.write(google)
        st.sidebar.header("High and Low Prices of Google")
        st.sidebar.write("High:", google['High'].max())
        st.sidebar.write("Low:", google['Low'].min())