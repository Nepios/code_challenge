import csv
import requests
import json

csv_data = [["Post ID","Post Title","User ID","User Username","User Email"]]

posts = requests.get('http://jsonplaceholder.typicode.com/posts')
if posts.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(posts.status_code))

posts = json.loads(posts.text)

users = requests.get('http://jsonplaceholder.typicode.com/users')
if users.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(users.status_code))

users = json.loads(users.text)
print users

for post in posts:
  new_array = []
  user = int(post["userId"]) -1
  new_array.append(post["id"])
  new_array.append(str(post["title"]))
  new_array.append(post["userId"])
  new_array.append(str(users[user]["username"]))
  new_array.append(str(users[user]["email"]))
  csv_data.append(new_array)

my_file = open('my_csv.csv', 'wb')
wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
wr.writerows(csv_data)