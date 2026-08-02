
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
      :emphasize-lines: 2-5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    The code in ``makePythonTdd.ps1`` from :ref:`Automated Teller Machine`

    .. literalinclude:: atm/make_tdd/makePythonTddATM.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-4, 11, 19

----

*********************************************************************************
Automated Teller Machine: tests
*********************************************************************************

The code in ``atm/tests/test_atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/test_atm.py
  :language: python
  :linenos:
  :caption: atm/tests/test_atm.py
  :lines: 1-28

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 30
  :caption: atm/tests/test_atm.py
  :lines: 30-48

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 50
  :caption: atm/tests/test_atm.py
  :lines: 50-68

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 70
  :caption: atm/tests/test_atm.py
  :lines: 70-88

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 90
  :caption: atm/tests/test_atm.py
  :lines: 90-108

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 110
  :caption: atm/tests/test_atm.py
  :lines: 110-128

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 130
  :caption: atm/tests/test_atm.py
  :lines: 130-148

.. literalinclude:: atm/test_atm.py
  :language: python
  :lineno-start: 150
  :caption: atm/tests/test_atm.py
  :lines: 150-

----

*********************************************************************************
Automated Teller Machine: solution
*********************************************************************************

The code in ``atm/src/atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/atm.py
  :language: python
  :linenos:
  :caption: atm/src/atm.py
