.. include:: ../../links.rst

#################################################################################
makePythonTdd.sh
#################################################################################

----

*********************************************************************************
makePythonTdd.sh program
*********************************************************************************

* Here is the ``makePythonTdd.sh`` program_ from :ref:`how to make a python test driven development environment`

  .. literalinclude:: makePythonTdd.sh
    :language: shell
    :linenos:

* use ``chmod`` to make the program_ executable

  .. code-block:: python
    :emphasize-lines: 1

    chmod +x makePythonTdd.sh

* give a name for the ``PROJECT_NAME`` :ref:`variable<test_attribute_error_w_variables>` when the program_ is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal_ in the folder_ where ``makePythonTdd.sh`` is saved makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project with the name :ref:`person<how to make a person>`

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh person

----

*********************************************************************************
BONUS: makePythonTdd.sh Plus
*********************************************************************************

Since you are the adventurous type and made it this deep in the book, I have added extra lines that

* make the project with ``PROJECT_NAME`` as the name if you do not give a name
* make the class name in :ref:`CapWords format<CapWords>`
* open the test file and source file in your editor

.. literalinclude:: makePythonTddPlus.sh
  :language: shell
  :linenos:
  :emphasize-lines: 2-6, 8-10, 12, 14, 29-30

this works with `Visual Studio Code`_ you can change it to use the command for any `Integrated Development Environment (IDE)`_ you like