import requests
from BeautifulSoup import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

html = response.content

soup = BeautifulSoup(html)

table = soup.find('table')

#We iterate over the rows
links = []

for row in table.findAll('tr',attrs={'class':'athing'}):
  for cell in row.findAll('td',attrs={'class':'title'}):
    link = cell.find('a',attrs={'class':'storylink'})
    if link:
      links.append({link.text.encode('utf-8') : link.get('href').encode('utf-8')})

for link in links:
  print link
