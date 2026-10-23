# File: README.md

# API Requests Demo

Python-based API calls that demonstrates how the request-response cycle works.
In these API calls, specific values are pulled out of the JSON response and displayed clearly.

## What It Does

- The user sends request to the API address(URL)
- The server receives the request, runs its logic and then prepares the response
- User receives the response in form of JSON
- Formats a clear report


## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
 ``rest countries

 if response.status_code == 200 and "data" in body:
    country = body["data"]["objects"][0]

    name = country["names"]["common"]
    capital = country["capitals"][0]["name"]

    print(f"Country: {name}")
    print(f"Capital: {capital}")


``email api

if response.status_code == 200 and "data" in body:
    email_info = body["data"]["objects"][0]

    email_address = email_info["email"]
    domain = email_info["domain"]["provider"]["name"]

    print(f"Email Address: {email_address}")
    print(f"Domain: {domain}")
```

## Sample Output

```
#rest countries

Country: Kenya
Capital: Nairobi


#email api

Email Address: raykokike@gmail.com
Domain: Google



```

## Stack

Python


