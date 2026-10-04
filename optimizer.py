import pandas as pd
import joblib


# Load the trained demand model
model = joblib.load("models/demand_model.pkl")


def optimize_price(
    wholesale_cost,
    competitor_price,
    inventory_level,
    day_of_week
):
    """
    Find the selling price that produces the highest expected profit.
    """

    # Weekend: Saturday = 5, Sunday = 6
    is_weekend = 1 if day_of_week >= 5 else 0

    # Minimum price: cannot sell below wholesale cost
    min_price = wholesale_cost

    # Maximum price: allow a reasonable premium over competitor price
    max_price = max(
        wholesale_cost + 1,
        competitor_price * 1.20
    )

    # Generate possible prices
    candidate_prices = pd.Series(
        [round(price, 2) for price in
         range(int(min_price), int(max_price) + 1)]
    )

    # Create input data for the ML model
    input_data = pd.DataFrame({
        "historical_price": candidate_prices,
        "base_wholesale_cost": wholesale_cost,
        "competitor_price": competitor_price,
        "inventory_level": inventory_level,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend
    })

    # Predict demand for every candidate price
    predicted_demand = model.predict(input_data)

    # Calculate expected profit
    profits = (
        candidate_prices - wholesale_cost
    ) * predicted_demand

    # Find the price with maximum profit
    best_index = profits.idxmax()

    best_price = candidate_prices.iloc[best_index]
    best_demand = predicted_demand[best_index]
    best_profit = profits.iloc[best_index]

    return best_price, best_demand, best_profit, candidate_prices, profits


# Test the optimizer
if __name__ == "__main__":

    price, demand, profit, candidate_prices, profits = optimize_price(
        wholesale_cost=200,
        competitor_price=300,
        inventory_level=250,
        day_of_week=5
    )

    print("Recommended Price:", round(price, 2))
    print("Expected Units Sold:", round(demand))
    print("Expected Profit:", round(profit, 2))