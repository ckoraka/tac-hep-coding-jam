cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

include(FetchContent)
FetchContent_Declare(
  eigen
  URL https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.bz2
  URL_HASH
    SHA256=b4c198460eba6f28d34894e3a5710998818515104d6e74e5cc331ce31e46e626
  SOURCE_SUBDIR ignore_cmakelists)
FetchContent_MakeAvailable(eigen)

pybind11_add_module(_core MODULE src/main.cpp)
pybind11_add_module(_eigenvalues MODULE
                    src/selfAdjointEigenSolver.cpp)

target_include_directories(_core PRIVATE "${eigen_SOURCE_DIR}")
target_include_directories(_eigenvalues PRIVATE "${eigen_SOURCE_DIR}")

install(TARGETS _core _eigenvalues DESTINATION ${SKBUILD_PROJECT_NAME})
pybind11_add_module(real_matrices MODULE src/real_matrices.cpp)
target_include_directories(_core PRIVATE "${eigen_SOURCE_DIR}")
target_include_directories(real_matrices PRIVATE "${eigen_SOURCE_DIR}")
install(TARGETS _core real_matrices DESTINATION ${SKBUILD_PROJECT_NAME})
