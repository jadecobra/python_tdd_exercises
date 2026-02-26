.. meta::
  :description: Learn how to turn your TDD calculator into a beautiful, interactive web app using Streamlit — the easiest way to build data apps in Python. No HTML, no routes, just pure Python.
  :keywords: Jacob Itegboje, streamlit python tutorial, streamlit tdd calculator, python streamlit web app, streamlit calculator project, easy python web apps with tdd

.. include:: ../links.rst

.. _streamlit: https://streamlit.io
.. _AppTest: docs.streamlit.io/develop/api-reference/app-testing#the-apptest-class
.. _from_file method: docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file

#################################################################################
how to make a calculator 10
#################################################################################

I want to try another way to make a website for the :ref:`Calculator<how to make a calculator>`, the last one is not beautiful yet. I test Streamlit_ which lets me build professional-looking web applications with almost no extra code.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_10.py
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

* I make a new test file_ for the Streamlit_ website

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_streamlit_calculator.py

* I add streamlit_ to the ``requirements.txt`` file_

  .. code-block:: shell
    :emphasize-lines: 1

    echo "streamlit" >> requirements.txt

  Streamlit_ is a Python_ library that is used for making websites, it is not part of `The Python Standard Library`_

* I install the `Python packages`_ I gave in the requirements file_

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

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 8 items

    tests/test_calculator.py .....                                [ 62%]
    tests/test_calculator_website.py ...                          [100%]

    ======================== 5 passed in X.YZs =========================

----

*********************************************************************************
test_streamlit_calculator_title
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I open ``test_streamlit_calculator.py`` from the ``tests`` folder_ in the :ref:`editor<2 editors>`

* I add a new test in ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-9

    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'streamlit' is not defined

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12-13
    :emphasize-text: NameError

    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )


    # Exceptions seen
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import streamlit
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'streamlit' has no attribute 'testing'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3
    :emphasize-text: AttributeError

    # Exceptions seen
    # NameError
    # AttributeError

* I add more to the `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import streamlit.testing
    import unittest

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'streamlit.testing' has no attribute 'v1'

* I add ``v1`` to the `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import streamlit.testing.v1
    import unittest

  the test passes

  I am using ``streamlit.testing.v1.AppTest.from_file`` to test the website made with streamlit_

  - AppTest_ is a :ref:`class<what is a class?>` from ``v1`` in ``testing`` in the streamlit_ library
  - ``.from_file`` uses the `from_file method`_ to run the :ref:`Python module<what is a module?>` that I use to make the application

* I add more to the test to see what happens when I try to run the application even though ``src/streamlit_calculator.py`` is empty

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for the title of the application

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(tester.title, 'Calculator')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ElementList() != 'Calculator'

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4
    :emphasize-text: AssertionError

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError

* I open ``streamlit_calculator.py``
* I add code to make a streamlit_ application

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4-5

    import streamlit


    def main():
        streamlit.title('Calculator')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ElementList() != 'Calculator'

* I add an :ref:`if statement<if statements>` to run the ``main`` :ref:`function<what is a function?>` when the :ref:`module<what is a module?>` gets called as a script

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    def main():
        streamlit.title('Calculator')


    if __name__ == '__main__':
        main()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ElementList(_list=[Title(tag='h1')]) != 'Calculator'

  - when I import a :ref:`module<what is a module?>` nothing happens until I call or use the things in it
  - ``if __name__ == '__main__':`` calls ``main()`` only when ``src/streamlit_calculator.py`` gets called like a script for example ``python3 src/streamlit_calculator.py`` not when it is imported
  - I could write it without the :ref:`condition<if statements>` which can lead to things I do not want when I import the file. It is better to use the :ref:`condition<if statements>`
  - it looks like ``ElementList(_list=[Title(tag='h1')])`` has a :ref:`list<what is a list?>` and I know how to work with :ref:`lists<what is a list?>`

* I change the :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertEqual(tester.title[0], 'Calculator')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Title(tag='h1') != 'Calculator'

* I use the ``value`` :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``Title`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertEqual(tester.title[0].value, 'Calculator')

  the test passes. Time to run the app

----

*********************************************************************************
how to view the streamlit calculator website
*********************************************************************************

* I open a new terminal_ then use uv_

  .. code-block:: python
    :emphasize-lines:

    uv run streamlit run src/streamlit_calculator.py

  the terminal_ shows

  .. code-block:: shell

    Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


      You can now view your Streamlit app in your browser.

      Local URL: http://localhost:8501
      Network URL: http://ABC.DEF.GHI.JKL:8501
      External URL: http://MNO.PQR.STU.VWX:8501

  it might also show a dialog box like this, and I click on ``Open in Browser``

  .. image:: /_static/calculator/streamlit_dialog.png
    :width: 600
    :align: left
    :alt: Confirm you want to view Streamlit app in browser

  or I use :kbd:`ctrl/option` on the keyboard and click on ``http://localhost:8501`` with the mouse to open the browser and it shows

  .. image:: /_static/calculator/calculator_streamlit_title.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit App with Title

  Success!

* I click the 3 dots by ``Deploy`` on the right hand side

  .. image:: /_static/calculator/streamlit_deploy_menu.png
    :width: 600
    :align: left
    :alt: Streamlit Deploy Menu

* then I click on ``Settings`` then the checkmark by ``Run on save`` to make sure the website changes as I make changes to the code

  .. image:: /_static/calculator/streamlit_deploy_settings.png
    :width: 600
    :align: left
    :alt: Streamlit Deploy Settings

----

*********************************************************************************
how to add a display
*********************************************************************************

* I want the :ref:`calculator<how to make a calculator>` to have a place to show results as the user clicks the numbers for a calculation. I add it to the ``main`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

* I go to the browser and there is a display bar under the ``Calculator`` title

  .. image:: /_static/calculator/calculator_streamlit_display.png
    :width: 600
    :align: left
    :alt: Calculate Streamlit Display

----

*********************************************************************************
test_streamlit_calculator_buttons
*********************************************************************************

Calculators have buttons for the numbers and operations, they are setup in rows and columns.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

-----

I add a new test with an :ref:`assertion<what is an assertion?>` for the ``4`` columns that hold the buttons in ``test_streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 7

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(tester.title[0].value, 'Calculator')

        def test_streamlit_calculator_buttons(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(len(tester.columns), 4)

the terminal_ shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0 != 4

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add columns to ``streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 5-7

  def main():
      streamlit.title('Calculator')
      streamlit.container(border=True)

      column_1, column_2, column_3, operation = streamlit.columns(
          4, vertical_alignment='bottom'
      )

the test passes, even though the website still looks the same

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for a button in ``test_streamlit_calculator.py``

  .. TIP:: ``<-`` is :kbd:`<+-` on the keyboard

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

            self.assertEqual(tester.title[0].value, 'Calculator')
            self.assertEqual(len(tester.columns), 4)

            self.assertEqual(tester.columns[0].button, '<-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError>`

  .. code-block:: python

    AssertionError: WidgetList() != '<-'

* I add a button to the first column in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5

        column_1, column_2, column_3, operation = streamlit.columns(
            4, vertical_alignment='bottom'
        )

        column_1.button('<-', type='secondary', width='stretch')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: WidgetList(_list=[Button(label='<-')]) != '<-'

  progress

* I can use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the button to get it, because it is in a :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertEqual(tester.columns[0].button[0], '<-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Button(label='<-') != '<-'

* I use the ``label`` :ref:`attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertEqual(tester.columns[0].button[0].label, '<-')

  the test passes

* I go to the browser and see the button I just added

  .. image:: /_static/calculator/calculator_streamlit_first_button.png
    :width: 600
    :align: left
    :alt: Calculate Streamlit First Button

* I add an :ref:`assertion<what is an assertion?>` for the next button in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

            self.assertEqual(tester.columns[0].button[0].label, '<-')
            self.assertEqual(tester.columns[0].button[1].label, '7')

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add :ref:`IndexError<test_index_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5
    :emphasize-text: IndexError

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError
    # IndexError

* I add a button for ``7`` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12

        column_1.button('<-', type='secondary', width='stretch')
        column_1.button('7', type='secondary', width='stretch')

  a duplication. The test passes

* I add another :ref:`assertion<what is an assertion?>` to ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

            self.assertEqual(tester.columns[0].button[0].label, '<-')
            self.assertEqual(tester.columns[0].button[1].label, '7')
            self.assertEqual(tester.columns[0].button[2].label, '4')

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add a button for ``4`` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

        column_1.button('<-', type='secondary', width='stretch')
        column_1.button('7', type='secondary', width='stretch')
        column_1.button('4', type='secondary', width='stretch')

  the test passes

* I add another :ref:`assertion<what is an assertion?>` to ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

            self.assertEqual(tester.columns[0].button[0].label, '<-')
            self.assertEqual(tester.columns[0].button[1].label, '7')
            self.assertEqual(tester.columns[0].button[2].label, '4')
            self.assertEqual(tester.columns[0].button[3].label, '1')

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add a button for ``1`` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

        column_1.button('<-', type='secondary', width='stretch')
        column_1.button('7', type='secondary', width='stretch')
        column_1.button('4', type='secondary', width='stretch')
        column_1.button('1', type='secondary', width='stretch')

  the test passes

* I add the last :ref:`assertion<what is an assertion?>` for this column to ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

            self.assertEqual(tester.columns[0].button[0].label, '<-')
            self.assertEqual(tester.columns[0].button[1].label, '7')
            self.assertEqual(tester.columns[0].button[2].label, '4')
            self.assertEqual(tester.columns[0].button[3].label, '1')
            self.assertEqual(tester.columns[0].button[4].label, '+/-')

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add a button for ``+/-`` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 13

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        column_1, column_2, column_3, operation = streamlit.columns(
            4, vertical_alignment='bottom'
        )

        column_1.button('<-', type='secondary', width='stretch')
        column_1.button('7', type='secondary', width='stretch')
        column_1.button('4', type='secondary', width='stretch')
        column_1.button('1', type='secondary', width='stretch')
        column_1.button('+/-', type='secondary', width='stretch')

  the test passes

* I click ``refresh`` in the browser and see all the columns I added

  .. image:: /_static/calculator/calculator_streamlit_column_1.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit First Column

  lovely, it looks more like a Calculator

* I use a :ref:`for loop<what is a for loop?>` with the `subTest method`_ for the :ref:`assertions<what is an assertion?>` for the columns in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-9

            self.assertEqual(tester.columns[0].button[4].label, '+/-')

            labels = ('<-', '7', '4', '1', '+/-')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[0].button[index].label,
                        'BOOM!!!'
                    )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(label='<-') ... - AssertionError: '<-' != 'BOOM!!!'
    SUBFAILED(label='7') ... - AssertionError: '7' != 'BOOM!!!'
    SUBFAILED(label='4') ... - AssertionError: '4' != 'BOOM!!!'
    SUBFAILED(label='1') ... - AssertionError: '1' != 'BOOM!!!'
    SUBFAILED(label='+/-') ... - AssertionError: '+/-' != 'BOOM!!!'

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

                    self.assertEqual(
                        tester.columns[0].button[index].label,
                        labels[index]
                    )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.maxDiff = None
            self.assertEqual(tester.title[0].value, 'Calculator')
            self.assertEqual(len(tester.columns), 4)

            labels = ('<-', '7', '4', '1', '+/-')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[0].button[index].label,
                        labels[index]
                    )


    # Exceptions seen

  the test is still green

----

* I add a :ref:`for loop<what is a for loop?>` for the next column

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 9-15

            labels = ('<-', '7', '4', '1', '+/-')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[0].button[index].label,
                        labels[index]
                    )

            labels = ('C', '8', '5', '2', '0')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[1].button[index].label,
                        labels[index]
                    )


    # Exceptions seen

  more repetition. The terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    SUBFAILED(label='C') ... - IndexError: list index out of range
    SUBFAILED(label='8') ... - IndexError: list index out of range
    SUBFAILED(label='5') ... - IndexError: list index out of range
    SUBFAILED(label='2') ... - IndexError: list index out of range
    SUBFAILED(label='0') ... - IndexError: list index out of range

* I add buttons for each label to the second column in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7-11
    :emphasize-text: column_2

        column_1.button('<-', type='secondary', width='stretch')
        column_1.button('7', type='secondary', width='stretch')
        column_1.button('4', type='secondary', width='stretch')
        column_1.button('1', type='secondary', width='stretch')
        column_1.button('+/-', type='secondary', width='stretch')

        column_2.button('C', type='secondary', width='stretch')
        column_2.button('8', type='secondary', width='stretch')
        column_2.button('5', type='secondary', width='stretch')
        column_2.button('2', type='secondary', width='stretch')
        column_2.button('0', type='secondary', width='stretch')

  the test passes

* I click ``refresh`` in the browser

  .. image:: /_static/calculator/calculator_streamlit_column_2.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Second Column

  alright

----

* I add a :ref:`for loop<what is a for loop?>` to ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 9-15

            labels = ('C', '8', '5', '2', '0')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[1].button[index].label,
                        labels[index]
                    )

            labels = ('AC', '9', '6', '3', '.')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[2].button[index].label,
                        labels[index]
                    )

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add the buttons to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 7-11
    :emphasize-text: column_3

        column_2.button('C', type='secondary', width='stretch')
        column_2.button('8', type='secondary', width='stretch')
        column_2.button('5', type='secondary', width='stretch')
        column_2.button('2', type='secondary', width='stretch')
        column_2.button('0', type='secondary', width='stretch')

        column_3.button('AC', type='secondary', width='stretch')
        column_3.button('9', type='secondary', width='stretch')
        column_3.button('6', type='secondary', width='stretch')
        column_3.button('3', type='secondary', width='stretch')
        column_3.button('.', type='secondary', width='stretch')

  the test passes

* I refresh the browser

  .. image:: /_static/calculator/calculator_streamlit_column_3.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Third Column

  one more column to go

----

* I add a :ref:`for loop<what is a for loop?>` to test the last column in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 9-15

            labels = ('AC', '9', '6', '3', '.')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[2].button[index].label,
                        labels[index]
                    )

            labels = ('/', 'X', '-', '+', '=')
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        tester.columns[3].button[index].label,
                        labels[index]
                    )

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add the buttons to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-11

        column_3.button('AC', type='secondary', width='stretch')
        column_3.button('9', type='secondary', width='stretch')
        column_3.button('6', type='secondary', width='stretch')
        column_3.button('3', type='secondary', width='stretch')
        column_3.button('.', type='secondary', width='stretch')

        operation.button('/', type='secondary', width='stretch')
        operation.button('X', type='secondary', width='stretch')
        operation.button('-', type='secondary', width='stretch')
        operation.button('+', type='secondary', width='stretch')
        operation.button('=', type='secondary', width='stretch')

  the test passes

* I refresh the browser

  .. image:: /_static/calculator/calculator_streamlit_column_4.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Fourth Column

  Good! There is a fourth column, it is missing ``-`` and ``+``

* I add ``r`` and ``\`` to escape the characters because they mean something to streamlit_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines:  3-4

        operation.button('/', type='secondary', width='stretch')
        operation.button('X', type='secondary', width='stretch')
        operation.button(r'\-', type='secondary', width='stretch')
        operation.button(r'\+', type='secondary', width='stretch')
        operation.button('=', type='secondary', width='stretch')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(label='-') ... - AssertionError: '\\-' != '-'
    SUBFAILED(label='+') ... - AssertionError: '\\+' != '+'

  - ``r`` make this a raw string_ which means the characters are taken as they are, not what they stand for
  - ``\`` escapes the character  so that ``+`` and ``-`` are taken exactly as they are to show on the buttons

* I change the labels in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1

            labels = ('/', 'X', r'\-', r'\+', '=')

  the test is green again

* I check the browser

  .. image:: /_static/calculator/calculator_streamlit_all_labels.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit All labels

  yes! The calculator shows all the labels

* the 4 :ref:`for loops<what is a for loop?>` in the test look the same

  .. code-block:: python

    labels = (x, y, z, a, b
    for index in range(len(labels)):
        with self.subTest(label=labels[index]):
            self.assertEqual(
                tester.columns[X].button[index].label,
                labels[index]
            )

  the parts that change are the labels and the number used to :ref:`index<test_index_returns_first_position_of_item_in_a_list>` the ``tester.columns`` :ref:`list<what is a list?>`

  I add a :ref:`method<what is a function?>` to remove the repetition of the :ref:`for loops<what is a for loop?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-9

    class TestStreamlitCalculator(unittest.TestCase):

        def assert_buttons_in_column(self, labels, column):
            for index in range(len(labels)):
                with self.subTest(label=labels[index]):
                    self.assertEqual(
                        column.button[index].label,
                        labels[index]
                    )

        def test_streamlit_calculator_title(self):

* I use it for the first :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-6

            self.assertEqual(len(tester.columns), 4)

            self.assert_buttons_in_column(
                labels=('a', 'b', 'c', 'd', 'e'),
                column=tester.columns[0]
            )

            labels = ('<-', '7', '4', '1', '+/-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(label='a') ... - AssertionError: '<-' != 'a'
    SUBFAILED(label='b') ... - AssertionError: '7' != 'b'
    SUBFAILED(label='c') ... - AssertionError: '4' != 'c'
    SUBFAILED(label='d') ... - AssertionError: '1' != 'd'
    SUBFAILED(label='e') ... - AssertionError: '+/-' != 'e'

  it works

* I change the labels

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

            self.assert_buttons_in_column(
                labels=('<-', '7', '4', '1', '+/-'),
                column=tester.columns[0]
            )

  the test passes

* I add another call to the ``assert_buttons_in_column`` :ref:`method<what is a method?>` for the second column

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5-8

            self.assert_buttons_in_column(
                labels=('<-', '7', '4', '1', '+/-'),
                column=tester.columns[0]
            )
            self.assert_buttons_in_column(
                labels=('C', '8', '5', '2', '0'),
                column=tester.columns[0]
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(label='C') ... - AssertionError: '<-' != 'C'
    SUBFAILED(label='8') ... - AssertionError: '7' != '8'
    SUBFAILED(label='5') ... - AssertionError: '4' != '5'
    SUBFAILED(label='2') ... - AssertionError: '1' != '2'
    SUBFAILED(label='0') ... - AssertionError: '+/-' != '0'

* I change the column

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3

            self.assert_buttons_in_column(
                labels=('C', '8', '5', '2', '0'),
                column=tester.columns[1]
            )

  the test passes

* I add 2 more calls for the other columns

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-12

            self.assert_buttons_in_column(
                labels=('C', '8', '5', '2', '0'),
                column=tester.columns[1]
            )
            self.assert_buttons_in_column(
                labels=('AC', '9', '6', '3', '.'),
                column=tester.columns[2]
            )
            self.assert_buttons_in_column(
                labels=('/', 'X', r'\-', r'\+', '='),
                column=tester.columns[3]
            )

            labels = ('<-', '7', '4', '1', '+/-')

  the test is still green

* these 4 calls look the same

  .. code-block:: python

    self.assert_buttons_in_column(
        labels=(a, b, c, d, e),
        column=tester.columns[number]
    )

  the parts that change are the labels and the numbers used to :ref:`index<test_index_returns_first_position_of_item_in_a_list>` the ``tester.columns`` :ref:`list<what is a list?>`. I add a :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-14

            self.assertEqual(len(tester.columns), 4)

            all_labels = (
                ('<-', '7', '4', '1', '+/-'),
                ('C', '8', '5', '2', '0'),
                ('AC', '9', '6', '3', '.'),
                ('/', 'X', r'\-', r'\+', '='),
            )
            for index in range(len(all_labels)):
                with self.subTest(index=index):
                    self.assert_buttons_in_column(
                        labels=(0, 1, 2, 3),
                        column=tester.columns[index]
                    )

            self.assert_buttons_in_column(

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with 16 failed

* I change the labels in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

                    self.assert_buttons_in_column(
                        labels=all_labels[index],
                        column=tester.columns[index]
                    )

  the test is still green

* I remove all the other statements

  .. code-block:: python
    :lineno-start: 15

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.maxDiff = None
            self.assertEqual(tester.title[0].value, 'Calculator')
            self.assertEqual(len(tester.columns), 4)

            all_labels = (
                ('<-', '7', '4', '1', '+/-'),
                ('C', '8', '5', '2', '0'),
                ('AC', '9', '6', '3', '.'),
                ('/', 'X', r'\-', r'\+', '='),
            )
            for index in range(len(all_labels)):
                with self.subTest(index=index):
                    self.assert_buttons_in_column(
                        labels=all_labels[index],
                        column=tester.columns[index]
                    )


    # Exceptions seen

----

----

----

  .. code-block:: python

    import streamlit


    def main():
        streamlit.title('Calculator')
        streamlit.header('BOOM!!!')


    if __name__ == '__main__':
        main()


  .. code-block:: python

    class TestStreamlitCalculator(unittest.TestCase):

        def test_streamlit_calculator_title(self):
            self.maxDiff = None
            tester = streamlit.testing.v1.AppTest.from_file('src/streamlit_calculator.py')
            tester.run()
            self.assertEqual(
                dir(tester),
                [
                    '__class__',
                    '__delattr__',
                    '__dict__',
                    '__dir__',
                    '__doc__',
                    '__eq__',
                    '__firstlineno__',
                    '__format__',
                    '__ge__',
                    '__getattribute__',
                    '__getitem__',
                    '__getstate__',
                    '__gt__',
                    '__hash__',
                    '__init__',
                    '__init_subclass__',
                    '__iter__',
                    '__le__',
                    '__len__',
                    '__lt__',
                    '__module__',
                    '__ne__',
                    '__new__',
                    '__reduce__',
                    '__reduce_ex__',
                    '__repr__',
                    '__setattr__',
                    '__sizeof__',
                    '__static_attributes__',
                    '__str__',
                    '__subclasshook__',
                    '__weakref__',
                    '_from_string',
                    '_page_hash',
                    '_run',
                    '_script_path',
                    '_tree',
                    'args',
                    'button',
                    'button_group',
                    'caption',
                    'chat_input',
                    'chat_message',
                    'checkbox',
                    'code',
                    'color_picker',
                    'columns',
                    'dataframe',
                    'date_input',
                    'datetime_input',
                    'default_timeout',
                    'divider',
                    'error',
                    'exception',
                    'expander',
                    'from_file',
                    'from_function',
                    'from_string',
                    'get',
                    'header',
                    'info',
                    'json',
                    'kwargs',
                    'latex',
                    'main',
                    'markdown',
                    'metric',
                    'multiselect',
                    'number_input',
                    'query_params',
                    'radio',
                    'run',
                    'secrets',
                    'select_slider',
                    'selectbox',
                    'session_state',
                    'sidebar',
                    'slider',
                    'status',
                    'subheader',
                    'success',
                    'switch_page',
                    'table',
                    'tabs',
                    'text',
                    'text_area',
                    'text_input',
                    'time_input',
                    'title',
                    'toast',
                    'toggle',
                    'warning'
                ]
            )
            self.assertEqual(
                tester.title[0].value,
                'Calculator'
            )



    .. code-block:: python
      :lineno-start: 8
      :emphasize-lines: 5-12

          def test_streamlit_can_be_imported(self):
              ...

          def test_streamlit_calculator_app(self):
              from src.streamlit_app import main
              self.assertTrue(callable(main))

the terminal shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I create the file

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/streamlit_app.py

* I open it and add the basic app

  .. code-block:: python
    :linenos:

    import streamlit as st
    import src.calculator as calc

    def main():
        st.title("🧮 My TDD Calculator")
        st.write("Built step-by-step with Test-Driven Development!")

    if __name__ == "__main__":
        main()

The test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

Now I build the full interactive calculator.

I update the test to also check core behavior (we already know it works from earlier chapters, but it feels good to see it here).

I expand ``src/streamlit_app.py``:

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-35

    def main():
        st.title("🧮 My TDD Calculator")
        st.write("Built step-by-step with Test-Driven Development!")

        col1, col2, col3 = st.columns([3, 1, 3])

        with col1:
            first = st.number_input("First number", value=0.0, step=0.1)

        with col2:
            operation = st.selectbox(
                "Operation",
                ["+", "-", "×", "÷"]
            )

        with col3:
            second = st.number_input("Second number", value=0.0, step=0.1)

        if st.button("Calculate", type="primary"):
            try:
                ops = {
                    "+": calc.add,
                    "-": calc.subtract,
                    "×": calc.multiply,
                    "÷": calc.divide
                }
                result = ops[operation](first, second)
                st.success(f"**Result:** {result}")

            except ZeroDivisionError:
                st.error("brmph?! I cannot divide by 0. Try again...")
            except Exception:
                st.error("brmph?! Numbers only. Try again...")

        # Bonus: show history
        if "history" not in st.session_state:
            st.session_state.history = []

        if st.button("Clear history"):
            st.session_state.history = []

        if st.session_state.history:
            st.subheader("Recent calculations")
            for item in reversed(st.session_state.history[-5:]):
                st.write(item)

    if __name__ == "__main__":
        main()

The app now looks and works beautifully.

----

*********************************************************************************
test_error_messages_in_streamlit
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add

.. code-block:: python
  :lineno-start: 20

      def test_error_messages_in_streamlit(self):
          self.assertEqual(
              src.calculator.divide(10, 0),
              'brmph?! I cannot divide by 0. Try again...'
          )

the test already passes (thanks to chapters 3–4).

----

*********************************************************************************
how to run the app
*********************************************************************************

In the terminal I type:

.. code-block:: shell
  :emphasize-lines: 1

  uv run streamlit run src/streamlit_app.py

A browser window opens automatically with my beautiful calculator!

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

I now have **three** different versions of the same calculator:

* Pure Python (chapters 1–8)
* Flask website (chapter 9)
* **Streamlit web app** (chapter 10) — the fastest and most beautiful version

The core calculator code never changed. All my tests still protect it.
This is the real power of Test-Driven Development.

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 10: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You have completed an amazing journey from pure functions to real web applications!

You now know how to:

* Build programs with Test-Driven Development
* Turn them into Flask websites
* Turn them into beautiful Streamlit apps

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