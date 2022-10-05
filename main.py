import requests

url_template = 'https://wttr.in/{}'
# Прогноз для Сан-Франциско, черно-белый, только 3 дня и день-ночь
id1 = 'san%20francisco?nTqu&lang=en'
url1 = url_template.format(id1)
resp1 = requests.get(url=url1)
resp1.raise_for_status()
#print(resp1.text)

# Прогноз для Лондона
id2 = 'London?MnqmT&lang=ru'
url2 = url_template.format(id2)
resp2 = requests.get(url=url2)
resp2.raise_for_status()
#print(resp2.text)

# Прогноз для аэропорта Шереметьево
id3 = 'svo?MnqmT&lang=ru'
url3 = url_template.format(id3)
resp3 = requests.get(url=url3)
resp3.raise_for_status()
#print(resp3.text)

# Прогноз для Череповца
id4 = 'Череповец?MnqmT&lang=ru'
url4 = url_template.format(id4)
resp4 = requests.get(url=url4)
resp4.raise_for_status()
print(resp4.text)

