
#################################################################################
Car: tests and solutions
#################################################################################

----

*********************************************************************************
makePythonTdd Car
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    The code in ``makePythonTdd.sh`` from :ref:`Car`

    .. literalinclude:: car/make_tdd/makePythonTddCar.sh
      :language: python
      :linenos:
      :emphasize-lines: 2-3, 10, 18

  .. tab-item:: no WSL
    :sync: no_wsl

    The code in ``makePythonTdd.ps1`` from :ref:`Car`

    .. literalinclude:: car/make_tdd/makePythonTddCar.ps1
      :language: Powershell
      :linenos:
      :emphasize-lines: 1-2, 9, 17

----

*********************************************************************************
Car: tests
*********************************************************************************

The code in ``car/tests/test_car.py`` from :ref:`Car`

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :linenos:
  :lines: 1-23

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 25
  :lines: 25-41

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 43
  :lines: 43-59

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 61
  :lines: 61-77

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 79
  :lines: 79-95

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 97
  :lines: 97-113

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 115
  :lines: 115-131

.. literalinclude:: car/test/test_car.py
  :caption: car/tests/test_car.py
  :language: python
  :lineno-start: 133
  :lines: 133-

----

*********************************************************************************
Car: solution
*********************************************************************************

The code in ``car/src/__init__.py`` from :ref:`Car`

.. literalinclude:: car/src/car.py
  :language: python
  :linenos:
  :caption: car/src/car.py
