import requests
import json
import streamlit as st

 
st.title('Movie Engine')
user = st.text_input('Movie Title')

url = f'http://www.omdbapi.com/?apikey=aad18307&t={user}'


r = requests.get(url)
json_data = r.json() # The Json Data


if user == '':
    st.write('')
else:
    st.write(json_data['Title'])
    poster_url = json_data['Poster']
    poster_content = requests.get(poster_url).content

    # The image file
    with open(f'{user} poster.jpg', mode='wb') as file:
        file.write(poster_content)

    st.image(f'{user} poster.jpg')
    
    st.write(json_data['Plot'])
    st.write('Genre : ' + json_data['Genre'])
    st.write('Language : ' + json_data['Language'])
    st.write('Released : ' + json_data['Released'])
    st.write('Runtime : ' + json_data['Runtime'])
    st.write('Director : ' + json_data['Director'])
    st.write('Writer : ' + json_data['Writer'])
    st.write('Actors : ' + json_data['Actors'])
    #for key, value in json_data.items():
        #st.write(key,' : ',value)
 



    



