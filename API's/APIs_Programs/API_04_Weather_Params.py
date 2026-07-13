import requests

# 1. Main address of the API (Base URL)
url = "https://api.openweathermap.org/data/2.5/weather"

# 2. Keeping the Key and City inside params (parameters)
query_parameters = {
    "q": "Larkana,PK",          # Name of the city
    "appid": "Write_API_Key_Here",    # Your secret key (API Key)
    "units": "metric"           # To get the temperature in Celsius
}

# 3. Sending the GET request along with the parameters
response = requests.get(url, params=query_parameters)

# 4. Checking the retrieved data
print(response.json())