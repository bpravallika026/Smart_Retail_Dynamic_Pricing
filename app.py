import streamlit as st
import pandas as pd
from src.optimizer import optimize_price

st.set_page_config(
    page_title="Smart Retail Dynamic Pricing",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Smart Retail Dynamic Pricing Engine")

st.write(
    "Use machine learning to predict demand and recommend "
    "a price that maximizes expected profit."
)

st.info(
    "This system uses historical retail data and a Random Forest "
    "model to predict product demand. It then evaluates multiple "
    "possible selling prices and recommends the price that is "
    "expected to generate the highest profit."
)

st.markdown("### How It Works")

st.markdown("""
1. **Enter product information** – wholesale cost, competitor price, inventory, and day of week.
2. **Predict demand** – the trained Random Forest model estimates expected units sold.
3. **Evaluate prices** – the system tests different possible selling prices.
4. **Calculate profit** – expected profit is calculated for each price.
5. **Recommend the best price** – the price with the highest expected profit is selected.
""")

st.subheader("Product Information")

wholesale_cost = st.number_input(
    "Wholesale Cost (₹)",
    min_value=1.0,
    value=200.0,
    step=10.0
)

competitor_price = st.number_input(
    "Competitor Price (₹)",
    min_value=1.0,
    value=300.0,
    step=10.0
)

inventory_level = st.number_input(
    "Current Inventory",
    min_value=1,
    value=250,
    step=10
)

day_of_week = st.selectbox(
    "Day of Week",
    options=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

day_number = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

selected_day = day_number[day_of_week]

if st.button("Calculate Recommended Price"):

    price, demand, profit, candidate_prices, profits = optimize_price(
        wholesale_cost,
        competitor_price,
        inventory_level,
        selected_day
    )

    st.success("Price recommendation generated!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Recommended Price", f"₹{price:.2f}")

    with col2:
        st.metric("Expected Units Sold", f"{demand:.0f}")

    with col3:
        st.metric("Expected Profit", f"₹{profit:,.2f}")

    st.subheader("Price vs Expected Profit")

    chart_data = pd.DataFrame({
        "Price": candidate_prices.to_numpy(),
        "Expected Profit": profits.to_numpy()
    })

    chart_data = chart_data.set_index("Price")

    chart_data["Recommended Price"] = None
    chart_data.loc[price, "Recommended Price"] = profit

    st.line_chart(chart_data)
