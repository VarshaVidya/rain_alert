import requests
# 4ea5ba59a7c308a121f3478d7b8bddba
api_key = "4ea5ba59a7c308a121f3478d7b8bddba"
endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "q": "Hougang,Singapore",
    "appid":api_key,
}
response = requests.get(endpoint, params=parameters)

print(response.status_code)
data = response.json()

# climate = data["weather"]



