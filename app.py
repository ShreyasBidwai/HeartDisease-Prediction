import streamlit as st
import pickle
import numpy as np
st.set_page_config(layout="wide")


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

features = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
            'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
            'diaBP', 'BMI', 'heartRate', 'glucose']

st.title("Chronic Heart Disease Predictor")

user_input = []

with st.form("Values Form", clear_on_submit=False):
    # 3 rows and 5 columns grid
    for row in range(3):
        cols = st.columns(5)
        for col in range(5):
            feature_index = row * 5 + col
            if feature_index < len(features):
                val = cols[col].number_input(f"{features[feature_index]}: ", value=0)
                user_input.append(val)

    submitted = st.form_submit_button("Submit",type="primary",)

if submitted:
    user_input = np.array(user_input).reshape(1, -1)
    output = model.predict(user_input)

    if output == 1:
        st.error("Chances of Chronic Heart Disease: Positive")
    elif output == 0:
        st.success("Chances of Chronic Heart Disease: Negative")
    else:
        st.warning("Chances of Chronic Heart Disease: Unknown")
    
