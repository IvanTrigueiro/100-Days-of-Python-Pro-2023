from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# Get all articles
articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    # Get the title
    text = article_tag.get_text()
    article_texts.append(text)
    # Get the link
    link = article_tag.find("a").get("href")
    article_links.append(link)
# print(article_texts)
# print(article_links)

# Check if class score exists inside class subline and get the score
all_sublines = soup.find_all(class_="subtext")
article_upvotes = []
for subline in all_sublines:
    if subline.find(class_="score"):
        article_upvotes.append(subline.find(class_="score").getText())
    else:
        article_upvotes.append("0")
# print(article_upvotes)
article_upvotes_split = [int(article.split(" ")[0]) for article in article_upvotes]
# print(article_upvotes_split)
# Get biggest number of upvotes
most_upvotes = max(article_upvotes_split)
# print(most_upvotes)
# Get bigger number index
biggest_upvotes_index = article_upvotes_split.index(most_upvotes)
# print(biggest_upvotes_index)

print(article_texts[biggest_upvotes_index])
print(article_links[biggest_upvotes_index])
print(f"Most upvoted: {most_upvotes}")

#################### CLASS ROOM #####################
# import lxml
#
# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.title.name)
# all_anchor_tabs = soup.find_all(name="a")
# for tag in all_anchor_tabs:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.string)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one("p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)
