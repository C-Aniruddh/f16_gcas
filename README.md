arch-benchmarks
===============

Installation
------------
To create a benchmark environment, you will need to ensure you have Python 3.7
available on your system. If you are using ubuntu, this can be installed using
the [Deadsnakes PPA](https://https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
by running the command `sudo apt install python3.7 python3.7-dev`. You will
also need to ensure that you have `pip` and `pipenv` available on your path as
well. Pip can be installed using `sudo apt install python3-pip` and Pipenv
can be installed using `python3 -m pip install --user pipenv`. Finally, you will
need to ensure that you have installed the MATLAB engine for python using
according to the following [documentation](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
from mathworks.

Running
-------
To run the benchmarks, first you will need to activate the generated
virtualenv, which can be accomplished using the command `pipenv shell`. A list
of all the benchmarks can be found by running the command
`python -m benchmarks --list`. An individual benchmark can be run using the
command `python -m benchmarks <benchmark>` and all of the benchmarks can be run
using the command `python -m benchmarks --all`. Each benchmark will provide a
_.mat_ file which can be inspected with MATLAB.

