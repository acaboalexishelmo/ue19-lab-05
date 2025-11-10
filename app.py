import requests
import time
joke = requests.get("https://official-joke-api.appspot.com/random_joke")

joke_json = joke.json()
print(joke_json)
print(joke_json["setup"])
for i in range(4):
    time.sleep(1)
    print(".", end="")
print()
print(joke_json["punchline"])