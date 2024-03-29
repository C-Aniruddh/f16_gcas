
F16 GCAS with updated PartX
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

To install the benchmark environment you will need to export two environment
variables, `GITLAB_USER` and `GITLAB_TOKEN`, which is your GitLab username
and a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
respectively. Then run the command `pipenv install --site-packages` to install 
the benchmark dependencies into a virtual environment managed by `pipenv`.

Commands
--------
| Command |Description |
|---------|------------|
|`poetry run python -m benchmark benchmark [benchmark, ...]` | Run specific benchmark(s) |
|`poetry run python -m benchmarks --all` | Run all available benchmarks |
|`poetry run python -m benchmarks --list`|Print all available benchmarks|

Output
------
Each benchmark will produce a _.mat_ file which can be inspected with MATLAB. 
