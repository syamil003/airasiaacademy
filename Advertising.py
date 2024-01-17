import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.svr import SVR

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

data = sns.load_dataset('Advertising')
X = data.drop(['Sales'],axis=1)
Y = data.species.copy()

modelSvr = SVR()
modelSvr.fit(X, Y)

prediction = modelSvr.predict(df)
prediction_proba = modelSvr.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
