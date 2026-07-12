import requests

# 1. The URL endpoint we want to get data from
url = "https://randomuser.me/api/"

# 2. Sending a GET request to the API
response = requests.get(url)

# 3. Checking if the request was successful (Status code 200 means OK)
if response.status_code == 200:
    # Parsing the response into JSON format (which looks like a Python dictionary)
    data = response.json()
    
    # Extracting specific information from the nested data
    user = data['results'][0]
    name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    
    print(f"Name: {name}")
    print(f"Email: {email}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")