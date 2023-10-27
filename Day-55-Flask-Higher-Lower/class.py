from flask import Flask

app = Flask(__name__)


# Decorator make_bold
def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"

    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'Bye!'


@app.route('/username/<username>')
def greet(username):
    return f'Hello, {username}!'


if __name__ == '__main__':
    app.run(debug=True)
