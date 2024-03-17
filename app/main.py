import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import numpy as np
import matplotlib.pyplot as plt


@st.cache_data
def load_data_and_model():
    with open('all_tickers_data.pkl', 'rb') as file:
        earnings_data = pickle.load(file)
    return earnings_data

earnings_data = load_data_and_model()
earnings_data['Target'] = earnings_data['End'].shift(-1)


user_input = st.text_input("Enter a ticker symbol:", '')
tickers = earnings_data['Ticker'].unique()
selected_ticker = st.selectbox('Or select a ticker:', options=[user_input] + list(tickers))


def predict_earnings(selected_ticker):
    
    ticker_data = earnings_data[earnings_data['Ticker'] == selected_ticker]
    
    
    ticker_data['Date'] = pd.to_datetime(ticker_data['Date'])
    ticker_data['Year'] = ticker_data['Date'].dt.year
    ticker_data['Month'] = ticker_data['Date'].dt.month
    ticker_data['Day'] = ticker_data['Date'].dt.day

   
    features = ['Open', 'High', 'Low', 'End', 'Volume', 'Year', 'Month', 'Day']
    X = ticker_data[features]
    y = ticker_data['Target']  
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   
    model = XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return y_test, predictions


if st.button('Predict Earnings'):
    if selected_ticker:
        y_test, predictions = predict_earnings(selected_ticker)
        
        
        
        plt.figure(figsize=(12, 6))  
        plt.plot(y_test.values, label='Actual Earnings', color='blue', marker='o')  
        plt.plot(predictions, label='Predicted Earnings', color='red', linestyle='--')  
        plt.xlabel('Sample Index', fontsize=14) 
        plt.ylabel('Earnings', fontsize=14)  
        plt.title(f'Earnings Prediction for {selected_ticker}', fontsize=18)  
        plt.legend(fontsize=12)  
        plt.tight_layout()  
        st.pyplot(plt)
    else:
        st.error("Please select a ticker.")
