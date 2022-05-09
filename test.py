import requests

API_KEY = ""

url = "https://maps.googleapis.com/maps/api/distancematrix/json"


origins = ["203 S Kendall Ave, Kalamazoo, MI 49006 | Solon St, Kalamazoo"]
destinations = ["3298 Stadium Dr, Kalamazoo, MI 49008 | 1610 Knollwood Ave, Kalamazoo, MI. 49006"]
payloads = {'origins': origins, 'destinations': destinations, 'key':API_KEY}

response = requests.get(url, params=payloads)

print(response.text)
