import requests
from random import randint

url = "https://icanhazdadjoke.com/search"

term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url,
    headers={"Accept": "application/JSON"},
    params={
        "term": term
    }
).json()

num_jokes = response["total_jokes"]
res = response["results"]

if num_jokes > 1:
    randjoke = res[randint(0,num_jokes)]['joke']
    print(f"I've got {num_jokes} about {term}. Here's one: {randjoke}")
elif num_jokes == 1:
    print(f"I've got one joke about {term}. Here it is: {res[0]['joke']}")
else:
    print(f"Sorry, I don't have any jokes about {term}")
