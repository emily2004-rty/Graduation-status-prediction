import streamlit as st
import pandas as pd
import joblib

model=joblib.load("Svm.pkl")




st.title("Welcome to Graduation status App")
st.header("Please fill in your details below to proceed with predicting your Graduation Status")

st.divider()

Gender=st.selectbox("Choose your Gender",("Male","Female"))
SKill_Level=st.selectbox("Skill Level",("Beginner","Intermediate","Elementary","Advanced"))
Commit_hours=st.selectbox("How many hours are you available in a week",("0-6 hours","7-14 hours","14-more hours"))
Aim=st.selectbox("What is your aim in applying to this track",('Upskill', 'Learn data afresh','Connect with fellow data professionals','Build a project portfolio','both upskilling and connecting with fellow data professionals'))
Learning_experience=st.selectbox("How many experience do you have in data field",("Less than six months","6-1year","1-3years","4-6years"))
Age_range=st.selectbox("Select your Age range",("18-24 years","25-34 years","45-54 years","35-44 years"))
Total_score=st.number_input("Enter your aplitude score",min_value=0.0,max_value=100.0)
Track=st.selectbox("Select the track you are applying to",("Data analysis","Data Science"))
Country=st.selectbox("Select which country you are from",("Kenya","South Africa"))
Test_Completion=st.selectbox("Have you completed yout test",("Yes","No"))
Hear_About_us=st.selectbox("How did you hear about us",("WhatsApp","Twitter","Geeks for geeks","Instagram","LinkeldIn","Word of mouth"))


    


if st.button("Predict"):
    input_data=pd.DataFrame([{
        "Gender":Gender,
        "Skill level":SKill_Level,
        "Hours_commit":Commit_hours,
        "Aim":Aim,
        "Learning_Experience":Learning_experience,
        "Age range":Age_range,
        "Total score":Total_score,
        "Track":Track,
        "Country":Country,
        "Test_Completion":Test_Completion,
        "Hear_About_us":Hear_About_us
    }])


    prediction =model.predict(input_data)[0]

    st.subheader(f"prediction: '{str(prediction)}'")

    if prediction == 1:
        st.error("The applicant will graduate")
    else:
        st.success("The applicant will not graduate")



