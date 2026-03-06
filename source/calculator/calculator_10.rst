.. meta::
  :description: Learn how to turn your TDD calculator into a beautiful, interactive web app using Streamlit — the easiest way to build data apps in Python. No HTML, no routes, just pure Python.
  :keywords: Jacob Itegboje, streamlit python tutorial, streamlit tdd calculator, python streamlit web app, streamlit calculator project, easy python web apps with tdd

.. include:: ../links.rst

.. _streamlit: https://streamlit.io
.. _streamlit library: streamlit
.. _streamlit buttons: docs.streamlit.io/develop/api-reference/widgets/st.button#stbutton
.. _streamlit container: docs.streamlit.io/develop/api-reference/layout/st.container#stcontainer
.. _streamlit Block object: docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock
.. _streamlit tester object: docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#sttestingv1apptest
.. _AppTest: docs.streamlit.io/develop/api-reference/app-testing#the-apptest-class
.. _from_file method: docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file
.. _session state object: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
.. _enums: https://docs.python.org/3/library/enum.html#module-enum

#################################################################################
how to make a calculator 10
#################################################################################

I want to try another way to make a website for the :ref:`Calculator<how to make a calculator>`, the last one is not beautiful yet. I test Streamlit_ which lets me build professional-looking web applications with almost no extra code.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_streamlit_calculator.py
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
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: AttributeError

    # Exceptions seen
    # NameError
    # AttributeError

* I add more to the `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1
    :emphasize-text: testing

    import streamlit.testing
    import unittest

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'streamlit.testing' has no attribute 'v1'

* I add ``v1`` to the `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1
    :emphasize-text: v1

    import streamlit.testing.v1
    import unittest

  the test passes

  ``streamlit.testing.v1.AppTest.from_file`` tests the website I am making with streamlit_

  - AppTest_ is a :ref:`class<what is a class?>` from ``v1`` in ``testing`` in the `streamlit library`_
  - ``.from_file`` uses the `from_file method`_ to run the :ref:`Python module<what is a module?>` that I use to make the application

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

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

* I open ``streamlit_calculator.py`` in the :ref:`editor<2 editors>`

* I add code to make a streamlit_ application with a title, in ``streamlit_calculator.py``

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
  - ``if __name__ == '__main__':`` calls ``main()`` only when ``src/streamlit_calculator.py`` gets called like a script, for example

    * in the terminal_

      .. code-block:: python

        python3 src/streamlit_calculator.py

    * or in ``test_streamlit_calculator.py``

      .. code-block:: python

        tester = streamlit.testing.v1.AppTest.from_file(
            'src/streamlit_calculator.py'
        )
        tester.run()

    it does not get called when the :ref:`module<what is a module?>` is imported

  - ``ElementList(_list=[Title(tag='h1')])`` has a :ref:`list<what is a list?>` and I know how to work with :ref:`lists<what is a list?>`

* I change the :ref:`assertion<what is an assertion?>` to get the first item from the :ref:`list<what is a list?>`, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertEqual(tester.title[0], 'Calculator')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Title(tag='h1') != 'Calculator'

* I use the ``value`` :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``Title`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_streamlit_calculator_title(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(tester.title[0].value, 'Calculator')

  the test passes. Time to run the application

----

*********************************************************************************
how to view the streamlit calculator website
*********************************************************************************

* I open a new terminal_ then use uv_

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

  it might also show a dialog box like this, and I click on ``Open in Browser``

  .. image:: /_static/calculator/streamlit/streamlit_dialog.png
    :width: 600
    :align: left
    :alt: Confirm you want to view Streamlit app in browser

  or I use :kbd:`ctrl/option` on the keyboard and click on ``http://localhost:8501`` with the mouse to open the browser and it shows

  .. image:: /_static/calculator/streamlit/title.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit App with Title

  Success!

* I click the 3 dots by ``Deploy`` on the right hand side

  .. image:: /_static/calculator/streamlit/streamlit_deploy_menu.png
    :width: 600
    :align: left
    :alt: Streamlit Deploy Menu

* I click on ``Settings``

* I click the checkmark by ``Run on save`` to make sure the website changes as I make changes to the code

  .. image:: /_static/calculator/streamlit/streamlit_deploy_settings.png
    :width: 600
    :align: left
    :alt: Streamlit Deploy Settings

----

*********************************************************************************
test_streamlit_calculator_display
*********************************************************************************

I want the :ref:`calculator<how to make a calculator>` to have a place to show results as the user clicks numbers

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

-----

I add a test to see all the :ref:`attributes<test_attribute_error_w_class_attributes>` of the application

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 8-13

      def test_streamlit_calculator_title(self):
          tester = streamlit.testing.v1.AppTest.from_file(
              'src/streamlit_calculator.py'
          )
          tester.run()
          self.assertEqual(tester.title[0].value, 'Calculator')

      def test_streamlit_calculator_display(self):
          tester = streamlit.testing.v1.AppTest.from_file(
              'src/streamlit_calculator.py'
          )
          tester.run()
          self.assertIsNone(tester.main)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  E       AssertionError: SpecialBlock(
  E           type='main',
  E           children={
  E               0: Title(tag='h1')
  E           }
  E       ) is not None

I see that the ``children`` :ref:`object<what is a class?>` is a :ref:`dictionary<what is a dictionary?>`. I know how to work with :ref:`dictionaries<what is a dictionary?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

-----

* I change assertIsNone_ to assertEqual_, then add an expectation

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6
    :emphasize-text: assertEqual children { }

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(tester.main.children, {})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: Title(tag='h1')} != {}

  the only thing in the application is the title

* I copy the :ref:`dictionary<what is a dictionary?>` from the terminal_ and use it as the expectation

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6-9

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(
                tester.main.children,
                {0: Title(tag='h1')}
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'Title' is not defined

* I change the ``Title`` :ref:`object<what is a class?>` to ``tester.title[0]``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

            self.assertEqual(
                tester.main.children,
                {0: tester.title[0]}
            )

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

-----

* I add a `streamlit container`_ to the ``main`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3

    def main():
        streamlit.title('Calculator')
        streamlit.container()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: Title(tag='h1'), 1: Block(
       type='flex_container'
    )} != {0: Title(tag='h1')}

  there is a new :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` because I added something to the application

* I change the :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3-6

            self.assertEqual(
                tester.main.children,
                {
                    0: tester.title[0],
                    1: Block(type='flex_container'),
                }
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'Block' is not defined

* I change the :ref:`assertion<what is an assertion?>` to get the `streamlit Block object`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2, 5
    :emphasize-text: 1

            self.assertEqual(
                tester.main.children[1],
                {
                    0: tester.title[0],
                    # 1: Block(type='flex_container')
                }
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Block(
       type='flex_container'
    )

* I use the ``__dict__`` :ref:`attribute<test_attribute_error_w_class_attributes>` to get the `streamlit Block object`_ as a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

            self.assertEqual(
                tester.main.children[1].__dict__,
                {
                    0: tester.title[0],
                    # 1: Block(type='flex_container')
                }
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'children': {}, 'proto': flex_container {[503 chars] )

* I set maxDiff_ to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2


            tester.run()
            self.maxDiff = None
            self.assertEqual(
                tester.main.children[1].__dict__,
                {
                    0: tester.title[0],
                    # 1: Block(type='flex_container')
                }
            )

  the terminal_ shows the full difference

* I copy the :ref:`dictionary<what is a dictionary?>`, remove the extra characters with ``Find and Replace`` (:kbd:`ctrl+H` (Windows_) or :kbd:`command+option+F` (MacOS_)) and use it as the expectation

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-38

            self.assertEqual(
                tester.main.children[1].__dict__,
                {
                    'children': {},
                    'proto': flex_container {
                        gap_config {
                            gap_size: SMALL
                        }
                        direction: VERTICAL
                        justify: JUSTIFY_START
                        align: ALIGN_START
                    }
                    height_config {
                        use_content: true
                    }
                    width_config {
                        use_stretch: true
                    },
                    'root': {
                        0: SpecialBlock(
                            type='main',
                            children={
                                0: Title(tag='h1'),
                                1: Block(
                                    type='flex_container'
                                )
                            }
                        ),
                        1: SpecialBlock(
                            type='sidebar'
                        ),
                        2: SpecialBlock(
                            type='event'
                        )
                    },
                    'type': 'flex_container'
                }
            )


    # Exceptions seen

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax. Perhaps you forgot a comma?

  this :ref:`dictionary<what is a dictionary?>` has too many things

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5
    :emphasize-text: SyntaxError

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError
    # SyntaxError

* I change the :ref:`assertion<what is an assertion?>` to use the ``proto`` :ref:`attribute<test_attribute_error_w_class_attributes>` since it looks like a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-3

        self.assertEqual(
            tester.main.children[1].proto,
            {}
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: flex_container {
    E         gap_config {
    E           gap_s[155 chars]ue
    E       }
    E        != {}

* I use the ``__dict__`` :ref:`attribute<test_attribute_error_w_class_attributes>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2

            self.assertEqual(
                tester.main.children[1].type,
                'flex_container'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: none

    AssertionError: mappingproxy({'Vertical': <class 'streaml[827 chars]one}) != {}

* I use the ``flex_container`` :ref:`attribute<test_attribute_error_w_class_attributes>` instead

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2

            self.assertEqual(
                tester.main.children[1].proto.flex_container,
                {}
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: gap_config {
    E         gap_size: SMALL
    E       }
    E       directio[49 chars]TART
    E        != {}

* I use the ``gap_size`` :ref:`attribute<test_attribute_error_w_class_attributes>` directly

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-6

            self.assertEqual(
                (
                    tester.main.children[1].proto
                          .flex_container
                          .gap_config.gap_size
                ),
                {}
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != {}

* I change the expectation

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 7

            self.assertEqual(
                (
                    tester.main.children[1].proto
                          .flex_container
                          .gap_config.gap_size
                ),
                1
            )

  the test passes

* I remove maxDiff_

  .. code-block:: python
    :lineno-start: 14

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()
            self.assertEqual(
                (
                    tester.main.children[1].proto
                          .flex_container
                          .gap_config.gap_size
                ),
                1
            )


    # Exceptions seen

* I add a :ref:`variable<what is a variable?>` for the ``flex_container`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 7-10

        def test_streamlit_calculator_display(self):
            tester = streamlit.testing.v1.AppTest.from_file(
                'src/streamlit_calculator.py'
            )
            tester.run()

            display = (
                tester.main.children[1].proto
                      .flex_container
            )
            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-7

            self.assertEqual(
                # (
                #     tester.main.children[1].proto
                #           .flex_container
                #           .gap_config.gap_size
                # ),
                display.gap_config.gap_size, 1
            )

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

            self.assertEqual(display.gap_config.gap_size, 1)

* I add an :ref:`assertion<what is an assertion?>` for the next :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``flex_container`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, '')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

            self.assertEqual(display.direction, 1)

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the next :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``flex_container`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, '')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertEqual(display.justify, 1)

  the test passes

* I add the last :ref:`attribute<test_attribute_error_w_class_attributes>` of the ``flex_container`` :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4

            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, '')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 1

            self.assertEqual(display.align, 1)


    # Exceptions seen

  the test passes. All the :ref:`attributes<test_attribute_error_w_class_attributes>` have 1 as their value which stands for different things in each case, they are called enums_

  - ``gap_config.gap_size`` - 1 - SMALL
  - ``direction`` - 1 - VERTICAL
  - ``justify`` - 1 - JUSTIFY_START
  - ``align`` - 1 - ALIGN_START

* I go to the browser and things look the same as before. I need to add a border

* I add an :ref:`assertion<what is an assertion?>` for a border in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5

            self.assertEqual(display.gap_config.gap_size, 1)
            self.assertEqual(display.direction, 1)
            self.assertEqual(display.justify, 1)
            self.assertEqual(display.align, 1)
            self.assertEqual(display.border, '')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != ''

* I change the assertEqual_ to assertFalse_ and remove the expectation

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            self.assertFalse(display.border)

  the test passes

* I change the assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 15

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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

* I add a border to the container in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3
    :emphasize-text: border

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

  the test passes

* I go to the browser and click refresh

  .. image:: /_static/calculator/streamlit/display.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Display

  there is a box under the ``Calculator`` title

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

* I add a new test with an :ref:`assertion<what is an assertion?>` for the first button, in ``test_streamlit_calculator.py``

  .. NOTE:: ``<-`` is :kbd:`<+-` on the keyboard

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-11, 13

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

* I add the ``key`` parameter

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1
    :emphasize-text: key

        streamlit.button('<-', key='<-')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Button(key='<-', label='<-') is not None

* I change the :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1
    :emphasize-text: label

            self.assertIsNone(tester.button('<-').label)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<-' is not None

* I change assertIsNone_ to assertEqual_, then add an expectation

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1
    :emphasize-text: assertEqual

            self.assertEqual(tester.button('<-').label, '')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '<-' != ''

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            self.assertEqual(tester.button('<-').label, '<-')

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I go to the browser, click refresh

  .. image:: /_static/calculator/streamlit/no_column_first_button.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit First Button no column

  I see the button I just added

* I add an :ref:`assertion<what is an assertion?>` for the next button, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 24
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
    :lineno-start: 4
    :emphasize-lines: 6

    def main():
        streamlit.title('Calculator')
        streamlit.container(border=True)

        streamlit.button('<-', key='<-')
        streamlit.button('7', key='7')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/no_column_second_button.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Second Button no column

  the second button is there

* I add a :ref:`for loop<what is a for loop?>` for all the buttons, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-10

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

        streamlit.button('<-', key='<-')
        streamlit.button('7', key='7')
        streamlit.button('4', key='4')
        streamlit.button('1', key='1')
        streamlit.button('+/-', key='+/-')

        streamlit.button('C', key='C')
        streamlit.button('8', key='8')
        streamlit.button('5', key='5')
        streamlit.button('2', key='2')
        streamlit.button('0', key='0')

        streamlit.button('AC', key='AC')
        streamlit.button('9', key='9')
        streamlit.button('6', key='6')
        streamlit.button('3', key='3')
        streamlit.button('.', key='.')

        streamlit.button('/', key='/')
        streamlit.button('X', key='X')
        streamlit.button('-', key='-')
        streamlit.button('+', key='+')
        streamlit.button('=', key='=')


    if __name__ == '__main__':

  the test passes

* I make a :ref:`function<what is a function?>` to make the buttons

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-9, 11-15, 17-21, 23-27

    import streamlit


    def add_buttons():
        streamlit.button('<-', key='<-')
        streamlit.button('7', key='7')
        streamlit.button('4', key='4')
        streamlit.button('1', key='1')
        streamlit.button('+/-', key='+/-')

        streamlit.button('C', key='C')
        streamlit.button('8', key='8')
        streamlit.button('5', key='5')
        streamlit.button('2', key='2')
        streamlit.button('0', key='0')

        streamlit.button('AC', key='AC')
        streamlit.button('9', key='9')
        streamlit.button('6', key='6')
        streamlit.button('3', key='3')
        streamlit.button('.', key='.')

        streamlit.button('/', key='/')
        streamlit.button('X', key='X')
        streamlit.button('-', key='-')
        streamlit.button('+', key='+')
        streamlit.button('=', key='=')


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

    streamlit.errors.StreamlitDuplicateElementKey: There are multiple elements with the same key='<-'. To fix this, please make sure that the key argument is unique for each element you create.

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
    :alt: Calculator Streamlit All Buttons no column

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

        def test_streamlit_calculator_title(self):

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

* I remove the other lines in :ref:`test_streamlit_calculator_title`

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
test_streamlit_calculator_columns
*********************************************************************************

Calculator buttons are arranged in Columns and Rows. I can do the same thing with Streamlit_

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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add columns to the ``main`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 29
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

* I change assertIsNone_ to assertEqual_ then add the expectation

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

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_streamlit_calculator_columns` in ``test_streamlit_calculator.py``

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

* I add a :ref:`for loop<what is a for loop?>` for all the buttons in the first column

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

----

* I check the browser and the buttons still look the same

* I remove the :ref:`assertion<what is an assertion?>` after the :ref:`for loop<what is a for loop?>`, then add another :ref:`for loop<what is a for loop?>` for the second column, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 8-13

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

* I use the keys for the second column

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 1

            for key in ('C', '8', '5', '2', '0'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.columns[1].button(key).label,
                        key
                    )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(key='C') ... - KeyError: 'C'
    SUBFAILED(key='8') ... - KeyError: '8'
    SUBFAILED(key='5') ... - KeyError: '5'
    SUBFAILED(key='2') ... - KeyError: '2'
    SUBFAILED(key='0') ... - KeyError: '0'

* I move buttons to the second column in ``streamlit_calculator,py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-7
    :emphasize-text: column_2

        column_1.button('+/-', key='+/-')

        column_2.button('C', key='C')
        column_2.button('8', key='8')
        column_2.button('5', key='5')
        column_2.button('2', key='2')
        column_2.button('0', key='0')

        streamlit.button('AC', key='AC')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/2_columns.png
    :width: 600
    :align: left
    :alt: Calculator 2 Columns

  there is a second column of buttons. Progress! It does not look right yet, baby steps.

----

* I add a :ref:`for loop<what is a for loop?>` for the third column in ``test_streamlit_calculator.py``

  .. code-block:: python
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
    :lineno-start: 56
    :emphasize-lines: 2

                    self.assertEqual(
                        self.tester.columns[2].button(key).label,
                        key
                    )

  the terminal_ shows :ref:`KeyError<test_key_error>`

* I move buttons to the third column in the ``add_buttons`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-7
    :emphasize-text: column_3

        column_2.button('0', key='0')

        column_3.button('AC', key='AC')
        column_3.button('9', key='9')
        column_3.button('6', key='6')
        column_3.button('3', key='3')
        column_3.button('.', key='.')

        streamlit.button('/', key='/')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/3_columns.png
    :width: 600
    :align: left
    :alt: Calculator 3 Columns

  3 columns

* On to the next one. I add a :ref:`for loop<what is a for loop?>` with an :ref:`assertion<what is an assertion?>` for the operations in the operations column, in ``test_streamlit_calculator.py``

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

* I remove :ref:`test_streamlit_calculator_buttons` because :ref:`test_streamlit_calculator_columns` tests the same things - the button labels

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

* All the :ref:`for loops<what is a for loop?>` in :ref:`test_streamlit_calculator_columns` look the same

  .. code-block:: python
    :emphasize-text: index key

    for key in (A, B, C, D, E):
        with self.subTest(key=key):
            self.assertEqual(
                self.tester.columns[index].button(key).label,
                key
            )

  I add 2 new :ref:`for loops<what is a for loop?>` that put all the others together

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4-18

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', '-', '+', '='))
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key).label
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
    :emphasize-lines: 6

                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key).label
                            ),
                            key
                        )

  the test passes

* I remove the other :ref:`for loops<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 27

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', '-', '+', '='))
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key).label
                            ),
                            key
                        )


    # Exceptions seen

----

* I want all the buttons to be the same size and `streamlit buttons`_ have a ``width`` option. I set it to ``stretch`` for the ``<-`` button in the first column in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4
    :emphasize-text: width

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button('7', key='7')

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
    :emphasize-lines: 5-8
    :emphasize-text: stretch

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button('7', key='7', width='stretch')
        column_1.button('4', key='4', width='stretch')
        column_1.button('1', key='1', width='stretch')
        column_1.button('+/-', key='+/-', width='stretch')

        column_2.button('C', key='C')

  still green

* I check the browser

  .. image:: /_static/calculator/streamlit/stretch_first_column.png
    :width: 600
    :align: left
    :alt: Calculator Stretched First Column

  all the buttons in the first column have the same size

* I stretch all the other buttons

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 10-26
    :emphasize-text: stretch

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button('7', key='7', width='stretch')
        column_1.button('4', key='4', width='stretch')
        column_1.button('1', key='1', width='stretch')
        column_1.button('+/-', key='+/-', width='stretch')

        column_2.button('C', key='C', width='stretch')
        column_2.button('8', key='8', width='stretch')
        column_2.button('5', key='5', width='stretch')
        column_2.button('2', key='2', width='stretch')
        column_2.button('0', key='0', width='stretch')

        column_3.button('AC', key='AC', width='stretch')
        column_3.button('9', key='9', width='stretch')
        column_3.button('6', key='6', width='stretch')
        column_3.button('3', key='3', width='stretch')
        column_3.button('.', key='.', width='stretch')

        operations.button('/', key='/', width='stretch')
        operations.button('X', key='X', width='stretch')
        operations.button('-', key='-', width='stretch')
        operations.button('+', key='+', width='stretch')
        operations.button('=', key='=', width='stretch')


    def main():

  green

* I refresh the browser

  .. image:: /_static/calculator/streamlit/column_4.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Fourth Column

  Good! The buttons all have the same size. I am still missing ``-`` and ``+`` that the tests says are there

* I add ``r`` and ``\`` to escape the characters because they mean something to streamlit_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines:  5-6
    :emphasize-text: \ - +

        column_3.button('.', key='.', width='stretch')

        operations.button('/', key='/', width='stretch')
        operations.button('X', key='X', width='stretch')
        operations.button(r'\-', key=r'\-', width='stretch')
        operations.button(r'\+', key=r'\+', width='stretch')
        operations.button('=', key='=', width='stretch')

    def main():

  the terminal_ shows :ref:`KeyError<test_key_error>` and :ref:`AssertionError<what causes AssertionError>`

  .. code-block:: python

    SUBFAILED(key='-') ... - KeyError: '-'
    SUBFAILED(key='+') ... - AssertionError: '\\+' != '+'

  - ``r`` makes this a raw string_ which means the characters are taken as they are, not what they stand for
  - ``\`` escapes the character  so that ``+`` and ``-`` are taken exactly as they are to show the characters on the buttons. ``'+'`` and ``'-'`` mean something different in streamlit_ so they do not show up as labels for the buttons

* I change the keys for ``-`` and ``+`` in :ref:`test_streamlit_calculator_columns` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 8
    :emphasize-text: \ - +

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', r'\-', r'\+', '='))
            ):
                for key in keys:

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/all_labels.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit All labels

  yes! The calculator shows all the labels

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
  :emphasize-lines: 20-21

        def test_streamlit_calculator_columns(self):
            self.assertEqual(len(self.tester.columns), 4)

            for column, keys in (
                (0, ('<-', '7', '4', '1', '+/-')),
                (1, ('C', '8', '5', '2', '0')),
                (2, ('AC', '9', '6', '3', '.')),
                (3, ('/', 'X', r'\-', r'\+', '='))
            ):
                for key in keys:
                    with self.subTest(key=key):
                        self.assertEqual(
                            (
                                self.tester.columns[column]
                                    .button(key).label
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
  :emphasize-lines: 1

            self.assertEqual(self.tester.button('/').proto.type, 'secondary')

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation from ``secondary`` to ``primary``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 1

            self.assertEqual(self.tester.button('/').proto.type, 'primary')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'secondary' != 'primary'

* I use the ``type`` parameter of `streamlit buttons`_ to change the colors of the buttons for the ``/`` button in the fourth column, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-5
    :emphasize-text: primary

        column_3.button('.', key='.', width='stretch')

        operations.button(
            '/', key='/', width='stretch', type='primary',
        )
        operations.button('X', key='X', width='stretch')

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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='X') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='\\-') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='\\+') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='=') ... - AssertionError: 'secondary' != 'primary'

* I add the ``type`` parameter to the buttons in the ``add_buttons`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6-17
    :emphasize-text: primary

        column_3.button('.', key='.', width='stretch')

        operations.button(
            '/', key='/', width='stretch', type='primary',
        )
        operations.button(
            'X', key='X', width='stretch', type='primary',
        )
        operations.button(
            r'\-', key=r'\-', width='stretch', type='primary',
        )
        operations.button(
            r'\+', key=r'\+', width='stretch', type='primary',
        )
        operations.button(
            '=', key='=', width='stretch', type='primary',
        )

    def main():

  the test passes

* I want the ``C`` and ``AC`` buttons to have the same colors as the buttons for the operations. I add them to the tuple_ in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

        def test_streamlit_calculator_operations_buttons(self):
            for key in ('/', 'X', r'\-', r'\+', '=', 'C', 'AC'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.button(key).proto.type,
                        'primary'
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='C') ... - AssertionError: 'secondary' != 'primary'
    SUBFAILED(key='AC') ... - AssertionError: 'secondary' != 'primary'

* I change the type for the ``AC`` button in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-5
    :emphasize-text: primary

        column_2.button('0', key='0', width='stretch')

        column_3.button(
            'AC', key='AC', width='stretch', type='primary',
        )
        column_3.button('9', key='9', width='stretch')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='C') ... - AssertionError: 'secondary' != 'primary'

* I change the type for the ``C`` button

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-5
    :emphasize-text: primary

        column_1.button('+/-', key='+/-', width='stretch')

        column_2.button(
            'C', key='C', width='stretch', type='primary',
        )
        column_2.button('8', key='8', width='stretch')

  the test passes

* I check the browser

  .. image:: /_static/calculator/streamlit/primary_buttons.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Primary Buttons

  much better

----

*********************************************************************************
how to display the numbers when I click on them
*********************************************************************************

I want the calculator to show the number when I click on a button

* I add a :ref:`variable<what is a variable?>` to name the container so I can use it to show the numbers

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3

    def main():
        streamlit.title('Calculator')
        display = streamlit.container(border=True)
        add_buttons()

* I add a :ref:`function<what is a function?>` to show the text of the button when it is clicked

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import streamlit


    def show(display, number):
        display.write(number)


    def add_buttons():

* `streamlit buttons`_ have an ``on_click`` parameter that lets me call a :ref:`function<what is a function?>` when a button is clicked. It also takes an argument named ``args`` where I can pass in the :ref:`positional arguments<test_functions_w_positional_arguments>` that the :ref:`function<what is a function?>` takes. I pass the :ref:`function<what is a function?>` and the ``display`` :ref:`variable<what is a variable?>` with a value as the arguments for the ``7`` button in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-8
    :emphasize-text: on_click args

    def add_buttons():
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button(
            '7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button('4', key='4', width='stretch')

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    ================== 26 failed, 12 passed in A.BCs ===================


  the terminal_ for the application shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'display' is not defined

* I move the display from ``main`` to the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

    def add_buttons():
        display = streamlit.container(border=True)
        column_1, column_2, column_3, operations = streamlit.columns(4)

  the test passes

* I go to the browser and click on the ``7`` button

  .. image:: /_static/calculator/streamlit/display_7.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Display 7 on click

  ``7`` shows on the display. Yes!

* I make the same change for the other numbers in the first column

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 10-17
    :emphasize-text: on_click args

    def add_buttons():
        display = streamlit.container(border=True)
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button(
            '7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            '4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            '1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button('+/-', key='+/-', width='stretch')

        column_2.button(
            'C', key='C', width='stretch', type='primary',
        )

  the test is still green

* I make the same change for the numbers in the second column

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6-21
    :emphasize-text: on_click args

        column_1.button('+/-', key='+/-', width='stretch')

        column_2.button(
            'C', key='C', width='stretch', type='primary',
        )
        column_2.button(
            '8', key='8', width='stretch',
            on_click=show, args=[display, '8'],
        )
        column_2.button(
            '5', key='5', width='stretch',
            on_click=show, args=[display, '5'],
        )
        column_2.button(
            '2', key='2', width='stretch',
            on_click=show, args=[display, '2'],
        )
        column_2.button(
            '0', key='0', width='stretch',
            on_click=show, args=[display, '0'],
        )

        column_3.button(
            'AC', key='AC', width='stretch', type='primary',
        )

  still green

* I make the same change for the numbers in the third column

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 9-24
    :emphasize-text: on_click args

        column_2.button(
            '0', key='0', width='stretch',
            on_click=show, args=[display, '0'],
        )

        column_3.button(
            'AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            '9', key='9', width='stretch',
            on_click=show, args=[display, '9'],
        )
        column_3.button(
            '6', key='6', width='stretch',
            on_click=show, args=[display, '6'],
        )
        column_3.button(
            '3', key='3', width='stretch',
            on_click=show, args=[display, '3'],
        )
        column_3.button(
            '.', key='.', width='stretch',
            on_click=show, args=[display, '.'],
        )

        operations.button(
            '/', key='/', width='stretch', type='primary',
        )

  green

* I go to the browser to test the numbers and they show up in the box, with one problem - every time I press a button it shows a new number. I want the numbers to stay so that I can make numbers that have more than one digit

----

*********************************************************************************
how to use state
*********************************************************************************

streamlit_ has a `session state object`_ that I can use to keep values in between button presses. They work the same as :ref:`class attributes<test_attribute_error_w_class_attributes>` and they are :ref:`dictionaries<what is a dictionary?>` - I can add :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to them

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `session state object`_, I want it to hold the number when I click the buttons, in ``test_streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 9-10

      def test_streamlit_calculator_operations_buttons(self):
          for key in ('/', 'X', r'\-', r'\+', '=', 'C', 'AC'):
              with self.subTest(key=key):
                  self.assertEqual(
                      self.tester.button(key).proto.type,
                      'primary'
                  )

      def test_streamlit_calculator_state(self):
          self.assertIsNone(self.tester.session_state['number'])


  # Exceptions seen

the terminal_ shows :ref:`KeyError<test_key_error>`

.. code-block:: shell

  KeyError: 'st.session_state has no key "number".
  Did you forget to initialize it?
  More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>` to add a :ref:`key<test_keys_of_a_dictionary>` that will hold the numbers to show in the Calculator, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', 0)
        add_buttons()


    if __name__ == '__main__':
        main()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I change the assertIsNone_ to assertEqual_ in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 2

        def test_streamlit_calculator_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the `session state object`_ to the ``show`` :ref:`function<what is a function?>` to update it when a button is clicked, then display the number

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-5

    def show(display, number):
        # display.write(number)
        streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

  the test passes

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    def show(display, number):
        streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

* I add an :ref:`assertion<what is an assertion?>` to test what happens to the `session state object`_ when I press a button for a number

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 3

        def test_streamlit_calculator_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')
            self.tester.button('1').click().run()
            self.assertEqual(self.tester.session_state['number'], '0')

  - ``.click()`` presses the button
  - ``.run()`` runs the program - ``streamlit_calculator.py``, same as when a person uses the application

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01' != '0'

  this is a problem

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 1

            self.assertEqual(self.tester.session_state['number'], '01')

* I add more button clicks

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2-5

            self.assertEqual(self.tester.session_state['number'], '01')
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('4').click().run()
            self.assertEqual(self.tester.session_state['number'], '01')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01234' != '01'

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 1-3

            self.assertEqual(
                self.tester.session_state['number'], '01234'
            )

  the test passes

* I refresh the browser and click on all the numbers

  .. image:: /_static/calculator/streamlit/many_numbers.png
    :width: 600
    :align: left
    :alt: Many Numbers

  the calculator keeps numbers when I press the buttons and the number starts with ``0`` like the test

* I want the calculator to remove ``0`` when it is the first number after I click on other numbers. I change the :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 4, 8-10

        def test_streamlit_calculator_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')
            self.tester.button('1').click().run()
            self.assertEqual(self.tester.session_state['number'], '1')
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('4').click().run()
            self.assertEqual(
                self.tester.session_state['number'], '1234'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01' != '1'

* I add a :ref:`condition<if statements>` to the ``show`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-5

    def show(display, number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

  the test passes

* I refresh the browser and try all the numbers

  .. image:: /_static/calculator/streamlit/many_numbers_no_zero_first.png
    :width: 600
    :align: left
    :alt: Many Numbers Without 0 first

  the number no longer starts with ``0``

* I import the `random module`_ to use random numbers for the test, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import streamlit.testing.v1
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

* I use it in :ref:`test_streamlit_calculator_state`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 2, 4-6
    :emphasize-text: x

        def test_streamlit_calculator_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            self.tester.button(x).click().run()
            self.assertEqual(self.tester.session_state['number'], '1')

  - ``numbers = '0123456789'`` makes a string with the ten numbers
  - ``x = random.choice(numbers)`` selects a random digit from the ten numbers and points ``x`` to it

  the terminal_ shows. :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X' != '1'

  where ``X`` is the random number

* I change the expectation

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 1

            self.assertEqual(self.tester.session_state['number'], x)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X234' != '1234'

* I use random numbers for the other button clicks

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2-10

            self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()
            # self.tester.button('3').click().run()
            # self.tester.button('4').click().run()
            y = random.choice(numbers)
            self.tester.button(y).click().run()
            z = random.choice(numbers)
            self.tester.button(z).click().run()
            a = random.choice(numbers)
            self.tester.button(a).click().run()
            self.assertEqual(
                self.tester.session_state['number'], '1234'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'XYZA' != '1234'

* I use the random numbers in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2

            self.assertEqual(
                self.tester.session_state['number'], f'{x}{y}{z}{a}'
            )

  the test passes

* I add a :ref:`for loop<what is a for loop?>` to test with a 10 digit number

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 4-18

            self.assertEqual(
                self.tester.session_state['number'], f'{x}{y}{z}{a}'
            )
            expectation = '0'
            for _ in range(0, 10):
                number = random.choice(numbers)
                (
                    self.tester.button(number)
                    .click().run()
                )
                if expectation == '0':
                    expectation = number
                else:
                    expectation += number
            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )


    # Exceptions seen

  ``for _ in range(0, 10):`` uses ``_`` as the name of the :ref:`variable<what is a variable?>` in the :ref:`for loop<what is a for loop?>` because it is not used in it

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'XYZABCDEFGHIJK' != 'BCDEFGHIJK'

  the last 10 digits are the same in the two strings_

* I comment out the other lines

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 3, 5-7, 11-19

        def test_streamlit_calculator_state(self):
            numbers = '0123456789'
            # self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            # x = random.choice(numbers)
            # self.tester.button(x).click().run()
            # self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()
            # self.tester.button('3').click().run()
            # self.tester.button('4').click().run()
            # y = random.choice(numbers)
            # self.tester.button(y).click().run()
            # z = random.choice(numbers)
            # self.tester.button(z).click().run()
            # a = random.choice(numbers)
            # self.tester.button(a).click().run()
            # self.assertEqual(
            #     self.tester.session_state['number'], f'{x}{y}{z}{a}'
            # )
            expectation = '0'
            for _ in range(0, 10):

  I use :kbd:`ctrl+s` on the keyboard to run the tests a few times and the test is still green

* I remove the commented lines and ``numbers`` :ref:`variable<what is a variable?>` and use the numbers directly

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 4

        def test_streamlit_calculator_state(self):
            expectation = '0'
            for _ in range(0, 10):
                number = random.choice('0123456789')
                (
                    self.tester.button(number)
                    .click().run()
                )
                if expectation == '0':
                    expectation = number
                else:
                    expectation += number
            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )


    # Exceptions seen

----

*********************************************************************************
test_streamlit_calculator_w_decimals
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for decimal numbers

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 6-24

            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )

        def test_streamlit_calculator_w_decimals(self):
            self.tester.button('0').click().run()
            self.tester.button('.').click().run()
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('.').click().run()
            self.tester.button('5').click().run()
            self.tester.button('.').click().run()
            self.tester.button('6').click().run()
            self.tester.button('.').click().run()
            self.tester.button('7').click().run()
            self.tester.button('.').click().run()
            self.tester.button('8').click().run()
            self.tester.button('.').click().run()
            self.tester.button('9').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '.2356789'
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '.23.5.6.7.8.9' != '0.2356789'

* I refresh the browser and do the same thing

  .. image:: /_static/calculator/streamlit/many_decimals.png
    :width: 600
    :align: left
    :alt: Many Decimals

  the Calculator allows me add many decimal points

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`condition<if statements>` to the ``show`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-10

    def show(display, number):
        if number == '.':
            if (
                streamlit.session_state['number']
                .count('.') != 0
            ):
                display.write(
                    streamlit.session_state['number']
                )
                return
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

  the test passes

* I refresh the browser and try many decimals again

  .. image:: /_static/calculator/streamlit/one_decimal.png
    :width: 600
    :align: left
    :alt: One Decimal

  Yes. I can only do one decimal in a number

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I make a :ref:`function<what is a function?>` to update the `session state object`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-14

    import streamlit


    def update_state(number):
        if number == '.':
            if (
                streamlit.session_state['number']
                .count('.') != 0
            ):
                return
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
            return
        streamlit.session_state['number'] += number


    def show(display, number):

* I call the new :ref:`function<what is a function?>` in the ``show`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-12

    def show(display, number):
        # if number == '.':
        #     if streamlit.session_state['number'].count('.') != 0:
        #         display.write(
        #             streamlit.session_state['number']
        #         )
        #         return
        # if streamlit.session_state['number'] == '0':
        #     streamlit.session_state['number'] = number
        # else:
        #     streamlit.session_state['number'] += number
        update_state(number)
        display.write(streamlit.session_state['number'])

  the test is still green

* I remove the commented lines from the ``show`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 17

    def show(display, number):
        update_state(number)
        display.write(streamlit.session_state['number'])

* I add a :ref:`for loop<what is a for loop?>` to :ref:`test_streamlit_calculator_w_decimals` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 2-6

        def test_streamlit_calculator_w_decimals(self):
            for button in ('0.23.5.6.7.8.9'):
                (
                    self.tester.button(button)
                    .click().run()
                )
            self.tester.button('0').click().run()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '.235678902356789' != '.2356789'

* I remove the other button clicks

  .. code-block:: python
    :lineno-start: 125

        def test_streamlit_calculator_w_decimals(self):
            for button in ('0.23.5.6.7.8.9'):
                (
                    self.tester.button(button)
                    .click().run()
                )
            self.assertEqual(
                self.tester.session_state['number'],
                '.2356789'
            )


    # Exceptions seen

  the test passes

----

*********************************************************************************
test_streamlit_calculator_w_plus_minus
*********************************************************************************

Nothing happens when I click ``+/-`` in the calculator. I want to be able to change positive numbers to negative numbers or negative numbers to positive numbers when I click ``+/-``

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 131
  :emphasize-lines: 6-17

          self.assertEqual(
              self.tester.session_state['number'],
              '.2356789'
          )

      def test_streamlit_calculator_w_plus_minus(self):
          number = '963.0258741'
          for button in number:
              (
                  self.tester.button(button)
                  .click().run()
              )
          self.tester.button('+/-').click().run()
          self.assertEqual(
              self.tester.session_state['number'],
              f'-{number}'
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: '963.0258741' != '-963.0258741'

nothing happens when I click on the ``+/-`` button in the calculator

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the ``on_click`` parameter to the ``+/-`` button in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 18-21

    def add_buttons():
        display = streamlit.container(border=True)
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button(
            '7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            '4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            '1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            '+/-', key='+/-', width='stretch',
            on_click=show, args=[display, '+/-'],
        )

        column_2.button('C', key='C', width='stretch', type='primary')

* I add :ref:`conditions<if statements>` to the ``update_state`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 11-22

    def update_state(number):
        if number == '.':
            if (
                streamlit.session_state['number']
                .count('.') != 0
            ):
                return
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
            return
        if number == '+/-':
            if not (
                streamlit.session_state['number']
                .startswith('-')
            ):
                negative = (
                    '-'  +
                    streamlit.session_state['number']
                )
                streamlit.session_state['number'] = \
                    negative
                return
        streamlit.session_state['number'] += number

  I can use ``\`` to break up a long line in two. The test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another click for ``+/-`` and an :ref:`assertion<what is an assertion?>` to make sure the Calculator will change a negative number to a positive one, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 5-9

            self.assertEqual(
                self.tester.session_state['number'],
                f'-{number}'
            )
            self.tester.button('+/-').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '-963.0258741+/-' != '963.0258741'

  it added ``+/-`` at the end of the number

* I add another :ref:`condition<if statements>` to the ``update_state`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 13-16

        if number == '+/-':
            if not (
                streamlit.session_state['number']
                .startswith('-')
            ):
                negative = (
                    '-'  +
                    streamlit.session_state['number']
                )
                streamlit.session_state['number'] = \
                    negative
                return
            else:
                streamlit.session_state['number'] = \
                    streamlit.session_state['number'][1:]
                return
        streamlit.session_state['number'] += number

  the test passes

* I refresh the browser and try to make a negative number

  .. image:: /_static/calculator/streamlit/negative_number.png
    :width: 600
    :align: left
    :alt: Negative Number

  when I click on the ``+/-`` button it turns a positive number negative

* I try the ``+/-`` button again

  .. image:: /_static/calculator/streamlit/positive_number.png
    :width: 600
    :align: left
    :alt: Negative Number

  the ``-`` is removed from the number to make it a positive number. Progress!

----

* I use the ``Rename Symbol`` feature to change ``number`` to ``value`` in the ``update_state`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1-2, 9, 11, 27
    :emphasize-text: value

    def update_state(value):
        if value == '.':
            if (
                streamlit.session_state['number']
                .count('.') != 0
            ):
                return
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = value
            return
        if value == '+/-':
            if not (
                streamlit.session_state['number']
                .startswith('-')
            ):
                negative = (
                    '-'  +
                    streamlit.session_state['number']
                )
                streamlit.session_state['number'] = \
                    negative
                return
            else:
                streamlit.session_state['number'] = \
                    streamlit.session_state['number'][1:]
                return
        streamlit.session_state['number'] += value

  the test is still green

* I do the same thing in the ``show`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1-2
    :emphasize-text: value

    def show(display, value):
        update_state(value)
        display.write(streamlit.session_state['number'])

  still green

----

*********************************************************************************
test_streamlit_calculator_reset_state
*********************************************************************************

I want the ``C`` and ``AC`` buttons to change the number the Calculator shows back to ``0``

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test

.. code-block:: python
  :lineno-start: 149
  :emphasize-lines: 6-18

            self.assertEqual(
                self.tester.session_state['number'],
                number
            )

        def test_streamlit_calculator_reset_state(self):
            numbers = '123456789'
            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )
            self.tester.button('C').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: X != '0'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import streamlit


    def reset_state():
        streamlit.session_state['number'] = '0'


    def update_state(value):

* I add the ``on_click`` parameter to the ``C`` button

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 23-26

    def add_buttons():
        display = streamlit.container(border=True)
        column_1, column_2, column_3, operations = streamlit.columns(4)

        column_1.button('<-', key='<-', width='stretch')
        column_1.button(
            '7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            '4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            '1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            '+/-', key='+/-', width='stretch',
            on_click=show, args=[display, '+/-'],
        )

        column_2.button(
            'C', key='C', width='stretch', type='primary',
            on_click=reset_state
        )
        column_2.button(
            '8', key='8', width='stretch',
            on_click=show, args=[display, '8'],
        )

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I refresh the browser, click on number buttons and when I click on ``C`` it clears the numbers I type

* I add an :ref:`assertion<what is an assertion?>` for the ``AC`` button in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 15-25

        def test_streamlit_calculator_reset_state(self):
            numbers = '123456789'
            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )
            self.tester.button('C').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )

            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )
            self.tester.button('AC').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

    AssertionError: X != '0'

* I add the ``on_click`` parameter to the ``AC`` button

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 22-25

        column_2.button(
            'C', key='C', width='stretch', type='primary',
            on_click=reset_state
        )
        column_2.button(
            '8', key='8', width='stretch',
            on_click=show, args=[display, '8'],
        )
        column_2.button(
            '5', key='5', width='stretch',
            on_click=show, args=[display, '5'],
        )
        column_2.button(
            '2', key='2', width='stretch',
            on_click=show, args=[display, '2'],
        )
        column_2.button(
            '0', key='0', width='stretch',
            on_click=show, args=[display, '0'],
        )

        column_3.button(
            'AC', key='AC', width='stretch', type='primary',
            on_click=reset_state
        )
        column_3.button(
            '9', key='9', width='stretch',
            on_click=show, args=[display, '9'],
        )

  the test passes

* I refresh the browser, click on number buttons and when I click on ``AC`` it clears the numbers I type

* I add a call to the ``write`` :ref:`method<what is a function?>` of the ``display`` :ref:`object<what is a class?>` to show ``0`` when I click on the ``C`` or ``AC`` buttons, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-5

    def reset_state():
        streamlit.session_state['number'] = '0'
        display.write(streamlit.session_state['number'])


    def update_state(value):

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'X'

  and :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'display' is not defined

* I add ``display`` as a :ref:`positional argument<test_functions_w_positional_arguments>` in parentheses

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    def reset_state(display):
        streamlit.session_state['number'] = '0'
        display.write(streamlit.session_state['number'])

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    AssertionError: 'X' != '0'

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block::

    TypeError: reset_state() missing 1 required positional argument: 'display'

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 8
    :emphasize-text: TypeError

    # Exceptions seen
    # NameError
    # AttributeError
    # AssertionError
    # SyntaxError
    # KeyError
    # streamlit.errors.StreamlitDuplicateElementKey
    # TypeError

* I add ``display`` to the ``args`` parameter for the ``C`` button in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

        column_2.button(
            'C', key='C', width='stretch', type='primary',
            on_click=reset_state, args=[display]
        )

  the terminal_ shows the same :ref:`Exceptions<errors>`

* I add ``display`` to the ``args`` parameter for the ``AC`` button

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3

        column_3.button(
            'AC', key='AC', width='stretch', type='primary',
            on_click=reset_state, args=[display]
        )

  the test passes

* I refresh the browser and try the ``C`` and ``AC`` buttons

  .. image:: /_static/calculator/streamlit/reset_state.png
    :width: 600
    :align: left
    :alt: Display 0 after C or AC

Time to do the operations

----

*********************************************************************************
test_streamlit_calculator_operations
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test

.. code-block:: python
  :lineno-start: 175
  :emphasize-lines: 6-8, 10-13, 15-18

            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            self.tester.button(first_number).click().run()
            self.tester.button('+').click().run()
            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()

            self.assertEqual(
                self.tester.session_state['number'],
                float(first_number) + float(second_number)
            )


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: '12' != 3.0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the first number after the ``+`` button is pressed, in :ref:`test_streamlit_calculator_operations`

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 3-6

            self.tester.button(first_number).click().run()
            self.tester.button('+').click().run()
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "first_number". Did you forget to initialize it? More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I make a :ref:`function<what is a function?>` to add the first number to the `session state object`_ when the ``+`` button is pressed, in ``streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-7

    import streamlit


    def make_variable(display):
        streamlit.session_state['first_number'] = \
            streamlit.session_state['number']
        reset_state(display)


    def reset_state(display):

* I add the ``on_click`` and ``args`` parameters to the ``+`` button in the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 4-7

        operations.button('/', key='/', width='stretch', type='primary')
        operations.button('X', key='X', width='stretch', type='primary')
        operations.button(r'\-', key='-', width='stretch', type='primary')
        operations.button(
            r'\+', key='+', width='stretch', type='primary',
            on_click=make_variable, args=[display],
        )
        operations.button('=', key='=', width='stretch', type='primary')


    def main():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != 3.0

* I add an :ref:`assertion<what is an assertion?>` for the second number after the ``=`` button is pressed, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 3-6

            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                float(first_number) + float(second_number)
            )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "second_number". Did you forget to initialize it? More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I make a new :ref:`function<what is a function?>` for the result, in ``streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-6

    import streamlit


    def show_result(display):
        streamlit.session_state['second_number'] = \
            streamlit.session_state['number']
        display.write(streamlit.session_state['number'])


    def make_variable(display):

  * I add the ``on_click`` and ``args`` parameters to the ``=`` button in the ``add_buttons`` :ref:`function<what is a function?>`

    .. code-block:: python
      :lineno-start: 122
      :emphasize-lines: 8-11

          operations.button('/', key='/', width='stretch', type='primary')
          operations.button('X', key='X', width='stretch', type='primary')
          operations.button(r'\-', key='-', width='stretch', type='primary')
          operations.button(
              r'\+', key='+', width='stretch', type='primary',
              on_click=make_variable, args=[display],
          )
          operations.button(
              '=', key='=', width='stretch', type='primary',
              on_click=show_result, args=[display],
          )


      def main():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != 3.0

* I add a calculation to the ``show_result`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-7

    def show_result(display):
        streamlit.session_state['second_number'] = \
            streamlit.session_state['number']
        streamlit.session_state['number'] = (
            streamlit.session_state['first_number']
          + streamlit.session_state['second_number']
        )
        display.write(streamlit.session_state['number'])

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '12' != 3.0

* I change the numbers to floats_

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6
    :emphasize-text: float

    def show_result(display):
        streamlit.session_state['second_number'] = \
            streamlit.session_state['number']
        streamlit.session_state['number'] = (
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )
        display.write(streamlit.session_state['number'])

  the test passes

* I refresh the browser and try the same calculation

  .. image:: /_static/calculator/streamlit/addition.png
    :width: 600
    :align: left
    :alt: Addition Result

  the result is correct but the number looks different from the others

* when I try another number, the browser shows :ref:`TypeError<what causes TypeError?>`

  .. image:: /_static/calculator/streamlit/type_error_after_addition.png
    :width: 600
    :align: left
    :alt: TypeError after Addition

  the terminal_ for the browser also shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +=: 'float' and 'str'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the result to look the same as the other numbers. I change it to a string_ in the ``show_result`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    def show_result(display):
        streamlit.session_state['second_number'] = \
            streamlit.session_state['number']
        streamlit.session_state['number'] = str(
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )
        display.write(streamlit.session_state['number'])

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '3.0' != 3.0

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_streamlit_calculator_operations` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 198
    :emphasize-lines: 3
    :emphasize-text: str

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number) + float(second_number))
            )

  the test passes

* I refresh the browser and try the calculation again

  .. image:: /_static/calculator/streamlit/addition_string_result.png
    :width: 600
    :align: left
    :alt: Addition with String Result

  I like it, though I do not need the ``.0`` after the ``3``

* I import ``test_calculator.py`` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    import random
    import streamlit.testing.v1
    import tests.test_calculator
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

* I use the ``a_random_number`` :ref:`function<what is a function?>` from ``test_calculator.py`` to add randomness to :ref:`test_streamlit_calculator_operations`

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 2-3

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            second_number = '2'

            self.tester.button(first_number).click().run()

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: ABC.DEFGHIJKLMNOP

* I have to change the number to button presses. I change the number to a string_

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 4

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)
            second_number = '2'

  the terminal_ shows :ref:`KeyError<test_key_error>`

    KeyError: 'QRS.TUVWXYZABCDEF'

* I add a :ref:`for loop<what is a for loop?>` for the button presses

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 7-9

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)
            second_number = '2'

            for character in first_number:
                self.tester.button(character).click().run()
            # self.tester.button(first_number).click().run()
            self.tester.button('+').click().run()

  I use :kbd:`ctrl+s` on the keyboard to run the test a few times, sometimes it passes and sometimes it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GH.IJKLMNOPQRSTUVW' != '-GH.IJKLMNOPQRSTUVW'

  there is no button for ``-`` it is ``+/-``

* I add a :ref:`condition<if statements>` to the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 2-3

            for character in first_number:
                if character == '-':
                    character = '+/-'
                self.tester.button(character).click().run()
            self.tester.button('+').click().run()



* I do the same thing with the second number

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 6-8

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)

            # second_number = '2'
            second_number = tests.test_calculator.a_random_number()
            second_number = str(second_number)

            for character in first_number:

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

----

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