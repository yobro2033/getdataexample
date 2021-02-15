from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_name():
    name = request.args.get('n', '')
    return 'Hello ' + name
