import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_English_football_champions"
response=requests.get(url)

html=response.content
soup=BeautifulSoup(html,"html.parser")

teamTable=soup.find('table',{'class':'wikitable sortable'})
team=teamTable.findAll('b')
title=teamTable.findAll('td',{'align':'center'})

for k,i in zip(team,range(0,len(title),2)):
    i=str(title[i].text)
    i=i.strip()
    print(k.text," --> ",i)