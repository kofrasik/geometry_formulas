import streamlit as st
sd= st.number_input("Enter side")
area = sd**2
st.write("Area of following square is :-")
st.write(area)

st.latex('\phi')