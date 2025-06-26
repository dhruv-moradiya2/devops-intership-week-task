import requests

# demo api: /repos/{owner}/{repo}/pulls
# https://github.com/kbernuetes/kubernetes

# https://api.github.com/repos/kbernuetes/kubernetes/pulls

# this come as json format convert in to dic list require 
github_api_key = "https://api.github.com/repos/kubernetes/kubernetes/pulls"


response = requests.get(github_api_key)

print(response)

output = response.json()


for user_data in range(len(output)):
    print(output[user_data]["user"]["login"])

