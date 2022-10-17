import random
import json
import requests
from flask import Flask

app = Flask(__name__)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}


@app.route('/', methods=['GET'])
def get_index():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    todos = json.loads(response.text)
    print(todos == response.json())  # True
    print(type(todos))  # <class 'list'>
    # print(todos)
    print(todos[5])
    rand = random.randint(1, 101)
    return f"<h1>{todos[rand]}</h1>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
