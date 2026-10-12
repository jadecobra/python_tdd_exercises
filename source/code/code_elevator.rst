
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
      :emphasize-lines: 2-3, 10, 18

  .. tab-item:: no WSL
    :sync: no_wsl

    The code in ``makePythonTdd.ps1`` from :ref:`Elevator`

    .. literalinclude:: elevator/make_tdd/makePythonTddElevator.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-2, 9, 17

----

*********************************************************************************
Elevator: tests
*********************************************************************************

The code in ``elevator/tests/test_elevator.py`` from :ref:`Elevator`

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :linenos:
  :lines: 1-23

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 25
  :lines: 25-41

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 43
  :lines: 43-59

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 61
  :lines: 61-77

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 79
  :lines: 79-95

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 97
  :lines: 97-113

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 115
  :lines: 115-131

.. literalinclude:: elevator/test_elevator.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :lineno-start: 133
  :lines: 133-

----

*********************************************************************************
Elevator: solution
*********************************************************************************

The code in ``elevator/src/elevator/__init__.py`` from :ref:`Elevator`

.. literalinclude:: elevator/src/elevator.py
  :caption: elevator/src/elevator/__init__.py
  :language: python
  :linenos:
