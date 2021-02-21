import requests
from datetime import datetime

USERNAME = "sachish"
TOKEN = "Sdahgdshagdshjagvsdvsvdasdbasdh"
GRAPH_ID = "graph12"

# ----------------- Create User ------------------------------- #
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ----------------- Create graph ------------------------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ----------------- Create pixel ------------------------------- #
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
TODAY = today.strftime("%Y%m%d")
print(TODAY)

pixel_data = {
    "date": TODAY,
    "quantity": input("How many commits did you commit today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ----------------- Update pixel ------------------------------- #
pixel_update_endpoint = f"{pixel_creation_endpoint}/{TODAY}"

pixel_update_data = {
    "quantity": "32",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

# ----------------- Delete Pixel ------------------------------- #

pixel_delete_endpoint = f"{pixel_creation_endpoint}/{TODAY}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)