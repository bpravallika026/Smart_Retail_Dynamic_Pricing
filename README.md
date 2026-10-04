# Smart Retail Dynamic Pricing Engine

## Overview

The Smart Retail Dynamic Pricing Engine is a machine learning-based application that recommends a selling price for a retail product by considering demand, wholesale cost, competitor pricing, inventory level, and day of the week.

The system uses a Random Forest Regression model to predict expected product demand and then evaluates different candidate prices to identify the price that can maximize expected profit.

## Project Workflow

Historical Retail Data
        ↓
Data Inspection
        ↓
Random Forest Regression
        ↓
Demand Prediction
        ↓
Price Optimization
        ↓
Expected Profit Calculation
        ↓
Recommended Retail Price
        ↓
Streamlit Dashboard

## Features

- Synthetic retail sales dataset generation
- Data inspection and validation
- Machine learning-based demand prediction
- Random Forest Regression model
- Dynamic price optimization
- Competitor price consideration
- Inventory-aware pricing
- Expected profit calculation
- Price vs. expected profit visualization
- Interactive Streamlit dashboard

## Machine Learning Model

The project uses a Random Forest Regressor to predict:

`units_sold`

The model uses the following features:

- Historical Price
- Base Wholesale Cost
- Competitor Price
- Inventory Level
- Day of Week
- Weekend Indicator

## Price Optimization

For each candidate selling price, the system predicts expected demand and calculates:

Profit = (Selling Price - Wholesale Cost) × Predicted Units Sold

The price producing the highest expected profit is selected as the recommended price.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Joblib
- Streamlit

## Project Structure

```text
Smart_Retail_Dynamic_Pricing/
│
├── data/
│   └── retail_sales.csv
│
├── models/
│   └── demand_model_compressed.pkl
│
├── src/
│   ├── generate_data.py
│   ├── inspect_data.py
│   ├── train_model.py
│   └── optimizer.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
