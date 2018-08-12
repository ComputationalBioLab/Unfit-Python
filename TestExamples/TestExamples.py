import unittest

from TestExamplesNelderMead import TestExamplesNelderMead
from TestExamplesLevenbergMarquardt import TestExamplesLevenbergMarquardt
from TestExamplesDifferentialEvolution import TestExamplesDifferentialEvolution
from TestExamplesGeneticAlgorithm import TestExamplesGeneticAlgorithm
from TestExamplesParticleSwarm import TestExamplesParticleSwarm
from TestExamplesSimulatedAnnealing import TestExamplesSimulatedAnnealing

test_list = [TestExamplesSimulatedAnnealing,
             TestExamplesParticleSwarm,
             TestExamplesGeneticAlgorithm,
             TestExamplesDifferentialEvolution,
             TestExamplesLevenbergMarquardt,
             TestExamplesNelderMead]
    
loader = unittest.TestLoader()
    
suites_list = []
for test_class in test_list:
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)
                
big_suite = unittest.TestSuite(suites_list)
                
runner = unittest.TextTestRunner()
results = runner.run(big_suite)
