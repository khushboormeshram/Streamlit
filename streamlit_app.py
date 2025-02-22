import streamlit as st

# Title
st.title("Simple Streamlit App")

# Input field
name = st.text_input("Enter your name:")

# Button to display the name
if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to Streamlit.")
