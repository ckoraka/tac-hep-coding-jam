# Computational HEP Traineeship Summer School Coding Jam

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

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
