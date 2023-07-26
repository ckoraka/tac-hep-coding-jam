#include <Eigen/Dense>
#include <iostream>
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

Eigen::LLT<Eigen::MatrixXf> foo;
Eigen::LLT<Eigen::MatrixXd> bar;

PYBIND11_MODULE(_eigenLLT, m) {

  m.def("matrix", [](int size) {
    Eigen::MatrixXf arr{size, size};
    arr.setZero();
    return arr;
  });

  m.def(
      "computeAndSolve",
      [](Eigen::MatrixXf a, Eigen::MatrixXf b) {
        std::cout << "Here is the matrix A:\n" << a << std::endl;
        std::cout << "Here is the right hand side b:\n" << b << std::endl;
        std::cout << "Computing LLT decomposition..." << std::endl;
        foo.compute(a);
        std::cout << "The solution is:\n" << foo.solve(b) << std::endl;
        return foo.solve(b);
      },
      "Compute Eigenvales of Matrix A to solve b = Ax problem. A = LL^T");

  m.def(
      "computeAndSolve",
      [](Eigen::MatrixXd a, Eigen::MatrixXd b) {
        std::cout << "Here is the matrix A:\n" << a << std::endl;
        std::cout << "Here is the right hand side b:\n" << b << std::endl;
        std::cout << "Computing LLT decomposition..." << std::endl;
        bar.compute(a);
        std::cout << "The solution is:\n" << bar.solve(b) << std::endl;
        return bar.solve(b);
      },
      "Compute Eigenvales of Matrix A to solve b = Ax problem. A = LL^T");
}
