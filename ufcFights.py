from bs4 import BeautifulSoup
import requests
import key

url = "https://api.sportsdata.io/v3/mma/scores/xml/Schedule/ufc/2022?key=" + key.api
xml = requests.get(url)

fights =[]

soup = BeautifulSoup(xml.content, 'lxml')
for event in soup.find_all(['name', 'day']):
  fights.append(event.text)

i=1

while i <len(fights):
  fights[i] = fights[i].split('T').pop(0)
  i +=2


fights = fights[::-1]

for fight in fights:
  print(''.join(fight))
