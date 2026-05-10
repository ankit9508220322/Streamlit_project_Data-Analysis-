import streamlit as st
import pandas as pd

option = st.sidebar.selectbox('Well Come',['all record','teame1','teame2'])
if option == 'all record':
    pass
elif option == 'teame1':
    st.sidebar('select name:')
    btn1=st.sidebar.button("click me")
    st.title("teame name record ")
else:
    st.sidebar.selectbox('select name')
    btn2=st.sidebar.button("find invester")
    
