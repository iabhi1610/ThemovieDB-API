import requests
import pprint
import pandas as pd



#HTTP requests

# What's our endpoint?(or a url) 

# What is the HHTP method we need?


# HTTP requests methods  ?

"""
GET -> Grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

"""
End Point

/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=ab68640e46308bca4231a738573aece0
"""
api_key = "ab68640e46308bca4231a738573aece0"

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
# print(endpoint)
# r = requests.get(endpoint) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)




api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))


output = 'movies.csv'
movie_data = []

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range (200, 299):
        print(r.json())
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head)
df.to_csv(output, index=False)