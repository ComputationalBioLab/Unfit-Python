import unittest

import sys
sys.path.insert(0, '../')

import libUnfitPython

class TestVector(unittest.TestCase):

    def test_Indexing(self):
        vector = libUnfitPython.std_vector_double()
        vector[:] = [1, 2, 3]
        
        #tests normal indexing
        self.assertEqual(1, vector[0])
        self.assertEqual(2, vector[1])
        self.assertEqual(3, vector[2])

        #tests python negative indexing
        self.assertEqual(3, vector[-1])
        self.assertEqual(2, vector[-2])
        self.assertEqual(1, vector[-3])

    def test_Slicing(self):
        vector1 = libUnfitPython.std_vector_double()
        vector1[:] = [1, 2, 3, 4, 5]
        
        vector2 = libUnfitPython.std_vector_double()
        vector2[:] = vector1[:3]
        test = [1, 2, 3]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])

        vector2[:] = [1, 2, 3, 4, 5, 6]
        vector2[1:5] = [3, 4, 5, 6]
        test = [1, 3, 4, 5, 6, 6]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])
        vector2[1:3] = [7, 8, 9, 10]
        test = [1, 7, 8, 9, 10, 5, 6, 6]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])
        vector2[2:6] = [11, 11]
        test = [1, 7, 11, 11, 6, 6]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])

    def test_AppendExtend(self):
        vector1 = libUnfitPython.std_vector_double()
        vector1[:] = [1, 2, 3, 4, 5]
        vector2 = libUnfitPython.std_vector_double()
        vector2[:] = [1, 2, 3]
        
        vector2.append(4)
        test = [1, 2, 3, 4]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])
        vector2.extend(vector1[3:5])
        test = [1, 2, 3, 4, 4, 5]
        for i, vi in enumerate(vector2):
            self.assertEqual(vi, test[i])
      
if __name__ == '__main__':
#If this module is executed directly, do all the test cases here   
    
    test_list = [TestVector]
    
    loader = unittest.TestLoader()
        
    suites_list = []
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
                
    big_suite = unittest.TestSuite(suites_list)
                
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
