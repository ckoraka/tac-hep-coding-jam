#include <Eigen/Dense>
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

Eigen::LLT<Eigen::MatrixXf> foo;

PYBIND11_MODULE(_eigenLLT, m) {

  m.def("matrix", [](int size) {
    Eigen::MatrixXf arr{size, size};
    arr.setZero();
    return arr;
  });

  m.def(
      "computeAndSolve",
      [](Eigen::MatrixXf a, Eigen::MatrixXf b) {
        foo.compute(a);
        return foo.solve(b);
      },
      "Compute Eigenvales of Matrix A to solve b = Ax problem. A = LL^T");
}