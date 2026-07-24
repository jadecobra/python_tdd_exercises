
#################################################################################
Parking Garage: tests and solutions
#################################################################################

----

*********************************************************************************
makePythonTdd ParkingGarage
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    the code in ``makePythonTdd.sh`` from :ref:`Parking Garage`

      .. literalinclude:: parking_garage/make_tdd/makePythonTddParkingGarage.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    the code in ``makePythonTdd.ps1`` from :ref:`Parking Garage`

      .. literalinclude:: parking_garage/make_tdd/makePythonTddParkingGarage.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Parking Garage: tests
*********************************************************************************

the code in ``parking_garage/tests/test_parking_garage.py`` from :ref:`Parking Garage`

.. literalinclude:: parking_garage/test_parking_garage.py
  :language: python
  :linenos:

----

*********************************************************************************
Parking Garage: solution
*********************************************************************************

the code in ``parking_garage/src/parking_garage.py`` from :ref:`Parking Garage`

.. literalinclude:: parking_garage/parking_garage.py
  :language: python
  :linenos:
