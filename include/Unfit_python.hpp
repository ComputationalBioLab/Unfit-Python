#ifndef MAIN_PYTHON_HPP_
#define MAIN_PYTHON_HPP_

#include <vector>
#include <boost/python.hpp>
#include "Unfit.hpp"

namespace Unfit
{

class GenericCostFunctionWrap : public GenericCostFunction, public boost::python::wrapper<GenericCostFunction>
{
 public:
  virtual ~GenericCostFunctionWrap() {};
  std::vector<double> operator()(const std::vector<double>& x);
};

class GenericOptimizerWrap : public GenericOptimizer, public boost::python::wrapper<GenericOptimizer>
{
 public:
  virtual ~GenericOptimizerWrap() {};
  virtual int FindMin(GenericCostFunction &cost_function,
      std::vector<double> &coordinates) = 0;
  virtual void Reset() = 0;
};

}

/*
class DummyOptimiser
{
 public:
   virtual ~DummyOptimiser() {};
   int FindMin(GenericCostFunction &CostFunction, std::vector<double> &coordinates);
};
*/

#endif // MAIN_PYTHON_HPP_
