# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save')
def save():
    msg = request.args.get('msg', '')
    f = open("messages.txt", "a")
    f.write(msg + '<br>')
    f.close()
    f = open("messages.txt", "r")
    return f.read()
