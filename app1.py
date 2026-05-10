import streamlit as st
import pandas as pd
import time
em = 'ankit@1234.com'
pas = '1234'
email = st.sidebar.text_input("enter rmail ")
password = st.sidebar.text_input("enter password ")
gender=st.sidebar.selectbox('select gender:',['male','femail','other'])

btn= st.sidebar.button("login")
if btn:
    if email == em and password == pas:
        st.sidebar.success("login sucessfull: ")
        st.sidebar.write(gender)
    else:
        st.error("email not write: ")

# /////////// uplode any file 
# file = st.file_uploader('uplode csv file ')
# if file is not None:
#     df=pd.read_csv(file)
#     st.dataframe(df.describe())