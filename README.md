# Computational HEP Traineeship Summer School Coding Jam

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/ckoraka/tac-hep-coding-jam.git/workflows/CI/badge.svg
[actions-link]:             https://github.com/ckoraka/tac-hep-coding-jam.git/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/tac-hep-coding-jam
[conda-link]:               https://github.com/conda-forge/tac-hep-coding-jam-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/ckoraka/tac-hep-coding-jam.git/discussions
[pypi-link]:                https://pypi.org/project/tac-hep-coding-jam/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/tac-hep-coding-jam
[pypi-version]:             https://img.shields.io/pypi/v/tac-hep-coding-jam
[rtd-badge]:                https://readthedocs.org/projects/tac-hep-coding-jam/badge/?version=latest
[rtd-link]:                 https://tac-hep-coding-jam.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

# Groups for each task

1. Connect interesting C++ functions to Python through pybind11.

- Choose some functions from the
  [eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) library. Some
  ideas :
  - [GeneralizedSelfAdjointEigenSolver](https://eigen.tuxfamily.org/dox/classEigen_1_1GeneralizedSelfAdjointEigenSolver.html),
    [LLT](https://eigen.tuxfamily.org/dox/classEigen_1_1LLT.html),
    [SelfAdjointEigenSolver](https://eigen.tuxfamily.org/dox/classEigen_1_1SelfAdjointEigenSolver.html)
    etc.

2. Make a Pythonic interface on the Python side, with type hints, docstrings
   etc.
3. Check for similar python functions (e.g. in NumPy or SciPy). If they exist,
   check and compare the performance with respect to the C++ eigen functions
   when intefraced with and called from python.
4. Write a suite of unit tests for the Pythonic interface, possibly using
   hypothesis to generate edge cases automatically.
   - Take note that some of the eigen functions have specific requirements for
     the matrices can act upon.
5. Use Sphinx to write documentation, including autodoc to turn docstrings and
   argument lists into reference documentation automatically.
6. One group responsible for reviewing PRs and merging them. (Members can be
   involved in other groups, since there won't be anything to do _at first_.)

# Before you push commits

Compile and install the package (from inside the tac-hep-coding-jam directory):

```
% pip install .
Processing /Users/jpivarski/talks/tac-hep-coding-jam
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy in /Users/jpivarski/mambaforge/lib/python3.10/site-packages (from tac-hep-coding-jam==0.1.0) (1.23.5)
Building wheels for collected packages: tac-hep-coding-jam
  Building wheel for tac-hep-coding-jam (pyproject.toml) ... done
  Created wheel for tac-hep-coding-jam: filename=tac_hep_coding_jam-0.1.0-cp310-cp310-macosx_13_0_arm64.whl size=49413 sha256=a342d6d2bce19f95f67f7fe24d99aa1ac0adca4f187a60ee1383a9db719df8fa
  Stored in directory: /Users/jpivarski/Library/Caches/pip/wheels/ca/1d/fb/1d0c9752ca1f7af54c59e5ca0aade6d00b1186c27e29c84c30
Successfully built tac-hep-coding-jam
Installing collected packages: tac-hep-coding-jam
  Attempting uninstall: tac-hep-coding-jam
    Found existing installation: tac-hep-coding-jam 0.1.0
    Uninstalling tac-hep-coding-jam-0.1.0:
      Successfully uninstalled tac-hep-coding-jam-0.1.0
Successfully installed tac-hep-coding-jam-0.1.0
```

Check the code quality:

```
% pre-commit run --all-files 
black-jupyter............................................................Passed
blacken-docs.............................................................Passed
check for added large files..............................................Passed
check for case conflicts.................................................Passed
check for merge conflicts................................................Passed
check for broken symlinks............................(no files to check)Skipped
check yaml...............................................................Passed
debug statements (python)................................................Passed
fix end of files.........................................................Passed
mixed line ending........................................................Passed
python tests naming......................................................Passed
fix requirements.txt.................................(no files to check)Skipped
trim trailing whitespace.................................................Passed
rst ``code`` is two backticks........................(no files to check)Skipped
rst directives end with two colons...................(no files to check)Skipped
rst ``inline code`` next to normal text..............(no files to check)Skipped
prettier.................................................................Passed
ruff.....................................................................Passed
clang-format.............................................................Passed
mypy.....................................................................Passed
codespell................................................................Passed
shellcheck...........................................(no files to check)Skipped
Disallow improper capitalization.........................................Passed
cmake-format.............................................................Passed
```

Run the tests:

```
% pytest tests
================================= test session starts =================================
platform darwin -- Python 3.10.8, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/jpivarski/talks/tac-hep-coding-jam
configfile: pyproject.toml
plugins: timeout-2.1.0, cov-4.1.0, anyio-3.7.1, typeguard-2.13.3, xdist-3.3.1
collected 4 items                                                                     

tests/test_compiled.py ...                                                      [ 75%]
tests/test_package.py .                                                         [100%]

================================== 4 passed in 0.23s ==================================
```

Build the documentation (optional):

```
nox -s docs -- --serve
```

(Copied from issue #4.)
