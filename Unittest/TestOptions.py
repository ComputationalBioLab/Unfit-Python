import unittest

import sys
sys.path.insert(0, '../')

import libUnfitPython

test_tol = 16       # Tolerance of 1e-16

class TestOptions(unittest.TestCase):

    def test_GetSetMaximumFunctionEvaluations(self):
        options = libUnfitPython.Options()
        self.assertEqual(options.GetMaxFunctionEvaluations(), 100000)
        options.SetMaxFunctionEvaluations(10)
        self.assertEqual(options.GetMaxFunctionEvaluations(), 10)
        options.SetMaxFunctionEvaluations(5000000)
        self.assertEqual(options.GetMaxFunctionEvaluations(), 5000000)
        options.SetMaxFunctionEvaluations(0)
        self.assertEqual(options.GetMaxFunctionEvaluations(), 0)
        options.ResetOptions()
        self.assertEqual(options.GetMaxFunctionEvaluations(), 100000)

    def test_GetSetMaximumIterations(self):
        options = libUnfitPython.Options()
        self.assertEqual(options.GetMaxIterations(), 10000)
        options.SetMaxIterations(10)
        self.assertEqual(options.GetMaxIterations(), 10)
        options.SetMaxIterations(5000000)
        self.assertEqual(options.GetMaxIterations(), 5000000)
        options.SetMaxIterations(0)
        self.assertEqual(options.GetMaxIterations(), 0)
        options.ResetOptions()
        self.assertEqual(options.GetMaxIterations(), 10000)

    def test_GetSetOutputLevel(self):
        options = libUnfitPython.Options()
        self.assertEqual(options.GetOutputLevel(), 0)
        options.SetOutputLevel(1)
        self.assertEqual(options.GetOutputLevel(), 1)
        options.SetOutputLevel(5)
        self.assertEqual(options.GetOutputLevel(), 5)
        options.ResetOptions()
        self.assertEqual(options.GetOutputLevel(), 0)

    def test_GetSetCostNormType(self):
        options = libUnfitPython.Options()
        self.assertEqual(options.GetCostNormType(), 2)
        options.SetCostNormType(1)
        self.assertEqual(options.GetCostNormType(), 1)
        options.SetCostNormType(0)
        self.assertEqual(options.GetCostNormType(), 2)
        options.SetCostNormType(3)
        self.assertEqual(options.GetCostNormType(), 2)
        options.ResetOptions()
        self.assertEqual(options.GetCostNormType(), 2)

    def test_GetSetTolerances(self):
        options = libUnfitPython.Options()
        self.assertAlmostEqual(1e-12, options.GetCostTolerance(), test_tol)
        self.assertAlmostEqual(1e-8, options.GetDegenerateTolerance(), test_tol)
        self.assertAlmostEqual(1e-4, options.GetGeometricTolerance(), test_tol)

        # Check allowed changes work
        options.SetCostTolerance(1e-16)
        options.SetDegenerateTolerance(1e-12)
        options.SetGeometricTolerance(1e-8)
        self.assertAlmostEqual(1e-16, options.GetCostTolerance(), test_tol)
        self.assertAlmostEqual(1e-12, options.GetDegenerateTolerance(), test_tol)
        self.assertAlmostEqual(1e-8, options.GetGeometricTolerance(), test_tol)
        
        # Check invalid changes do nothing
        options.SetCostTolerance(0.0)
        options.SetDegenerateTolerance(0.0)
        options.SetGeometricTolerance(0.0)
        self.assertAlmostEqual(1e-16, options.GetCostTolerance(), test_tol)
        self.assertAlmostEqual(1e-12, options.GetDegenerateTolerance(), test_tol)
        self.assertAlmostEqual(1e-8, options.GetGeometricTolerance(), test_tol)
        options.SetCostTolerance(-1e-16)
        options.SetDegenerateTolerance(-1e-12)
        options.SetGeometricTolerance(-1e-8)
        self.assertAlmostEqual(1e-16, options.GetCostTolerance(), test_tol)
        self.assertAlmostEqual(1e-12, options.GetDegenerateTolerance(), test_tol)
        self.assertAlmostEqual(1e-8, options.GetGeometricTolerance(), test_tol)

        # Check reset works
        options.ResetOptions()
        self.assertAlmostEqual(1e-12, options.GetCostTolerance(), test_tol)
        self.assertAlmostEqual(1e-8, options.GetDegenerateTolerance(), test_tol)
        self.assertAlmostEqual(1e-4, options.GetGeometricTolerance(), test_tol)

    def test_AlphaBetaDeltaGamma(self):
        options = libUnfitPython.Options()
        
        # Check the defaults
        self.assertAlmostEqual(1.0, options.GetAlpha(), test_tol)
        self.assertAlmostEqual(2.0, options.GetBeta(), test_tol)
        self.assertAlmostEqual(0.5, options.GetDelta(), test_tol)
        self.assertAlmostEqual(0.5, options.GetGamma(), test_tol)

        # Set some different values and check they are set
        options.SetAlpha(1.1)
        options.SetBeta(2.1)
        options.SetDelta(0.6)
        options.SetGamma(0.4)
        self.assertAlmostEqual(1.1, options.GetAlpha(), test_tol)
        self.assertAlmostEqual(2.1, options.GetBeta(), test_tol)
        self.assertAlmostEqual(0.6, options.GetDelta(), test_tol)
        self.assertAlmostEqual(0.4, options.GetGamma(), test_tol)

        options.ResetOptions()
        self.assertAlmostEqual(1.0, options.GetAlpha(), test_tol)
        self.assertAlmostEqual(2.0, options.GetBeta(), test_tol)
        self.assertAlmostEqual(0.5, options.GetDelta(), test_tol)
        self.assertAlmostEqual(0.5, options.GetGamma(), test_tol)
    
    def test_NelderMeadAlphaBetaDeltaGamma(self):
        options = libUnfitPython.Options()
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        
        # Check the defaults
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
    
        # Set some different values and check they are set
        options.SetNelderMeadStepSizes(1.1, 2.1, 0.6, 0.4)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.1, alpha, test_tol)
        self.assertAlmostEqual(2.1, beta, test_tol)
        self.assertAlmostEqual(0.6, delta, test_tol)
        self.assertAlmostEqual(0.4, gamma, test_tol)
    
        # Rest and check they are reset
        options.ResetOptions()
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

    def test_NelderMeadAlphaBetaDeltaGammaConstraints(self):
        options = libUnfitPython.Options()
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        
        # Check the defaults
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

        # Gamma too high (>=1) or too low (<=0) should result in no changes
        options.SetNelderMeadStepSizes(1.0, 2.0, 0.5, 0.0)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, 0.5, -1.0)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, 0.5, 1.0)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, 0.5, 2.0)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

        # Delta too high (>=1) or too low (<=0) should result in no changes
        options.SetNelderMeadStepSizes(1.0, 2.0, 0.0, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, -1.0, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, 1.0, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(1.0, 2.0, 2.0, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

        # Gamma >= alpha should result in no changes
        options.SetNelderMeadStepSizes(0.5, 2.0, 0.5, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(0.2, 2.0, 0.5, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

        # Alpha >= beta should result in no changes
        options.SetNelderMeadStepSizes(2.0, 2.0, 0.5, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)
        options.SetNelderMeadStepSizes(5.0, 2.0, 0.5, 0.5)
        alpha, beta, delta, gamma = options.GetNelderMeadStepSizes()
        self.assertAlmostEqual(1.0, alpha, test_tol)
        self.assertAlmostEqual(2.0, beta, test_tol)
        self.assertAlmostEqual(0.5, delta, test_tol)
        self.assertAlmostEqual(0.5, gamma, test_tol)

    def test_GetSetTau(self):
        options = libUnfitPython.Options()
        
        # Check the default
        self.assertAlmostEqual(1e-3, options.GetTau(), test_tol)
        
        # Try to set an invalid value, should be ignored
        options.SetTau(-1.0)
        self.assertAlmostEqual(1e-3, options.GetTau(), test_tol)
        
        # Try to set a valid value
        options.SetTau(1.0)
        self.assertAlmostEqual(1.0, options.GetTau(), test_tol)
        
        # Try a reset, should go back to default
        options.ResetOptions()
        self.assertAlmostEqual(1e-3, options.GetTau(), test_tol)

    def test_GetSetUseAdaptive(self):
        options = libUnfitPython.Options()
        self.assertFalse(options.GetUseAdaptiveParameters())
        options.SetUseAdaptiveParameters(True)
        self.assertTrue(options.GetUseAdaptiveParameters())
        options.SetUseAdaptiveParameters(False)
        self.assertFalse(options.GetUseAdaptiveParameters())
        options.SetUseAdaptiveParameters(True)
        self.assertTrue(options.GetUseAdaptiveParameters())
        options.ResetOptions()
        self.assertFalse(options.GetUseAdaptiveParameters())

    def test_GetSetPopulationSize(self):
        options = libUnfitPython.Options()
        self.assertEqual(20, options.GetPopulationSize())
        options.SetPopulationSize(10)
        self.assertEqual(10, options.GetPopulationSize())
        options.ResetOptions()
        self.assertEqual(20, options.GetPopulationSize())

    def test_GetSetRandomSeed(self):
        options = libUnfitPython.Options()
        self.assertEqual(0, options.GetRandomSeed())
        options.SetRandomSeed(10)
        self.assertEqual(10, options.GetRandomSeed())
        options.ResetOptions()
        self.assertEqual(0, options.GetRandomSeed())

    def test_GetSetStrategy(self):
        options = libUnfitPython.Options()
        self.assertEqual(1, options.GetStrategy())
        options.SetStrategy(5)
        self.assertEqual(5, options.GetStrategy())
        options.ResetOptions()
        self.assertEqual(1, options.GetStrategy())

    def test_GetSetElitism(self):
        options = libUnfitPython.Options()
        self.assertEqual(1, options.GetElitism())
        
        # Valid (default population size is 20)
        options.SetElitism(5)
        self.assertEqual(5, options.GetElitism())
        
        # Invalid (above 20 = ignored)
        options.SetElitism(25)
        self.assertEqual(5, options.GetElitism())
        options.ResetOptions()
        self.assertEqual(1, options.GetElitism())

    def test_GetSetWeightingFactor(self):
        options = libUnfitPython.Options()
        self.assertAlmostEqual(0.8, options.GetWeightingFactor(), test_tol)
        options.SetWeightingFactor(0.5)
        self.assertAlmostEqual(0.5, options.GetWeightingFactor(), test_tol)
        options.ResetOptions()
        self.assertAlmostEqual(0.8, options.GetWeightingFactor(), test_tol)

    def test_GetSetCrossOver(self):
        options = libUnfitPython.Options()
        self.assertAlmostEqual(0.9, options.GetCrossOver(), test_tol)
        
        # Within valid range
        options.SetCrossOver(0.5)
        self.assertAlmostEqual(0.5, options.GetCrossOver(), test_tol)
        
        # Below valid range
        options.SetCrossOver(-1.0)
        self.assertAlmostEqual(0.0, options.GetCrossOver(), test_tol)
        
        # Above valid range
        options.SetCrossOver(1.5)
        self.assertAlmostEqual(1.0, options.GetCrossOver(), test_tol)
        
        options.ResetOptions()
        self.assertAlmostEqual(0.9, options.GetCrossOver(), test_tol)

    def test_GetSetSurvivalRate(self):
        options = libUnfitPython.Options()
        self.assertAlmostEqual(0.5, options.GetSurvivalRate(), test_tol)
        
        # Within valid range
        options.SetSurvivalRate(0.9)
        self.assertAlmostEqual(0.9, options.GetSurvivalRate(), test_tol)
        
        # Below valid range
        options.SetSurvivalRate(-1.0)
        self.assertAlmostEqual(0.0, options.GetSurvivalRate(), test_tol)
        
        # Above valid range
        options.SetSurvivalRate(1.5)
        self.assertAlmostEqual(1.0, options.GetSurvivalRate(), test_tol)
        
        options.ResetOptions()
        self.assertAlmostEqual(0.5, options.GetSurvivalRate(), test_tol)

    def test_GetSetAddInitialToPopulation(self):
        options = libUnfitPython.Options()
        self.assertFalse(options.GetAddInitialToPopulation())
        options.SetAddInitialToPopulation(True)
        self.assertTrue(options.GetAddInitialToPopulation())
        options.ResetOptions()
        self.assertFalse(options.GetAddInitialToPopulation())

    def test_GetSetUseHardBounds(self):
        options = libUnfitPython.Options()
        self.assertFalse(options.GetUseHardBounds())
        options.SetUseHardBounds(True)
        self.assertTrue(options.GetUseHardBounds())
        options.ResetOptions()
        self.assertFalse(options.GetUseHardBounds())

    def test_GetSetUseMultiThreaded(self):
        options = libUnfitPython.Options()
        self.assertFalse(options.GetUseMultiThreaded())
        options.SetUseMultiThreaded(True)
        self.assertTrue(options.GetUseMultiThreaded())
        options.ResetOptions()
        self.assertFalse(options.GetUseMultiThreaded())

    def test_SimulatedAnnealingParameters(self):
        options = libUnfitPython.Options()
        
        # Check the defaults
        self.assertAlmostEqual(1000.0, options.GetTemperature(), test_tol)
        self.assertAlmostEqual(0.9, options.GetStepReductionFactor(), test_tol)
        self.assertAlmostEqual(0.5, options.GetTemperatureReductionFactor(), test_tol)
        self.assertEqual(20, options.GetNumberOfCycles())
        self.assertEqual(5, options.GetNumberOfTemperatureLoops())

        # Set non-default values to parameters
        options.SetTemperature(373.0)
        options.SetStepReductionFactor(0.8)
        options.SetTemperatureReductionFactor(0.8)
        options.SetNumberOfCycles(10)
        options.SetNumberOfTemperatureLoops(10)
        self.assertAlmostEqual(373.0, options.GetTemperature(), test_tol)
        self.assertAlmostEqual(0.8, options.GetStepReductionFactor(), test_tol)
        self.assertAlmostEqual(0.8, options.GetTemperatureReductionFactor(), test_tol)
        self.assertEqual(10, options.GetNumberOfCycles())
        self.assertEqual(10, options.GetNumberOfTemperatureLoops())
        
        # Reset and check for parameters' default values
        options.ResetOptions()
        self.assertAlmostEqual(1000.0, options.GetTemperature(), test_tol)
        self.assertAlmostEqual(0.9, options.GetStepReductionFactor(), test_tol)
        self.assertAlmostEqual(0.5, options.GetTemperatureReductionFactor(), test_tol)
        self.assertEqual(20, options.GetNumberOfCycles())
        self.assertEqual(5, options.GetNumberOfTemperatureLoops())



if __name__ == '__main__':
#If this module is executed directly, do all the test cases here

    test_list = [TestOptions]
    
    loader = unittest.TestLoader()
    
    suites_list = []
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)





