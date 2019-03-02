from util import get_config
import random
import json

config = get_config()

"""
This function decides on priorities and makes a decision about what to do
"""
def choose_move(data):
    print(config)
    directions = ['up', 'down', 'left', 'right']
    return random.choice(directions)