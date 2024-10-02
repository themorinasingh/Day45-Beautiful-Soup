from bs4 import BeautifulSoup

with open("./website.html", "r") as file:
    file_data = file.read()

file_info = BeautifulSoup(file_data, "html.parser")

a_tags = file_info.find_all("a")

for tag in a_tags:
    print(tag.get("href"))
print("\n")
#finding something in particular:
tag = file_info.find(name="a", class_="tag").get("href")
print(tag)
print("\n")
company_url = file_info.select_one(selector="p em strong a") #works like css selector
print(company_url)

print("\n")
#select selects all the available items, for ex tags of same class
same_class = file_info.select(selector=".testing")
for class_ in same_class:
    print(class_)