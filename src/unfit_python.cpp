#include <vector>
#include <iostream>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include "Unfit_python.hpp"
#include "Unfit.hpp"

std::vector<double> Unfit::GenericCostFunctionWrap::operator()(const std::vector<double>& x)
{
  return this->get_override("__call__")(x);
}

BOOST_PYTHON_MODULE(libUnfitPython)
{
  boost::python::class_<std::vector<double>>("std_vector_double")
      .def(boost::python::vector_indexing_suite<std::vector<double>>())
  ;
  boost::python::class_<Unfit::GenericCostFunctionWrap, boost::noncopyable>("GenericCostFunction")
      .def("__call__", boost::python::pure_virtual(&Unfit::GenericCostFunction::operator()), boost::python::args("x"))
  ;

  //Wrapper for Options::GetNelderMeadStepSizes, since it takes reference to double
  struct wrapper{
    static boost::python::tuple GetNelderMeadStepSizes(Unfit::Options &options){
        double alpha, beta, delta, gamma;
        options.GetNelderMeadStepSizes(alpha, beta, delta, gamma);
        return boost::python::make_tuple(alpha, beta, delta, gamma);
    }
  };

  boost::python::class_<Unfit::Options>("Options")
       .def("GetCostTolerance", &Unfit::Options::GetCostTolerance)
       .def("SetCostTolerance", &Unfit::Options::SetCostTolerance, boost::python::args("tolerance"))
       .def("GetDegenerateTolerance", &Unfit::Options::GetDegenerateTolerance)
       .def("SetDegenerateTolerance", &Unfit::Options::SetDegenerateTolerance, boost::python::args("tolerance"))
       .def("GetGeometricTolerance", &Unfit::Options::GetGeometricTolerance)
       .def("SetGeometricTolerance", &Unfit::Options::SetGeometricTolerance, boost::python::args("tolerance"))
       .def("GetAlpha", &Unfit::Options::GetAlpha)
       .def("SetAlpha", &Unfit::Options::SetAlpha, boost::python::args("alpha"))
       .def("GetBeta", &Unfit::Options::GetBeta)
       .def("SetBeta", &Unfit::Options::SetBeta, boost::python::args("beta"))
       .def("GetGamma", &Unfit::Options::GetGamma)
       .def("SetGamma", &Unfit::Options::SetGamma, boost::python::args("gamma"))
       .def("GetDelta", &Unfit::Options::GetDelta)
       .def("SetDelta", &Unfit::Options::SetDelta, boost::python::args("delta"))
       .def("GetEpsilon", &Unfit::Options::GetEpsilon)
       .def("SetEpsilon", &Unfit::Options::SetEpsilon, boost::python::args("epsilon"))
       .def("GetTau", &Unfit::Options::GetTau)
       .def("SetTau", &Unfit::Options::SetTau, boost::python::args("tau"))
       .def("GetMaxFunctionEvaluations", &Unfit::Options::GetMaxFunctionEvaluations)
       .def("SetMaxFunctionEvaluations", &Unfit::Options::SetMaxFunctionEvaluations, boost::python::args("max_func_evals"))
       .def("GetMaxIterations", &Unfit::Options::GetMaxIterations)
       .def("SetMaxIterations", &Unfit::Options::SetMaxIterations, boost::python::args("max_iters"))
       .def("GetNelderMeadStepSizes", &wrapper::GetNelderMeadStepSizes, "Returns a tuple containing values of alpha, beta, delta and gamma respectively")
       .def("SetNelderMeadStepSizes", &Unfit::Options::SetNelderMeadStepSizes, boost::python::args("alpha", "beta", "delta", "gamma"))
       .def("GetOutputLevel", &Unfit::Options::GetOutputLevel)
       .def("SetOutputLevel", &Unfit::Options::SetOutputLevel, boost::python::args("output_level"))
       .def("GetCostNormType", &Unfit::Options::GetCostNormType)
       .def("SetCostNormType", &Unfit::Options::SetCostNormType, boost::python::args("cost_norm_type"))
       .def("GetUseAdaptiveParameters", &Unfit::Options::GetUseAdaptiveParameters)
       .def("SetUseAdaptiveParameters", &Unfit::Options::SetUseAdaptiveParameters, boost::python::args("adaptive"))
       .def("GetPopulationSize", &Unfit::Options::GetPopulationSize)
       .def("SetPopulationSize", &Unfit::Options::SetPopulationSize, boost::python::args("pop_size"))
       .def("GetUserSetPopulationSize", &Unfit::Options::GetUserSetPopulationSize)
       .def("GetRandomSeed", &Unfit::Options::GetRandomSeed)
       .def("SetRandomSeed", &Unfit::Options::SetRandomSeed, boost::python::args("seed"))
       .def("GetStrategy", &Unfit::Options::GetStrategy)
       .def("SetStrategy", &Unfit::Options::SetStrategy, boost::python::args("strategy"))
       .def("GetCrossOver", &Unfit::Options::GetCrossOver)
       .def("SetCrossOver", &Unfit::Options::SetCrossOver, boost::python::args("cross_over"))
       .def("GetWeightingFactor", &Unfit::Options::GetWeightingFactor)
       .def("SetWeightingFactor", &Unfit::Options::SetWeightingFactor, boost::python::args("weighting_factor"))
       .def("GetAddInitialToPopulation", &Unfit::Options::GetAddInitialToPopulation)
       .def("SetAddInitialToPopulation", &Unfit::Options::SetAddInitialToPopulation, boost::python::args("add_initial"))
       .def("GetUseBroydenUpdates", &Unfit::Options::GetUseBroydenUpdates)
       .def("SetUseBroydenUpdates", &Unfit::Options::SetUseBroydenUpdates, boost::python::args("use_broyden"))
       .def("GetElitism", &Unfit::Options::GetElitism)
       .def("SetElitism", &Unfit::Options::SetElitism, boost::python::args("elite"))
       .def("GetSurvivalRate", &Unfit::Options::GetSurvivalRate)
       .def("SetSurvivalRate", &Unfit::Options::SetSurvivalRate, boost::python::args("rate"))
       .def("GetUseHardBounds", &Unfit::Options::GetUseHardBounds)
       .def("SetUseHardBounds", &Unfit::Options::SetUseHardBounds, boost::python::args("use_hard_bounds"))
       .def("GetUserSetPopulation", &Unfit::Options::GetUserSetPopulation)
       .def("SetUserSetPopulation", &Unfit::Options::SetUserSetPopulation, boost::python::args("has_set_population"))
       .def("GetUseMultiThreaded", &Unfit::Options::GetUseMultiThreaded)
       .def("SetUseMultiThreaded", &Unfit::Options::SetUseMultiThreaded, boost::python::args("use_multi_threaded"))
       .def("GetTemperature", &Unfit::Options::GetTemperature)
       .def("SetTemperature", &Unfit::Options::SetTemperature, boost::python::args("temperature"))
       .def("GetStepReductionFactor", &Unfit::Options::GetStepReductionFactor)
       .def("SetStepReductionFactor", &Unfit::Options::SetStepReductionFactor, boost::python::args("step_factor"))
       .def("GetTemperatureReductionFactor", &Unfit::Options::GetTemperatureReductionFactor)
       .def("SetTemperatureReductionFactor", &Unfit::Options::SetTemperatureReductionFactor, boost::python::args("temperature_factor"))
       .def("GetNumberOfCycles", &Unfit::Options::GetNumberOfCycles)
       .def("SetNumberOfCycles", &Unfit::Options::SetNumberOfCycles, boost::python::args("num_cycles"))
       .def("GetNumberOfTemperatureLoops", &Unfit::Options::GetNumberOfTemperatureLoops)
       .def("SetNumberOfTemperatureLoops", &Unfit::Options::SetNumberOfTemperatureLoops, boost::python::args("num_temperature_loops"))
       .def("ResetOptions", &Unfit::Options::ResetOptions)
  ;

  boost::python::class_<Unfit::Bounds>("Bounds", boost::python::init<>())
       .def(boost::python::init<std::size_t>())
       .def("ClampWithinBounds", &Unfit::Bounds::ClampWithinBounds, boost::python::args("point"))
       .def("GetBounds", &Unfit::Bounds::GetBounds, boost::python::args("lower_bound", "upper_bound"))
       .def("GetNumberOfBounds", &Unfit::Bounds::GetNumberOfBounds)
       .def("IsAboveLowerBound", &Unfit::Bounds::IsAboveLowerBound, boost::python::args("index", "point"))
       .def("IsBelowUpperBound", &Unfit::Bounds::IsBelowUpperBound, boost::python::args("index", "point"))
       .def<bool (Unfit::Bounds::*)(std::size_t, double) const noexcept>
            ("IsWithinBounds", &Unfit::Bounds::IsWithinBounds, boost::python::args("index", "point"))
       .def<bool (Unfit::Bounds::*)(const std::vector<double> &) const noexcept>
            ("IsWithinBounds", &Unfit::Bounds::IsWithinBounds, boost::python::args("point"))
       .def("ResetBounds", &Unfit::Bounds::ResetBounds)
       .def<bool (Unfit::Bounds::*)(std::size_t, double, double)>
            ("SetBounds", &Unfit::Bounds::SetBounds, boost::python::args("index", "lower_bound", "upper_bound"))
       .def<bool (Unfit::Bounds::*)(const std::vector<double> &, const std::vector<double> &)>
            ("SetBounds", &Unfit::Bounds::SetBounds, (boost::python::args("lower_bound", "upper_bound")))
       .def("SetNumberOfBounds", &Unfit::Bounds::SetNumberOfBounds, boost::python::args("number_of_bounds"))
       .def("GetLowerBound", &Unfit::Bounds::GetLowerBound, boost::python::args("index"))
       .def("SetLowerBound", &Unfit::Bounds::SetLowerBound, boost::python::args("index", "lower_bound"))
       .def("GetUpperBound", &Unfit::Bounds::GetUpperBound, boost::python::args("index"))
       .def("SetUpperBound", &Unfit::Bounds::SetUpperBound, boost::python::args("index", "upper_bound"))
  ;

  boost::python::class_<Unfit::NelderMead, boost::noncopyable>("NelderMead")
      .def("FindMin", &Unfit::NelderMead::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::NelderMead::Reset)
      .def_readwrite("options", &Unfit::NelderMead::options)
      .def_readwrite("bounds", &Unfit::NelderMead::bounds)
  ;

  boost::python::class_<Unfit::LevenbergMarquardt, boost::noncopyable>("LevenbergMarquardt")
      .def("FindMin", &Unfit::LevenbergMarquardt::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::LevenbergMarquardt::Reset)
      .def_readwrite("options", &Unfit::LevenbergMarquardt::options)
      .def_readwrite("bounds", &Unfit::LevenbergMarquardt::bounds)
  ;

  boost::python::class_<Unfit::DifferentialEvolution, boost::noncopyable>("DifferentialEvolution")
      .def("FindMin", &Unfit::DifferentialEvolution::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::DifferentialEvolution::Reset)
      .def_readwrite("options", &Unfit::DifferentialEvolution::options)
      .def_readwrite("bounds", &Unfit::DifferentialEvolution::bounds)
  ;

  boost::python::class_<Unfit::GeneticAlgorithm, boost::noncopyable>("GeneticAlgorithm")
      .def("FindMin", &Unfit::GeneticAlgorithm::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::GeneticAlgorithm::Reset)
      .def_readwrite("options", &Unfit::GeneticAlgorithm::options)
      .def_readwrite("bounds", &Unfit::GeneticAlgorithm::bounds)
  ;

  boost::python::class_<Unfit::ParticleSwarm, boost::noncopyable>("ParticleSwarm")
      .def("FindMin", &Unfit::ParticleSwarm::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::ParticleSwarm::Reset)
      .def_readwrite("options", &Unfit::ParticleSwarm::options)
      .def_readwrite("bounds", &Unfit::ParticleSwarm::bounds)
  ;

  boost::python::class_<Unfit::SimulatedAnnealing, boost::noncopyable>("SimulatedAnnealing")
      .def("FindMin", &Unfit::SimulatedAnnealing::FindMin, boost::python::args("CostFunction", "coordinates"))
      .def("Reset", &Unfit::SimulatedAnnealing::Reset)
      .def_readwrite("options", &Unfit::SimulatedAnnealing::options)
      .def_readwrite("bounds", &Unfit::SimulatedAnnealing::bounds)
  ;
}
