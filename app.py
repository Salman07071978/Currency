import streamlit as st
import matplotlib.pyplot as plt

# Exchange rates for 10 different currencies to PKR
exchange_rates = {
    "USD": 280.0,    # 1 USD to PKR
    "EUR": 300.0,    # 1 EUR to PKR
    "GBP": 350.0,    # 1 GBP to PKR
    "INR": 3.5,      # 1 INR to PKR
    "JPY": 2.0,      # 1 JPY to PKR
    "CAD": 210.0,    # 1 CAD to PKR
    "AUD": 190.0,    # 1 AUD to PKR
    "CNY": 40.0,     # 1 CNY to PKR
    "SAR": 75.0,     # 1 SAR to PKR
    "AED": 76.0      # 1 AED to PKR
}

# Currency converter function
def currency_converter(amount, currency):
    """Convert the given amount of foreign currency to PKR."""
    if currency in exchange_rates:
        pkr_value = amount * exchange_rates[currency]
        return pkr_value
    else:
        return None

# Function to plot the exchange rates
def plot_exchange_rates():
    """Plot a bar chart of the exchange rates."""
    currencies = list(exchange_rates.keys())
    rates = list(exchange_rates.values())
    
    plt.figure(figsize=(8, 5))
    plt.bar(currencies, rates, color='lightgreen')
    plt.title('Exchange Rates to PKR', fontsize=16)
    plt.ylabel('Rate (1 Unit to PKR)', fontsize=12)
    plt.xlabel('Currency', fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

# Streamlit app for currency conversion
def main():
    st.title("🌍 Interactive Currency Converter")
    st.write("Convert foreign currencies to Pakistani Rupees (PKR).")

    # Display current exchange rates
    st.subheader("Current Exchange Rates")
    st.write("Here are the exchange rates of 10 currencies against the Pakistani Rupee (PKR):")
    st.table(exchange_rates)

    # User input for currency conversion
    st.subheader("Currency Conversion")
    
    with st.form(key="conversion_form"):
        currency = st.selectbox("Select the currency:", options=list(exchange_rates.keys()), help="Choose a currency to convert.")
        amount = st.number_input(f"Enter the amount in {currency}:", min_value=0.0, format="%.2f", help="Input the amount you want to convert.")
        
        # Submit button
        submitted = st.form_submit_button(label="Convert")
        
        if submitted:
            converted_amount = currency_converter(amount, currency)
            if converted_amount is not None:
                st.success(f"💸 {amount} {currency} is equal to {converted_amount:.2f} PKR.")
            else:
                st.error("⚠️ Invalid currency selection! Please choose a valid currency.")

    # Visualization of exchange rates
    st.subheader("📊 Visualize Exchange Rates")
    st.write("The following chart shows the exchange rates of different currencies to PKR.")
    plot_exchange_rates()

    # Add a note about exchange rate fluctuations
    st.info("💡 Exchange rates can fluctuate. The rates displayed here are hypothetical and static for demonstration purposes.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
