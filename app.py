import streamlit as st
import joblib 
import pandas as pd
import numpy as np

# load the model

model  = joblib.load('linear_regression_model.pkl')

# Title to the APP 
st.title('Aircraft Fuel Consumption Predictor')

# Input Fields

flight_distance = st.number_input('Flight_Distance (KM)')
number_of_passenger = st.number_input('Number_of_Passenger')
flight_duration= st.number_input('Flight_Duration(Hours)')
aircraft_type = st.selectbox('Aircraft_Type',['Type1','Type2','Type3'])

# Creating DataFrame

input_data = pd.DataFrame(
    {
        'Flight_Distance' : [flight_distance],
        'Number_of_Passengers' :[number_of_passenger],
        'Flight_Duration' : [flight_duration],
        'Aircraft_Type_Type1' : [1 if aircraft_type == 'Type1' else 0 ],
        'Aircraft_Type_Type2' : [1 if aircraft_type == 'Type2' else 0 ],
        'Aircraft_Type_Type3' : [1 if aircraft_type == 'Type3' else 0 ]


    }

) 

if st.button('Predict'):
    Fuel_Consumption = model.predict(input_data)
    st.write(Fuel_Consumption)