"""
Question 3:
3: Simple Interest Calculator
Develop a Streamlit application that accepts Principal Amount, Rate of Interest and Time Period. Provide a
Calculate button to calculate and display the Simple Interest.
"""

import streamlit as st

st.title("Marvellous Infosystems")

st.header("Simple Interest Calculator")

principal = st.number_input("Enter Principal Amount", value=0.0, step=100.0)
rate = st.number_input("Enter Rate of Interest (%)", value=0.0, step=0.5)
time = st.number_input("Enter Time Period (Years)", value=0.0, step=1.0)

if st.button("Calculate"):
    simple_interest = (principal * rate * time) / 100

    st.success("Simple Interest is : " + str(simple_interest))