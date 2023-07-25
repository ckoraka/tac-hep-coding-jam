#include <Eigen/Eigenvalues>
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(real_matrices, m) {

  m.def("eigenvectors", [](Eigen::MatrixXf matrix) {
    Eigen::EigenSolver<Eigen::MatrixXf> es(matrix);
    return es.eigenvectors();
  });

  m.def("eigenvalues", [](Eigen::MatrixXf matrix) {
    Eigen::EigenSolver<Eigen::MatrixXf> es(matrix);
    return es.eigenvalues();
  });

  m.def("eigenvectors", [](Eigen::MatrixXd matrix) {
    Eigen::EigenSolver<Eigen::MatrixXd> es(matrix);
    return es.eigenvectors();
  });

  m.def("eigenvalues", [](Eigen::MatrixXd matrix) {
    Eigen::EigenSolver<Eigen::MatrixXd> es(matrix);
    return es.eigenvalues();
  });
}
