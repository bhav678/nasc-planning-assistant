import streamlit as st

st.title("NASC Labor Planning Assistant")

st.write("Welcome to the NASC Labor Planning Assistant. This is a basic version.")

user_input = st.text_input("Ask a question about labor planning:")

if user_input:
    st.write(f"You asked: {user_input}")
    st.write("I'm sorry, I'm not fully functional yet. Check back soon!")