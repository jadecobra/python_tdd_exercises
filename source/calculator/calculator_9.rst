.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator website. This tutorial covers Flask, templates, forms, and integrating your existing TDD calculator.
  :keywords: Jacob Itegboje, python tdd calculator website, flask tdd tutorial, python flask calculator project, test driven development flask example, python web calculator, flask beginner tutorial, python tdd web app

.. include:: ../links.rst

.. _Flask: https://flask.palletsprojects.com/en/stable/
.. _HTTP status code: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
.. _404 Not Found: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/404
.. _200 OK: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200
.. _jinja2.exceptions.TemplateNotFound: https://jinja.palletsprojects.com/en/stable/api/#jinja2.TemplateNotFound
.. _HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
.. _assertIn method: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn
.. _unittest.TestCase.assertIn method: `assertIn method`_
.. _decode method: https://docs.python.org/3/library/stdtypes.html#bytes.decode

#################################################################################
how to make a calculator 9
#################################################################################

I want to make a website for the :ref:`calculator<how to make a calculator>` so that anyone can use it in their browser without installing Python_ or running code.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_website.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

* I make a new test file for the website

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_calculator_website.py

* I add Flask_ to the ``requirements.txt`` file_

  .. code-block:: shell
    :emphasize-lines: 1

    echo "flask" >> requirements.txt

  Flask_ is a Python_ library that is used for making websites, it is not part of `The Python Standard Library`_

* I install the Python packages I gave in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I use ``pytest-watcher`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 5 items

    tests/test_calculator.py .....                                [100%]

    ======================== 5 passed in X.YZs =========================

----

*********************************************************************************
test_home_page
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I open ``test_calculator_website.py`` from the ``tests`` folder_ in the :ref:`editor<2 editors>`

* I add a test to ``test_calculator_website.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestCalculatorWebsite(unittest.TestCase):

        def test_home_page(self):
            client = src.website.app.test_client()

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: NameError

    class TestCalculatorWebsite(unittest.TestCase):

        def test_home_page(self):
            client = src.website.app.test_client()


    # Exceptions seen
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for the ``website`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.website
    import unittest

  the terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.website'

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # NameError
    # ModuleNotFoundError

* then I add ``website.py`` to the ``src`` folder_ and the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.website' has no attribute 'app'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # NameError
    # ModuleNotFoundError
    # AttributeError

* I make the Flask_ app in ``website.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4

    import flask


    app = flask.Flask(__name__)

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_home_page` in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4

        def test_home_page(self):
            client = src.website.app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 'BOOM!!!')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 404 != 'BOOM!!!'

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5
    :emphasize-text: AssertionError

    # Exceptions seen
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # AssertionError

* I change the expectation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            self.assertEqual(response.status_code, 404)

  the test passes.

  - ``client = src.website.app.test_client()`` points the name ``client`` to the Flask_ app in ``website.py``
  - ``response = client.get('/')`` points the name ``response`` to the result of the call to the ``get`` :ref:`method<what is a function?>` of the :ref:`client object<what is a class?>`
  - ``client.get('/')`` returns an :ref:`response object<what is a class?>`
  - ``'/'`` is short for root or home in this case, the homepage of the website I am making also known as ``index.html``
  - ``response.status_code`` gets the ``status_code`` :ref:`attribute<test_attribute_error_w_class_attributes>` or the :ref:`response object`
  - the above can also be written as ``src.website.app.test_client().get('/').status_code``
  - ``404`` is `HTTP status code`_, it is short for `404 Not Found`_ which means the page cannot be found
  - I want a ``200`` `HTTP status code`_, it is short for `200 OK` and means the request was successful

* I change the expectation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_home_page(self):
            client = src.website.app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 404 != 200

* I add a :ref:`function<what is a function?>` for the homepage in ``website.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-9

    import flask


    app = flask.Flask(__name__)


    @app.route('/')
    def home():
        return flask.render_template('index.html')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 500 != 200

  it also shows `jinja2.exceptions.TemplateNotFound`_

  .. code-block:: python

    jinja2.exceptions.TemplateNotFound: index.html

  I have to make a template file for ``index.html``

* I add a new folder_ to the ``src`` folder_ named ``templates``, the terminal_ still shows the same :ref:`Exception<errors>`
* I add a new file_ in the ``templates`` folder named ``index.html``, the terminal_ still shows the same :ref:`Exception<errors>`

* I go back to ``test_calculator_website.py`` then use :kbd:`ctrl+s` on the keyboard to save the file_ which makes `pytest-watcher`_ run the tests again, and the test passes

----

*********************************************************************************
how to view the website
*********************************************************************************

* I want to see what I just made. I open a new terminal_, then use uv_ to run the Flask_ server

  .. code-block:: python
    :emphasize-lines: 1

    uv run flask --app src/website run --debug

  the terminal_ shows

  .. code-block:: shell

     * Serving Flask app 'src/website'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
     * Restarting with watchdog (inotify)
     * Debugger is active!
     * Debugger PIN: ABC-DEF-GHI

* it might also show a dialog box like this, and I click on ``Open in Browser``

  .. image:: /_static/calculator/flask_dialog.png
    :width: 600
    :align: center
    :alt: Confirm you want to run Flask Development Server

  or I use :kbd:`ctrl` on the keyboard and click on ``http://127.0.0.1:5000`` with the mouse to open the browser and it shows an empty page. Success!

* I add another :ref:`assertion<what is an assertion?>` for text from the website to :ref:`test_home_page` in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_home_page(self):
            client = src.website.app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Calculator', response.data.decode())

  - the `assertIn method`_ checks if the input on the left is part of the :ref:`object<what is a class?>` on the right.
  - ``response.data.decode()`` returns the result of calling the ``decode`` :ref:`method<what is a function?>` of the ``data`` :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``response`` :ref:`object<what is a class?>`
  - the `decode method`_ is part of the bytes_ data type, it converts bytes_ to strings_
  - bytes_ are like strings_ , they have a ``b`` before the :ref:`quotes`, for example

    .. code-block:: python

      b'single quote byte'
      b'''triple single quote byte'''
      b"double quote byte"
      b"""triple double quote byte"""

  The terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Calculator' not found in ''

  there is nothing in ``src/templates/index.html``

* I open ``index.html`` from the ``templates`` folder_, then add some HTML_

  .. code-block:: python

    <h1>Calculator</h1>

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` because `pytest-watcher`_ only checks my :ref:`Python files<what is a module?>`, it does not run the tests when I change other files

  - ``<></>`` are called tags, they are :ref:`enclosures`
  - ``<h1>HEADING</h1>`` tells the computer to make ``HEADING`` a heading

* I go back to ``test_calculator_website.py`` and use :kbd:`ctrl+s` on the keyboard and the test passes

* I go back to the browser and hit ``refresh``, it shows ``Calculator``

  .. image:: /_static/calculator/calculator_heading.png
    :width: 600
    :align: center
    :alt: Calculator Header

  I know how to make a website with Python_

----

*********************************************************************************
test_calculate_route
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for doing calculations with the website

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 7-17

      def test_home_page(self):
          client = src.website.app.test_client()
          response = client.get('/')
          self.assertEqual(response.status_code, 200)
          self.assertIn(b'Calculator', response.data)

      def test_calculate_route(self):
          client = src.website.app.test_client()
          response = client.post(
              '/calculate',
              data={
                  'first_input': 0,
                  'second_input': 1,
                  'operation': 'add',
              }
          )
          self.assertEqual(response.status_code, 200)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 404 != 200

the address for ``calculate`` does not exist yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a new :ref:`function<what is a function?>` to ``website.py``

.. code-block:: python
  :lineno-start: 8

  @app.route('/')
  def home():
      return flask.render_template('index.html')


  @app.route('/calculate', methods=['POST'])
  def calculate():
      first_input = float(flask.request.form.get('first_input', 0))
      second_input = float(flask.request.form.get('second_input', 0))
      operation = flask.request.form.get('operation')

      result = src.calculator.add(first_input, second_input)
      return f'<h1>result: {result}</h1>'

the test passes because the route to ``/calculate`` now exists

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to make sure I get the right result back in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 12

        def test_calculate_route(self):
            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': 0,
                    'second_input': 1,
                    'operation': 'add',
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'BOOM!!!', response.data)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: b'BOOM!!!' not found in b'<h1>result: 1.0</h1>'

* I change ``BOOM!!!`` to the expected result

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

            self.assertIn(b'result: 1.0', response.data)

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I import the `random module`_ to make random numbers for the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import src.website
    import unittest

* I add a :ref:`variable<what is a variable>` to the test

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

        def test_calculate_route(self):
            x = random.randint(-1000, 1000)

            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': x,
                    'second_input': 1,
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'result: 1.0', response.data)

* I use ``x`` for the first input

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines:

            response = client.post(
                '/calculate',
                data={
                    # 'first_input': 0,
                    'first_input': x,
                    'second_input': 1,
                }
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'result: 1.0' not found in '<h1>result: ABC.D</h1>'



* I add ``x`` in an `f-string`_ to the :ref:`assertion<what is an assertion?>` for the result

  .. code-block:: python

----


----

----




I open ``src/app.py`` and add the route

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 7-20

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/calculate', methods=['POST'])
    def calculate():
        first = float(request.form['first'])
        operation = request.form['operation']
        second = float(request.form['second'])

        from src.calculator import add, subtract, multiply, divide

        ops = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        result = ops[operation](first, second)
        return f"<h1>Result: {result}</h1>"

I add the import for request at the top

.. code-block:: python
  :lineno-start: 1

  from flask import Flask, render_template, request

the test passes.


    def test_calculate_route(self):
        x = tests.test_calculator.a_random_number()
        y = tests.test_calculator.a_random_number()

        client = src.website.app.test_client()
        response = client.post(
            '/calculate',
            data={
                # 'first_input': 0,
                'first_input': x,
                'second_input': 1,
                'operation': 'add',
            }
        )
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'result: 1.0', response.data)
        self.assertIn(b'result: 1.0', response.data)

----


----

----

----

----


----


.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5-12


      def test_home_page(self):
          client = app.test_client()
          response = client.get('/')
          self.assertEqual(response.status_code, 200)
          self.assertIn(b'Calculator', response.data)

  the test still fails because there is no template.

* I make the templates folder and file

  .. code-block:: shell
    :emphasize-lines: 1-2

    mkdir templates
    touch templates/index.html

* I open ``templates/index.html`` and add a simple page

  .. code-block:: html
    :linenos:

    <h1>Calculator</h1>
    <form method="post" action="/calculate">
        <input type="number" name="first" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="second" required>
        <button type="submit">Calculate</button>
    </form>

  the test passes.


@app.route('/calculate', methods=['POST'])
def calculate():
    first_input = flask.request.form.get('first_input', 0)
    second_input = flask.request.form.get('second_input', 0)
    operation = flask.request.form.get('operation')

    result = src.calculator.add(first_input, second_input)
    return f'<h1>result: {result}</h1>'



*********************************************************************************
test_error_handling_in_web
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add tests for errors

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 5-20

      def test_calculate_route(self):
          ...

      def test_error_handling_in_web(self):
          from src.app import app
          client = app.test_client()

          # non-number
          response = client.post('/calculate', data={
              'first': 'abc',
              'operation': 'add',
              'second': '3'
          })
          self.assertIn(b'brmph?! Numbers only', response.data)

          # divide by zero
          response = client.post('/calculate', data={
              'first': '5',
              'operation': 'divide',
              'second': '0'
          })
          self.assertIn(b'I cannot divide by 0', response.data)

the tests fail with exceptions or wrong messages.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I update the calculate route to catch exceptions and use the existing error messages

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 10-25

    def calculate():
        try:
            first = float(request.form['first'])
            operation = request.form['operation']
            second = float(request.form['second'])

            from src.calculator import add, subtract, multiply, divide

            ops = {
                'add': add,
                'subtract': subtract,
                'multiply': multiply,
                'divide': divide
            }

            result = ops[operation](first, second)
            return render_template('index.html', result=result)
        except Exception as e:
            error = str(e)
            if 'Numbers only' in error or 'brmph' in error:
                error = 'brmph?! Numbers only. Try again...'
            elif 'division by zero' in error:
                error = 'brmph?! I cannot divide by 0. Try again...'
            return render_template('index.html', error=error)

I update the template to show result or error

.. code-block:: html
  :lineno-start: 1
  :emphasize-lines: 10-20

    <h1>Calculator</h1>
    {% if result is defined %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
    {% if error is defined %}
        <h2 style="color:red">{{ error }}</h2>
    {% endif %}
    <form method="post" action="/calculate">
        ...

the tests pass.

----

*********************************************************************************
close the project
*********************************************************************************

* I close all files
* I click in the terminal_, then use :kbd:`q` to leave the tests
* I `change directory`_ to the parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that

* I can use `Flask`_ with TDD
* I can make routes, handle forms, and integrate the existing calculator
* Error messages from the calculator appear nicely in the browser
* The website reuses all the hard work from chapters 1-8

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 9: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* how to make a test driven development environment
* how to build a full calculator with TDD
* how to turn it into a website with Flask

:ref:`Would you like to deploy the website?<how to deploy a flask app>` or add a database for calculation history?

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->