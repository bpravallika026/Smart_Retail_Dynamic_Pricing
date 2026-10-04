import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Load the dataset
df = pd.read_csv("data/retail_sales.csv")

# Features used to predict demand
features = [
    "historical_price",
    "base_wholesale_cost",
    "competitor_price",
    "inventory_level",
    "day_of_week",
    "is_weekend"
]

X = df[features]
y = df["units_sold"]


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create the Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


# Make predictions on test data
predictions = model.predict(X_test)


# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model training completed!")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.4f}")


# Save the trained model
model_path = "models/demand_model.pkl"
joblib.dump(model, model_path)

print(f"Model saved to: {model_path}")