import streamlit as st

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

# Streamlit app
def main():
    st.title("Currency Converter")
    st.write("Convert foreign currencies to Pakistani Rupees (PKR).")
    
    # User inputs
    currency = st.selectbox("Select the currency", options=list(exchange_rates.keys()))
    amount = st.number_input(f"Enter the amount in {currency}", min_value=0.0, format="%.2f")
    
    # Convert and display result
    if st.button("Convert"):
        converted_amount = currency_converter(amount, currency)
        
        if converted_amount is not None:
            st.success(f"{amount} {currency} is equal to {converted_amount:.2f} PKR.")
        else:
            st.error("Invalid currency code. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
