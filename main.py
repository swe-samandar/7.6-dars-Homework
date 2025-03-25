import requests

url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'

response = requests.get(url)
data = response.json()

for dict in data:
    print(dict['Rate'])
