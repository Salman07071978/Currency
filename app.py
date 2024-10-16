pip install matplotlib
pip install matplotlib==3.7.1

import streamlit as st
import matplotlib.pyplot as plt

# Currency rates as of a certain date
exchange_rates = {
    "USD": 280,    # 1 USD to PKR
    "EUR": 300,    # 1 EUR to PKR
    "GBP": 350,    # 1 GBP to PKR
    "INR": 3.5,    # 1 INR to PKR
    "JPY": 2.0,    # 1 JPY to PKR
}

# Currency converter function
def currency_converter(amount, currency):
    if currency in exchange_rates:
        pkr_value = amount * exchange_rates[currency]
        return pkr_value
    else:
        return None

# Plotting function for exchange rates
def plot_exchange_rates():
    currencies = list(exchange_rates.keys())
    rates = list(exchange_rates.values())
    
    plt.figure(figsize=(6,4))
    plt.bar(currencies, rates, color='teal')
    plt.title('Exchange Rates (1 Unit to PKR)')
    plt.xlabel('Currency')
    plt.ylabel('Rate (PKR)')
    st.pyplot(plt)

# Streamlit app
def main():
    # App title and description
    st.title("💱 Interactive Currency Converter")
    st.write("Convert foreign currencies to **Pakistani Rupees (PKR)** in real-time and visualize exchange rates.")

    # Plot exchange rates for better visualization
    st.subheader("Exchange Rates Overview")
    plot_exchange_rates()

    # User inputs
    st.subheader("Currency Conversion")
    currency = st.selectbox("Select the currency", options=list(exchange_rates.keys()))
    amount = st.number_input(f"Enter the amount in {currency}", min_value=0.0, format="%.2f", help="Amount of foreign currency to convert into PKR.")
    
    # Automatically update the conversion as the user types
    if amount > 0:
        converted_amount = currency_converter(amount, currency)
        st.success(f"💵 **{amount} {currency}** is equal to **{converted_amount:.2f} PKR**.")
    else:
        st.info("Please enter an amount greater than 0.")

    # Conversion Tips
    st.sidebar.header("💡 Currency Conversion Tips")
    st.sidebar.write("""
    - Exchange rates fluctuate frequently.
    - Always check for updated rates before making large conversions.
    - You can use this tool to estimate conversions for small transactions.
    """)

# Run the app
if __name__ == "__main__":
    main()
