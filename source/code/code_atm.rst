
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

    the code in ``makePythonTdd.sh`` from :ref:`Automated Teller Machine`

    .. literalinclude:: atm/make_tdd/makePythonTddATM.sh
      :language: python
      :linenos:
      :emphasize-lines: 2-3, 5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    the code in ``makePythonTdd.ps1`` from :ref:`Automated Teller Machine`

    .. literalinclude:: atm/make_tdd/makePythonTddATM.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Automated Teller Machine: tests
*********************************************************************************

the code in ``atm/tests/test_atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/test_atm.py
  :language: python
  :linenos:

----

*********************************************************************************
Automated Teller Machine: solution
*********************************************************************************

the code in ``atm/src/atm.py`` from :ref:`Automated Teller Machine`

.. literalinclude:: atm/atm.py
  :language: python
  :linenos:
