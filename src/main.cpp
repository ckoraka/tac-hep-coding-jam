#include <Eigen/Dense>
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

int add(int i, int j) { return i + j; }

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.def("add", &add, "Add two numbers");

  m.def(
      "subtract", [](int i, int j) { return i - j; }, "Subtract two numbers");

  m.def("matrix", [](int size) {
    Eigen::MatrixXd arr{size, size};
    arr.setZero();
    return arr;
  });
}
