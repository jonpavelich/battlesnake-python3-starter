from flask import Flask
app = Flask(__name__)

@app.route('/')
def route_root():
    return "I'm a snake, and I have good grammar."

if __name__ == '__main__':
    app.run(host='0.0.0.0')

