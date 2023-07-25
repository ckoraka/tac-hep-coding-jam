#include <Eigen/Dense>
#include <Eigen/Eigenvalues> 
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> thisSolver;

PYBIND11_MODULE(_eigenvalues, m) {

  m.def("eigenvalues", [](Eigen::MatrixXd matrix) {
    return thisSolver.compute(matrix).eigenvalues();
  },
    "Return eigenvalues of given matrix"
  );

}