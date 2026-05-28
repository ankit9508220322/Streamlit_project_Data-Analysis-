import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title="startup")
# df = pd.read_csv("startup_cleen.csv")
# df = pd.read_csv('clin_startup.csv')
# df= pd.read_csv('ClineStatup_Data.csv')
df=pd.read_csv('Startup_data1.csv')
df1 = pd.read_csv("simple1.csv", encoding='latin1')
# st.dataframe(df)
# st.sidebar.title("statup")

# first function investor
def load_investor(investor):
        st.title(investor)
        last5data=df[df['investors'].str.contains(investor, na=False)].head(10)[['date','startup','city','round','amount']]
        st.subheader('Most Resent  investor ')
        st.dataframe(last5data)
        # some print data

# all data in biggest investament
        bid_data=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
        st.markdown(
        "<h1 style='color:Purple;'>Most Top 5 biggest investor Name And Statup: </h1>",
             unsafe_allow_html=True
        )
        st.dataframe(bid_data)
        # graph plio in chart
        st.markdown(
            "<h1 style='color:red;'>This is my project All investor Information include: </h1>",
              unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            # biggest investments
            big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
            st.subheader('Biggest Investments')
            fig, ax = plt.subplots()
            ax.bar(big_series.index,big_series.values)
            st.pyplot(fig)

# git graph
        with col2:
            vertical = df[df['investors'].str.contains(investor, na=False)]['city'].dropna().value_counts()
            st.subheader("City name")
            fig1,ax1 = plt.subplots()
            ax1.pie(vertical,labels=vertical.index,autopct='%0.1f%%')
            st.pyplot(fig1)
        
# /////////////////////////
     #    gg=df[df['investors'].str.contains('IDG Ventures',na=False)]['date'].head(22).value_counts().plot(kind='pie',autopct='%0.1f%%')
        # # top 1 date 
        st.title("1 Big Data")
     #    st.title("jai ram ji ki jai")
        big_year1 = df[df['investors'].str.contains(investor, na=False)][['city','date']].head(5)
        st.dataframe(big_year1)
            #  //////////////////////////////
# only amount data in file
# amount =pd.read_csv("statup_amount.csv")
def All_year(years):
     st.title("year Analysis")
     Year = df[df['year'] == years][['date', 'city', 'startup', 'amount']].drop_duplicates(subset=['startup','date','city','amount'])
     st.dataframe(Year)


def overAllAnalysis():
    st.title('Overall Analysis')
    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups',num_startups)

# //////////////////////////////////////////////////////
# main code and main page start 

option=st.sidebar.selectbox('Select One Options',['Overall Analysis','Startup','investor',"find_By_year"])

if option == 'Overall Analysis':
    btn0 = st.sidebar.button("Show OverAll Analysis")
    if btn0:
         overAllAnalysis()


elif option == 'Startup':
    # st.sidebar.selectbox('Select Startup',sorted(tuple(list(df.unique()))))
    st.sidebar.selectbox('Select Startup',sorted(tuple(list(df['startup'].drop_duplicates().unique()))))
    
    btn1=st.sidebar.button("Find Startup")
    # st.title("Dont add data please nest time try ")
    st.title("Startup Analysis")
    

elif option == "investor":
      select_investor= st.sidebar.selectbox('Select investor',sorted(set(df['investors'].str.split(',').sum())))
    
      btn2=st.sidebar.button("find invester")
      if btn2:
         load_investor(select_investor)
         st.title("Investor Analysis")

else:
     select_year = st.sidebar.selectbox('slect_year',sorted(df['year'].drop_duplicates()))
     btny = st.sidebar.button("Click Me")

     if btny:
          All_year(select_year)

          st.header('MoM graph')

          selected_option = st.selectbox('Select Type',['Total','Count'])

          if selected_option == 'Total':
               temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()

          else:
               temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

          temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

          fig3, ax3 = plt.subplots(figsize=(15,5))

          ax3.plot(temp_df['x_axis'], temp_df['amount'])

          plt.xticks(rotation='vertical')

          plt.tight_layout()
          st.pyplot(fig3)
    #  st.title("emazing now")
# 
# st.header('MoM graph')
     
     


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




