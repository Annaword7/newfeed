import requests
import json
url = 'https://httpbin.org/post'

post_params = {'user': 'admin', 'password': 'admin_pass1'}

response = requests.post(url, data=post_params)
response.json()