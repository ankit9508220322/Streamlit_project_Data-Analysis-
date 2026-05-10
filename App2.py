import streamlit as st
import pandas as pd
import time
st.title('jai ram ji ki')
st.header("i am learn neu part")
st.subheader("chaubey jii")
st.write('write name')
st.markdown("""
### man point
            ankit
            vikash
            mohit
            muna
            manoj
            ajit

""")
# you can show the your display code
st.code("""
def add(a + b)
        return a + b
obb = add(3,4)
""")
# laTex
st.latex('x + y = 44')
# ///////////////////////////////////
# display dataframe
st.title("all data ")
df = pd.DataFrame(
    {
        'name':['ankit','ajit','bikash','mohit'],
        'marks':[30,40,50,60],
        'package':[10,30,11,12]
    }
)
st.dataframe(df)
# metrises
st.metric('response','Rs 3L','+33%')
# jshon
st.json(
    {
        'name':['ankit','ajit','bikash','mohit'],
        'marks':[30,40,50,60],
        'package':[10,30,11,12]
    }

)
# how too display media
st.image('ankit pick.png')
st.video('v1.mp4')
st.audio('audio file name ')
# side by side images
col1,col2 = st.columns(2)
with col1:
    st.image('ankit pick.png')
with col2:
    st.image('ankit pick.png')
# ////////////////////////////
# how to create layout
st.sidebar.title("side bar")
# sowing status
st.error("faild")
st.success("congrate")
st.info("information ")
# bar = st.progress(0)
# for i in range(1,55):
#     time.sleep(0.1)
#     bar.progress(i)
# ///////////////////////////////
# user input text
st.text_input("enter name ")
st.number_input("number ")
st.date_input("registation date ")
st.time_input("time enter ")
# //////////////////////////////
# button  input
