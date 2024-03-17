# Stock Prediction Project
This repository contains the code and data for a stock prediction project, leveraging historical stock prices, EPS data, and options data to predict stock performance.

## Project Structure
data_processing_and_ML: This directory contains scripts and Jupyter notebooks for data collection, processing, and machine learning model training.
pickle: This directory includes serialized Python objects that store pre-trained models and processed datasets for quick loading.
app: The Streamlit application for interactive data analysis and stock prediction visualization is stored here.

## Data Collection
The project utilizes various financial APIs to collect data:

- Historical stock prices from yfinance and Alpha Vantage
- EPS data and earnings date information from Alpha Vantage
- Options chain data from Polygon.io


![image](https://github.com/sjrpokemon/stock-prediction-project/assets/128329266/c8153925-b92a-41a9-8a88-f01689e20be5)
## Running the Streamlit App
The main.py script in the app directory is the entry point for running the Streamlit application. To run the app locally, follow these steps:

1. Ensure you have Streamlit installed. If not, install it using pip:

pip install streamlit
2. Navigate to the app directory in your command line interface.
3. Run the Streamlit app with the command:
streamlit run main.py

## Features
- Ticker Selection: Enter a ticker symbol or select one from the dropdown menu to view its earnings data.
- Earnings Prediction: Click 'Predict Earnings' to view the predicted earnings for the selected ticker based on the trained XGBoost regression model.

## Data Preprocessing and Model Training
The model training and data preprocessing are done in the data_processing_and_ML directory. The pre-trained model and processed data are saved using pickle and loaded into the Streamlit app for predictions.

## Visualization
The app visualizes the actual earnings and predicted values using matplotlib, offering a clear graphical representation of the model's performance.

## Dependencies
The project requires the following Python libraries:

pandas
numpy
xgboost
matplotlib
pickle
sklearn

Ensure all dependencies are installed using pip:
pip install pandas numpy xgboost matplotlib scikit-learn

Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
