import unittest

import sys
sys.path.insert(0, '../')

import libUnfitPython

import Linear
import Quadratic
import Exponential

guess_tol = 11       #tolerance of 1e-6
cost_tol = 11        #tolerance of 1e-11

class TestExamplesLevenbergMarquardt(unittest.TestCase):
    def setUp(self):
        '''
            Processes done at the start of every test in this class.
        '''
        lower = libUnfitPython.std_vector_double()
        lower[:] = [-10, -10, -10]
        upper = libUnfitPython.std_vector_double()
        upper[:] = [10, 10, 10]
        
        self.lm = libUnfitPython.LevenbergMarquardt()
        self.lm.bounds.SetBounds(lower, upper)
    
    def test_LinearDirectInput(self):
        cf = Linear.LinearCostFunction([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                       [8, 11, 14, 17, 20, 23, 26, 29, 32, 35])
            
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0]
                      
        cost = 0
        for r in cf(guess):
            cost = cost + r * r
                      
        self.assertAlmostEqual(cost, 5365, cost_tol)
                          
        self.lm.FindMin(cf, guess)
                      
        self.assertAlmostEqual(guess[0], 4.99999998785, guess_tol)
        self.assertAlmostEqual(guess[1], 3.00000000175, guess_tol)

    def test_LinearFileInput(self):
        cf = Linear.LinearCostFunction()
        cf.FileInit('Values/TestLinear.txt')
    
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0]
    
        cost = 0
        for r in cf(guess):
            cost = cost + r * r

        self.assertAlmostEqual(cost, 5365, cost_tol)
        
        self.lm.FindMin(cf, guess)
        
        self.assertAlmostEqual(guess[0], 4.99999998785, guess_tol)
        self.assertAlmostEqual(guess[1], 3.00000000175, guess_tol)

    def test_QuadraticDirectInput(self):
        cf = Quadratic.QuadraticCostFunction([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                             [-2, -4, -4, -2, 2, 8, 16, 26, 38, 52])
        
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0, 0]
                  
        cost = 0
        for r in cf(guess):
            cost = cost + r * r
                              
        self.assertAlmostEqual(cost, 5188, cost_tol)
                              
        self.lm.FindMin(cf, guess)
                              
        self.assertAlmostEqual(guess[0], 1.99999958222, guess_tol)
        self.assertAlmostEqual(guess[1], -4.99999983709, guess_tol)
        self.assertAlmostEqual(guess[2], 0.999999986896, guess_tol)

    def test_QuadraticFileInput(self):
        cf = Quadratic.QuadraticCostFunction()
        cf.FileInit('Values/TestQuadratic.txt')
    
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0, 0]
        
        cost = 0
        for r in cf(guess):
            cost = cost + r * r
    
        self.assertAlmostEqual(cost, 5188, cost_tol)
        
        self.lm.FindMin(cf, guess)
        
        self.assertAlmostEqual(guess[0], 1.99999958222, guess_tol)
        self.assertAlmostEqual(guess[1], -4.99999983709, guess_tol)
        self.assertAlmostEqual(guess[2], 0.999999986896, guess_tol)

    def test_ExponentialDirectInput(self):
        cf = Exponential.ExponentialCostFunction([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                                 [1.0, 0.6065, 0.3679, 0.2231, 0.1353, 0.0821, 0.0498, 0.0302, 0.0183, 0.0111, 0.0067])
            
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0]
                      
        cost = 0
        for r in cf(guess):
            cost = cost + r * r
                      
        self.assertAlmostEqual(cost, 1.58190784, cost_tol)

        self.lm.FindMin(cf, guess)
    
        self.assertAlmostEqual(guess[0], 0.99999682538, guess_tol)
        self.assertAlmostEqual(guess[1], 0.500017605642, guess_tol)
    
    def test_ExponentialFileInput(self):
        cf = Exponential.ExponentialCostFunction()
        cf.FileInit('Values/TestExponential.txt')
        
        guess = libUnfitPython.std_vector_double()
        guess[:] = [0, 0]
        
        cost = 0
        for r in cf(guess):
            cost = cost + r * r
        
        self.assertAlmostEqual(cost, 1.58190784, cost_tol)
        
        self.lm.FindMin(cf, guess)
        
        self.assertAlmostEqual(guess[0], 0.99999682538, guess_tol)
        self.assertAlmostEqual(guess[1], 0.500017605642, guess_tol)

if __name__ == '__main__':
    #If this module is executed directly, do all the test cases here
    
    test_list = [TestExamplesLevenbergMarquardt]
    
    loader = unittest.TestLoader()
    
    suites_list = []
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


