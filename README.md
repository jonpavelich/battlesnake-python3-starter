# battlesnake-python3-starter

A [Battlesnake](http://battlesnake.io) starter written in Python 3 and Flask.

Visit [https://github.com/battlesnakeio/community/blob/master/starter-snakes.md](https://github.com/battlesnakeio/community/blob/master/starter-snakes.md) for API documentation and instructions for running your AI.

This AI client uses [Flask](http://flask.pocoo.org/) to serve requests and the [gunicorn web server](http://gunicorn.org/) to run on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

#### You will need...

* a Python 3.7 development environment
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies
* [virtualenv](https://virtualenv.pypa.io/en/stable/installing/) to contain the dependencies
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## Running the Snake Locally

1) [Fork this repo](https://github.com/jonpavelich/battlesnake-python3-starter/fork).

2) Clone repo to your development environment:
```
git clone git@github.com:<your github username>/battlesnake-python3-starter.git
```

3) Set up a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
```
# Use the default Python on your path:
virtualenv venv

# Or use a specific path:
virtualenv -p /path/to/python3 venv
```

4) Activate the virtual environment (you have to do this every time you open a new shell)
```
# Linux, macOS
source venv/bin/activate

# Windows
venv/Scripts/activate.bat
```

5) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
cd src
python app.py
```

5) Test your snake by sending a curl to the running snake
```
curl -XPOST -H 'Content-Type: application/json' -d '{ "hello": "world"}' http://localhost:5000/start
```

## Deploying to Heroku

1) Create a new Heroku app:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [https://APP_NAME.herokuapp.com](https://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command:
```
heroku logs --tail
```

## License
This code is licensed under the MIT License. See [LICENSE](https://github.com/jonpavelich/battlesnake-python3-starter/blob/master/LICENSE).

## Credit
Written by [Jon Pavelich](https://github.com/jonpavelich) and [Tyler Harnadek](https://github.com/THarnadek) for BattleSnake 2019. This README file is based on the [battlesnakeio/starter-snake-python README](https://github.com/battlesnakeio/starter-snake-python/blob/master/README.md).
