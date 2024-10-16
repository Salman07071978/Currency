import streamlit as st

# Exchange rates for 10 different currencies to PKR (hidden from user view)
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

# Streamlit app for currency conversion
def main():
    st.title("🌍 Interactive Currency Converter")
    st.write("Easily convert your foreign currencies to Pakistani Rupees (PKR).")

    # Adding a dynamic selection with emojis for an interactive experience
    st.subheader("Select Your Currency and Enter the Amount")

    # Define currency choices with a friendly display
    currency_dict = {
        "🇺🇸 US Dollar (USD)": "USD",
        "🇪🇺 Euro (EUR)": "EUR",
        "🇬🇧 British Pound (GBP)": "GBP",
        "🇮🇳 Indian Rupee (INR)": "INR",
        "🇯🇵 Japanese Yen (JPY)": "JPY",
        "🇨🇦 Canadian Dollar (CAD)": "CAD",
        "🇦🇺 Australian Dollar (AUD)": "AUD",
        "🇨🇳 Chinese Yuan (CNY)": "CNY",
        "🇸🇦 Saudi Riyal (SAR)": "SAR",
        "🇦🇪 UAE Dirham (AED)": "AED"
    }

    # Selectbox to choose currency in a more user-friendly way
    currency = st.selectbox("Select your currency:", list(currency_dict.keys()))
    
    # Convert the selected friendly name back to currency code
    selected_currency = currency_dict[currency]
    
    # User inputs amount
    amount = st.number_input(f"Enter the amount in {currency.split()[1]}:", min_value=0.0, format="%.2f")
    
    # Convert and display result
    if st.button("Convert"):
        converted_amount = currency_converter(amount, selected_currency)
        
        if converted_amount is not None:
            st.success(f"💸 {amount} {selected_currency} is equal to {converted_amount:.2f} PKR.")
        else:
            st.error("⚠️ Conversion failed. Please try again.")

    # Add a fun message to encourage further interaction
    st.write("💡 Curious to know more? Try converting amounts in different currencies!")

# Run the Streamlit app
if __name__ == "__main__":
    main()
