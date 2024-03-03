.. include:: ../links.rst

######################
ModuleNotFoundError
######################

The drill below will help you remember how to solve a ``ModuleNotFoundError`` in Python and what a python module is.

``ModuleNotFoundError`` is raised when python attempts to import a module that does not exist or it cannot find a given module name for an `import`` statement.
A Python Module is a file that ends in ``.py`` or a directory that contains an ``__init__.py``.

Programming allows us to gain from our previous efforts as well as the efforts of others in the form of packages and modules that can be distributed for other people to use. To use these packages in Python they have to be imported.

****************
requirements
****************


:doc:`How to make a Test Driven Development Environment </how_to/make_tdd_environment>`

----

*********************
red: make it fail
*********************

Open a new file in the Interactive Development Environment editor and save it as ``test_module_not_found_error.py`` in the ``tests`` folder made from :doc:`How to make a Test Driven Development Environment </how_to/make_tdd_environment>`

Type the following in the file

.. code-block:: python

  import module_0
  import module_1
  import module_2
  import module_3
  import module_4
  import module_5
  import module_6
  import module_7
  import module_8
  import module_9
  import module_10
  import module_11
  import module_12
  import module_13
  import module_14
  import module_15
  import module_16
  import module_17
  import module_18
  import module_19
  import module_20
  import module_21
  import module_22
  import module_23
  import module_24
  import module_25
  import module_26
  import module_27
  import module_28
  import module_29
  import module_30
  import module_34
  import module_32
  import module_33
  import module_34
  import module_35
  import module_36
  import module_37
  import module_38
  import module_39
  import module_40
  import module_41
  import module_42
  import module_43
  import module_44
  import module_45
  import module_46
  import module_47
  import module_48
  import module_49
  import module_50
  import module_51
  import module_52
  import module_53
  import module_54
  import module_55
  import module_56
  import module_57
  import module_58
  import module_59
  import module_60
  import module_61
  import module_62
  import module_63
  import module_64
  import module_65
  import module_66
  import module_67
  import module_68
  import module_69
  import module_70
  import module_71
  import module_72
  import module_73
  import module_74
  import module_75
  import module_76
  import module_77
  import module_78
  import module_79
  import module_80
  import module_81
  import module_82
  import module_83
  import module_84
  import module_85
  import module_86
  import module_87
  import module_88
  import module_89
  import module_90
  import module_91
  import module_92
  import module_93
  import module_94
  import module_95
  import module_96
  import module_97
  import module_98
  import module_99

If you left ``pytest-watch`` running from :doc:`How to make a Test Driven Development Environment </how_to/make_tdd_environment>` you should see something like the following in your terminal

.. code-block:: python

  ModuleNotFoundError: No module called 'module_0'

Looking at the traceback starting from the bottom


* ``ModuleNotFoundError`` is raised when an `import statement`_ fails because python cannot find a module/package with the given name, in this case ``module_0`` does not exist
* ``import module_0`` is the line of code that caused the failure
* Add the error to the list of Exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ImportError
    # ModuleNotFoundError

  If you want more information about imports you can read `The Import Statement <https://docs.python.org/3/reference/simple_stmts.html#import>`_

*********************
green: make it pass
*********************

* make ``module_0.py`` in the ``project_name`` folder and the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_1'

* make ``module_1.py`` in the ``project_name`` folder, the terminal shows the same error for a new line

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_2'

* make ``module_2.py`` in the ``project_name`` folder, the terminal shows the following

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_3'

* this is the pattern, repeat it until you have made ``module_99.py`` and the terminal shows a passing test

*WELL DONE!*
You are on your way to being a troubleshooting master.
You now know how to solve ``ModuleNotFoundError``

you encountered the following exceptions

* :ref:`AssertionError`
* ImportError
* :ref:`ModuleNotFoundError`