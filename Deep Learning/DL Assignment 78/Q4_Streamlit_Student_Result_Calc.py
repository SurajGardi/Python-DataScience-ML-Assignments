"""
Question 4:
4: Student Result Calculator
Develop a Streamlit application that accepts a student's name and marks in three subjects. Calculate total marks,
percentage and display whether the student has passed or failed. Consider 40 marks out of 100 as the minimum
passing marks in each subject.
"""

import streamlit as st

st.title("Marvellous Infosystems")

st.header("Student Result Calculator")

name = st.text_input("Enter Student Name")

marks1 = st.number_input("Enter Marks for Subject 1", min_value=0, max_value=100, value=0, step=1)
marks2 = st.number_input("Enter Marks for Subject 2", min_value=0, max_value=100, value=0, step=1)
marks3 = st.number_input("Enter Marks for Subject 3", min_value=0, max_value=100, value=0, step=1)

if st.button("Calculate Result"):
    total = marks1 + marks2 + marks3
    percentage = total / 3

    st.write("Student Name :", name)
    st.write("Total Marks :", total)
    st.write("Percentage :", percentage, "%")

    if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
        st.success("Result : Pass")
    else:
        st.error("Result : Fail")