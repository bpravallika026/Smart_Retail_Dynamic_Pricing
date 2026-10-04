import pandas as pd
import numpy as np

# Make the random data reproducible
np.random.seed(42)

# Number of historical sales records
n = 5000

# Generate basic retail features
base_wholesale_cost = np.random.uniform(50, 500, n)

historical_price = base_wholesale_cost * np.random.uniform(1.2, 2.2, n)

competitor_price = historical_price * np.random.uniform(0.85, 1.15, n)

inventory_level = np.random.randint(10, 501, n)

day_of_week = np.random.randint(0, 7, n)

is_weekend = (day_of_week >= 5).astype(int)

# Generate realistic demand
price_effect = 120 - 0.15 * historical_price

competitor_effect = 0.10 * (competitor_price - historical_price)

inventory_effect = 0.02 * inventory_level

weekend_effect = 15 * is_weekend

random_effect = np.random.normal(0, 10, n)

units_sold = (
    price_effect
    + competitor_effect
    + inventory_effect
    + weekend_effect
    + random_effect
)

# Units sold cannot be negative
units_sold = np.maximum(units_sold, 0).round().astype(int)

# Create DataFrame
df = pd.DataFrame({
    "historical_price": historical_price.round(2),
    "base_wholesale_cost": base_wholesale_cost.round(2),
    "competitor_price": competitor_price.round(2),
    "inventory_level": inventory_level,
    "day_of_week": day_of_week,
    "is_weekend": is_weekend,
    "units_sold": units_sold
})

# Save dataset
output_path = "data/retail_sales.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print(f"Rows: {len(df)}")
print(f"Saved to: {output_path}")
print("\nFirst 5 rows:")
print(df.head())