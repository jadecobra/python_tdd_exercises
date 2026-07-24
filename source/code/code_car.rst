
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

    the code in ``makePythonTdd.sh`` from :ref:`Car`

      .. literalinclude:: car/make_tdd/makePythonTddCar.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    the code in ``makePythonTdd.ps1`` from :ref:`Car`

      .. literalinclude:: car/make_tdd/makePythonTddCar.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Car: tests
*********************************************************************************

the code in ``car/tests/test_car.py`` from :ref:`Car`

.. literalinclude:: car/test_car.py
  :language: python
  :linenos:

----

*********************************************************************************
Car: solution
*********************************************************************************

the code in ``car/src/car.py`` from :ref:`Car`

.. literalinclude:: car/car.py
  :language: python
  :linenos:
