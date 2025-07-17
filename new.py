import streamlit as st
import pickle 

with open('knn.pkl', 'rb') as f:
    model = pickle.load(f)

age = st.number_input("Enter age")
salary = st.number_input("Enter Salary")
exp = st.number_input("enter your Experience")
dept = st.number_input("Enter department : (0-HR;1-IT;2-Saales)")

pred = model.predict([[age,salary,exp,dept]])

if st.button("Analyze"):
    if pred == 1:
        st.success("You are doing good")
    else:
        st.info("chances of layoff")
