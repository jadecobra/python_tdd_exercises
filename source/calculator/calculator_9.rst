.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator website. This tutorial covers Flask, templates, forms, and integrating your existing TDD calculator.
  :keywords: Jacob Itegboje, python tdd calculator website, flask tdd tutorial, python flask calculator project, test driven development flask example, python web calculator, flask beginner tutorial, python tdd web app

.. include:: ../links.rst

.. _bytes object: bytes_
.. _bytes objects: bytes_
.. _Flask: https://flask.palletsprojects.com/en/stable/
.. _HTTP status code: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
.. _404 Not Found: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/404
.. _200 OK: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200
.. _jinja2.exceptions.TemplateNotFound: https://jinja.palletsprojects.com/en/stable/api/#jinja2.TemplateNotFound
.. _assertIn method: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn
.. _unittest.TestCase.assertIn method: `assertIn method`_
.. _decode method: https://docs.python.org/3/library/stdtypes.html#bytes.decode
.. _bytes.decode: https://docs.python.org/3/library/stdtypes.html#bytes.decode
.. _HTTP request methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
.. _HTTP request method: `HTTP request methods`_
.. _GET request method: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET
.. _POST request method: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST
.. _sys.path: https://docs.python.org/3/library/sys.html#sys.path
.. _system path: `sys.path`_
.. _HTML forms: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms

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
  - the ``get`` :ref:`method<what is a function?>` calls the `GET request method`_ which is an `HTTP request method`_ to get information from a server
  - ``client.get('/')`` returns a :ref:`response object<what is a class?>`
  - ``'/'`` is short for root or home in this case, the homepage of the website I am making also known as ``index.html``
  - ``response.status_code`` gets the ``status_code`` :ref:`attribute<test_attribute_error_w_class_attributes>` or the :ref:`response object<what is a class?>`
  - the above can also be written as ``src.website.app.test_client().get('/').status_code``
  - ``404`` is `HTTP status code`_, it is short for `404 Not Found`_ which means the page cannot be found
  - I want a ``200`` `HTTP status code`_, it is short for `200 OK`_ and means the request was successful

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

  - ``@app.route`` is a :ref:`decorator function<what is a decorator function?>` that routes the pages of the website to the :ref:`function<what is a function?>` it :ref:`wraps<what is a decorator function?>`
  - ``'/'`` is short for root or home in this case, the homepage of the website I am making also known as ``index.html``

* I add `jinja2.exceptions.TemplateNotFound`_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :emphasize-lines: 6
    :emphasize-text: jinja2.exceptions.TemplateNotFound

    # Exceptions seen
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # AssertionError
    # jinja2.exceptions.TemplateNotFound

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
    :emphasize-lines: 5-8

        def test_home_page(self):
            client = src.website.app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.data,
                '<h1>Calculator</h1>'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: b'' != '<h1>Calculator</h1>'

  - there is nothing in ``src/templates/index.html``
  - ``b''`` is the empty `bytes object`_
  - `bytes objects`_ are like strings_ , they have a ``b`` before the :ref:`quotes`, for example

    .. code-block:: python

      b'single quote bytes'
      b'''triple single quote bytes'''
      b"double quote bytes"
      b"""triple double quote bytes"""

* I open ``index.html`` from the ``templates`` folder_ in the :ref:`editor<2 editors>`, then add some HTML_

  .. code-block:: HTML
    :linenos:
    :emphasize-lines: 1

    <h1>Calculator</h1>

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` because `pytest-watcher`_ only checks my :ref:`Python files<what is a module?>`, it does not run the tests when I change other files_

  - ``<></>`` are called tags, they are :ref:`enclosures`
  - ``<h1>HEADING</h1>`` tells the computer to make ``HEADING`` a heading

* I go back to ``test_calculator_website.py`` and use :kbd:`ctrl+s` on the keyboard to run the test, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: b'<h1>Calculator</h1>' != '<h1>Calculator</h1>'

* I make the expectation a `bytes object`_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertEqual(
                response.data,
                b'<h1>Calculator</h1>'
            )

  the test passes

* I go back to the browser and click ``refresh``, it shows ``Calculator``

  .. image:: /_static/calculator/calculator_heading.png
    :width: 600
    :align: center
    :alt: Calculator Header

  Yes! I know how to make a website with Python_!!

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
  :emphasize-lines: 10-19

        def test_home_page(self):
            client = src.website.app.test_client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.data.decode(),
                '<h1>Calculator</h1>'
            )

        def test_calculation(self):
            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': 0,
                    'second_input': 1,
                }
            )
            self.assertEqual(response.status_code, 200)


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 404 != 200

this is like :ref:`AttributeError<what causes AttributeError?>`, the address for ``calculate`` does not exist yet.

* ``client.post`` calls the ``post`` :ref:`method<what is a function?>`
* which calls the `POST request method`_, an `HTTP request method`_ that sends information to a server. I am using it to test sending numbers to the website to do a calculation
* the ``post`` :ref:`method<what is a function?>` is called with 2 inputs in this case

  - ``'/calculate'`` - the path to the :ref:`function<what is a function?>` in ``website.py``
  - ``data`` - a :ref:`dictionary<what is a dictionary?>` with the inputs I want the :ref:`function<what is a function?>` to process

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a new :ref:`function<what is a function?>` to ``website.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-9, 11-15

      @app.route('/')
      def home():
          return flask.render_template('index.html')


      @app.route('/calculate', methods=['POST'])
      def calculate():
          first_input = flask.request.form.get('first_input')
          second_input = flask.request.form.get('second_input')

          result = calculator.add(first_input, second_input)
          return (
              f'<h2>{first_input} + {second_input} '
              f'= {result}</h2>'
          )

  - ``@app.route`` is a :ref:`decorator function<what is a decorator function?>` that routes the pages of the website to the :ref:`function<what is a function?>` it :ref:`wraps<what is a decorator function?>`
  - ``'/calculate'`` is the route I want to point to the ``calculate`` :ref:`function<what is a function?>`
  - ``['POST']`` is a :ref:`list<what is a list?>` of `HTTP request methods`_ that I can send, in this case I am using the `POST request method`_ to send information to the server
  - ``flask.request.form.get(NAME)`` uses the :ref:`get method<test_get_value_of_a_key_in_a_dictionary>` to get the :ref:`value<test_values_of_a_dictionary>` of the ``NAME`` :ref:`key<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>` when the user makes a request
  - ``<h2>SMALLER HEADING</h2>`` tells the computer to make ``SMALLER HEADING`` a heading that is smaller than ``h1`` headings

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'calculator' is not defined. Did you mean: 'calculate'?

* I add an `import statement`_ for the ``calculator`` :ref:`module<what is a module?>` at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import calculator
    import flask

  the terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'calculator

  because the test cannot find the ``calculator.py`` :ref:`module<what is a module?>`

* I change the `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.calculator
    import flask

  the test passes and the terminal_ for the website shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src'

  this is a problem

  - ``website.py`` is in the ``src`` folder_ with ``calculator.py`` so ``import src.calculator`` will not work for the website
  - ``test_calculator_website.py`` is in the ``tests`` folder_ so ``import calculator`` will not work for the tests

  I need a way that allows both the tests and website to work

* I change the `import statement`_ back

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import calculator
    import flask

  the terminal_ shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'calculator'

* I add an `import statement`_ for the `sys module`_, it is part of `The Python Standard Library`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import sys

    import calculator
    import flask

  I can use sys_ to get :ref:`variables<what is a variable?>` that the computer uses without going to the terminal_

* I add another `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import pathlib
    import sys

    import calculator
    import flask

  - the `pathlib module`_ is also part of `The Python Standard Library`_
  - I can use it to get paths(addresses) for files_ and folders_ on the computer without going to the terminal_

* I use pathlib_ to add the path for ``calculator.py`` to the `system path`_ which is a :ref:`list<what is a list?>` of strings_ where Python_ looks for :ref:`modules<what is a module?>` when I write an `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-5

    import pathlib
    import sys
    sys.path.insert(
        0, str(pathlib.Path(__file__).resolve().parent)
    )

    import calculator
    import flask

  the test passes and the terminal_ for the browser shows no errors

  - the path to ``calculator.py`` is now correct for ``website.py`` and ``test_calculator.py``
  - ``sys.path.insert`` uses the :ref:`insert method of lists<test_insert_item_at_position_in_a_list>` to place the ``src`` folder_ as the first item in the :ref:`list<what is a list?>` for Python_ to look for :ref:`modules<what is a module?>`
  - ``pathlib.Path(__file__).resolve().parent`` returns the parent of the current file - ``src`` in this case
  - ``__file__`` is a variable with the name of the file ``website.py`` in this case
  - the route to ``/calculate`` now exists

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to make sure I get the right result back in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 11

        def test_calculations(self):
            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': 0,
                    'second_input': 1,
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, 'BOOM!!!')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: b'<h2>0 + 1 = brmph?! Numbers only. Try again...</h2>' != 'BOOM!!!'

  Ah! The calculator only works with numbers. The numbers I sent as values in the test ``0`` and ``1`` are getting converted to something the :ref:`calculator<how to make a calculator>` does not like

* I change ``first_input`` to a float_ in ``website.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4

    @app.route('/calculate', methods=['POST'])
    def calculate():
        first_input = flask.request.form.get('first_input')
        first_input = float(first_input)
        second_input = flask.request.form.get('second_input')

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +: 'float' and 'str'

* I change ``second_input`` to a float_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6

    @app.route('/calculate', methods=['POST'])
    def calculate():
        first_input = flask.request.form.get('first_input')
        first_input = float(first_input)
        second_input = flask.request.form.get('second_input')
        second_input = float(second_input)

        result = calculator.add(first_input, second_input)
        return (
            f'<h2>{first_input} + {second_input} '
            f'= {result}</h2>'
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: b'<h2>0.0 + 1.0 = 1.0</h2>' != 'BOOM!!!'

* I copy the result from the terminal_ and paste it in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 11-14

        def test_calculations(self):
            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': 0,
                    'second_input': 1,
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.data,
                b'<h2>0.0 + 1.0 = 1.0</h2>'
            )

  the test passes

* I want to use random numbers in the test. I add an `import statement`_ for the ``test_calculator`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import src.website
    import tests.test_calculator
    import unittest

* I point a :ref:`variable<what is a variable?>` to the result of a call to the ``a_random_number`` :ref:`function<what is a function?>` of ``test_calculator``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

        def test_calculations(self):
            x = tests.test_calculator.a_random_number()
            client = src.website.app.test_client()

* I use the new :ref:`variable<what is a variable?>` as the first input

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-5

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

    AssertionError: b'<h2>ABC.DEFGHIJKLMNOP + 1.0 = ABQ.DEFGHIJKLMNOP</h2>' != b'<h2>0.0 + 1.0 = 1.0</h2>'

  good, the input gets to the website

* I try an `f-string`_ so I can use the :ref:`variable<what is a variable?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

            self.assertEqual(
                response.data,
                fb'<h2>0.0 + 1.0 = 1.0</h2>'
            )

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot make a `bytes object`_ an `f-string`_

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 7
    :emphasize-text: SyntaxError

    # Exceptions seen
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # AssertionError
    # jinja2.exceptions.TemplateNotFound
    # SyntaxError

----

*********************************************************************************
how to change a bytes object to a string
*********************************************************************************

* I change the `bytes object`_ to a string_ with `bytes.decode`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

            self.assertEqual(
                response.data.decode(),
                f'<h2>0.0 + 1.0 = 1.0</h2>'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<h2>RS.TUVWXYZABCDEFG + 1.0 = RH.TUVWXYZABCDEFG</h2>' != '<h2>0.0 + 1.0 = 1.0</h2>'

  - ``response.data.decode()`` returns the result of calling the `decode method`_ of the ``data`` :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``response`` :ref:`object<what is a class?>`
  - the `decode method`_ is part of the bytes_ data type, it converts bytes_ to strings_

* I add the :ref:`variable<what is a variable?>` to the expectation

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

            self.assertEqual(
                response.data.decode(),
                f'<h2>{x} + 1.0 = {x+1}</h2>'
            )

  the test passes

----

* I add another :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3

        def test_calculations(self):
            x = tests.test_calculator.a_random_number()
            y = tests.test_calculator.a_random_number()
            client = src.website.app.test_client()

* I use the :ref:`variable<what is a variable?>` for the second input

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 6-7

            response = client.post(
                '/calculate',
                data={
                    # 'first_input': 0,
                    'first_input': x,
                    # 'second_input': 1,
                    'second_input': y,
                }
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<h2>HIJ.KLMNOPQRSTUVWX + YZA.BCDEFGHIJKLMNOP = QRS.TUVWXYZABCDEFG</h2>' != '<h2>-HIJ.KLMNOPQRSTUVWX + 1.0 = HIY.KLMNOPQRSTUVWX</h2>'

* I add ``y`` to the `f-string`_ in the expectation

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

            self.assertEqual(
                response.data.decode(),
                f'<h2>{x} + {y} = {x+y}</h2>'
            )

  the test passes

* I remove the comments

  .. code-block:: python
    :lineno-start: 17

        def test_calculations(self):
            x = tests.test_calculator.a_random_number()
            y = tests.test_calculator.a_random_number()
            client = src.website.app.test_client()
            response = client.post(
                '/calculate',
                data={
                    'first_input': x,
                    'second_input': y,
                }
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.data.decode(),
                f'<h2>{x} + {y} = {x+y}</h2>'
            )

  the test is still green

* I want to test the other operations. I add a :ref:`dictionary<what is a dictionary?>` for the operations

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-10

        def test_calculations(self):
            x = tests.test_calculator.a_random_number()
            y = tests.test_calculator.a_random_number()

            operations = {
                'add': '+',
                'subtract': '-',
                'divide': '/',
                'multiply': '*',
            }

            client = src.website.app.test_client()

* I add a :ref:`for loop<what is a for loop?>` to the test

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-16

            client = src.website.app.test_client()

            for operation in operations:
                with self.subTest(operation=operation):
                    response = client.post(
                        '/calculate',
                        data={
                            'first_input': x,
                            'second_input': y,
                        }
                    )
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(
                        response.data.decode(),
                        f'<h2>{x} + {y} = {x+y}</h2>'
                    )


    # Exceptions seen

* I add a :ref:`key<test_keys_of_a_dictionary>` to the ``data`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 6

                    response = client.post(
                        '/calculate',
                        data={
                            'first_input': x,
                            'second_input': y,
                            'operation': operation,
                        }
                    )

* I add a :ref:`variable<what is a variable?>` for the :ref:`calculator function<how to make a calculator>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 3-5

                    self.assertEqual(response.status_code, 200)

                    function = src.calculator.__getattribute__(
                        operation
                    )
                    self.assertEqual(
                        response.data.decode(),
                        f'<h2>{x} + {y} = {x+y}</h2>'
                    )

* I add another :ref:`variable<what is a variable?>` for the expected result

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

                    function = src.calculator.__getattribute__(
                        operation
                    )
                    result = function(x, y)
                    self.assertEqual(
                        response.data.decode(),
                        f'<h2>{x} + {y} = {x+y}</h2>'
                    )

* I change the expectation in the :ref:`assertion<what is an assertion?>` to use the new :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-7

                    self.assertEqual(
                        response.data.decode(),
                        # f'<h2>{x} + {y} = {x+y}</h2>'
                        (
                            f'<h2>{x} {operations[operation]} {y} '
                            f'= {result}</h2>'
                        )
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<h2>YZA.BCDEFGHIJKLMNO + PQR.STUVWXYZABCDEFG = HIJ.KLMNOPQRSTUVWXY</h2>' != '<h2>YZA.BCDEFGHIJKLMNO * PQR.STUVWXYZABCDEFG = ZABCD.EFGHIJKLMNO</h2>'

  - the subtest for :ref:`addition<test_addition>` passes
  - the operation symbols for the other 3 functions and their results changed

* I add a :ref:`variable<what is a variable?>` for value the test passes for the operation

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7

    @app.route('/calculate', methods=['POST'])
    def calculate():
        first_input = flask.request.form.get('first_input')
        first_input = float(first_input)
        second_input = flask.request.form.get('second_input')
        second_input = float(second_input)
        operation = flask.request.form.get('operation')

        result = calculator.add(first_input, second_input)

  the test still shows :ref:`AssertionError<what causes AssertionError?>` for the 3 sub tests

* I add a :ref:`dictionary<what is a dictionary?>` for the operations

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-8

        operation = flask.request.form.get('operation')

        operations = {
            'add': '+',
            'subtract': '-',
            'divide': '/',
            'multiply': '*',
        }

        result = calculator.add(first_input, second_input)

* I use the ``__getattribute__`` :ref:`method<what is a function?>` for the result

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1-4

        # result = calculator.add(first_input, second_input)
        result = calculator.__getattribute__(operation)(
            first_input, second_input
        )
        return (
            f'<h2>{first_input} + {second_input} '
            f'= {result}</h2>'
        )

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

        return (
            # f'<h2>{first_input} + {second_input} '
            f'<h2>{first_input} {operations[operation]} {second_input} '
            f'= {result}</h2>'
        )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

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

  the test is still green

* I remove the comments from :ref:`test_calculations` in ``test_calculator_website.py``

  .. code-block:: python
    :lineno-start: 17

        def test_calculations(self):
            x = tests.test_calculator.a_random_number()
            y = tests.test_calculator.a_random_number()

            operations = {
                'add': '+',
                'subtract': '-',
                'divide': '/',
                'multiply': '*',
            }

            client = src.website.app.test_client()

            for operation in operations:
                with self.subTest(operation=operation):
                    response = client.post(
                        '/calculate',
                        data={
                            'first_input': x,
                            'second_input': y,
                            'operation': operation,
                        }
                    )
                    self.assertEqual(response.status_code, 200)

                    function = src.calculator.__getattribute__(
                        operation
                    )
                    result = function(x, y)
                    self.assertEqual(
                        response.data.decode(),
                        (
                            f'<h2>{x} {operations[operation]} {y} '
                            f'= {result}</h2>'
                        )
                    )


    # Exceptions seen

----

*********************************************************************************
how to make a form
*********************************************************************************

`HTML Forms`_ are the most popular thing we see with websites, we use them when we sign in or put any information on a website. I can add a form to the website for users to do calculations since the route now exists.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add more HTML_ to ``index.html`` in the ``templates`` folder_ in the ``src`` folder_

  .. code-block:: HTML
    :lineno-start: 1
    :emphasize-lines: 2-3

      <h1>Calculator</h1>
      <form method="post" action="/calculate">
      </form>

  - ``<form></form>`` is an HTML_ tag (:ref:`enclosure<enclosures>`) for making forms
  -  ``method="post"`` means the form will use the `POST request method`_
  -  ``action="/calculate"`` means the form will send the data to the ``calculate`` :ref:`function<what is a function?>` in ``website.py``

* I go to the website and click refresh, there is no change
* I click on ``test_calculator_website.py`` and use :kbd:`ctrl+s` on the keyboard to run the tests again, the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: b'<h1>Calculator</h1>\n<form method="post" action="/calculate">\n</form>' != b'<h1>Calculator</h1>'

  my change made :ref:`test_home_page` fail because there is now more HTML_ on that page

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the assertion to look for the title and not the entire page

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 5-7

      def test_home_page(self):
          client = src.website.app.test_client()
          response = client.get('/')
          self.assertEqual(response.status_code, 200)
          self.assertIn(
              b'<h1>Calculator</h1>',
              response.data
          )

      def test_calculations(self):

the test passes because the `assertIn method`_ of the `unittest.TestCase class`_ checks if the thing on the left is in the :ref:`object<what is a class?>` on the right

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add more HTML_ to ``index.html`` in the ``templates`` folder_ in the ``src`` folder_

  .. code-block:: HTML
    :lineno-start: 2
    :emphasize-lines: 2

    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
    </form>

* I go to the browser and click refresh to see the change, the website has a place where I can put numbers or use the up and down arrows to change the numbers

  .. image:: /_static/calculator/calculator_first_input.png
    :width: 600
    :align: center
    :alt: Calculator form with first input

* I use :kbd:`ctrl+s` on the keyboard in ``test_calculator_website.py`` to run the tests, still green

* I add another input for the second number in ``index.html``

  .. code-block:: HTML
    :lineno-start: 2
    :emphasize-lines: 3

    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
        <input type="number" name="second_input" required>
    </form>

* I go to the browser and click refresh to see the change, the website now has 2 places for me to put numbers

  .. image:: /_static/calculator/calculator_second_input.png
    :width: 600
    :align: center
    :alt: Calculator form with second input

* I use :kbd:`ctrl+s` on the keyboard in ``test_calculator_website.py`` to run the tests, green

* I add options for the operation in ``index.html``

  .. code-block:: HTML
    :lineno-start: 2
    :emphasize-lines: 4-6

    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
        <input type="number" name="second_input" required>
        <select name="operation">
            <option value="add">+</option>
        </select>
    </form>

* I go to the browser and click refresh to see the change, the website now has a place for me to choose the operation, even though ``+`` is the only option

  .. image:: /_static/calculator/calculator_first_operation.png
    :width: 600
    :align: center
    :alt: Calculator form with first operation

* I use :kbd:`ctrl+s` on the keyboard in ``website.py`` to run the tests, they are still green

* I want the operation to show up between the 2 numbers, I change the order in ``index.html``

  .. code-block:: HTML
    :lineno-start: 2
    :emphasize-lines: 3-6

    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
        <select name="operation">
            <option value="add">+</option>
        </select>
        <input type="number" name="second_input" required>
    </form>

* I go to the browser and click refresh to see the change, the operation is now between the 2 numbers

  .. image:: /_static/calculator/calculator_first_operation_reorder.png
    :width: 600
    :align: center
    :alt: Calculator form with first operation redordered

* I use :kbd:`ctrl+s` on the keyboard in ``website.py`` to run the tests. Green

* I add the other operations to ``index.html``

  .. code-block:: HTML
    :lineno-start: 2
    :emphasize-lines: 5-7

    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="divide">/</option>
            <option value="multiply">*</option>
        </select>
        <input type="number" name="second_input" required>
    </form>

  the browser shows all the options when I click refresh

* I add a button to the form so the user can submit the numbers and operation for a calculation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11

    <h1>Calculator</h1>
    <form method="post" action="/calculate">
        <input type="number" name="first_input" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="divide">/</option>
            <option value="multiply">*</option>
        </select>
        <input type="number" name="second_input" required>
        <button type="submit">calculate</button>
    </form>

* I go to the browser and click refresh to see the change

  .. image:: /_static/calculator/calculator_submit_button.png
    :width: 600
    :align: center
    :alt: Calculator form with calculate button

* I enter ``10000`` as the first number and ``20000`` as the second number, with ``*`` as the operation

  .. image:: /_static/calculator/calculator_first_calculation.png
    :width: 600
    :align: center
    :alt: Calculator form first calculation

  I click ``calculate`` and the browser shows

  .. image:: /_static/calculator/calculator_first_result.png
    :width: 600
    :align: center
    :alt: Calculator first result

ugly and it works

----

*********************************************************************************
test_error_handling_in_web
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

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