import random

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    rand = random.randint(1, 667)
    return f"<h1>{rand}</h1>"

