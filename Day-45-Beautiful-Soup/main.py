import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html_text = response.text
soup = BeautifulSoup(html_text, "html.parser")

# Find all the movie titles
movie_description = soup.find_all(class_="article-title-description")

movies_titles_100_to_1 = [movie.find("h3").getText() for movie in movie_description]
movies_titles = movies_titles_100_to_1[::-1]

# Open the file in write mode
with open("movies.txt", "w", encoding="utf-8") as file:
    # Write each movie on a new line
    for movie in movies_titles:
        file.write(f"{movie}\n")
