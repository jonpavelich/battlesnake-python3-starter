from flask import Flask
app = Flask(__name__)

@app.route('/')
def route_root():
    return "I'm a snake, and I have good grammar."

