import requests
from api_key import TOKEN
from datetime import date
USERNAME = "codystiffleraz"


pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}



post_graph_endpoint = f"{graph_endpoint}/{graph_config['id']}"
print(post_graph_endpoint)

post_graph_params = {
    "date": "20231117",
    "quantity": "1"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response = requests.post(url=post_graph_endpoint, json=post_graph_params,headers=headers)
requests.post(url=post_graph_endpoint, json=post_graph_params,headers=headers)