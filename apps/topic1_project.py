import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling as pp
# #get_ipython().run_line_magic('matplotlib', 'inline')
#
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.pipeline import Pipeline
#
#
# from sklearn.preprocessing import LabelEncoder
#
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# from xgboost import XGBRegressor
# from sklearn.metrics import r2_score
# from sklearn.metrics import mean_squared_error, mean_absolute_error
# from math import sqrt
#
# from statsmodels.tsa.seasonal import seasonal_decompose
# from pmdarima import auto_arima
#
# from fbprophet import Prophet
# from fbprophet.plot import add_changepoints_to_plot


def app():
    st.title('Topic 1')
    st.header("PHÂN TÍCH KẾT QUẢ DỰ BÁO")
    #data = pd.read_csv(r"D:\DAC\HAnh\demo1\avocado.csv")
    #print(data.head())
    #st.write(data.info())
    #data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    #df = data.copy(deep=True)
    #report = pp.ProfileReport(df)
    #show_displot(df)
    #show_imf_result()
    #show_ts_result()
    #demo_plot()
# In[2]:

# def show_displot(df):
#     fig = plt.figure(figsize=(10, 4))
#     sns.displot(df, x="AveragePrice", hue="type", stat="density")
#     st.pyplot(fig)
