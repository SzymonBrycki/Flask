from flask import Flask, redirect

app = Flask(__name__)

@app.route('/redirect')
def index():
    return redirect('http://www.example.com')