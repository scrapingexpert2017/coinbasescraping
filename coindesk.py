from bs4 import BeautifulSoup
import csv
import requests

url = "www.coindesk.com/category/technology-news/bitcoin/"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data,'html.parser')

csvfile = open('coindesk_page.csv', 'w')

csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

links = []

for article in soup.find_all('div'):
    id = ''
    link = ''
    try:
        id = article['id']
    except:
        id = 'none'
    if 'post' in id:
        link = article.div.a['href']
        links.append(link)
for i in links:
    print(i)
for page in links:
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    
    for link in soup.find_all('a'):
        link_src = ''
        hclass = ''
        try:
            hclass = link['class']
        except:
            hclass = 'none'
        if 'article-author-link-btn' in hclass:
            link_src = link['href']
            if 'mailto:' in link_src:
                print(link_src[7:])
                csvwriter.writerow([link_src[7:]])
csvfile.close()


