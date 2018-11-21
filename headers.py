import requests

url = "https://icanhazdadjoke.com"

#get the plain text version of the site
response = requests.get(url, headers={"Accept": "text/plain"})

print(response.text)
