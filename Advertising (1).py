import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

st.write("# Advertising Prediction App")
st.write("This app predicts the **TV, Radio and Newspaper** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('Sales', 0.70, 296.4, 80.3)
    Radio = st.sidebar.slider('Sales', 0.0, 49.6, 19.2)
    Newspaper = st.sidebar.slider('Sales', 0.3, 114.0, 77.6)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

modelSvr = pickle.load(open("Advertising.h5", "rb"))

prediction = loaded_model.predict(df)
st.subheader('Class labels and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)
