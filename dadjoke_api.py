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
)

data = response.json()["results"]

#make a list of just the jokes
jokesonly = list(map(lambda j: j["joke"], data))

if len(jokesonly) == 0:
    print(f"Sorry, I don't have any jokes about {term}")
elif len(jokesonly) == 1:
    print(f"I've got one joke about {term}. Here it is: {jokes[0]}")
elif len(jokesonly) > 1:
    randjoke = jokesonly[randint(0,len(jokesonly))]
    print(f"I've got {len(jokesonly)} jokes about {term}. Here's one: {randjoke}")
