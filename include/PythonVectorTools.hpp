#ifndef TO_STD_VECTOR_HPP_
#define TO_STD_VECTOR_HPP_

#include <boost/python.hpp>
#include <boost/python/stl_iterator.hpp>
#include <vector>

// Code to convert python objects to STL vectors for use in C++.
// The alternative is to make an equivalent to the STL object in Python
// and just use that. That is in the main_python.cpp file.
template<typename T>
    std::vector<T> ToStdVector(const boost::python::object& x)
{
  return std::vector<T>(boost::python::stl_input_iterator<T>(x),
      boost::python::stl_input_iterator<T>());
}

// Does the reverse, converts STL vector to a Python list for use in Python.
// The alternative is to read the STL vector into an equivalent STL object
// in Python and use that. The code for that is in the main_python.cpp file.
template<typename T>
    boost::python::list FromStdVector(const std::vector<T>& x)
{
  boost::python::list the_list;
  for (auto entry : x) the_list.append(entry);
  return the_list;
}

#endif // TO_STD_VECTOR_HPP_








