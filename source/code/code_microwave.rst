
#################################################################################
Microwave: tests and solutions
#################################################################################

----

*********************************************************************************
makePythonTdd Microwave
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    the code in ``makePythonTdd.sh`` from :ref:`Microwave`

      .. literalinclude:: microwave/make_tdd/makePythonTddMicrowave.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

  .. tab-item:: no WSL
    :sync: no_wsl

    the code in ``makePythonTdd.ps1`` from :ref:`Microwave`

      .. literalinclude:: microwave/make_tdd/makePythonTddMicrowave.ps1
        :language: Powershell
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

----

*********************************************************************************
Microwave: tests
*********************************************************************************

the code in ``microwave/tests/test_microwave.py`` from :ref:`Microwave`

.. literalinclude:: microwave/test_microwave.py
  :language: python
  :linenos:

----

*********************************************************************************
Microwave: solution
*********************************************************************************

the code in ``microwave/src/microwave.py`` from :ref:`Microwave`

.. literalinclude:: microwave/microwave.py
  :language: python
  :linenos:
