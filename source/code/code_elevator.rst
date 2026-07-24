
#################################################################################
Elevator: tests and solutions
#################################################################################

----

*********************************************************************************
makePythonTdd Elevator
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    the code in ``makePythonTdd.sh`` from :ref:`Elevator`

      .. literalinclude:: elevator/make_tdd/makePythonTddElevator.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    the code in ``makePythonTdd.ps1`` from :ref:`Elevator`

      .. literalinclude:: elevator/make_tdd/makePythonTddElevator.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Elevator: tests
*********************************************************************************

the code in ``elevator/tests/test_elevator.py`` from :ref:`Elevator`

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :linenos:

----

*********************************************************************************
Elevator: solution
*********************************************************************************

the code in ``elevator/src/elevator.py`` from :ref:`Elevator`

.. literalinclude:: elevator/elevator.py
  :language: python
  :linenos:
