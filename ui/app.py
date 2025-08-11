import streamlit as st
import requests

st.title("Intelligent Data Analysis Agent")

query = st.text_input("Enter your natural language query:")
if st.button("Run Pipeline"):
    res = requests.post("http://orchestrator:8000/run", params={"query": query})
    st.json(res.json())
