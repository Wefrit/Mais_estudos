# requests para requisições http
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3003/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

article = top_jobs_heading.parent

print(article)