from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('simple_form.html')

@app.route('/reply')
def reply():
    name = request.args.get('name', '')
    return 'hello ' + name
