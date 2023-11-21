import requests
from api_key import TOKEN
from datetime import datetime
USERNAME = "codystiffleraz"


pixela_endpoint = "https://pixe.la/v1/users"

# Parameters for endpoints
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# parameters for graph
graph_config = {
    "id": "graph",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# Need for url 
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

# end point for post graph
post_graph_endpoint = f"{graph_endpoint}/{graph_config['id']}"
print(post_graph_endpoint)


post_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}


# response = requests.post(url=post_graph_endpoint, json=post_graph_params,headers=headers)
requests.post(url=post_graph_endpoint, json=post_graph_params,headers=headers)

# End point for updates
update_endpoint = f"{pixela_endpoint}/{USERNAME}/{graph_config['id']}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": 2.5
}

# requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# End point for deletes
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/{graph_config['id']}/{today.strftime('%Y%m%d')}"

requests.delete(url=delete_endpoint, headers=headers)