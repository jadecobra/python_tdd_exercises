.. include:: calculator_links.rst

#################################################################################
how to make a calculator 10: part 2
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_streamlit_calculator_2.py
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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 10 items

    tests/test_calculator.py .....                                [ 50%]
    tests/test_calculator_website.py ...                          [ 80%]
    tests/test_streamlit_calculator.py ..                         [100%]

    ======================== 10 passed in X.YZs =========================

* I open another terminal_ then use uv_ in the ``calculator`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    uv run streamlit run src/streamlit_calculator.py

  the terminal_ shows

  .. code-block:: shell

    Collecting usage statistics.
    To deactivate, set browser.gatherUsageStats to false.


      You can now view your Streamlit app in your browser.

      Local URL: http://localhost:8501
      Network URL: http://ABC.DEF.GHI.JKL:8501
      External URL: http://MNO.PQR.STU.VWX:8501

  I use :kbd:`ctrl/option` on the keyboard and click on ``http://localhost:8501`` with the mouse to open the browser and it shows

  .. image:: /_static/calculator/streamlit/display.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Display

----

*********************************************************************************
test_streamlit_calculator_buttons
*********************************************************************************

I want to add buttons for the numbers and operations.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

-----

* I hold :kbd:`ctrl/command` on the keyboard and click on ``tests/test_streamlit_calculator.py`` with the mouse to open it in the :ref:`editor<2 editors>`

* I add a new test with an :ref:`assertion<what is an assertion?>` for the first button, in ``test_streamlit_calculator.py``

  .. NOTE:: ``<-`` is :kbd:`<+-` on the keyboard

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 17-21, 23

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            display = (
                tester.main.children[1].proto
                      .flex_container
            )
            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, 1)
            self.assertTrue(display.border)

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            self.assertIsNone(tester.button('<-'))


    # Exceptions seen

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '<-'

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 6
    :emphasize-text: KeyError

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError
    # SyntaxError
    # KeyError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a button in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        streamlit.button('<-')

  the terminal_ still shows :ref:`KeyError<test_key_error>`

* `streamlit buttons`_ have a key parameter. I add it

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1
    :emphasize-text: key

        streamlit.button('<-', key='<-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Button(key='<-', label='<-') is not None

  the ``Button`` :ref:`object<what is a class?>` has two keys - ``key`` and ``label``

* I change the :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1
    :emphasize-text: label

            self.assertIsNone(tester.button('<-').label)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<-' is not None

* I add ``<-`` as the expectation

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            self.assertIsNone(tester.button('<-').label, '<-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<-' is not None : <-

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1
    :emphasize-text: assertEqual

            self.assertEqual(tester.button('<-').label, '<-')

  the test passes

* I go to the browser, click refresh

  .. image:: /_static/calculator/streamlit/no_column_first_button.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit First Button no column

  I see the button I just added

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the label parameter to the button in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5
    :emphasize-text: label

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        streamlit.button(label='<-', key='<-')

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for the next button, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            self.assertEqual(tester.button('<-').label, '<-')
            self.assertEqual(tester.button('7').label, '7')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '7'

* I add the button to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

        streamlit.button(label='<-', key='<-')
        streamlit.button(label='7', key='7')

  the test passes

* I click refresh in the browser

  .. image:: /_static/calculator/streamlit/no_column_second_button.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Second Button no column

  the second button is there

* I add a :ref:`for loop<what is a for loop?>` for all the buttons, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 7-14, 16-17

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            for key in (
                '<-', '7', '4', '1', '+/-',
                'C', '8', '5', '2', '0',
                'AC', '9', '6', '3', '.',
                '/', 'X', '-', '+', '=',
            ):
                with self.subTest(key=key):
                    self.assertEqual(tester.button(key).label, key)

            self.assertEqual(tester.button('<-').label, '<-')
            self.assertEqual(tester.button('7').label, '7')

  the terminal_ shows :ref:`KeyError<test_key_error>` for 18 sub tests

  .. code-block:: python

    ================== 18 failed, 11 passed in X.YZs ===================

* I add the buttons to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-9, 11-15, 17-21, 23-27

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        streamlit.button(label='<-', key='<-')
        streamlit.button(label='7', key='7')
        streamlit.button(label='4', key='4')
        streamlit.button(label='1', key='1')
        streamlit.button(label='+/-', key='+/-')

        streamlit.button(label='C', key='C')
        streamlit.button(label='8', key='8')
        streamlit.button(label='5', key='5')
        streamlit.button(label='2', key='2')
        streamlit.button(label='0', key='0')

        streamlit.button(label='AC', key='AC')
        streamlit.button(label='9', key='9')
        streamlit.button(label='6', key='6')
        streamlit.button(label='3', key='3')
        streamlit.button(label='.', key='.')

        streamlit.button(label='/', key='/')
        streamlit.button(label='X', key='X')
        streamlit.button(label='-', key='-')
        streamlit.button(label='+', key='+')
        streamlit.button(label='=', key='=')


    if __name__ == '__main__':

  the test passes

* I make a :ref:`function<what is a function?>` to make the buttons

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-9, 11-15, 17-21, 23-27

    import streamlit


    def add_buttons():
        streamlit.button(label='<-', key='<-')
        streamlit.button(label='7', key='7')
        streamlit.button(label='4', key='4')
        streamlit.button(label='1', key='1')
        streamlit.button(label='+/-', key='+/-')

        streamlit.button(label='C', key='C')
        streamlit.button(label='8', key='8')
        streamlit.button(label='5', key='5')
        streamlit.button(label='2', key='2')
        streamlit.button(label='0', key='0')

        streamlit.button(label='AC', key='AC')
        streamlit.button(label='9', key='9')
        streamlit.button(label='6', key='6')
        streamlit.button(label='3', key='3')
        streamlit.button(label='.', key='.')

        streamlit.button(label='/', key='/')
        streamlit.button(label='X', key='X')
        streamlit.button(label='-', key='-')
        streamlit.button(label='+', key='+')
        streamlit.button(label='=', key='=')

    def main():

* I call the new :ref:`function<what is a function?>` in ``main``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)
        add_buttons()

        streamlit.button('<-', key='<-')

  the test is still passing

* the second terminal_ (for the streamlit_ application) shows ``streamlit.errors.StreamlitDuplicateElementKey``

  .. code-block:: python

    streamlit.errors.StreamlitDuplicateElementKey:
    There are multiple elements with the same key='<-'.
    To fix this, please make sure that the key argument is unique for each element you create.

* I add ``streamlit.errors.StreamlitDuplicateElementKey`` to the list of :ref:`Exceptions<errors>` seen, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 7
    :emphasize-text: streamlit.errors.StreamlitDuplicateElementKey

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError
    # SyntaxError
    # KeyError
    # streamlit.errors.StreamlitDuplicateElementKey

* I check the browser and see all the buttons and the :ref:`Exception<errors>`

* I remove the buttons from ``main`` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 30

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)
        add_buttons()


    if __name__ == '__main__':
        main()

  the test is still green

* The second terminal_ still shows ``streamlit.errors.StreamlitDuplicateElementKey``

* I check the browser

  .. image:: /_static/calculator/streamlit/no_column_all_buttons.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit No Column All Buttons

  I see all the buttons, and problems

  - all the buttons are in one column, simple calculators have 4 columns - 3 for numbers and 1 for operations
  - 2 buttons are missing - addition and subtraction
  - the buttons have different sizes

* I remove the other two :ref:`assertions<what is an assertion?>` from :ref:`test_streamlit_calculator_buttons` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 30

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            for key in (
                '<-', '7', '4', '1', '+/-',
                'C', '8', '5', '2', '0',
                'AC', '9', '6', '3', '.',
                '/', 'X', '-', '+', '=',
            ):
                with self.subTest(key=key):
                    self.assertEqual(tester.button(key).label, key)


    # Exceptions seen

* before I continue, there is some repetition to remove. Each test makes the same `streamlit tester object`_. I add it to the `setUp method`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-7

    class TestStreamlitCalculator(unittest.TestCase):

        def setUp(self):
            self.tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            self.tester.run()

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_streamlit_calculator_title`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7
    :emphasize-text: tester

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            # self.assertEqual(tester.title[0].value, 'Calculator')
            self.assertEqual(self.tester.title[0].value, 'Calculator')

  the test is still green

* I remove the other lines from :ref:`test_streamlit_calculator_title`

  .. code-block:: python
    :lineno-start: 13

        def test_streamlit_calculator_title(self):
            self.assertEqual(self.tester.title[0].value, 'Calculator')

        def test_streamlit_calculator_display(self):

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_streamlit_calculator_display`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 8-9
    :emphasize-text: tester

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            display = (
                # tester.main.children[1].proto
                self.tester.main.children[1].proto
                    .flex_container
            )
            self.assertEqual(display.gap_config.gap_size, 1)

  still green

* I remove the commented line, ``tester`` :ref:`variable<what is a variable?>` and call to ``tester.run()`` from :ref:`test_streamlit_calculator_display`

  .. code-block:: python
    :lineno-start: 16

        def test_streamlit_calculator_display(self):
            display = (
                self.tester.main.children[1].proto
                    .flex_container
            )
            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, 1)
            self.assertTrue(display.border)

        def test_streamlit_calculator_buttons(self):

* I do the same thing in :ref:`test_streamlit_calculator_buttons`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 14-15
    :emphasize-text: tester

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            for key in (
                '<-', '7', '4', '1', '+/-',
                'C', '8', '5', '2', '0',
                'AC', '9', '6', '3', '.',
                '/', 'X', '-', '+', '=',
            ):
                with self.subTest(key=key):
                    # self.assertEqual(tester.button(key).label, key)
                    self.assertEqual(self.tester.button(key).label, key)

  green

* I remove the commented line, ``tester`` :ref:`variable<what is a variable?>` and call to ``tester.run()`` from :ref:`test_streamlit_calculator_buttons`

  .. code-block:: python
    :lineno-start: 27

        def test_streamlit_calculator_buttons(self):
            for key in (
                '<-', '7', '4', '1', '+/-',
                'C', '8', '5', '2', '0',
                'AC', '9', '6', '3', '.',
                '/', 'X', '-', '+', '=',
            ):
                with self.subTest(key=key):
                    self.assertEqual(self.tester.button(key).label, key)


    # Exceptions seen

  on to columns

----

*********************************************************************************
test_streamlit_calculator_columns_and_buttons
*********************************************************************************

Calculator buttons are arranged in Columns and Rows. I can use `streamlit columns`_ to arrange the buttons.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to make sure the Calculator has 4 columns

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 4-5

              with self.subTest(key=key):
                  self.assertEqual(self.tester.button(key).label, key)

      def test_streamlit_calculator_columns(self):
          self.assertEqual(len(self.tester.columns), 4)


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 0 != 4

- ``len(self.tester.columns)`` returns the length of the columns object
- `streamlit columns`_ are :ref:`lists<what is a list?>` and I know how to work with :ref:`lists<what is a list>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add columns to the ``main`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 6

  def main():
      streamlit.title('Calculator')
      streamlit.container(border=True)
      add_buttons()

      streamlit.columns(4)


  if __name__ == '__main__':
      main()

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to check what is in the first column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            self.assertIsNone(self.tester.columns[0].children)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not None

* I add the expectation

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1

            self.assertIsNone(self.tester.columns[0].children, {})

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-6
    :emphasize-text: assertEqual { }

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            self.assertEqual(
                self.tester.columns[0].children, {}
            )

  the test passes

* I name the columns because I want to put buttons in them, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)
        add_buttons()

        column_1, column_2, column_3, operations = streamlit.columns(4)

  the test is still green

* I move the columns to the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        streamlit.button('<-', key='<-')
        streamlit.button('7', key='7')
        streamlit.button('4', key='4')
        streamlit.button('1', key='1')
        streamlit.button('+/-', key='+/-')

  still green

* I add the button for ``<-`` to the first column

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5
    :emphasize-text: column_1

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        # streamlit.button('<-', key='<-')
        column_1.button('<-', key='<-')
        streamlit.button('7', key='7')
        streamlit.button('4', key='4')
        streamlit.button('1', key='1')
        streamlit.button('+/-', key='+/-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: Button(key='<-', label='<-')} != {}

  good, the button is in the column and I know how to test buttons

* I change the :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator_columns`` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5-6

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            self.assertEqual(
                self.tester.columns[0].button('<-').label,
                ''
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<-' != ''

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 3

            self.assertEqual(
                self.tester.columns[0].button('<-').label,
                '<-'
            )

  the test passes

----

* I add a :ref:`for loop<what is a for loop?>` for all the buttons in the first column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-9

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for key in ('<-', '7', '4', '1', '+/-'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[0].button(key).label,
                        'BOOM!!!'
                    )

            self.assertEqual(
                self.tester.columns[0].button('<-').label,
                '<-'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the ``<-`` button

  .. code-block:: python

    SUBFAILED(key='<-') ... - AssertionError: '<-' != 'BOOM!!!'

  and :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='7') ... - KeyError: '7'
    SUBFAILED(key='4') ... - KeyError: '4'
    SUBFAILED(key='1') ... - KeyError: '1'
    SUBFAILED(key='+/-') ... - KeyError: '+/-'

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 3

                    self.assertEqual(
                        self.tester.columns[0].button(key).label,
                        key
                    )

  the terminal_ still shows :ref:`KeyError<test_key_error>`

* I remove the commented line in the ``add_buttons`` :ref:`function<what is a function?>` then move buttons to the first column in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-8
    :emphasize-text: column_1

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-')
        column_1.button('7', key='7')
        column_1.button('4', key='4')
        column_1.button('1', key='1')
        column_1.button('+/-', key='+/-')

        streamlit.button('C', key='C')

  the test passes

* I add a :ref:`function<what is a function?>` for the buttons in the first column

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-9

    import streamlit


    def add_buttons_to_column_1(column_1):
        column_1.button(label='<-', key='<-')
        column_1.button(label='7', key='7')
        column_1.button(label='4', key='4')
        column_1.button(label='1', key='1')
        column_1.button(label='+/-', key='+/-')


    def add_buttons():

* I call the new :ref:`function<what is a function?>` in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        column_1.button(label='<-', key='<-')

  the terminal_ shows :ref:`KeyError<test_key_error>` and ``streamlit.errors.StreamlitDuplicateElementKey``

* I remove the buttons for column 1 from the ``add_buttons`` :ref:`function<what is a function?>` since ``add_buttons_to_column_1`` now makes them

  .. code-block:: python
    :lineno-start: 12

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)

        streamlit.button(label='C', key='C')

  the test is green again

----

* I check the browser and the buttons still look the same

* I remove the :ref:`assertion<what is an assertion?>` after the :ref:`for loop<what is a for loop?>`, then add another :ref:`for loop<what is a for loop?>` for the second column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 11-16

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for key in ('<-', '7', '4', '1', '+/-'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[0].button(key).label,
                        key
                    )

            for key in ('<-', '7', '4', '1', '+/-'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )


    # Exceptions seen

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='<-') ... - KeyError: '<-'
    SUBFAILED(key='7') ... - KeyError: '7'
    SUBFAILED(key='4') ... - KeyError: '4'
    SUBFAILED(key='1') ... - KeyError: '1'
    SUBFAILED(key='+/-') ... - KeyError: '+/-'

* I move buttons to the second column in ``streamlit_calculator,py``

  .. code-block:: python
    :lineno-start: 2
    :emphasize-lines: 6-10
    :emphasize-text: column_2

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)

        column_2.button(label='C', key='C')
        column_2.button(label='8', key='8')
        column_2.button(label='5', key='5')
        column_2.button(label='2', key='2')
        column_2.button(label='0', key='0')

        streamlit.button(label='AC', key='AC')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='C') ... - KeyError: 'C'
    SUBFAILED(key='8') ... - KeyError: '8'
    SUBFAILED(key='5') ... - KeyError: '5'
    SUBFAILED(key='2') ... - KeyError: '2'
    SUBFAILED(key='0') ... - KeyError: '0'

* I use the keys for the second column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 1

            for key in ('C', '8', '5', '2', '0'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/2_columns.png
    :width: 600
    :align: left
    :alt: Calculator 2 Columns

  there is a second column of buttons. Progress! It does not look right yet, baby steps.

* I add a :ref:`function<what is a function?>` for adding buttons to the second column in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 9-14

    def add_buttons_to_column_1(column_1):
        column_1.button(label='<-', key='<-')
        column_1.button(label='7', key='7')
        column_1.button(label='4', key='4')
        column_1.button(label='1', key='1')
        column_1.button(label='+/-', key='+/-')


    def add_buttons_to_column_2(column_2):
        column_2.button(label='C', key='C')
        column_2.button(label='8', key='8')
        column_2.button(label='5', key='5')
        column_2.button(label='2', key='2')
        column_2.button(label='0', key='0')


    def add_buttons():

* I call ``add_buttons_to_column_2`` in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)

        column_2.button(label='C', key='C')

  the terminal_ shows :ref:`KeyError<test_key_error>` and ``streamlit.errors.StreamlitDuplicateElementKey``

* I remove the buttons for the second column from the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 20

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)

        streamlit.button(label='AC', key='AC')

  the test is green again

----

* I add a :ref:`for loop<what is a for loop?>` for the third column in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 8-13

            for key in ('C', '8', '5', '2', '0'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )

            for key in ('AC', '9', '6', '3', '.'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )


    # Exceptions seen

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='AC') ... - KeyError: 'AC'
    SUBFAILED(key='9') ... - KeyError: '9'
    SUBFAILED(key='6') ... - KeyError: '6'
    SUBFAILED(key='3') ... - KeyError: '3'
    SUBFAILED(key='.') ... - KeyError: '.'

* I change the column in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4
    :emphasize-text: 2

            for key in ('AC', '9', '6', '3', '.'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[2].button(key).label,
                        key
                    )

  the terminal_ still shows :ref:`KeyError<test_key_error>`

* I move buttons to the third column in the ``add_buttons`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 7-11
    :emphasize-text: column_3

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)

        column_3.button(label='AC', key='AC')
        column_3.button(label='9', key='9')
        column_3.button(label='6', key='6')
        column_3.button(label='3', key='3')
        column_3.button(label='.', key='.')

        streamlit.button(label='/', key='/')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/3_columns.png
    :width: 600
    :align: left
    :alt: Calculator 3 Columns

  3 columns

* I add a :ref:`function<what is a function?>` for adding buttons to the third column

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 9-14

    def add_buttons_to_column_2(column_2):
        column_2.button(label='C', key='C')
        column_2.button(label='8', key='8')
        column_2.button(label='5', key='5')
        column_2.button(label='2', key='2')
        column_2.button(label='0', key='0')


    def add_buttons_to_column_3(column_3):
        column_3.button(label='AC', key='AC')
        column_3.button(label='9', key='9')
        column_3.button(label='6', key='6')
        column_3.button(label='3', key='3')
        column_3.button(label='.', key='.')


    def add_buttons():

* I call the new :ref:`function<what is a a function?>` in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)

        column_3.button(label='AC', key='AC')

  the terminal_ shows :ref:`KeyError<test_key_error>` and ``streamlit.errors.StreamlitDuplicateElementKey``

* I remove the buttons for column 3 from the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)

        streamlit.button(label='/', key='/')

  the test is green again. On to the next one.

----

* I add a :ref:`for loop<what is a for loop?>` with an :ref:`assertion<what is an assertion?>` for the operations in the operations column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 8-13

            for key in ('AC', '9', '6', '3', '.'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[2].button(key).label,
                        key
                    )

            for key in ('/', 'X', '-', '+', '='):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[3].button(key).label,
                        key
                    )


    # Exceptions seen

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='/') ... - KeyError: '/'
    SUBFAILED(key='X') ... - KeyError: 'X'
    SUBFAILED(key='-') ... - KeyError: '-'
    SUBFAILED(key='+') ... - KeyError: '+'
    SUBFAILED(key='=') ... - KeyError: '='

* I move the buttons to the fourth column, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-7
    :emphasize-text: operations

        column_3.button('.', key='.')

        operations.button('/', key='/')
        operations.button('X', key='X')
        operations.button('-', key='-')
        operations.button('+', key='+')
        operations.button('=', key='=')


    def main():

  the test passes

* I look in the browser

  .. image:: /_static/calculator/streamlit/4_columns.png
    :width: 600
    :align: left
    :alt: Calculator 4 Columns

  there are 4 columns

* I add a :ref:`function<what is a function?>` to add buttons to the fourth column, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 9-14

    def add_buttons_to_column_3(column_3):
        column_3.button(label='AC', key='AC')
        column_3.button(label='9', key='9')
        column_3.button(label='6', key='6')
        column_3.button(label='3', key='3')
        column_3.button(label='.', key='.')


    def add_buttons_to_column_4(column_4):
        column_4.button(label='/', key='/')
        column_4.button(label='X', key='X')
        column_4.button(label='-', key='-')
        column_4.button(label='+', key='+')
        column_4.button(label='=', key='=')


    def add_buttons():

* I use ``add_buttons_to_column_4`` in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 7

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)

        operations.button(label='/', key='/')

  the terminal_ shows :ref:`KeyError<test_key_error>` and ``streamlit.errors.StreamlitDuplicateElementKey``

* I remove the buttons for the fourth column from the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 36

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)


    def main():

* I write the statements in the ``add_buttons`` :ref:`function<what is a function?>` in the ``main`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4, 6-10

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)
        # add_buttons()

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 365

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)


    if __name__ == '__main__':
        main()

* I remove the ``add_buttons`` :ref:`function<what is a function?>` because I no longer need it

  .. code-block:: python
    :lineno-start: 28

    def add_buttons_to_column_4(column_4):
        column_4.button(label='/', key='/')
        column_4.button(label='X', key='X')
        column_4.button(label='-', key='-')
        column_4.button(label='+', key='+')
        column_4.button(label='=', key='=')


    def main():

* I remove :ref:`test_streamlit_calculator_buttons` because ``test_streamlit_calculator_columns`` tests the same things - the button labels, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 16

        def test_streamlit_calculator_display(self):
            display = (
                self.tester.main.children[1].proto
                    .flex_container
            )
            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, 1)
            self.assertTrue(display.border)

        def test_streamlit_calculator_columns(self):

* I change the name of ``test_streamlit_calculator_columns`` to :ref:`test_streamlit_calculator_columns_and_buttons`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 12

        def test_streamlit_calculator_display(self):
            display = (
                self.tester.main.children[1].proto
                    .flex_container
            )
            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, 1)
            self.assertTrue(display.border)

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for key in ('<-', '7', '4', '1', '+/-'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[0].button(key).label,
                        key
                    )

            for key in ('C', '8', '5', '2', '0'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )

            for key in ('AC', '9', '6', '3', '.'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[2].button(key).label,
                        key
                    )

            for key in ('/', 'X', '-', '+', '='):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[3].button(key).label,
                        key
                    )


    # Exceptions seen

* All the :ref:`for loops<what is a for loop?>` in :ref:`test_streamlit_calculator_columns_and_buttons` look like this

  .. code-block:: python
    :emphasize-text: index key

    for key in (A, B, C, D, E):
        with self.subTest(key=key):
            self.assertEqual(
                self.tester.columns[index].button(key).label,
                key
            )

  I add 2 new :ref:`for loops<what is a for loop?>` that put all the for loops for testing the buttons together

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-19

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', '-', '+', '=')),
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key)
                                    .label
                            ),
                            'BOOM!!!'
                        )

            for key in ('<-', '7', '4', '1', '+/-'):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for 20 sub tests

  .. code-block:: python

    ================== 20 failed, 11 passed in X.YZs ===================

* I change the expectation

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7

                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key)
                                    .label
                            ),
                            key
                        )

  the test passes

* I remove the other :ref:`for loops<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 27

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', '-', '+', '=')),
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key)
                                    .label
                            ),
                            key
                        )


    # Exceptions seen

----

*********************************************************************************
how to change the size of streamlit buttons
*********************************************************************************

I want all the buttons to be the same size.

* `streamlit buttons`_ have a ``width`` option. I set it to ``stretch`` for the ``<-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2
    :emphasize-text: width

    def add_buttons_to_column_1(column_1):
        column_1.button(label='<-', key='<-', width='stretch')
        column_1.button(label='7', key='7')
        column_1.button(label='4', key='4')
        column_1.button(label='1', key='1')
        column_1.button(label='+/-', key='+/-')

  the test is still green

* I refresh the browser

  .. image:: /_static/calculator/streamlit/stretch_first_button.png
    :width: 600
    :align: left
    :alt: Calculator Stretched First

  better

* I stretch the rest of the buttons in the first column

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-6
    :emphasize-text: stretch

    def add_buttons_to_column_1(column_1):
        column_1.button(label='<-', key='<-', width='stretch')
        column_1.button(label='7', key='7')
        column_1.button(label='4', key='4')
        column_1.button(label='1', key='1')
        column_1.button(label='+/-', key='+/-')


    def add_buttons_to_column_2(column_2):

  still green

* I check the browser

  .. image:: /_static/calculator/streamlit/stretch_first_column.png
    :width: 600
    :align: left
    :alt: Calculator Stretched First Column

  all the buttons in the first column have the same size

* I stretch the buttons in the second column

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-6

    def add_buttons_to_column_2(column_2):
        column_2.button(label='C', key='C', width='stretch')
        column_2.button(label='8', key='8', width='stretch')
        column_2.button(label='5', key='5', width='stretch')
        column_2.button(label='2', key='2', width='stretch')
        column_2.button(label='0', key='0', width='stretch')


    def add_buttons_to_column_3(column_3):

  green

* I stretch the buttons in the third column

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-6

    def add_buttons_to_column_3(column_3):
        column_3.button(label='AC', key='AC', width='stretch')
        column_3.button(label='9', key='9', width='stretch')
        column_3.button(label='6', key='6', width='stretch')
        column_3.button(label='3', key='3', width='stretch')
        column_3.button(label='.', key='.', width='stretch')


    def add_buttons_to_column_4(column_4):

  still green

* I stretch the buttons in the fourth column

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-6

    def add_buttons_to_column_4(column_4):
        column_4.button(label='/', key='/', width='stretch')
        column_4.button(label='X', key='X', width='stretch')
        column_4.button(label='-', key='-', width='stretch')
        column_4.button(label='+', key='+', width='stretch')
        column_4.button(label='=', key='=', width='stretch')


    def main():

  the tests are still green

* I refresh the browser

  .. image:: /_static/calculator/streamlit/stretch_4_columns.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Stretch 4 Columns

  Good! The buttons all have the same size. I am still missing ``-`` and ``+`` that the tests says are there

----

*********************************************************************************
how to use raw strings and escape characters
*********************************************************************************

* I add ``r`` and ``\`` to escape the ``-`` character because it means something to streamlit_, which is why it does not show on the button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4

    def add_buttons_to_column_4(column_4):
        column_4.button(label='/', key='/', width='stretch')
        column_4.button(label='X', key='X', width='stretch')
        column_4.button(label=r'\-', key=r'\-', width='stretch')
        column_4.button(label='+', key='+', width='stretch')
        column_4.button(label='=', key='=', width='stretch')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '-'

* I change the ``-`` to ``r'\-'`` in :ref:`test_streamlit_calculator_columns_and_buttons` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 8-9

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                # (3, ('/', 'X', '-', '+', '=')),
                (3, ('/', 'X', r'\-', '+', '=')),
            ):
                for key in keys:

  the test passes

  - ``r`` makes this a raw string_ which means the characters are taken as they are, not what they stand for
  - ``\`` escapes the character  so that ``-`` is taken exactly as it is to show the character on the button. ``'-'`` means something different in streamlit_ so it does not show up as a label for the button

* I add ``r`` and ``\`` to escape the ``+`` character because it means something to streamlit_, which is why it does not show on the button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5

    def add_buttons_to_column_4(column_4):
        column_4.button(label='/', key='/', width='stretch')
        column_4.button(label='X', key='X', width='stretch')
        column_4.button(label=r'\-', key=r'\-', width='stretch')
        column_4.button(label=r'\+', key=r'\+', width='stretch')
        column_4.button(label='=', key='=', width='stretch')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '+'

* I change the ``+`` to ``r'\+'`` in :ref:`test_streamlit_calculator_columns_and_buttons` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 9-10

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                # (3, ('/', 'X', '-', '+', '=')),
                # (3, ('/', 'X', r'\-', '+', '=')),
                (3, ('/', 'X', r'\-', r'\+', '=')),
            ):
                for key in keys:

  the test passes

  - ``r`` makes this a raw string_ which means the characters are taken as they are, not what they stand for
  - ``\`` escapes the character  so that ``+`` is taken exactly as it is to show the character on the button. ``'+'`` means something different in streamlit_ so it does not show up as a label for the button

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 27

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', r'\-', r'\+', '=')),
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key)
                                    .label
                            ),
                            key
                        )


    # Exceptions seen

* I check the browser

  .. image:: /_static/calculator/streamlit/all_labels.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit All labels

  yes! The calculator shows all the labels.

----

*********************************************************************************
test_streamlit_calculator_operations_buttons
*********************************************************************************

I want to change the colors of the buttons in the ``operations`` column

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the ``type`` parameter of `streamlit buttons`_

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 21-22

        def test_streamlit_calculator_columns_and_buttons(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', r'\-', r'\+', '=')),
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key)
                                    .label
                            ),
                            key
                        )

        def test_streamlit_calculator_operations_buttons(self):
            self.assertEqual(self.tester.button('/').proto.type, '')


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'secondary' != ''

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 47
  :emphasize-lines: 2-5

        def test_streamlit_calculator_operations_buttons(self):
            self.assertEqual(
                self.tester.button('/').proto.type,
                'secondary'
            )

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation from ``secondary`` to ``primary``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3

            self.assertEqual(
                self.tester.button('/').proto.type,
                'primary'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'secondary' != 'primary'

* I use the ``type`` parameter of `streamlit buttons`_ to change the colors of the buttons for the ``/`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-4
    :emphasize-text: primary

    def add_buttons_to_column_4(column_4):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(label='X', key='X', width='stretch')
        column_4.button(label=r'\-', key=r'\-', width='stretch')
        column_4.button(label=r'\+', key=r'\+', width='stretch')
        column_4.button(label='=', key='=', width='stretch')

  the test passes

* I refresh the browser

  .. image:: /_static/calculator/streamlit/first_primary_button.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit First Primary Button

  good

* I add a :ref:`for loop<what is a for loop?>` for all the buttons in the operations column

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-7

        def test_streamlit_calculator_operations_buttons(self):
            for key in ('/', 'X', r'\-', r'\+', '='):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.button(key).proto.type,
                        'primary'
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='X') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='\\-') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='\\+') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='=') ... - AssertionError: 'secondary' != 'primary'

* I add the ``type`` parameter to the buttons in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-16
    :emphasize-text: primary

    def add_buttons_to_column_4(column_4):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
        )


    def main():

  the test passes

* I want the ``C`` and ``AC`` buttons to have the same colors as the buttons for the operations. I add them to the tuple_ in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

        def test_streamlit_calculator_operations_buttons(self):
            for key in ('/', 'X', r'\-', r'\+', '=', 'C', 'AC'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.button(key).proto.type,
                        'primary'
                    )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='C') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='AC') ... - AssertionError: 'secondary' != 'primary'

* I change the type for the ``AC`` button in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-4
    :emphasize-text: primary

    def add_buttons_to_column_3(column_3):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(label='9', key='9', width='stretch')
        column_3.button(label='6', key='6', width='stretch')
        column_3.button(label='3', key='3', width='stretch')
        column_3.button(label='.', key='.', width='stretch')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='C') ... - AssertionError: 'secondary' != 'primary'

* I change the type for the ``C`` button in the ``add_buttons_to_column_2`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-4
    :emphasize-text: primary

    def add_buttons_to_column_2(column_2):
        column_2.button(
            label='C', key='C', width='stretch', type='primary',
        )
        column_2.button(label='8', key='8', width='stretch')
        column_2.button(label='5', key='5', width='stretch')
        column_2.button(label='2', key='2', width='stretch')
        column_2.button(label='0', key='0', width='stretch')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/primary_buttons.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Primary Buttons

  much better

----

*********************************************************************************
how to show the numbers when I click on them
*********************************************************************************

I want the calculator to show the number when I press a button

* I add a :ref:`variable<what is a variable?>` to name the container so I can use it to show the numbers

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2

    def main():
        streamlit.title('Calculator')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)

* I add a :ref:`function<what is a function?>` to show the text of the button when it is clicked

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import streamlit


    def show(display, number):
        display.write(number)


    def add_buttons_to_column_1(column_1):

* `streamlit buttons`_ have an ``on_click`` parameter that lets me call a :ref:`function<what is a function?>` when a button is pressed. It also takes an argument named ``args`` where I can pass in the :ref:`positional arguments<test_functions_w_positional_arguments>` that the :ref:`function<what is a function?>` I give for the ``on_click`` parameter takes. I pass the :ref:`function<what is a function?>` and the ``display`` :ref:`variable<what is a variable?>` with a value as the arguments for the ``7`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3-6
    :emphasize-text: on_click args

    def add_buttons_to_column_1(column_1):
        column_1.button(label='<-', key='<-', width='stretch')
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(label='4', key='4', width='stretch')
        column_1.button(label='1', key='1', width='stretch')
        column_1.button(label='+/-', key='+/-', width='stretch')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    ================== 26 failed, 12 passed in A.BCs ===================

  the terminal_ for the application shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'display' is not defined

* I add a parameter for the ``display`` :ref:`variable<what is a variable?>` in the :ref:`function<what is a function?>` signature for ``add_buttons_to_column_1``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1

    def add_buttons_to_column_1(column_1, display):

  the terminal_ shows :ref:`KeyError<test_key_error>` for 27 sub tests and the terminal_ for the streamlit_ application shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add_buttons_to_column_1() missing 1 required positional argument: 'display'

* I add the ``display`` :ref:`variable<what is a variable?>` to the call to ``add_buttons_to_column_1`` in the ``main`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6

    def main():
        streamlit.title('Calculator')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)

  the test passes

* I go to the browser and click on the ``7`` button

  .. image:: /_static/calculator/streamlit/display_7.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Display 7 on click

  ``7`` shows on the display. Yes!

* I make the same change to the other numbers in the first column

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 7-18
    :emphasize-text: on_click args

    def add_buttons_to_column_1(column_1, display):
        column_1.button(label='<-', key='<-', width='stretch')
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )

  the test is still green

* I do the same thing for the numbers in the second column

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-20
    :emphasize-text: on_click args

    def add_buttons_to_column_2(column_2):
        column_2.button(
            label='C', key='C', width='stretch', type='primary',
        )
        column_2.button(
            label='8', key='8', width='stretch',
            on_click=show, args=[display, '8'],
        )
        column_2.button(
            label='5', key='5', width='stretch',
            on_click=show, args=[display, '5'],
        )
        column_2.button(
            label='2', key='2', width='stretch',
            on_click=show, args=[display, '2'],
        )
        column_2.button(
            label='0', key='0', width='stretch',
            on_click=show, args=[display, '0'],
        )

  the terminal_ shows :ref:`KeyError<test_key_error>` for 20 sub tests and the terminal_ for the application shows :ref:`NameError<test_catching_name_error_in_tests>`

* I add ``display`` to the :ref:`function<what is a function?>` signature of the ``add_buttons_to_column_2`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

    def add_buttons_to_column_2(column_2, display):

  the terminal_ shows :ref:`KeyError<test_key_error>` for 22 sub tests and the terminal_ for the application shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add_buttons_to_column_2() missing 1 required positional argument: 'display'

* I add ``display`` to the call to the ``add_buttons_to_column_2`` :ref:`function<what is a function?>` in the ``main`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 7

    def main():
        streamlit.title('Calculator')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3)
        add_buttons_to_column_4(operations)

  the test passes

* I make the same change for the numbers in the third column

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 5-24
    :emphasize-text: on_click args

    def add_buttons_to_column_3(column_3):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch',
            on_click=show, args=[display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch',
            on_click=show, args=[display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch',
            on_click=show, args=[display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch',
            on_click=show, args=[display, '.'],
        )

  the terminal_ shows :ref:`KeyError<test_key_error>` for 14 sub tests

  .. code-block:: python

    ================== 14 failed, 12 passed in X.YZs ===================


  and the terminal_ for the application shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'display' is not defined

* I add ``display`` to the signature of the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 1

    def add_buttons_to_column_3(column_3, display):

  the terminal_ shows :ref:`KeyError<test_key_error>` and the terminal_ for the application shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add_buttons_to_column_3() missing 1 required positional argument: 'display'

* I add ``display`` to the call to the ``add_buttons_to_column_3`` in the ``main`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 8

    def main():
        streamlit.title('Calculator')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations)

  the test passes.

* I go to the browser to test the numbers and they show up in the box, with one problem - every time I press a button it shows a new number.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_streamlit_calculator.py``, ``streamlit_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the first terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I click in the second terminal_, then use :kbd:`ctrl+c` on the keyboard to close the web server. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I made a website using Streamlit_ with a :ref:`title<test_streamlit_calculator_title>`, :ref:`display<test_streamlit_calculator_display>` and :ref:`buttons<test_streamlit_calculator_columns_and_buttons>`

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 10: part 2: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know how to:

* build a website with streamlit_
* how to test the parts of the website
* :ref:`how to add a title to the streamlit website<test_streamlit_calculator_title>`
* :ref:`how to add a display to the streamlit website<test_streamlit_calculator_display>`
* :ref:`how to add buttons to the streamlit website<test_streamlit_calculator_columns_and_buttons>`
* :ref:`how to change the colors of the buttons<test_streamlit_calculator_operations_buttons>`
* :ref:`how to show something when a button is pressed<how to show the numbers when I click on them>`

:ref:`Would you like to continue with adding buttons to the calculator?<how to make a calculator 10: part 3>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->