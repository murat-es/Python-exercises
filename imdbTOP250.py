import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"
response=requests.get(url)

html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")

movieName= soup.find_all("td",{"class":"titleColumn"},"a")
movieRating= soup.find_all("td",{"class":"ratingColumn imdbRating"})

for i,j in zip(movieName,movieRating):

    movieName=str(i.text)
    movieName=movieName.strip()
    movieName=movieName.replace("\n","")

    movieRating=str(j.text)
    movieRating=movieRating.strip()
    movieRating=movieRating.replace("\n","")
   
    print(movieName," --> ""Rating: ",movieRating,"\n")