import requests
import json
import streamlit as st
import pandas as pd
 
st.title('Movie Engine🎬')
user = st.text_input('Movie Title')


 
url = f'http://www.omdbapi.com/?apikey=aad18307&t={user}'


r = requests.get(url)
json_data = r.json() # The Json Data

movie = pd.read_csv('movie_dataset.csv')



if user == '':
    st.write('')
else:
    title = json_data['Title']
    st.write(f"""
    <p style="font-family:Lucida Console, Courier New, monospace; color:black; font-size: 35px;">{title}
    </p>
    """, unsafe_allow_html=True)
    poster_url = json_data['Poster']
    poster_content = requests.get(poster_url).content
    
    with open(f'{user} poster.jpg', mode='wb') as file:
        file.write(poster_content)
    col1, col2 = st.columns([50, 40])
    with col1:
        # The image file
        st.image(f'{user} poster.jpg', width = 370)
    with col2:
        st.write(json_data['Plot'])
        plot = json_data['Genre']
        st.write(f"""
        **Genre**
        <br>
        {plot}
        """,  unsafe_allow_html=True)
        lan = json_data['Language']
        st.write(f"""
        **Language**
        <br>
        {lan}
        """,  unsafe_allow_html=True)
        rel = json_data['Released']
        st.write(f"""
        **Released**
        <br>
        {rel}
        """,  unsafe_allow_html=True)
        run = json_data['Runtime']
        st.write(f"""
        **Runtime**
        <br>
        {run}
        """,  unsafe_allow_html=True)
        dir = json_data['Director']
        st.write(f"""
        **Director**
        <br>
        {dir}
        """,  unsafe_allow_html=True)
        write = json_data['Writer']
        st.write(f"""
        **Writer**
        <br>
        {write}
        """,  unsafe_allow_html=True)
        act = json_data['Actors']
        st.write(f"""
        **Actors**
        <br>
        {act}
        """,  unsafe_allow_html=True)
    #for key, value in json_data.items():
        #st.write(key,' : ',value)

genre = st.text_input('Genre')
st.caption('Kindly enter your desired genre to recommend movies')

if genre == '':
    st.write('')
else:
    genre =genre[0].upper()+genre[1:]
    gen = movie[movie['genres'] == genre]
    gen = gen[['title']]
    st.write(gen.head(10))



    



