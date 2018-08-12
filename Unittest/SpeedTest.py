#File to compare speed between the optimizers in Python,
#and against the C++ version. Takes a while, so it is not
#included as part of the Unittest.

import sys
sys.path.insert(0, '../')

import libUnfitPython

import mycostfunction
import time

lower_bounds = libUnfitPython.std_vector_double()
upper_bounds = libUnfitPython.std_vector_double()
lower_bounds[:] = [-1000000, -1000000]
upper_bounds[:] = [1000000, 1000000]



print('NelderMead:')

nm = libUnfitPython.NelderMead()

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_100000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
nm.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')

###############################################
print('LevenbergMarquardt:')

lm = libUnfitPython.LevenbergMarquardt()

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_100000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
lm.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')

###############################################
print('GeneticAlgorithm:')

ga = libUnfitPython.GeneticAlgorithm()
ga.bounds.SetBounds(lower_bounds, upper_bounds)

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_100000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
ga.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')

###############################################
print('DifferentialEvolution:')

de = libUnfitPython.DifferentialEvolution()
de.bounds.SetBounds(lower_bounds, upper_bounds)

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_10000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
de.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')

###############################################
print('ParticleSwarm:')

ps = libUnfitPython.ParticleSwarm()
ps.bounds.SetBounds(lower_bounds, upper_bounds)

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_10000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
ps.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')

###############################################
print('SimulatedAnnealing:')

sa = libUnfitPython.SimulatedAnnealing()
sa.bounds.SetBounds(lower_bounds, upper_bounds)

cf = mycostfunction.MyCostFunction()
cf.FileInit('Values/values_10000.txt')
guess = libUnfitPython.std_vector_double()
guess[:] = [0, 0]

start = time.clock()
sa.FindMin(cf, guess)
elapsed = time.clock() - start

for x in guess:
    print(x)

print('Time elapsed: ' + repr(elapsed) + 's')







