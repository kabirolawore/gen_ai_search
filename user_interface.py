import re, json, requests
import streamlit as st


st.title('_:blue[Local GenAI Search]_ :sunglasses:')
question = st.text_input("Ask a question based on your local files", "")