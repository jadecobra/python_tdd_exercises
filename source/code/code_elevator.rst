
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

    The code in ``makePythonTdd.sh`` from :ref:`Elevator`

    .. literalinclude:: elevator/make_tdd/makePythonTddElevator.sh
      :language: python
      :linenos:
      :emphasize-lines: 2-3, 5-6, 13, 21

  .. tab-item:: no WSL
    :sync: no_wsl

    The code in ``makePythonTdd.ps1`` from :ref:`Elevator`

    .. literalinclude:: elevator/make_tdd/makePythonTddElevator.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Elevator: tests
*********************************************************************************

The code in ``elevator/tests/test_elevator.py`` from :ref:`Elevator`

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :linenos:
  :caption: elevator/tests/test_elevator.py
  :lines: 1-23

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 25
  :caption: elevator/tests/test_elevator.py
  :lines: 25-41

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 43
  :caption: elevator/tests/test_elevator.py
  :lines: 43-59

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 61
  :caption: elevator/tests/test_elevator.py
  :lines: 61-77

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 79
  :caption: elevator/tests/test_elevator.py
  :lines: 79-95

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 97
  :caption: elevator/tests/test_elevator.py
  :lines: 97-113

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 115
  :caption: elevator/tests/test_elevator.py
  :lines: 115-131

.. literalinclude:: elevator/test_elevator.py
  :language: python
  :lineno-start: 133
  :caption: elevator/tests/test_elevator.py
  :lines: 133-

----

*********************************************************************************
Elevator: solution
*********************************************************************************

The code in ``elevator/src/elevator.py`` from :ref:`Elevator`

.. literalinclude:: elevator/elevator.py
  :language: python
  :linenos:
  :caption: elevator/src/elevator.py
