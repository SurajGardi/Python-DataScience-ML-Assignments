"""
Question 1:
1: Addition of Two Numbers
Develop a Streamlit application that accepts two numbers from the user using input fields. Provide an Add
button to calculate and display the addition of the entered numbers..
"""

import streamlit as st

st.title("Marvellous Infosystems")

st.header("Addition of Two Numbers")

no1 = st.number_input("Enter First Number", value=0, step=1)
no2 = st.number_input("Enter Second Number", value=0, step=1)

if st.button("Add"):
    result = no1 + no2
    st.success("Addition is : " + str(result))