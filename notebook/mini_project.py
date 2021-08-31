#
# Streamlit의 Iris Flower 예측 APP.
#

import pandas as pd
import numpy as np
import pickle
from seaborn import load_dataset
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import streamlit as st

st.title("MPG 연비 예측 APP")


# MPG data load
data = load_dataset("mpg")

st.sidebar.header("차량의 SPEC을 입력해주세요")
my_cylinders = st.sidebar.slider("cylinders", 3,5,8)
my_displacement = st.sidebar.slider("displacement", 68.00, 455.00)
my_horsepower = st.sidebar.slider("horsepower", 46.00, 230.00)
my_weight = st.sidebar.slider("weight", 1613.00, 5140.00)
my_acceleration = st.sidebar.slider("acceleration", 8.00, 24.80)
my_model_year = st.sidebar.slider("model_year", 70, 82)

my_origin = st.sidebar.selectbox("origin", 
                data["origin"].unique())


# 입력된 X 데이터.
st.header("입력된 X 데이터:")
my_X_raw = np.array([[my_cylinders,my_displacement,my_horsepower,my_weight, my_acceleration, my_model_year]])
my_df_X_raw = pd.DataFrame(data=my_X_raw)
st.write(my_df_X_raw)


# 전처리된 X 데이터.
with open("../data/my_scaler.pkl","rb") as f:
    my_scaler = pickle.load(f)
my_X_scaled = my_scaler.transform(my_X_raw)     # fit_transform이 아닌 transform!!

st.header("전처리된 X 데이터:")
my_df_X_scaled = pd.DataFrame(data=my_X_scaled)
st.write(my_df_X_scaled)

# 예측.
with open("../data/my_regressor.pkl","rb") as f:
    my_classifier = pickle.load(f)

my_proba = my_classifier.predict_proba(my_X_scaled)
my_Y_pred = y_labels[my_classifier.predict(my_X_scaled)[0]]

st.header("예측 결과:")
my_proba_df = pd.DataFrame(data=my_proba)
st.write("유형별 예측 확률:  ", my_proba_df)
st.write("가장 유력한 유형:  ", my_Y_pred)