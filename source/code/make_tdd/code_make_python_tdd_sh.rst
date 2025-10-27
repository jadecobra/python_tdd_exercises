.. include:: ../../links.rst

#################################################################################
makePythonTdd.sh
#################################################################################

* Here is the ``./makePythonTdd.sh`` program from :doc:`/how_to/make_tdd/make_tdd_environment`

  .. literalinclude:: makePythonTdd.sh
    :language: shell

* use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x makePythonTdd.sh

* give a name for the ``$PROJECT_NAME`` variable when the program is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal in the folder where ``makePythonTdd.sh`` is saved will make a `Test Driven Development`_ environment for a project called :ref:`calculator<how to make a calculator>`

  .. code-block:: shell

    ./makePythonTdd.sh calculator