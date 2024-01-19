import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f369ec1d52572f881aa2ebf0388cd6dd".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path


def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse =True ,key = lambda x : x[1])[1:6]
     
    recommended_movies_names = []                   
    recommended_movies_posters = []
    
    for i in movie_list:
            
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies_names.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies_names,recommended_movies_posters
    
    
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values)

if st.button('Recommend'):
    
    names,posters=recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])


    with col3:
        st.text(names[2])
        st.image(posters[2])

        
    with col4:
        st.text(names[3])
        st.image(posters[3])

        
    with col5:
        st.text(names[4])
        st.image(posters[4])

