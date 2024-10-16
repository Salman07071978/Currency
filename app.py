import streamlit as st

def calculate_tax(salary, tax_rate):
    """Calculate tax based on salary and tax rate."""
    tax = salary * (tax_rate / 100)
    salary_after_tax = salary - tax
    return tax, salary_after_tax

# Streamlit app to simulate a tax calculation program for an IT customer
def main():
    st.title("💻 Tax Calculator Simulation")
    st.write("""
    This program simulates a scenario where an IT firm is tasked to create a C program that calculates 
    the tax a user has to pay and their salary after tax deduction. 
    We'll do this interactively in Python to demonstrate.
    """)

    # Step 1: Take the tax rate input
    st.subheader("Step 1: Input Tax Rate")
    tax_rate = st.number_input("Enter the tax rate (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

    # Step 2: Take the salary input
    st.subheader("Step 2: Input Salary")
    salary = st.number_input("Enter the salary", min_value=0.0, value=50000.0, step=500.0)

    # Step 3: Calculate tax and salary after tax
    if st.button("Calculate Tax"):
        tax, salary_after_tax = calculate_tax(salary, tax_rate)
        
        # Display results
        st.write(f"💵 **Tax to Pay**: {tax:.2f} PKR")
        st.write(f"💰 **Salary after Tax**: {salary_after_tax:.2f} PKR")

        st.success("Tax calculation complete!")

    # Add a final message to summarize the IT firm’s request fulfillment
    st.subheader("Simulation Summary")
    st.write("This interactive simulation fulfills the client's request for a C program that calculates tax and salary.")

if __name__ == "__main__":
    main()
