
#################################################################################
Automated Teller Machine: tests and solutions
#################################################################################

----

*********************************************************************************
makePythonTdd ATM
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    The code in ``makePythonTdd.sh`` from :ref:`Automated Teller Machine`

    .. literalinclude:: atm/make_tdd/makePythonTddATM.sh
      :language: python
      :linenos:
      :emphasize-lines: 2-3, 10, 18

  .. tab-item:: no WSL
    :sync: no_wsl

    The code in ``makePythonTdd.ps1`` from :ref:`Automated Teller Machine`

    .. literalinclude:: atm/make_tdd/makePythonTddATM.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-2, 9, 17

----

*********************************************************************************
Automated Teller Machine: tests
*********************************************************************************

The code in ``atm/tests/test_atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :linenos:
  :lines: 1-28

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 30
  :lines: 30-48

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 50
  :lines: 50-68

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 70
  :lines: 70-88

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 90
  :lines: 90-108

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 110
  :lines: 110-128

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 130
  :lines: 130-148

.. literalinclude:: atm/tests/test_atm.py
  :caption: atm/tests/test_atm.py
  :language: python
  :lineno-start: 150
  :lines: 150-

----

*********************************************************************************
Automated Teller Machine: solution
*********************************************************************************

The code in ``atm/src/atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/src/atm.py
  :caption: atm/src/__init__.py
  :language: python
  :linenos:
