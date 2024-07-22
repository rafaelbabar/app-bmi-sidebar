import streamlit as st
st.sidebar.header("BMI Calculator")    

def dashboard():

    units = st.sidebar.radio("Please select your units",
    [":rainbow[Metric]", ":rainbow[Imperial]"])
    if units == ":rainbow[Metric]":
        st.write("You selected Metric.")
        height=st.sidebar.slider("Height in m", 1.55,2.15,1.74)
        weight=st.sidebar.slider("Weight in kg", 40,120,75)
        bmi=int(weight/(height**2))
        st.write("BMI is ",bmi)
    else:
        st.write("You selected Imperial.")
        height=st.sidebar.slider("Height in inches", 60,80,69)
        weight=st.sidebar.slider("Weight in lbs", 90,250,165)
        bmi=int(703*(weight/(height**2)))
        st.write("BMI is ",bmi)
    if bmi < 18.5:
        st.write("Underweight")
        st.image("red.png")
    elif bmi >=18.5 and bmi <=24.9:
        st.write("Healthy weight")
        st.image("green.png")
    elif bmi >=24.9 and bmi <=29.9:
        st.write("Overweight")
        st.image("yellow.png")
    else:
        st.write("Obese")
        st.image("red.png")
        
dashboard(
