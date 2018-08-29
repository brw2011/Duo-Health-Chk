#!/usr/bin/python
import requests

url = "https://api-3a4f93f4.duosecurity.com/auth/v2/ping"


response = requests.request("GET", url)

print(response.text)