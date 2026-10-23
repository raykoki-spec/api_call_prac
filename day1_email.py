import requests
API_KEY = "rc_live_9731993b15a747ed9c5bf5bb90bdec08"
url="https://api.restcountries.com/email-intelligence/v1/process?email=raykokike@gmail.com"
headers={"Authorization": f"Bearer {API_KEY}"}

response= requests.get(url, headers=headers, timeout=10)
body = response.json()

if response.status_code == 200 and "data" in body:
    email_info = body["data"]["objects"][0]

    email_address = email_info["email"]
    domain = email_info["domain"]["provider"]["name"]
    url = email_info["domain"]["provider"]["url"]
    
    


    print(f"Email Address: {email_address}")
    print(f"Domain: {domain}")
    print(f"URL: {url}")

print("Status code:", response.status_code)
