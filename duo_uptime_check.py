import requests

url = "https://api-3a4f93f4.duosecurity.com/auth/v2/check"

headers = {
    'authorization': "Basic <redacted>",
    }

response = requests.request("GET", url, headers=headers)
print(response.text)