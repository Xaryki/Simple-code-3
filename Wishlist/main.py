import requests
from bs4 import BeautifulSoup

response = requests.get("https://genshin-impact.fandom.com/wiki/Events")
soup = BeautifulSoup(response.text, "html.parser")

print(soup.find_all("tbody"))

events_list = []
for i in soup.find_all(class_="wikitable sortable"):
    events_list += i.text.split(",")

#print(events_list)
