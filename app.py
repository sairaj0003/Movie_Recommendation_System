import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    # url = "https://api.themoviedb.org/3/movie/{}?api_key=1fe8664004a575418f10ed18df69cf4f&language=en-US".format(movie_id)
    # data = requests.get(url)

    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZmU4NjY0MDA0YTU3NTQxOGYxMGVkMThkZjY5Y2Y0ZiIsInN1YiI6IjY1YTU2MzIzMThiNzUxMDEyMjk2Mjk0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hGiCVAAxKntEVbNaI9fesvzijlGfBXiuVSLzTOP2jTw"
    }

    data = requests.get(url, headers=headers)

    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommendation')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.header(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.header(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.header(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.header(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.header(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

    with col7:
        st.header(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

    with col8:
        st.header(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])

    with col9:
        st.header(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])

    with col10:
        st.header(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
else:
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)

    movie_id = movies['movie_id'].values
    movie_names = []
    movie_posters = []

    for i in range(10):
        movie_names.append(movie_list[i])
        movie_posters.append(fetch_poster(movie_id[i]))

    with col1:
        st.header(movie_names[0])
        st.image(movie_posters[0])

    with col2:
        st.header(movie_names[1])
        st.image(movie_posters[1])

    with col3:
        st.header(movie_names[2])
        st.image(movie_posters[2])

    with col4:
        st.header(movie_names[3])
        st.image(movie_posters[3])

    with col5:
        st.header(movie_names[4])
        st.image(movie_posters[4])

    with col6:
        st.header(movie_names[5])
        st.image(movie_posters[5])

    with col7:
        st.header(movie_names[6])
        st.image(movie_posters[6])

    with col8:
        st.header(movie_names[7])
        st.image(movie_posters[7])

    with col9:
        st.header(movie_names[8])
        st.image(movie_posters[8])

    with col10:
        st.header(movie_names[9])
        st.image(movie_posters[9])
