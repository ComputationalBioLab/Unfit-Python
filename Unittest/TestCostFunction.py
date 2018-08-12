import unittest
import mycostfunction

import sys
sys.path.insert(0, '../')

import libUnfitPython

class TestCostFunction(unittest.TestCase):

    def test_init(self):
        empty = mycostfunction.MyCostFunction()
        self.assertEqual(empty.t.__len__(), 0)
        self.assertEqual(empty.y.__len__(), 0)
        
        t_data = [1, 2, 3]
        y_data = [3, 4, 5]
        cf = mycostfunction.MyCostFunction(t_data, y_data)

        self.assertTrue(type(cf.t) is libUnfitPython.std_vector_double)
        for i, ti in enumerate(cf.t):
            self.assertEqual(ti, t_data[i])

        self.assertTrue(type(cf.y) is libUnfitPython.std_vector_double)
        for i, yi in enumerate(cf.y):
            self.assertEqual(yi, y_data[i])

    def test_Call(self):
        t_data = [1, 2, 3]
        y_data = [7, 5, 10]
        cf = mycostfunction.MyCostFunction(t_data, y_data)

        x = [1, 1]
        results = [5, 2, 6]

        r = cf(x)
        for i, ri in enumerate(r):
            self.assertTrue(ri, results[i])

if __name__ == '__main__':
    #If this module is executed directly, do all the test cases here
    
    test_list = [TestCostFunction]
    
    loader = unittest.TestLoader()
        
    suites_list = []
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
                
    big_suite = unittest.TestSuite(suites_list)
                
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
