import requests
from BeautifulSoup import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('table')


#We iterate over the rows
links = []

for row in table.findAll('tr',attrs={'class':'athing'}):
  for cell in row.findAll('td',attrs={'class':'title'}):
    link = cell.findAll('a',attrs={'class':'storylink'})
    if link:
      links.append({link[0].text.encode('utf-8') : link[0].get('href').encode('utf-8')})

for link in links:
  print link
