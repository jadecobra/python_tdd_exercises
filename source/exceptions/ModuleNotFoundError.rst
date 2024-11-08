.. include:: ../links.rst

.. _ModuleNotFoundError:

#################################################################################
ModuleNotFoundError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

The drill below will help you remember how to solve a ``ModuleNotFoundError`` in Python and what a Python module is.

``ModuleNotFoundError`` is raised when Python attempts to import a module that does not exist or it cannot find a given module name for an `import statement`_.
A Python Module is a file that ends in ``.py`` or a directory that has an ``__init__.py``.

Programming allows us to gain from our previous efforts as well as the efforts of others in the form of packages and modules that can be distributed for other people to use. To use these packages in Python they have to be imported.

*********************************************************************************
requirements
*********************************************************************************


:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

----

*********************************************************************************
red: make it fail
*********************************************************************************

Open a new file in the Integrated Development Environment editor and save it as ``test_module_not_found_error.py`` in the ``tests`` folder made from :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

Type the following in the file

.. code-block:: python

  import src.module_0
  import src.module_1
  import src.module_2
  import src.module_3
  import src.module_4
  import src.module_5
  import src.module_6
  import src.module_7
  import src.module_8
  import src.module_9
  import src.module_10
  import src.module_11
  import src.module_12
  import src.module_13
  import src.module_14
  import src.module_15
  import src.module_16
  import src.module_17
  import src.module_18
  import src.module_19
  import src.module_20
  import src.module_21
  import src.module_22
  import src.module_23
  import src.module_24
  import src.module_25
  import src.module_26
  import src.module_27
  import src.module_28
  import src.module_29
  import src.module_30
  import src.module_34
  import src.module_32
  import src.module_33
  import src.module_34
  import src.module_35
  import src.module_36
  import src.module_37
  import src.module_38
  import src.module_39
  import src.module_40
  import src.module_41
  import src.module_42
  import src.module_43
  import src.module_44
  import src.module_45
  import src.module_46
  import src.module_47
  import src.module_48
  import src.module_49
  import src.module_50
  import src.module_51
  import src.module_52
  import src.module_53
  import src.module_54
  import src.module_55
  import src.module_56
  import src.module_57
  import src.module_58
  import src.module_59
  import src.module_60
  import src.module_61
  import src.module_62
  import src.module_63
  import src.module_64
  import src.module_65
  import src.module_66
  import src.module_67
  import src.module_68
  import src.module_69
  import src.module_70
  import src.module_71
  import src.module_72
  import src.module_73
  import src.module_74
  import src.module_75
  import src.module_76
  import src.module_77
  import src.module_78
  import src.module_79
  import src.module_80
  import src.module_81
  import src.module_82
  import src.module_83
  import src.module_84
  import src.module_85
  import src.module_86
  import src.module_87
  import src.module_88
  import src.module_89
  import src.module_90
  import src.module_91
  import src.module_92
  import src.module_93
  import src.module_94
  import src.module_95
  import src.module_96
  import src.module_97
  import src.module_98
  import src.module_99

If you left ``pytest-watch`` running from :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` you should see something like the following in your terminal

.. code-block:: python

  ModuleNotFoundError: No module called 'module_0'

Looking at the traceback starting from the bottom

* ``ModuleNotFoundError`` is raised when an `import statement`_ fails because python cannot find a module/package with the given name, in this case ``module_0`` does not exist
* ``import module_0`` is the line of code that caused the failure
* Add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

  If you want more information about imports you can read `The Import Statement <https://docs.python.org/3/reference/simple_stmts.html#import>`_

*********************************************************************************
green: make it pass
*********************************************************************************

* make ``module_0.py`` in the ``magic`` folder and the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_1'

* make ``module_1.py`` in the ``magic`` folder, the terminal shows the same error for a new line

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_2'

* make ``module_2.py`` in the ``magic`` folder, the terminal shows the following

  .. code-block:: python

    ModuleNotFoundError: No module called 'module_3'

* this is the pattern, repeat it until you have made ``module_99.py`` and the terminal shows a passing test

----

*********************************************************************************
review
*********************************************************************************

*WELL DONE!*
You are on your way to being a troubleshooting master.
You now know how to solve ``ModuleNotFoundError``

you encountered the following exceptions

* :ref:`AssertionError`
* ImportError_
* :ref:`ModuleNotFoundError`

Would you like to test :ref:`AssertionErrors<AssertionError>`?