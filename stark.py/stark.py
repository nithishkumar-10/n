import streamlit as st
st.title("calculator")
a=st.number_input("enter the number")
b=st.number_input("enter the second number")
if st.button("add"):
    st.write(a+b)
elif st.button("sub"):
    st.write(a-b)
elif st.button("multiply"):
    st.write(a*b)
elif st.button("divide"):
    st.write(a/b)
