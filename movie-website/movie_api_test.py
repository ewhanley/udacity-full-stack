import requests
import json

id = 'tt0418279'
url = 'https://theimdbapi.org/api/movie?movie_id='+id

response = requests.get(url)
resp_dict = json.loads(response.text)
print(resp_dict['poster']['large'])


