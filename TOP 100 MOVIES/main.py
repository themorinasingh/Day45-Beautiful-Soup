from bs4 import BeautifulSoup
import requests

#example output = 1) Movie name

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content= response.text
# print(content)

#thwrowing ingredients in and making a soup
soup = BeautifulSoup(content, "html.parser")

list_of_top_100_movies = soup.find_all(name="h3", class_="title")

for i in range(len(list_of_top_100_movies) -1, -1, -1):
    with open("movies.txt", "a") as movies:
        movies.write(list_of_top_100_movies[i].text + "\n")