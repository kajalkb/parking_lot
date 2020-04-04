Directory structure
========================
parking_lot/
│
├── bin/
│   └── setup.sh
|   └── parking_lot.py
|   └── run_functional_specs.py
|
└── run_functional_specs
|    └── fixtures
|      └── file_inputs.txt
|     
|
└──

Development and testing infrastructure -
=========================================
1. Used Virtual Box and Ubuntu 18.04
2. Solution is built with python 3.6.9. This is by default installed in Ubuntu 18.04
2. Ran and build the code on Ubuntu
3. Used VS code to write the solution.
4. Use Git to do all checkins form the the Ubuntu 18.04

Unzip the tar ball 
===================

Application module -
========================
1. Primary application is parking_lot.py found under parking_lot\bin directory
2. On the terminal go to the bin directory.
3. Run the command -
python3 parking_lot.py
4. For interactive mode pass the commands one bye one...
5. For file mode pass like(copy file_input.ext to the bin directory
from functional_spec\fixtures) -
python3 parking_lot.py file_input.txt

Testing module -
===================
1. Using unittest, the run_functional_specs.py is written which has a series of unit tests.
2. This is a suite of automated unit test thats implemented using a practise of test driven development.
3. Its under parking_lot\bin directory
4. Run the following command to execute this, go to the bin directory first -
bash setup.sh


