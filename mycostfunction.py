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

    def __call__(self, x):
        '''
            Method called by FindMin function. Modify the model if needed.
        '''
        r = libUnfitPython.std_vector_double()
        r[:] = self.y[:]
        for i, ti in enumerate(self.t):
            model = x[0] * math.exp(-x[1] * ti)
            r[i] -= model
        return r

