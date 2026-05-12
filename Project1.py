import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title="startup")
# df = pd.read_csv("startup_cleen.csv")
df = pd.read_csv('clin_startup.csv')
df1 = pd.read_csv("simple1.csv", encoding='latin1')
# st.dataframe(df)
# st.sidebar.title("statup")

def load_investor(investor):
        st.title(investor)
        last5data=df[df['investors'].str.contains(investor, na=False)][['date','city','startup','amount','round']]
        st.subheader('most resent  investor ')
        st.dataframe(last5data)
        # some print data
# all data in biggest investament
        bid_data=df[df['investors'].str.contains(investor)].groupby('startup')['city'].sum().sort_values(ascending=False)
        st.markdown(
        "<h1 style='color:Purple;'>Most Top 5 City Name And Statup: </h1>",
             unsafe_allow_html=True
        )
        st.dataframe(bid_data)
        # graph plio in chart
        st.markdown(
            "<h1 style='color:red;'>This is my project All investor Information include: </h1>",
              unsafe_allow_html=True
        )

        # col1,col2,col3 = st.columns(3)
        # with col1:
        bid_serise=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader('most biggest investment Graph')
        fig,ax = plt.subplots()
        ax.bar(bid_serise.values, bid_serise.index)
        st.pyplot(fig)
        
        # with col2:
        vertical = df[df['investors'].str.contains(investor,na=False)]['city'].value_counts()
        st.subheader("city name")
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct='%0.1f%%')
        st.pyplot(fig1)
        
# /////////////////////////
# df[df['investors'].str.contains('IDG Ventures',na=False)]['date'].head(22).value_counts().plot(kind='pie',autopct='%0.1f%%')
        # with col3:
        big_year = df[df['investors'].str.contains(investor, na=False)]['date'].head(22).value_counts()
        #  st.subheader('Most biggest Date ')
        #  
        st.markdown(
        "<h1 style='color:red;'>Most all investment Date: </h1>",
             unsafe_allow_html=True
        )
            # 
        fig3, ax3 = plt.subplots()
        ax3.pie(big_year.values, labels=big_year.index.astype(str), autopct='%0.1f%%')
             
        st.pyplot(fig3)
        # top 1 date 
        st.title("1 Big Data")
        big_year1 = df[df['investors'].str.contains(investor, na=False)]['date'].head(5).value_counts()
        st.write(big_year1)
             
def overAllAnalysis():
    st.title('overall analysis')
    #  total ammount
    
    total = round(pd.to_numeric(df['amount'], errors='coerce').sum())
    st.metric('total',str(total) + 'cr')
    # /////////////
    st.title('overall max')
    total1 = round(pd.to_numeric(df['amount'], errors='coerce').mean())
    st.metric('total',str(total1) + 'cr')


option=st.sidebar.selectbox('select one',['overall analysis','startup','investor'])
if option == 'overall analysis':
    btn0 = st.sidebar.button("Show OverAll Analysis")
    if btn0:
         overAllAnalysis()



elif option == 'startup':
    st.sidebar.selectbox('select startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button("find startup")
    st.title("startup nalysis")
    
else:
    select_investor= st.sidebar.selectbox('select startup',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button("find invester")
    if btn2:
        load_investor(select_investor)


# # cricket information
# df2 = pd.read_csv("ipl20081.csv").head(3)
# def iplinformation():
#     st.title("all ipl information: ")
#     df2
# iplinformation()
# df2 = pd.read_csv("ipl20081.csv")
# # st.title("Ipl information ")
# option1=st.sidebar.selectbox('Ipl Information',['All ipl data','city','playrs_Name'])
# if option1 == 'All ipl data':
    
#     btn0 = st.sidebar.button("cate information")
#     if btn0:
#          iplinformation()



# elif option1 == 'city':
#     st.sidebar.selectbox('select startup',df2['city'].drop_duplicates(inplace=False).tolist())
#     btn1=st.sidebar.button("find scity")
#     st.title("city name")
    
# else:
#     playrs_Name= st.sidebar.selectbox('Teame Name',df2['venue'].str.split(',').str[0].drop_duplicates().tolist())
#     btn2=st.sidebar.button("playrs_Name")
#     if btn2:
#         load_investor(playrs_Name)

    