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
        st.subheader('Most Resent  investor ')
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
        st.subheader('Most biggest investment Graph')
        fig,ax = plt.subplots()
        ax.bar(bid_serise.values, bid_serise.index)
        st.pyplot(fig)
        
        # with col2:
        vertical = df[df['investors'].str.contains(investor,na=False)]['city'].value_counts()
        st.subheader("City name")
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


# main code and main page start 
option=st.sidebar.selectbox('Select One Options',['Overall Analysis','Startup','investor'])
if option == 'overall analysis':
    st.title("OverAll Analysis")
    btn0 = st.sidebar.button("Show OverAll Analysis")
    if btn0:
         overAllAnalysis()



elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button("Find Startup")
    st.title("Dont add data please nest time try ")
    # st.title("Startup Analysis")
    
else:
    select_investor= st.sidebar.selectbox('Select investor',sorted(set(df['investors'].str.split(',').sum())))
    
    btn2=st.sidebar.button("find invester")
    if btn2:
        load_investor(select_investor)
        st.title("Investor Analysis")
# /////////////////////////////////////////////


# # cricket information
# df2 = pd.read_csv("ipl20081.csv")
# df2.drop_duplicates(subset=[
#      "match_id",
#      "season_id",
#      "balls_per_over",
#      "city",
#      "match_date",
#      "gender",
#      "match_type"
#      ])


# # def iplinformation():
# #      pass
# #     # st.title("IPL OLD Data")
# #     # df2
# # iplinformation()

# df2 = pd.read_csv("ipl20081.csv")
# # delivery ipl data sheet
# data=pd.read_csv('deliveries.csv')

# # olt data this
# data2=pd.read_csv('ipl-matches_data.csv') 
# def All_teame_name(teame_info):
#         st.title(teame_info)
#         last5data=data2[(data2['Season'] == teame_info) &(data2['WinningTeam'].notnull()) &(data2['City'].notnull())][['City','Season','Date','TossWinner','WinningTeam']]
        
#         # last5data = data[data['batsman'] == teame_info].drop(columns=['match_id','dismissal_kind','player_dismissed','penalty_runs','bye_runs']).set_index('batsman')
#         st.subheader('All information this Activity')
#         st.dataframe(last5data)
#         st.title("second information ")
#         most=data2[["Team1","Team2","Venue",'WinningTeam']].drop_duplicates(subset=['Team1','Team2','Venue']).head()
#         st.dataframe(most)

       
# st.title("IPL OLD Data")
# options=st.sidebar.selectbox('Ipl Old Information Data',['Select options','All ipl data','Select_Year','Highest'])

# if options == 'All ipl data':
#     btn0 = st.sidebar.button("Click Me")
#     if btn0:
#          df2

# elif options == 'Select_Year':
#     names=st.sidebar.selectbox(
#         'Find All Info',
#         data2['Season'].drop_duplicates().sort_values(ascending=True)
#     )
#     btn1=st.sidebar.button("Click Hear")
#     if btn1:
#       All_teame_name(names)

# else:
#     playrs_Name= st.sidebar.selectbox(
#         'Teame Name',
#         data['batting_team'].drop_duplicates().tolist()
#     )
#     btn2=st.sidebar.button("playrs_Name")

#     if btn2:
#         All_teame_name(playrs_Name)
#     # //////////////////////


# # all ipl 2026 data function 
# ipl26 = pd.read_csv("ipl_2026_deliveries.csv")

# def All_2026_data(ipl_2026):

#      st.title(f"one Cricketer information 2026 IPL - {ipl_2026}")

#      Alldata2026 = (ipl26[ipl26['striker'] == ipl_2026].groupby(['striker','season','date','batting_team'],as_index=False)['runs_of_bat'].sum().sort_values(by='runs_of_bat', ascending=True))

#     #  st.subheader("one teame information",st.title(ipl_2026))
#      st.dataframe(Alldata2026)

# st.title("New_2026_ipl_data")

# ipl_2026 = st.sidebar.selectbox('Ipl_2026_info',ipl26['striker'].drop_duplicates().tolist())

# btni = st.sidebar.button("Click me",key="btni")
# if btni:
#      All_2026_data(ipl_2026)

# # ////////////////////////////////// new 2022




