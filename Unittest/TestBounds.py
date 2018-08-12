import unittest

import sys
sys.path.insert(0, '../')

import libUnfitPython

import sys

max_positive_num = (2 - 2**-23) * 2**127        #max value for 32-bit float
max_negative_num = -max_positive_num
test_tol = 16        # tolerance of 1e-16

class TestBounds(unittest.TestCase):

    def test_BoundsConstructors(self):
        # Start with no bounds
        no_bounds = libUnfitPython.Bounds()
        self.assertEqual(0, no_bounds.GetNumberOfBounds())
        
        # Now set the number of bounds
        no_bounds.SetNumberOfBounds(5)
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        no_bounds.GetBounds(lower, upper)
        for bnd in lower:
            self.assertAlmostEqual(max_negative_num, bnd, test_tol)
        for bnd in upper:
            self.assertAlmostEqual(max_positive_num, bnd, test_tol)

        # Start with some bounds
        some_bounds = libUnfitPython.Bounds(5)
        self.assertEqual(5, some_bounds.GetNumberOfBounds())
        some_bounds.GetBounds(lower, upper)
        for bnd in lower:
            self.assertAlmostEqual(max_negative_num, bnd, test_tol)
        for bnd in upper:
            self.assertAlmostEqual(max_positive_num, bnd, test_tol)

    def test_SetAndReset(self):
        some_bounds = libUnfitPython.Bounds(5)
        self.assertEqual(5, some_bounds.GetNumberOfBounds())
        
        # Set bounds and check they are set
        some_bounds.SetBounds(2, 0.0, 1.0)
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        some_bounds.GetBounds(lower, upper)
        self.assertAlmostEqual(0.0, lower[2], test_tol)
        self.assertAlmostEqual(1.0, upper[2], test_tol)

        # Reset bounds and check they have been reset
        some_bounds.ResetBounds()
        some_bounds.GetBounds(lower, upper)
        for bnd in lower:
            self.assertAlmostEqual(max_negative_num, bnd, test_tol)
        for bnd in upper:
            self.assertAlmostEqual(max_positive_num, bnd, test_tol)

    def test_SetUpperAndLower(self):
        some_bounds = libUnfitPython.Bounds(5)
        self.assertEqual(5, some_bounds.GetNumberOfBounds())

        # Set bounds and check they are set
        some_bounds.SetLowerBound(2, 0.0)
        some_bounds.SetUpperBound(3, 1.0)
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        some_bounds.GetBounds(lower, upper)
        self.assertAlmostEqual(0.0, lower[2], test_tol)
        self.assertAlmostEqual(max_positive_num, upper[2], test_tol)
        self.assertAlmostEqual(max_negative_num, lower[3], test_tol)
        self.assertAlmostEqual(1.0, upper[3], test_tol)

    def test_OnePointWithinBounds(self):
        some_bounds = libUnfitPython.Bounds()
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        lower[:] = [0.0, 0.0, 0.0]
        upper[:] = [1.0, 1.0, 1.0]
        some_bounds.SetBounds(lower, upper)

        self.assertTrue(some_bounds.IsWithinBounds(1, 0.5))
        self.assertFalse(some_bounds.IsWithinBounds(1, -1.0))
        self.assertFalse(some_bounds.IsWithinBounds(1, 2.0))
        self.assertFalse(some_bounds.IsWithinBounds(5, 0.5))

    def test_OnePointWithinOneSidedBounds(self):
        some_bounds = libUnfitPython.Bounds()
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        lower[:] = [0.0, 0.0, 0.0]
        upper[:] = [1.0, 1.0, 1.0]
        some_bounds.SetBounds(lower, upper)

        self.assertTrue(some_bounds.IsBelowUpperBound(1, 0.5))
        self.assertTrue(some_bounds.IsAboveLowerBound(1, 0.5))
        self.assertFalse(some_bounds.IsBelowUpperBound(3, 0.5))
        self.assertFalse(some_bounds.IsAboveLowerBound(3, 0.5))
        self.assertFalse(some_bounds.IsBelowUpperBound(1, 2.0))
        self.assertFalse(some_bounds.IsAboveLowerBound(1, -1.0))

    def test_PointsWithinBounds(self):
        some_bounds = libUnfitPython.Bounds()
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        lower[:] = [0.0, 0.0, 0.0]
        upper[:] = [1.0, 1.0, 1.0]
        some_bounds.SetBounds(lower, upper)

        point = libUnfitPython.std_vector_double()
        point[:] = [0.5, 0.5, 0.5]
        self.assertTrue(some_bounds.IsWithinBounds(point))
        point[1] = -1.0
        self.assertFalse(some_bounds.IsWithinBounds(point))
        point[1] = 2.0
        self.assertFalse(some_bounds.IsWithinBounds(point))

    def test_PointsWithinBoundsEdgeCases(self):
        some_bounds = libUnfitPython.Bounds(3)
        point = libUnfitPython.std_vector_double()
        point[:] = [max_positive_num, max_negative_num, max_positive_num]
        self.assertTrue(some_bounds.IsWithinBounds(point))
        point[0] = point[0] * 10.0
        self.assertFalse(some_bounds.IsWithinBounds(point))
        point[0] = max_positive_num
        point[1] = point[1] * 10
        self.assertFalse(some_bounds.IsWithinBounds(point))

    def test_ClampPointWithinBounds(self):
        some_bounds = libUnfitPython.Bounds()
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        lower[:] = [0.0, 0.0, 0.0]
        upper[:] = [1.0, 1.0, 1.0]
        some_bounds.SetBounds(lower, upper)

        # Already within bounds, should do nothing
        point = libUnfitPython.std_vector_double()
        point[:] = [0.5, 0.5, 0.5]
        some_bounds.ClampWithinBounds(point)
        self.assertAlmostEqual(0.5, point[0], test_tol)
        self.assertAlmostEqual(0.5, point[1], test_tol)
        self.assertAlmostEqual(0.5, point[2], test_tol)

        # Clamp to lower bound
        point[1] = -1.0
        some_bounds.ClampWithinBounds(point)
        self.assertAlmostEqual(0.5, point[0], test_tol)
        self.assertAlmostEqual(0.0, point[1], test_tol)
        self.assertAlmostEqual(0.5, point[2], test_tol)

        # Clamp to upper bound
        point[1] = 2.0
        some_bounds.ClampWithinBounds(point)
        self.assertAlmostEqual(0.5, point[0], test_tol)
        self.assertAlmostEqual(1.0, point[1], test_tol)
        self.assertAlmostEqual(0.5, point[2], test_tol)

    def test_SetBoundsErrorCases(self):
        # Array sizes don't match
        some_bounds = libUnfitPython.Bounds(3)
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        lower[:] = [0.0, 0.0]
        upper[:] = [1.0, 1.0, 1.0]
        self.assertFalse(some_bounds.SetBounds(lower, upper))

        # Negative infinite bound
        lower.append(-float('inf'))
        self.assertFalse(some_bounds.SetBounds(lower, upper))

        # Positive infinite bound
        lower[2] = 0.0
        upper[1] = float('inf')
        self.assertFalse(some_bounds.SetBounds(lower, upper))

        # Lower bound > upper bound
        upper[1] = -1.0
        self.assertFalse(some_bounds.SetBounds(lower, upper))

        # Now check that the original bounds are intact
        some_bounds.GetBounds(lower, upper)
        for bnd in lower:
            self.assertAlmostEqual(max_negative_num, bnd, test_tol)
        for bnd in upper:
            self.assertAlmostEqual(max_positive_num, bnd, test_tol)

    def test_SetOneBoundErrorCases(self):
        # Array sizes don't match
        some_bounds = libUnfitPython.Bounds(3)
        
        # Negative inifinite bound
        self.assertFalse(some_bounds.SetBounds(2, -float('inf') , 1.0))
        
        # Positive inifnite bounds
        self.assertFalse(some_bounds.SetBounds(2, 0.0, float('inf')))
        
        # Lower bound > upper bound
        self.assertFalse(some_bounds.SetBounds(2, 1.0, 0.0))
        
        # Check adding an index greater than the vector size (should scale)
        self.assertTrue(some_bounds.SetBounds(5, max_negative_num, max_positive_num))
        self.assertEqual(6, some_bounds.GetNumberOfBounds())
        
        # Now check that the original and extended bounds are intact
        lower = libUnfitPython.std_vector_double()
        upper = libUnfitPython.std_vector_double()
        some_bounds.GetBounds(lower, upper)
        for bnd in lower:
            self.assertAlmostEqual(max_negative_num, bnd, test_tol)
        for bnd in upper:
            self.assertAlmostEqual(max_positive_num, bnd, test_tol)

    def test_GetSetLowerBound(self):
        some_bounds = libUnfitPython.Bounds(2)
        
        # Default bounds
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(0), test_tol)
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(1), test_tol)
        
        # Invalid indices
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(2), test_tol)
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(3), test_tol)

        some_bounds.SetLowerBound(0, 1.0)
        some_bounds.SetLowerBound(1, 0.0)
        
        # Default bounds
        self.assertAlmostEqual(1.0, some_bounds.GetLowerBound(0), test_tol)
        self.assertAlmostEqual(0.0, some_bounds.GetLowerBound(1), test_tol)
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(0), test_tol)
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(1), test_tol)
        
        # Invalid indices
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(2), test_tol)
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(3), test_tol)

    def test_GetSetUpperBound(self):
        some_bounds = libUnfitPython.Bounds(2)
        
        # Default bounds
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(0), test_tol)
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(1), test_tol)
        
        # Invalid indices
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(2), test_tol)
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(3), test_tol)

        some_bounds.SetUpperBound(0, 1.0)
        some_bounds.SetUpperBound(1, 0.0)
        
        # Default bounds
        self.assertAlmostEqual(1.0, some_bounds.GetUpperBound(0), test_tol)
        self.assertAlmostEqual(0.0, some_bounds.GetUpperBound(1), test_tol)
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(0), test_tol)
        self.assertAlmostEqual(max_negative_num, some_bounds.GetLowerBound(1), test_tol)
        
        # Invalid indices
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(2), test_tol)
        self.assertAlmostEqual(max_positive_num, some_bounds.GetUpperBound(3), test_tol)

if __name__ == '__main__':
#If this module is executed directly, do all the test cases here

     test_list = [TestBounds]
 
     loader = unittest.TestLoader()
 
     suites_list = []
     for test_class in test_list:
         suite = loader.loadTestsFromTestCase(test_class)
         suites_list.append(suite)
 
     big_suite = unittest.TestSuite(suites_list)
 
     runner = unittest.TextTestRunner()
     results = runner.run(big_suite)
        
