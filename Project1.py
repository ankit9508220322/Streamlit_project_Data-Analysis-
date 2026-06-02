import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

st.set_page_config(
    page_title="Startup Analysis",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
df=pd.read_csv('Startup_data1.csv')
df1 = pd.read_csv("simple1.csv", encoding='latin1')
# st.dataframe(df)
# st.sidebar.title("statup")

# month by year graph
def mom_graph():

    st.header('MoM graph')

    selected_option = st.selectbox('Select Type',['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()

    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = (temp_df['month'].astype(str)+ '-'+ temp_df['year'].astype(str))

    fig3, ax3 = plt.subplots(figsize=(15,5))

    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    plt.xticks(rotation='vertical')

    plt.tight_layout()
    st.pyplot(fig3)

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

def Startup_data(startp):
    st.header(startp)
    # Selected startup ka data filter karo
    temp_df = df[df['startup'] == startp][['city', 'startup', 'investors', 'amount']].sort_values(by=['city', 'amount', 'startup', 'investors'],
    ascending=[True, True, True, True]
)
    # Startup details
    st.subheader(temp_df)
    st.dataframe(temp_df)
    # two data freame

    yeara = df[df['startup'] == startp][['year','month','day','date']].reset_index(drop=True)
    st.dataframe(yeara)
    st.title("Top 10 Startup ")
    topdata=df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
    st.dataframe(topdata)
    # Total funding
    st.subheader("amount analysis")
    total = temp_df['amount'].sum()
    avg_funding = temp_df['amount'].mean()

    col1, col2 = st.columns(2)

    with col1:
       st.metric("Total Funding", f"{total:,.0f}")

    with col2:
      st.metric("Average Funding", f"{avg_funding:,.0f}")
    

    topdata = df.groupby('startup')['amount'].sum() .sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(topdata.index, topdata.values)

    ax.set_title("Top 10 Funded Startups")
    ax.set_xlabel("Startup")
    ax.set_ylabel("Funding Amount")
    plt.xticks(rotation=45)
    st.pyplot(fig)


st.title("startup name and investor")

def All_year(years):
     st.title("year Analysis")
     Year = df[df['year'] == years][['date', 'city', 'startup', 'amount']].drop_duplicates(subset=['startup','date','city','amount'])
     st.dataframe(Year)
    #  //////////////////////////
     st.title("Top 10 Name 4 Column ")
     Year2 = df[['startup',"investors",'amount','month']].drop_duplicates(subset=['startup','investors','amount','month']).head(10)
     st.dataframe(Year2)

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

option=st.sidebar.selectbox('Startus_Funding',["select option",'Overall Analysis','Startup','investor',"find_By_year"])

if option == 'Overall Analysis':
    btn0 = st.sidebar.button("Show OverAll Analysis")
    if btn0:
         overAllAnalysis()
        #  month year call function
    if btn0:
         mom_graph()


elif option == 'Startup':
    startup = st.sidebar.selectbox('Select Startup',sorted(df['startup'].drop_duplicates().unique()))
    st.title("Startup Analysis")
    btn1 = st.sidebar.button("Find Startup")

    if btn1:
        Startup_data(startup)
        mom_graph()


elif option == "investor":
      select_investor= st.sidebar.selectbox('Select investor',sorted(set(df['investors'].str.split(',').sum())))
    
      btn2=st.sidebar.button("find invester")
      if btn2:
         load_investor(select_investor)
         st.title("Investor Analysis")
      if btn2:
           mom_graph()
      
else:
     select_year = st.sidebar.selectbox('slect_year',sorted(df['year'].drop_duplicates()))
     btny = st.sidebar.button("Click Me")
     if btny:
          All_year(select_year)
          mom_graph()
          

# # cricket information
df2 = pd.read_csv("ipl20081.csv")
df2.drop_duplicates(subset=[
     "match_id",
     "season_id",
     "balls_per_over",
     "city",
     "match_date",
     "gender",
     "match_type"
     ])


# def iplinformation():
#      pass
#     # st.title("IPL OLD Data")
#     # df2
# iplinformation()

df2 = pd.read_csv("ipl20081.csv")
# delivery ipl data sheet
data=pd.read_csv('deliveries.csv')

# olt data this
data2=pd.read_csv('ipl-matches_data.csv') 
def All_teame_name(teame_info):
        st.title(teame_info)
        last5data=data2[(data2['Season'] == teame_info) &(data2['WinningTeam'].notnull()) &(data2['City'].notnull())][['City','Season','Date','TossWinner','WinningTeam']]
        
        # last5data = data[data['batsman'] == teame_info].drop(columns=['match_id','dismissal_kind','player_dismissed','penalty_runs','bye_runs']).set_index('batsman')
        st.subheader('All information this Activity')
        st.dataframe(last5data)
        st.title("second information ")
        most=data2[["Team1","Team2","Venue",'WinningTeam']].drop_duplicates(subset=['Team1','Team2','Venue']).head()
        st.dataframe(most)

       
# st.title("IPL OLD Data")
options=st.sidebar.selectbox('Ipl Old Information Data',['Select options','All ipl data','Select_Year','Highest'])

if options == 'All ipl data':
    btn0 = st.sidebar.button("Click Me")
    if btn0:
         df2

elif options == 'Select_Year':
    names=st.sidebar.selectbox(
        'Find All Info',
        data2['Season'].drop_duplicates().sort_values(ascending=True)
    )
    btn1=st.sidebar.button("Click Hear")
    if btn1:
      All_teame_name(names)

else:
    playrs_Name= st.sidebar.selectbox(
        'Teame Name',
        data['batting_team'].drop_duplicates().tolist()
    )
    btn2=st.sidebar.button("playrs_Name")

    if btn2:
        All_teame_name(playrs_Name)
    # //////////////////////


# all ipl 2026 data function 
ipl26 = pd.read_csv("ipl_2026_deliveries.csv")

def All_2026_data(ipl_2026):

     st.title(f"one Cricketer information 2026 IPL - {ipl_2026}")

     Alldata2026 = (ipl26[ipl26['striker'] == ipl_2026].groupby(['striker','season','date','batting_team'],as_index=False)['runs_of_bat'].sum().sort_values(by='runs_of_bat', ascending=True))

    #  st.subheader("one teame information",st.title(ipl_2026))
     st.dataframe(Alldata2026)

# st.title("New_2026_ipl_data")

ipl_2026 = st.sidebar.selectbox('Ipl_2026_info',ipl26['striker'].drop_duplicates().tolist())

btni = st.sidebar.button("Click me",key="btni")
if btni:
     All_2026_data(ipl_2026)

# ////////////////////////////////// new 2022

movies = pd.read_csv("imdb-1000.csv")

# def movies_data():

#     movi_imdb = st.sidebar.selectbox('Movi Information',['Select options', 'Select_Year', 'Genrs_name'])
#     # Year Wise Data
#     if movi_imdb == 'Select_Year':

#         selected_year = st.sidebar.selectbox('Find All Info',sorted(movies['Released_Year'].dropna().unique(), reverse=True))
#         btn1 = st.sidebar.button("Click Here")

#         if btn1:
#             st.subheader(f"Movies Released in {selected_year}")

#             year_data = movies[movies['Released_Year'] == selected_year][['Series_Title', 'Genre', 'Director', 'Metascore']]
#             st.dataframe(year_data)

#     # Genre Wise Data
#     elif movi_imdb == 'Genrs_name':

#         selected_genre = st.sidebar.selectbox('Select Genre',sorted(movies['Genre'].dropna().unique()))

#         btn2 = st.sidebar.button("Show Genre Data")

#         if btn2:
#             st.subheader(f"Genre : {selected_genre}")

#             genre_data = movies[
#                 movies['Genre'] == selected_genre
#             ][['Series_Title', 'Released_Year', 'Director', 'Metascore']]

#             st.dataframe(genre_data)

# movies_data()
def Movi_information(choice):
    All_movi_data = movies[movies['Genre'] == choice][['Released_Year','Genre','Director']].drop_duplicates()
    st.subheader(choice)
    st.dataframe(All_movi_data)
    # //////////////// only two data
    st.title("second info")
    All_movi_data1 = movies[movies['Genre'] == choice][['Released_Year','Director','Gross']].drop_duplicates()
    st.dataframe(All_movi_data1)
    # ///////////  Third information
    st.title("top 5 genres by total earning")
    most_earn=movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(5).reset_index()
    st.dataframe(most_earn)
    # ////////////////////////////////////////////
    st.title("Jai bajrang bali")
    everyData=movies.groupby('Genre').agg({
    'Director': 'first',
    'Released_Year': 'first',
    'Gross': 'sum'
 }).sort_values('Gross', ascending=False)
    st.dataframe(everyData)
    #  four graph
    st.title("graph to do")
    fig, ax = plt.subplots(figsize=(8,4))

    movies.groupby('Genre')['Gross'] \
      .sum() \
      .sort_values(ascending=False) \
      .head(5) \
      .plot(kind='bar', ax=ax)
    
    ax.set_title('Top 5 Genres by Gross Collection')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Gross')
    st.pyplot(fig)

    st.title("highest rated movie of each genre")
# import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10,5))

    movies.groupby('Genre')['IMDB_Rating'] \
        .max() \
        .sort_values(ascending=False) \
        .head(10) \
        .plot(kind='barh', ax=ax)

    ax.set_title('Top Genres by Maximum IMDb Rating')
    ax.set_xlabel('IMDb Rating')
    ax.set_ylabel('Genre')

    st.pyplot(fig)
    # ////////////////////////////////////////////
    st.title("number of movies done by each actor")
    done_each=movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False).reset_index()
    st.dataframe(done_each)
    # ///////////////////////////////////
def Director_info(director):
    st.subheader(director)

    director_genrs = movies[movies['Director'] == director][
        ['Series_Title','Released_Year','Genre','Gross','IMDB_Rating']
    ].sort_values('Gross', ascending=False)

    st.dataframe(director_genrs)
    # //////////////////////////////////////////// new code
    st.title("Genre And Director With Released_Year And total Gross")
    all_director=movies.groupby('Genre').agg({
    'Director': 'first',
    'Gross': 'sum',
    'Released_Year': 'first'
    }).sort_values('Gross', ascending=False)
    st.dataframe(all_director)
    # //////////////////////////////new code
    st.title("Most Voted Movies Top 10")
    voats=movies.sort_values('No_of_Votes', ascending=False)[['Series_Title','No_of_Votes']].head(10)
    st.dataframe(voats)
    # //////////////////////////////new data code
    st.title("Director-wise Total Gross")
    data_earn=movies.groupby('Director')['Gross'].sum().sort_values(ascending=False)
    st.dataframe(data_earn)
movi_info = st.sidebar.selectbox('Movi information',["select Option","Genrs_name","Director_Name","Select_year"])

if movi_info == "Genrs_name":
    yearm = st.sidebar.selectbox("select One",sorted(movies['Genre'].dropna().unique()))
    btnm = st.sidebar.button("Click")

    if btnm:
        Movi_information(yearm)

elif movi_info == 'Director_Name':
    Director = st.sidebar.selectbox("Select One",sorted(movies['Director'].dropna().unique()))

    if st.sidebar.button("Click"):
        Director_info(Director)

