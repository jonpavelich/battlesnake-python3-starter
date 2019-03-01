from flask import Response
import json

def ping_response():
    return Response(
        status=200
    )

"""
Set the snake's color, let the server know we're alive
"""
def start_response(color):
    return Response(
        status=200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
            'color': color
        })
    )