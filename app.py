import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df_process = preprocessor.preprocess(df,region_df)

st.sidebar.title('Olympics Analysis')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Telly','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

# year = st.sidebar(
#     'Select Year',
#     ('1032','1023','1223')
# )

# st.dataframe(df)

if user_menu == 'Medal Telly':
    st.sidebar.header("Medal Tally")
    year , country = helper.country_year_list(df_process)
    selected_year = st.sidebar.selectbox("Select year",year)
    selected_country = st.sidebar.selectbox("Select Country",country)

    medal_tally = helper.fetched_medal_telly(df_process,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Telly")

    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Telly in " + str(selected_year))

    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + "  Overall Performance")

    if selected_country != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Performance in "+ str(selected_year) +" Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df_process['Year'].unique().shape[0] - 1
    cities = df_process['City'].unique().shape[0]
    sports = df_process['Sport'].unique().shape[0]
    events = df_process['Event'].unique().shape[0]
    athletes = df_process['Name'].unique().shape[0]
    nations = df_process['region'].unique().shape[0]

    st.title("Top Statastics")


    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nation_overtime = helper.data_overtime(df_process,'region')
    fig = px.line(nation_overtime,x='Year',y='count')
    st.title("Participating Nations Over the Years")
    st.plotly_chart(fig)

    event_overtime = helper.data_overtime(df_process,'Event')
    fig = px.line(event_overtime,x='Year',y='count')
    st.title("Events Over the Years")
    st.plotly_chart(fig)

    athletes_overtime = helper.data_overtime(df_process,'Name')
    fig = px.line(athletes_overtime,x='Year',y='count')
    st.title("Athles Over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events OverTime(Every Sport)")
    fig,ax = plt.subplots(figsize=(10,10))

    x = df_process.drop_duplicates(['Year','Sport','Event'])

    ax = sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)

    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df_process['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Selecet Sport',sport_list)
    x = helper.most_successful_athletes(df_process,selected_sport)
    st.table(x)


if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country Wise Analysis')

    country_list = df_process['region'].dropna().unique().tolist()
    country_list.sort()

    select_country = st.sidebar.selectbox('Select Country',country_list)

    country_df = helper.yearwise_medal(df_process,select_country)

    fig = px.line(country_df,x='Year',y='Medal')
    st.title(select_country + 'Medal Telly Over the Year')
    st.plotly_chart(fig)


    st.title(select_country + " Excels in the following sports")
    pt = helper.country_event_heatmap(df_process,select_country)
    fig,ax = plt.subplots(figsize=(10,10))
    #x = df_process.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)


    st.title("Top 15 Athletes of " + select_country)
    top15_df = helper.most_successful_athletes_countrywise(df_process,select_country)
    st.table(top15_df)


if user_menu == 'Athlete wise Analysis':
    athlte_df = df_process.drop_duplicates(subset=['Name','region'])

    x1 = athlte_df['Age'].dropna()
    x2 = athlte_df[athlte_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlte_df[athlte_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlte_df[athlte_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalist','Silver Medalist','Bronze Medalist'],show_hist=False,show_rug=False)
    fig.update_layout(autosize = False,width =1000,height= 600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)


    famous_sport = ['Basketball',
                    'Judo',
                    'Football',
                    'Tug-Of-War',
                    'Athletics',
                    'Swimming',
                    'Badminton',
                    'Sailing',
                    'Gymnastics',
                    'Art Competitions',
                    'Handball',
                    'Weightlifting',
                    'Wrestling',
                    'Water Polo',
                    'Hockey',
                    'Rowing',
                    'Fencing',
                    'Equestrianism',
                    'Shooting',
                    'Boxing',
                    'Taekwondo',
                    'Cycling',
                    'Diving',
                    'Canoeing',
                    'Tennis']

    x = []
    name = []
    for sport in famous_sport:
        temp_df = athlte_df[athlte_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    
    fig = ff.create_distplot(x,name,show_hist=False,show_rug=False)
    fig.update_layout(autosize = False,width =1000,height= 600)
    st.title('Distribution of Age with Respect to Sports(Gold Medal)')
    st.plotly_chart(fig)