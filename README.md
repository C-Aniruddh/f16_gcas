
ARCH benchmarks 2021
====================

Prerequisites
-------------
To create a benchmark environment, you will need to ensure you have Python 3.7
available on your system. If you are using ubuntu, this can be installed using
the [Deadsnakes PPA](https://https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
by running the command `sudo apt install python3.7 python3.7-dev`. You will
also need to ensure that you have `pip` and `pipenv` available on your path as
well. Pip can be installed using `sudo apt install python3-pip`and [Pipenv](https://pipenv.pypa.io/en/latest/)
can be installed using `python3 -m pip install --user pipenv`.

All of the benchmarks except for the F16 require the MATLAB engine for
python, which can be installed according to the instructions from
MathWorks found [here](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).

To install the benchmark environment you will need to export two environment
variables, `GITLAB_USER` and `GITLAB_TOKEN`, which is your GitLab username
and a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
respectively. Then run the command `pipenv install --site-packages` to install 
the benchmark dependencies into a virtual environment managed by `pipenv`.

Commands
--------
| Command |Description |
|---------|------------|
|`pipenv run list`| Print all available benchmarks |
|`pipenv run benchmark benchmark [benchmark, ...]` | Run specific benchmark(s) |
|`pipenv run all` | Run all available benchmarks |

Output
------
Each benchmark will produce a _.mat_ file which can be inspected with MATLAB. 
