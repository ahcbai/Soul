cmake_minimum_required(VERSION 3.15)
project(pylib_wrapper_project)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_COMPILE_WARNING_AS_ERROR ON)

# 1. Include pybind11
add_subdirectory(external/pybind11)

# 2. Add the subdirectory
# This triggers the execution of external/NeuSim/CMakeLists.txt
# and exposes the target neu_sim to the current scope
add_subdirectory(external/NeuSim)

# 3. Create the Python extension module
# The module name must match the name used in bindings.cpp
# and in the corresponding __init__.py import
pybind11_add_module(sim src/bindings.cpp)

# 4. Link the extension module with the standalone C++ library
# The target neu_sim is defined inside the added subdirectory
target_link_libraries(sim PRIVATE neu_sim)

# Get the directory where the current CMakeLists.txt is located
set(ROOT_DIR ${CMAKE_CURRENT_SOURCE_DIR})

# Force the generated library to be placed inside the Python package source directory
# Assuming your Python package folder is named pylib_wrapper
set_target_properties(sim PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${ROOT_DIR}/soul/backend/neusim"
    # On Windows, RUNTIME_OUTPUT_DIRECTORY must also be specified
    RUNTIME_OUTPUT_DIRECTORY "${ROOT_DIR}/soul/backend/neusim"
)