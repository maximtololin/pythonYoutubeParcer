import requests

url = 'YOUR_LINK'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Page load error:', response.status_code)
