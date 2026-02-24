.. meta::
  :description: Learn how to turn your TDD calculator into a beautiful, interactive web app using Streamlit — the easiest way to build data apps in Python. No HTML, no routes, just pure Python.
  :keywords: Jacob Itegboje, streamlit python tutorial, streamlit tdd calculator, python streamlit web app, streamlit calculator project, easy python web apps with tdd

.. include:: ../links.rst

#################################################################################
how to make a calculator 10
#################################################################################

I have a solid calculator from chapters 1–8 and a Flask website from chapter 9.
Now I want to make it **beautiful and ridiculously easy** to use by turning it into a modern web app with **Streamlit**.

Streamlit lets me build professional-looking web apps with almost no extra code.

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

* I install Streamlit

  .. code-block:: shell
    :emphasize-lines: 1

    uv add streamlit

* I use ``pytest-watcher`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    uv run pytest-watcher . --now

* I create a new test file for the Streamlit version

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_calculator_streamlit.py

----

*********************************************************************************
test_streamlit_installed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I open ``tests/test_calculator_streamlit.py`` and write

.. code-block:: python
  :linenos:

  import unittest
  import streamlit as st

  class TestCalculatorStreamlit(unittest.TestCase):

      def test_streamlit_can_be_imported(self):
          self.assertIsNotNone(st)

the terminal shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I already ran ``uv add streamlit``, so the test passes.

----

*********************************************************************************
test_streamlit_calculator_app
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the app itself

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