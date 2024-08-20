import requests

user = input('Kindly enter a the name of the movie: ')

url = f'http://www.omdbapi.com/?apikey=aad18307&t={user}'

r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key, ':', value)