import requests

url = "https://icanhazdadjoke.com/search"

#get the plain text version of the site
response = requests.get(
    url,
    headers={"Accept": "application/JSON"},
    params={
        "term": "cat"
    }
)

#set a variable that's a Python dictionary of the JSON data
data = response.json()
print(data)

#print the joke from the Python dictionary
#print(data["joke"])

#print response status code
#print(f"status: {data['status']}")
