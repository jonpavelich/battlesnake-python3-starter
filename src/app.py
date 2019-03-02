from flask import Flask, Response, request, send_from_directory
from api import ping_response, start_response, move_response, end_response
import random
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
"""
@app.route('/start')
def start():
    print(request.get_json())
    color = "#8C271E"
    return start_response(color)

"""
This is called whenever the server wants our next move
It's where the magic happens
"""
@app.route('/move')
def move():
    data = request.get_json()
    print(data)

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)


"""
Just responds with 200 to let the server know it's All Good In The Hood
"""
@app.route('/end')
def end():
    data = request.get_json()
    print(json.dumps(data))

    return end_response()

"""
This is the main function, for arcane reasons
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0')

