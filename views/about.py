import streamlit as st
st.title("About Page")
st.header("This is about us")
col1,col2 = st.columns(2)
col1.text("This is column 1")
col2.subheader("This is column 2")