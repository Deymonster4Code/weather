import requests

url_template = 'https://wttr.in/{}'

# Прогноз для Лондона
id1 = 'London'
# Прогноз для аэропорта Шереметьево
id2 = 'svo'
# Прогноз для Череповца
id3 = 'Череповец'
places = [id1, id2, id3]
payload = {'MnqmT':'', 'lang': 'ru'}

for place in places:
    url = url_template.format(place)
    resp = requests.get(url, params=payload)
    resp.raise_for_status()
    print(resp.text)


