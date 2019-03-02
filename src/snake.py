from util import get_config
import random
import json

config = get_config()

"""
TODO: Write your snake logic here. See sample data argument below.
"""
def choose_move(data):
    print(data)
    directions = ['up', 'down', 'left', 'right']
    return random.choice(directions)

"""
Sample data:
{
  "game": {
    "id": "game-id-string"
  },
  "turn": 4,
  "board": {
    "height": 15,
    "width": 15,
    "food": [
      {
        "x": 1,
        "y": 3
      }
    ],
    "snakes": [
      {
        "id": "snake-id-string",
        "name": "Sneky Snek",
        "health": 90,
        "body": [
          {
            "x": 1,
            "y": 3
          }
        ]
      }
    ]
  },
  "you": {
    "id": "snake-id-string",
    "name": "Sneky Snek",
    "health": 90,
    "body": [
      {
        "x": 1,
        "y": 3
      }
    ]
  }
}
"""
