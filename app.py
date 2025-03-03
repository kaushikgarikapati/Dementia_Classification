import streamlit as st
import pandas as pd
import numpy as np
import pickle


LABEL_MAPPING = {
    0: "ADHD Negative",
    1: "ADHD Positive"
}

@st.cache_resource
def load_sklearn_models(model_path):

    with open(model_path, 'rb') as model_file:
        final_model = pickle.load(model_file)

    return final_model

# load the model
adhd_model = load_sklearn_models("best_model_rf")


#title of the web page
st.title("ADHD Predicting WebApp")

IMAGE_ADDRESS = "https://media.npr.org/assets/img/2024/05/22/gettyimages-1805884626_custom-12456c773bb5d72837b1b3534ff4e90e4f68a983.jpg?s=1100&c=85&f=jpeg"
# set the image
st.image(IMAGE_ADDRESS)

st.subheader("Please enter the details:")

#input for Gender
gender=st.selectbox("Choose a gender",("Male","Female"),)
if gender=="Male":
    g=0

else:
    g=1
#st.write("You selected: ",gender)

#input for age
age=st.slider("What is the age", 0, 30,0)
#st.write("Age is", age, "years old")

#Input for Handedness
handedness=st.selectbox("Please select the dominant hand",("Right-Handed","Left-Handed","Ambidextrous-both the hands"))
if handedness=="Right-Handed":
    h=0
elif handedness=="Left-Handed":
    h=1
else:
    h=2
#st.write("You selected:",handedness )


# Input for Inattentive score 
inattentive = st.slider("Rate the level of inattentiveness (0-100)", 0, 100, 0)
#st.write(f"Inattentiveness score: {inattentive}")



# Input for Impulsive score 
impulsive = st.slider("Rate the level of impulsiveness (0-100)", 0, 100, 0)
#st.write(f"Impulsiveness score: {impulsive}")

# IQ Measure input
iq_measure=st.slider("Select IQ Measure (1-5)", 1,5,0) 
#st.write(f"Selected IQ Measure: {iq_measure}")

# Verbal IQ input
verbal_iq = st.slider("Enter the  Verbal IQ", 0, 200, 0)
#st.write(f"Verbal IQ score: {verbal_iq}")

# Performance IQ input
performance_iq = st.slider("Enter your Performance IQ", 0, 200,0)
#st.write(f"Performance IQ score: {performance_iq}")

# Full4 IQ input
full4_iq = st.slider("Enter your Full-Scale IQ (full4 IQ)", 0, 200, 0)
#st.write(f"Full scale IQ score: {full4_iq}")

# Med Status input
med_status = st.radio("Are you on medication?", ("Yes", "No"))
if med_status=='Yes':
    m=1
else:
    m=2
#st.write(f"Medication Status: {med_status}")



#make Predictions

if st.button('Predict ADHD'):
    input_data=[[g,age,h,inattentive,impulsive,iq_measure,verbal_iq,performance_iq,full4_iq,m]]
    predictions=adhd_model.predict(input_data)
    st.spinner(text="In progress...")
    st.subheader("User Condition: {}".format(LA
