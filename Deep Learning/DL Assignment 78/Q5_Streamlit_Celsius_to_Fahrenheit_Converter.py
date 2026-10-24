"""
Question 5:
5: Celsius to Fahrenheit Converter
Develop a Streamlit application that accepts temperature in Celsius. Provide a Convert button to convert the
entered temperature into Fahrenheit and display the result.
"""

import streamlit as st

st.title("Marvellous Infosystems")

st.header("Celsius to Fahrenheit Converter")

celsius = st.number_input(
    "Enter Temperature in Celsius",
    value=0.0,
    step=1.0
)

if st.button("Convert"):
    fahrenheit = (celsius * 9 / 5) + 32

    st.success("Temperature in Fahrenheit : " + str(fahrenheit) + " °F")

