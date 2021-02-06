# Add links to urllist for more pages. 
# Code can be expanded to scrape more.

import requests
from bs4 import BeautifulSoup

urllist = [
	'http://www.amazon.com/Flash-Boys-Wall-Street-Revolt/dp/0393244660',
	'http://www.amazon.com/The-Big-Short-Doomsday-Machine/dp/0393338827'
	]

for url in urllist:
	r = requests.get(url)

	soup = BeautifulSoup(r.text, features="lxml")
	tmp = ''
	for line in soup.get_text().split():
		if line.lower() == 'pages' and tmp.isdigit():
			print(tmp,line, ' - ',soup.html.head.title.text)
		else:
			tmp = line