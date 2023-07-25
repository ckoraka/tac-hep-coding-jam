# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.22.1)

# We name the project and the target for the ExternalProject_Add() call
# to something that will highlight to the user what we are working on if
# something goes wrong and an error message is produced.

project(eigen-populate NONE)



include(ExternalProject)
ExternalProject_Add(eigen-populate
                     "UPDATE_DISCONNECTED" "False" "URL" "https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.bz2" "URL_HASH" "SHA256=b4c198460eba6f28d34894e3a5710998818515104d6e74e5cc331ce31e46e626" "SOURCE_SUBDIR" "ignore_cmakelists"
                    SOURCE_DIR          "/home/mmaroun/tac-hep-coding-jam/_deps/eigen-src"
                    BINARY_DIR          "/home/mmaroun/tac-hep-coding-jam/_deps/eigen-build"
                    CONFIGURE_COMMAND   ""
                    BUILD_COMMAND       ""
                    INSTALL_COMMAND     ""
                    TEST_COMMAND        ""
                    USES_TERMINAL_DOWNLOAD  YES
                    USES_TERMINAL_UPDATE    YES
)


