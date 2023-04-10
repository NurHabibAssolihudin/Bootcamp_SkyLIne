# API
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
data = r.json()

print(data)

# Request Post Data
data_baru = {
    "body" : "Lorem Ipsum",
    "title" : "Title",
    "userId" : 5
}

req = requests.post("https://jsonplaceholder.typicode.com/posts", data_baru)
print(type(req.json()))

# Lambda Function
z = lambda x : x + 2

print(z(5))