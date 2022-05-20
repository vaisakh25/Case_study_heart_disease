import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model_new.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_heart_disease(BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth,DiffWalking,
                          Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer,
                          Age, Sex_Female, Sex_Male, Race_American_Indian_Alaskan_Native, Race_Asian, Race_Black, Race_Hispanic,
                          Race_Other, Race_White):
    
    """Let's check if the person has heart disease
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: BMI
        in: query
        type: number
        required: true
      - name: Smoking
        in: query
        type: number
        required: true
      - name: AlcoholDrinking
        in: query
        type: number
        required: true
      - name: Stroke
        in: query
        type: number
        required: true
      - name: PhysicalHealth
        in: query
        type: number
        required: true
      - name: MentalHealth
        in: query
        type: number
        required: true
      - name: DiffWalking
        in: query
        type: number
        required: true
      - name: Diabetic
        in: query
        type: number
        required: true
      - name: PhysicalActivity
        in: query
        type: number
        required: true
      - name: GenHealth
        in: query
        type: number
        required: true
      - name: SleepTime
        in: query
        type: number
        required: true
      - name: Asthma
        in: query
        type: number
        required: true
      - name: KidneyDisease
        in: query
        type: number
        required: true
      - name: SkinCancer
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: Sex_Female
        in: query
        type: number
        required: true
      - name: Sex_Male
        in: query
        type: number
        required: true
      - name: Race_American_Indian_Alaskan_Native
        in: query
        type: number
        required: true
      - name: Race_Asian
        in: query
        type: number
        required: true
      - name: Race_Black
        in: query
        type: number
        required: true
      - name: Race_Hispanic
        in: query
        type: number
        required: true
      - name: Race_Other
        in: query
        type: number
        required: true
      - name: Race_White
        in: query
        type: number
        required: true
      
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth,DiffWalking,
                          Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer,
                          Age, Sex_Female, Sex_Male, Race_American_Indian_Alaskan_Native, Race_Asian, Race_Black, Race_Hispanic,
                          Race_Other, Race_White]])
    print(prediction)
    return prediction



def main():
    st.title("Heart Disease prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease prediction
    </h2> ML App
    </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    BMI = st.text_input("BMI","Type Here")
    Smoking = st.text_input("Smoking -(1 - 'yes', 0 - 'no')","Type Here")
    AlcoholDrinking= st.text_input("AlcoholDrinking-(1 - 'yes', 0 - 'no')","Type Here")
    Stroke= st.text_input("Stroke-(1 - 'yes', 0 - 'no')","Type Here")
    PhysicalHealth= st.text_input("PhysicalHealth(Numeric from: 1- 30","Type Here")
    MentalHealth= st.text_input("MentalHealth(Numeric from: 1- 30","Type Here")
    DiffWalking= st.text_input("DiffWalking-(1 - 'yes', 0 - 'no')","Type Here")
    Diabetic= st.text_input("Diabetic-(1 - 'yes', 0 - 'no')","Type Here")
    PhysicalActivity= st.text_input("PhysicalActivity-(1 - 'yes', 0 - 'no')","Type Here")
    GenHealth= st.text_input("GenHealth-(5 - 'excellent', 4 - 'very good', 3 - 'good', 2 - 'fair', 1 - 'poor')","Type Here")
    SleepTime= st.text_input("SleepTime(In Hours)","Type Here")   
    Asthma= st.text_input("Asthma-(1 - 'yes', 0 - 'no')","Type Here")
    KidneyDisease= st.text_input("KidneyDisease-(1 - 'yes', 0 - 'no')","Type Here")
    SkinCancer= st.text_input("SkinCancer-(1 - 'yes', 0 - 'no')","Type Here")
    Age= st.text_input("Age","Type Here")
    Sex_Female= st.text_input("Sex_Female-(1 - 'yes', 0 - 'no')","Type Here")
    Sex_Male= st.text_input("Sex_Male -(1 - 'yes', 0 - 'no')","Type Here")
    Race_American_Indian_Alaskan_Native= st.text_input("Race_American_Indian_Alaskan_Native-(1 - 'yes', 0 - 'no')","Type Here")
    Race_Asian= st.text_input("Race_Asian-(1 - 'yes', 0 - 'no')","Type Here")
    Race_Black= st.text_input("Race_Black-(1 - 'yes', 0 - 'no')","Type Here") 
    Race_Hispanic= st.text_input("Race_Hispanic-(1 - 'yes', 0 - 'no')","Type Here")
    Race_Other= st.text_input("Race_Other-(1 - 'yes', 0 - 'no')","Type Here")
    Race_White= st.text_input("Race_White-(1 - 'yes', 0 - 'no')","Type Here")
    result="" 
    if st.button("Predict"):
        result=predict_heart_disease(BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth,DiffWalking,
                          Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer,
                          Age, Sex_Female, Sex_Male, Race_American_Indian_Alaskan_Native, Race_Asian, Race_Black, Race_Hispanic,
                          Race_Other, Race_White)
        if result == 1:
            st.success('The person has heart disease')
            #st.success('The output is {}'.format(result))
        else:
            st.success('The person does not have heart disease')
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()