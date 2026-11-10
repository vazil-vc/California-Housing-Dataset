import streamlit as st
import pandas as pd
import joblib

model = joblib.load('house_price_model.pkl')
scaler = joblib.load('house_price_scaler.pkl')

st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

st.title("House Price Prediction App")

st.write("enter the details of the house to predict its price.")

MedInc = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.5
)

HouseAge = st.number_input(
    "House Age",
    min_value=1.0,
    value=25.0
)

AveRooms = st.number_input(
    "Average Rooms",
    min_value=1.0,
    value=5.0
)

AveBedrms = st.number_input(
    "Average Bedrooms",
    min_value=1.0,
    value=1.0
)

Population = st.number_input(
    "Population",
    min_value=1.0,
    value=1000.0
)

AveOccup = st.number_input(
    "Average Occupancy",
    min_value=1.0,
    value=3.0
)

Latitude = st.number_input(
    "Latitude",
    value=34.0
)

Longitude = st.number_input(
    "Longitude",
    value=-118.0
)

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "MedInc":[MedInc],
        "HouseAge":[HouseAge],
        "AveRooms":[AveRooms],
        "AveBedrms":[AveBedrms],
        "Population":[Population],
        "AveOccup":[AveOccup],
        "Latitude":[Latitude],
        "Longitude":[Longitude]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.success(
        f"Predicted Median House Value : ${prediction[0]*100000:,.2f}"
    )