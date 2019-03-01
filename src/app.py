from flask import Flask, Response, request, send_from_directory
from api import ping_response, start_response
import json

app = Flask(__name__)

"""
Check the vitals
"""
@app.route('/')
def route_root():
    return "I'm a snake, and I have good grammar."

"""
Serve a static file for the snake head image
"""
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

"""
This keeps the snake alive, in case of Heroku
taking an early coffee break.
"""
@app.route('/ping')
def ping():
    return ping_response()

"""
Our snake has a very small brain so it's stateless
This is just a quick heads-up that the game is starting
JON ADD A CONFIG FILE
"""
@app.route('/start')
def start():
    print(json.dumps(request.data))
    color = "#8C271E"
    return start_response(color)

"""
This is the main function, for arcane reasons
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0')

