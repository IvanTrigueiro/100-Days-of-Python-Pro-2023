import os
import requests
from datetime import datetime

USERNAME = "ivantrigueiro"
token = os.environ["PIXELA_API_KEY"]
headers = {
    "X-USER-TOKEN": token
}

# Create user
user_params = {
    "token": token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
pixela_endpoint_graph = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

# response = requests.post(url=pixela_endpoint_graph, json=graph_params, headers=headers)
# print(response.text)

# Post a pixel
pixela_endpoint_postpixel = f"{pixela_endpoint_graph}/{graph_params['id']}"
date = datetime.today().strftime("%Y%m%d")
postpixel_params = {
    "date": date,
    "quantity": "16",
}

# response = requests.post(url=pixela_endpoint_postpixel, json=postpixel_params, headers=headers)
# print(response.text)

# Update a pixel
pixela_endpoint_updatepixel = f"{pixela_endpoint_postpixel}/{postpixel_params['date']}"
updatepixel_params = {
    "quantity": "10",
}

# response = requests.put(url=pixela_endpoint_updatepixel, json=updatepixel_params, headers=headers)
# print(response.text)

# Delete a pixel
pixela_endpoint_deletepixel = f"{pixela_endpoint_postpixel}/20231008"
response = requests.delete(url=pixela_endpoint_deletepixel, headers=headers)
print(response.text)