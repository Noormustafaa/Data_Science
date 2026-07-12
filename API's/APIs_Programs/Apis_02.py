import requests

url = "https://v2.jokeapi.dev/joke/Programming?type=single"
response = requests.get(url)

if response.status_code == 200:
    data =response.json()
    joke =data["joke"]
    print("here is your Joke")
    print(joke)
else:
    print("could not connect Api's")
    