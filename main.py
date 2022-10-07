import requests

url_template = 'https://wttr.in/{}'

# Прогноз для Лондона
place1 = 'London'
# Прогноз для аэропорта Шереметьево
place2 = 'svo'
# Прогноз для Череповца
place3 = 'Череповец'
places = [place1, place2, place3]
payload = {'MnqmT':'', 'lang': 'ru'}

for place in places:
    url = url_template.format(place)
    resp = requests.get(url, params=payload)
    resp.raise_for_status()
    print(resp.text)


