Directory structure
========================
parking_lot/bin/setup.sh
parking_lot/bin/parking_lot.py
parking_lot/bin/unit_tests.py
parking_lot/bin/run_functional_tests

parking_lot/run_functional_specs/fixtures/file_inputs.txt
parking_lot/run_functional_specs/spec/end_to_end_spec.rb
parking_lot/run_functional_specs/spec/parking_lot_spec.rb
parking_lot/run_functional_specs/spec/spec_helper.rb

Development and testing infrastructure -
=========================================
1. Used Virtual Box and Ubuntu 18.04
2. Solution is built with python 3.6.9. This is by default installed in Ubuntu 18.04
2. Ran and build the code on Ubuntu
3. Used VS code to write the solution.
4. Development done on Ubuntu 18.04 and used Git to do all checkins.
5. The application executes successfully on macOS Mojave version 10.14.4 with unit and functional tests. Also, all the unit test and functional spec testing is done on Ubuntu.

Application module -
========================
1. Primary application is parking_lot.py found under parking_lot\bin directory
2. On the terminal go to the bin directory.
3. Run the command -
python3 parking_lot.py
4. For interactive mode pass the commands one bye one...
5. For file mode pass like the following (but copy file_input.ext to the bin directory
from functional_spec\fixtures) -
python3 parking_lot.py file_input.txt

Testing module(automated unit test) -
======================================
1. Using unittest, the unit_tests.py is written which has a series of unit tests for the helper functions.
2. This is a suite of automated unit test thats implemented using a practise of test driven development.
3. Its under parking_lot\bin directory
4. Run the following command to execute this, go to the bin directory first from the terminal -
bash setup.sh

Functional tests -
===================
1. updated the python3 command and parking_lot.py file path in the  pty.spawn command in end_to_end_spec.rb and in parking_lot_spec.rb.
For example ---> PTY.spawn("python3 /Users/kajalbiswas/Documents/work/practisePython/parking_lot/bin/parking_lot.py")
2. And ran command -->
parking_lot $ bin/run_functional_test
3. On Mac machine it ran successfully. 
3. On the linux machine with Ubuntu, I'd to do one more step to run the functional specs successfully. The gem file did not get created while creating the environment. So, I copied the gemfile/rakefiles from the mac machine to Ubuntu box and ran the functional tests with bin/run_functional_test and it worked fine.
