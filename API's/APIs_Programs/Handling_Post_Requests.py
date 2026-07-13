import requests

# 1. API ka URL jahan humein data bhejna hai
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Jo data hum bhejna chahte hain (Python Dictionary)
apna_data = {
    "title": "Mera Pehla Post",
    "body": "API seekhna bohot aasan hai!",
    "userId": 1
}

# 3. POST request bhejna (.post() use kar ke)
response = requests.post(url, json=apna_data)

# 4. Server ka jawab dekhna
print("Status Code:", response.status_code)
print("Server ka Response:")
print(response.json())