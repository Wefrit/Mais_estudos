# requests para requisições http
import requests

url = 'http://localhost:3003/'
response = requests.get(url)

print(response.status_code)