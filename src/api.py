from flask import Response
import json

"""
Formats the response string to include status and content type
"""
def make_response(content, status=200, headers={"Content-type": "application/json"}):
    return (json.dumps(content), status, headers)

"""
Returns 200, lets the server know we're here
"""
def ping_response():
    return Response(
        status=200
    )

"""
Set the snake's color, let the server know we're alive
"""
def start_response(color, headType, tailType):
    assert type(color) is str, \
        "Color value must be string, not a difficult concept."

    return make_response({
        "color": color,
        "headType": headType,
        "tailType": tailType
    })

"""
Respond with a valid move
"""
def move_response(move):
    assert move in ['up', 'down', 'left', 'right'], \
        "Move must be one of [up, down, left, right], this is a 2d snake."

    return make_response({"move": move})

"""
Just let the server know we're OK with the game being over
"""
def end_response():
    return Response(
        status=200
    )