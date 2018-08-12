import sys
sys.path.insert(0, '../')

import libUnfitPython

import math

class MyCostFunction(libUnfitPython.GenericCostFunction):
    t = libUnfitPython.std_vector_double()
    y = libUnfitPython.std_vector_double()

    def __init__(self, t_data = None, y_data = None):
        libUnfitPython.GenericCostFunction.__init__(self)
    
        if t_data != None and y_data != None:
            self.t[:] = t_data
            self.y[:] = y_data
        else:
            self.t[:] = []
            self.y[:] = []

    def FileInit(self, filename):
        i = 0
        
        with open(filename) as f:
            for line in f:
            if(i == 0):
                self.t[:] = [float(x) for x in line.split()]
                i = 1
            else:
                self.y[:] = [float(x) for x in line.split()]

    def __call__(self, x):
        '''
            Method called by FindMin function. Modify the model if needed.
        '''
        r = libUnfitPython.std_vector_double()
        r[:] = self.y[:]
        for i, ti in enumerate(self.t):
            model = x[0] + x[1] * ti
            r[i] -= model
        return r

