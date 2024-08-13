import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
headers = {
    "Authorization": "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 "
}

response = requests.get(url, headers=headers)  #this outputs u in list form
for i in range(len(response)):
    print(response.json()[i]["user"])
#print(response.status_code)