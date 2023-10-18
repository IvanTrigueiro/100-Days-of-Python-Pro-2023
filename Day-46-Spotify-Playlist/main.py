import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import bs4

spotipy_client_id = os.environ.get("SPOTIPY_CLIENT_ID")
spotipy_client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
spotipy_redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")

date = input("Which year would you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = bs4.BeautifulSoup(response.text, "html.parser")

# find div with class o-chart-results-list-row-container
div_elements = soup.find_all("div", class_="o-chart-results-list-row-container")

# find the first span in div_elements to get the top 100 enumeration
span_elements = [element.find("span").getText().strip() for element in div_elements]

# find the h3 elements in div_elements to get the song titles
song_names = [element.find("h3").getText().strip() for element in div_elements]

# select the span element to find artist or band
li_elements = soup.find_all("li", class_="lrv-u-width-100p")
artists_names_untreated = [element.find("span").getText().strip() for element in li_elements]

# get every 2 elements from artists_names_untreated
artists_names = [element for i, element in enumerate(artists_names_untreated) if i % 2 == 0]

# top 100 ranking
rank_100 = [f"{span_elements[i]} - {song_names[i]}" for i in range(100)]

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotipy_client_id,
                                               client_secret=spotipy_client_secret,
                                               redirect_uri=spotipy_redirect_uri,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]

# Search spotify by song name
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
