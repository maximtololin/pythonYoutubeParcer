import requests

url = 'https://www.youtube.com/watch?v=zu2ZCQ6VQIY'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Ошибка при получении страницы:', response.status_code)