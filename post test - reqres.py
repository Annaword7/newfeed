url = 'https://reqres.in/api/register'

post_params = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(url, data=post_params)
response.json()