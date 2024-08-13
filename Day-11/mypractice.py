import requests

#/repos/{owner}/{repo}/pulls get it from github documentation pulls
response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#print(type(response))
print(response.status_code)
print(response)     #this is the output u got <Response [403]>
#complete_detail=response.json()    #if u want to get content like in the web browser then do
    #to get the id of first person how pulled request

#headers = {
  #  "Authorization": "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 "
#}

#responses = requests.get(response, headers=headers)
#print(responses[0]["id"])