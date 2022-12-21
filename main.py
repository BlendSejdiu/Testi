import streamlit as st

titulli = st.text_input("Shkruani numrin 3 : ")

if titulli == "3":
    st.title("Numri juaj ishte i sakt")
elif titulli == "":
    st.title("")
else:
    st.title("Numri juaj nuk ishte i sakte")