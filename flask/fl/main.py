# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

from flask import render_template, app


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('flask.html', name=name)

