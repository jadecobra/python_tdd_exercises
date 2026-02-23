import pathlib
import sys
sys.path.insert(
    0, str(pathlib.Path(__file__).resolve().parent)
)

import calculator
import flask


app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    first_input = flask.request.form.get('first_input')
    first_input = float(first_input)
    second_input = flask.request.form.get('second_input')
    second_input = float(second_input)
    operation = flask.request.form.get('operation')

    operations = {
        'add': '+',
        'subtract': '-',
        'divide': '/',
        'multiply': '*',
    }

    result = calculator.__getattribute__(operation)(
        first_input, second_input
    )
    return (
        f'<h2>{first_input} {operations[operation]} {second_input} '
        f'= {result}</h2>'
    )