from flask import Flask, Response, send_from_directory
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
    return Response(
        status=200
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0')

