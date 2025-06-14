import streamlit as st
from datetime import datetime

st.title("🎉 Age Calculator App")

# User input
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)

# Logic to compute year
if name and age:
    current_year = datetime.now().year
    year_turn_100 = current_year + (100 - age)
    st.success(f"Hi {name}! 🎈 You will turn 100 years old in the year {year_turn_100}.")
