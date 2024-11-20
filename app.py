import requests
def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "single":
            return joke["joke"]
        else:
            return f"{joke['setup']} - {joke['delivery']}"

    else:
        return "failed to retrieve a joke."



if __name__ == "__main__":
    print("Here is a joke for you")
    print(get_joke())