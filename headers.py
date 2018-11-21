import requests

url = "https://icanhazdadjoke.com"

#get the plain text version of the site
response = requests.get(url, headers={"Accept": "application/JSON"})

#returns the data as a string
print(response.text)

#take the JSON response and convert into Python
print(response.json())
