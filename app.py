import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import datetime as dt

st.title('Sentiment Analysis of Tweets about US Airlines')
st.sidebar.title('Sentiment Analysis of Tweets about US Airlines')

st.markdown(' This web app is a streamlit dashboard used to analyze sentiment of Tweets 🐦')
st.sidebar.markdown(' This web app is a streamlit dashboard used to analyze sentiment of Tweets 🐦')

DATA_URL = ('./data/Tweets.csv')

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()

# Random Tweet
st.sidebar.subheader('Show Random Tweet:')
random_tweet = st.sidebar.radio('Sentiment'
                                , ('positive', 'neutral', 'negative'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0,0])

# Plot of Sentiment
st.sidebar.markdown('### Number of Tweets by Sentiment')
select = st.sidebar.selectbox('Visualization Type'
                              , ['Bar Plot', 'Pie Chart']
                              , key = '1' # reference for streamlit
                             )
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index
                                , 'Tweets': sentiment_count.values
                               }
                              )
if not st.sidebar.checkbox('Hide', True):
    st.markdown('### Number of Tweets by Sentiment')
    if select == 'Bar Plot':
        fig = px.bar(sentiment_count
                     , x = 'Sentiment'
                     , y = 'Tweets'
                     , color = 'Tweets'
                     , height = 500
                    )
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count
                     , values = 'Tweets'
                     , names = 'Sentiment'
                     , color = 'Tweets'
                     , height = 500
                    )
        st.plotly_chart(fig)
    

# Plot map
COORDS_URL = ('./data/coords.csv')
@st.cache(persist=True)
def load_coords():
    data_coords = pd.read_csv(COORDS_URL)
    return data_coords

data_coords = load_coords()
st.map(data_coords)

st.sidebar.subheader('When and where are users tweeting from?')
hour = st.sidebar.slider("Hour of day"
                         , min_value = 0
                         , max_value =23
                        )
modified_data = data[data['tweet_created'].dt.hour == hour]
if not st.sidebar.checkbox("Close", True, key = '1'):
    st.markdown('### Tweet locations based on the time of day')







































        