import requests

url = 'https://www.youtube.com/watch?v=9VNXAfr4MG4'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
    with open('response.html', 'wb') as f:
        f.write(response.content)

    with open('response.html', 'r') as f:
        content = f.read()
else:
    print('Page load error:', response.status_code)
