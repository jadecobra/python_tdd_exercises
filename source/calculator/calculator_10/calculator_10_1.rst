.. include:: calculator_links.rst

#################################################################################
how to make a calculator 10: part 1
#################################################################################

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

* I check to see what is in my ``requirements.txt``

  .. code-block:: python
    :emphasize-lines: 1

    cat requirements.txt

  the terminal_ shows

  .. code-block:: python

    pytest
    pytest-watcher
    flask
    streamlit

* I install the `Python packages`_ that I wrote in the requirements file_

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

    ======================== 8 passed in X.YZs =========================

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

* I make a new file_ in the ``src`` folder_ and call it ``streamlit_calculator.py``

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
how to see the streamlit calculator website
*********************************************************************************

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

* I click the check marks by ``Run on save`` and ``Wide mode`` to make sure the website changes as I make changes to the code

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

I see that the ``children`` :ref:`object<what is a class?>` is a :ref:`dictionary<what is a dictionary?>`. I know how to work with :ref:`dictionaries<what is a dictionary?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

-----

* I add an expectation with the ``children`` :ref:`attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

            self.assertIsNone(tester.main.children, {})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0: Title(tag='h1')} is not None : {}

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1
    :emphasize-text: assertEqual children { }

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

* I remove ``self.maxDiff``

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

I made a website using Streamlit_ with a :ref:`title<test_streamlit_calculator_title>` and a :ref:`display<test_streamlit_calculator_display>`

* :ref:`How to add a title to a Streamlit Application<test_streamlit_calculator_title>`
* :ref:`How to see the Streamlit Calculator Website<how to see the streamlit calculator website>`
* :ref:`How to make a display for the application<test_streamlit_calculator_display>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know how to:

* Build a website with streamlit_
* How to test the parts of the website
* :ref:`How to add a title to the streamlit website<test_streamlit_calculator_title>`
* :ref:`How to add a display to the streamlit website<test_streamlit_calculator_display>`

:ref:`Would you like to continue with adding buttons to the calculator?<how to make a calculator 10: part 2>`