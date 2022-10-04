import requests

#url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
#resp = requests.get(url=url)
#resp.raise_for_status()
#print(resp.text)
url1 = 'https://wttr.in/London?MnqmT&lang=ru'
url2 = 'https://wttr.in/svo?MnqmT&lang=ru'
url3 = 'https://wttr.in/Череповец?MnqmT&lang=ru'
resp = requests.get(url3)
resp.raise_for_status()
print(resp.text)