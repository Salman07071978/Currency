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
    """Convert the given amount of foreign currency to PKR"""
    if currency in exchange_rates:
        pkr_value = amount * exchange_rates[currency]
        return pkr_value
    else:
        return None

# Plotting function for visualizing exchange rates
def plot_exchange_rates():
    """Plots a bar chart of the exchange rates"""
    currencies = list(exchange_rates.keys())
    rates = list(exchange_rates.values())

    plt.figure(figsize=(8, 4))
    plt.bar(currencies, rates, color='skyblue')
    plt.title('Exchange Rates to PKR')
    plt.ylabel('Rate (1 Unit to PKR)')
    plt.xlabel('Currency')
    st.pyplot(plt.gcf())  # Display the plot in Streamlit

# Streamlit app function
def main():
    st.title("💱 Interactive Currency Converter")
    st.write("Easily convert foreign currencies to Pakistani Rupees (PKR).")

    # Input form for conversion
    with st.form(key="currency_form"):
        st.subheader("Currency Conversion")
        
        currency = st.selectbox("Select the currency to convert from:", options=list(exchange_rates.keys()))
        amount = st.number_input(f"Enter the amount in {currency}", min_value=0.0, format="%.2f")
        
        submitted = st.form_submit_button(label="Convert")
        
        if submitted:
            converted_amount = currency_converter(amount, currency)
            if converted_amount is not None:
                st.success(f"{amount} {currency} is equal to {converted_amount:.2f} PKR.")
            else:
                st.error("Error: Invalid currency code. Please select a valid currency.")

    # Interactive visualization of exchange rates
    st.subheader("Visualize Exchange Rates")
    st.write("This chart shows the current exchange rates of different currencies to PKR.")
    plot_exchange_rates()

# Run the Streamlit app
if __name__ == "__main__":
    main()
