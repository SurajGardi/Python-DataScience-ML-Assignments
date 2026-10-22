"""
Question 2:
2: Even or Odd Number
Develop a Streamlit application that accepts an integer from the user. Provide a Check button to determine
whether the entered number is even or odd and display the result.
"""

import streamlit as st

st.title("Marvellous Infosystems")

st.header("Even or Odd Number")

num = st.number_input("Enter an Integer", value=0, step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success("The number is Even")
    else:
        st.success("The number is Odd")