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


