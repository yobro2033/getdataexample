# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def name_home():
    name = request.args.get('n', '')
    return 'Hello ' + name
