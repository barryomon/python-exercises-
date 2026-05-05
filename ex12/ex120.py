import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count + 1):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
    url = tags[position - 1].get('href')

name = url.split('known_by_')[1].replace('.html', '')
print('The answer is:', name)