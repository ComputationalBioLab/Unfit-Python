#Main testing module that tests all the tests at once
#For individual tests, execute the modules individually

import unittest

#import any additional tests here
from TestBounds import TestBounds
from TestOptions import TestOptions
from TestVector import TestVector
from TestCostFunction import TestCostFunction

test_list = [TestBounds, TestOptions, TestVector, TestCostFunction]
    
loader = unittest.TestLoader()
    
suites_list = []
for test_class in test_list:
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)
                
big_suite = unittest.TestSuite(suites_list)
                
runner = unittest.TextTestRunner()
results = runner.run(big_suite)
