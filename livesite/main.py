import requests
from bs4 import  BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")

articles = soup.select(selector=".titleline")
# print(articles[0])
# print(articles[0].text)
# print(articles[0].select_one(".titleline a").get("href"))

scores = soup.find_all(name="span", class_="score")
# print(scores[0].text.split(" ")[0])

yc_headlines =[]
yc_links = []
yc_scores = []

for article in articles:
    yc_headlines.append(article.text)
    yc_links.append(article.select_one(".titleline a").get("href"))

for score in scores:
    yc_scores.append(int(score.text.split(" ")[0]))

print(yc_headlines)
print(yc_links)
print(yc_scores)

max_score = max(yc_scores)
index = yc_scores.index(max_score)


print(articles[index].text)
print(articles[index].select_one(".titleline a").get("href"))
print(scores[index].text.split(" ")[0])