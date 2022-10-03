from flask import Flask
from random import randint

from projects.calculator_lib.calculator_lib import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/')
def add():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "Did you know {} + {} = {}?".format(num1, num2, calc.add(num1, num2))
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0')
