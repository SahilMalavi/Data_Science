import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_p(m_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7c1b29091b8ce2b0516521ab48c89744&language=en-USb48c89744/285".format(m_id)
    data = requests.get(url)
    data=data.json()
    p_path=data['poster_path']
    p_path="http://image.tmdb.org/t/p/w500"+p_path
    return p_path

similarity=pickle.load(open("similarity.pkl",'rb'))
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    return distances


st.title("Movie Recommendation System")

movie_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movie_dict)

option = st.selectbox(
    'Movies',
    (movies['title'].values))

movie_rec=[]
if st.button('Recommend'):
    # recommend() function return list of distance between each movie
    movie_rec=recommend(option)
    st.header("\nYou may like this")
    st.write("Top 5 movies are:\n\n")
    
col = st.columns(5)

k=0;
for i in movie_rec[:5]:

    with col[k]:
         j=k+1
         st.text(j,":",movies.iloc[i[0]].title)
         img_path=fetch_p(movies.iloc[i[0]].movie_id)
         st.write("\n")
         st.image(img_path)
         k+=1

