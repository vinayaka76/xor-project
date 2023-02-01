
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/search?q=command&s=31d07ece-62f6-41e5-8d30-bae62bb77419 "
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.find_all("a", {"class": "question-hyperlink"})

for question in questions:
    print(question.text)