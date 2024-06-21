import pickle
import streamlit as st
from streamlit_lottie import st_lottie
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import requests
import base64

CLIENT_ID = "e508f11c800b4fd38ddd1c91eb468f53"
CLIENT_SECRET = "05e52bc895ae4086b70427a7cf4dc0a9"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    idx = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names,recommended_music_posters

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Encode the image to base64
encoded_image =  base64.b64encode(open("Git.png", "rb").read()).decode()

# HTML and CSS to place the image in the topmost corner
st.markdown(
    f"""
    <style>
    .top-left-corner {{
        position: absolute;
        top: 10px;
        left: 10px;
    }}
    </style>
    <div class="top-left-corner">
        <a href="https://github.com/TanmoyGuria/">
            <img src="data:image/png;base64,{encoded_image}" width="25">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


lottie_hello = load_lottieurl("https://lottie.host/4dba83fa-694e-4cf9-8729-aaf79aa02662/sl737MkvHj.json")
title='Music Recommender System'

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(f"""
        <style>
        .custom-title {{
            font-family: 'Verdana', sans-serif;
            font-size: 42px;
            color: #FF00FF;
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;
        }}
        </style>
        <div class="center">
            <h1 class="custom-title">{title}</h1>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high # canvas
        height=300,
        width=300,
        key=None,
    )
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names,recommended_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(recommended_music_names[5])
        st.image(recommended_music_posters[5])
    with col7:
        st.text(recommended_music_names[6])
        st.image(recommended_music_posters[6])
    with col8:
        st.text(recommended_music_names[7])
        st.image(recommended_music_posters[7])
    with col9:
        st.text(recommended_music_names[8])
        st.image(recommended_music_posters[8])
    with col10:
        st.text(recommended_music_names[9])
        st.image(recommended_music_posters[9])
