# -*- coding: utf-8 -*-
"""Streamlit_Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vDFkwS8tUiroAj53W4okX9inE9JLQJ1F
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

path = 'https://github.com/paytonncourt96/TimeSeries_Project/tree/main/'
microsoft_stock = pd.read_csv(path + "Microsoft_Stock.csv")
microsoft_stock['Date'] = pd.to_datetime(microsoft_stock['Date'], format="%m/%d/%Y %H:%M:%S")
microsoft_stock.set_index('Date', inplace=True)
microsoft_stock_weekly = microsoft_stock['Close'].resample('W').mean()

msft_data_filled = pd.read_csv(path + "Microsoft_Stock.csv")
msft_data_filled['Date'] = pd.to_datetime(msft_data_filled['Date'], format="%m/%d/%Y %H:%M:%S")
msft_data_filled = microsoft_stock.set_index('Date').asfreq('D')
msft_data_filled = msft_data_filled.reset_index()

def home_page():
    st.title("Microsoft Stock Prediction Based On Trading Patterns")
    st.write("Group Members: Benson Gichinga, Courtney Payton, Sahil Adrakatti")


def decomposition(microsoft_stock_weekly):
    st.write("Multiplicative Decomposition")
    decomposition_mult = seasonal_decompose(microsoft_stock_weekly, model='multiplicative')
    fig, ax = plt.subplots(figsize=(10, 6))
    decomposition_mult.plot(ax=ax)
    st.pyplot(fig)

    st.write("Additive Decomposition")
    decomposition_add = seasonal_decompose(microsoft_stock_weekly, model='additive')
    fig, ax = plt.subplots(figsize=(10, 6))
    decomposition_add.plot(ax=ax)
    st.pyplot(fig)


def ts_plots(microsoft_stock_weekly, msft_data_filled):
    st.write("Time Series Plots")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(microsoft_stock_weekly.index, microsoft_stock_weekly.values)
    ax.set_xlabel('Date')
    ax.set_ylabel('Close ($)')
    ax.set_title('Weekly Time Series Plot of Microsoft Stock')
    ax.grid(True)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(msft_data_filled['Volume'], msft_data_filled['Close'], alpha=0.5)
    ax.set_xlabel('Trading Volume')
    ax.set_ylabel('Closing Price ($)')
    ax.set_title('Scatter Plot of Trading Volume vs. Closing Price')
    ax.grid(True)
    st.pyplot(fig)


def forecasts():
    st.write("Linear Forecast")
    image_url = path + "Images/Linear_Forecast.png"
    st.image(image_url,  width=200, use_column_width=False)

    st.write("Naive Forecast")
    image_url = path + "Images/Naive_Forecast.png"
    st.image(image_url,  width=200, use_column_width=False)

def main():
    st.sidebar.title("Navigation")
    page_options = ["Home", "Decompositions", "Time Series Plots", "Forecasts"]
    choice = st.sidebar.selectbox("Go to", page_options)

    if choice == "Home":
        home_page()
    elif choice == "Decompositions":
        decomposition()
    elif choice == "Time Series Plots":
        ts_plots()
    elif choice == "Forecasts":
        forecasts()

if __name__ == "__main__":
    main()