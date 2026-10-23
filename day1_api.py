import requests

API_KEY = "rc_live_9731993b15a747ed9c5bf5bb90bdec08"
url = "https://api.restcountries.com/countries/v5/names.common/kenya"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers, timeout=10)

print("Status code:", response.status_code)
print("Data received:", response.json())