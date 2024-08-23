import requests
import json

user = input('Kindly enter a the name of the movie: ').strip()

url = f'http://www.omdbapi.com/?apikey=aad18307&t={user}'

r = requests.get(url)
json_data = r.json() # The Json Data

for key, value in json_data.items():
    print(key, ':', value)
    

poster_url = json_data['Poster']
poster_content = requests.get(poster_url).content

# The image file
with open(f'{user} poster.jpg', mode='wb') as file:
    file.write(poster_content)

from PIL import Image
img = Image.open(f'{user} poster.jpg')
img.show()