import requests

key = "934b50c495c34aedb0d114747252804"
city = "São Paulo"

BASE_URL = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&lang=pt"

request = requests.get(BASE_URL)

print(request)

