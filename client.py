import requests


class Movie:
  def __init__(self, row):
    self.movie_id = row[0]
    self.release_date = row[1]
    self.runtime = row[2]
    self.original_language = row[3]
    self.budget = row[4]
    self.revenut = row[5]
    self.title = row[6]


#################################################
# main
#
print('** client starting **')
print()

baseurl = 'API Gateway Endpoint'

# build URL:
url = baseurl + '/movies'

# call the web service:
response = requests.get(url)

# output the result:
body = response.json()

print('status code:', response.status_code)
print('# of movies:', len(body))
print()

#
# convert rows to Movie objects:
#
movies = []
for row in body:
  movie = Movie(row)
  movies.append(movie)
 
#
# output movie ids and titles:
# 
for m in movies:
  print(m.movie_id, m.title)

print()
print('** client done **')


