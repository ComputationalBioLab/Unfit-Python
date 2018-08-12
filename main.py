#This is an example on how to use the optimizers. The data
#are fitted to an exponential model, which can be seen in
#the mycostfunction.py file. The answers should be close to
#1 and 0.5.
#
#Run this by opening python (version 2.7.x) and typing:
#    
#    execfile("main.py:)"
#
import libUnfitPython

import mycostfunction

guess = libUnfitPython.std_vector_double()
guess[:] = [0,0]

lower_bounds = libUnfitPython.std_vector_double()
upper_bounds = libUnfitPython.std_vector_double()
lower_bounds[:] = [-10, -10]
upper_bounds[:] = [10, 10]

t_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [1.0, 0.6065, 0.3679, 0.2231, 0.1353, 0.0821, 0.0498, 0.0302, 0.0183, 0.0111, 0.0067]
cf = mycostfunction.MyCostFunction(t_data,y_data)

##############################################
print("LevenbergMarquardt:")

guess[:] = [0,0]

lm = libUnfitPython.LevenbergMarquardt()
rc = lm.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')

##############################################
print("NelderMead:")

guess[:] = [0,0]

nm = libUnfitPython.NelderMead()
rc = nm.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')

##############################################
print("DifferentialEvolution:")

guess[:] = [0,0]

de = libUnfitPython.DifferentialEvolution()
de.bounds.SetBounds(lower_bounds, upper_bounds)
rc = de.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')

##############################################
print("GeneticAlgorithm:")

guess[:] = [0,0]

ga = libUnfitPython.GeneticAlgorithm()
ga.bounds.SetBounds(lower_bounds, upper_bounds)
rc = ga.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')

##############################################
print("ParticleSwarm:")

guess[:] = [0,0]

ps = libUnfitPython.ParticleSwarm()
ps.bounds.SetBounds(lower_bounds, upper_bounds)
rc = ps.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')

##############################################
print("SimulatedAnnealing:")

guess[:] = [0,0]

sa = libUnfitPython.SimulatedAnnealing()
sa.bounds.SetBounds(lower_bounds, upper_bounds)
rc = sa.FindMin(cf, guess)

if rc == 0:
    for x in guess:
        print(x)
else:
    print('Error encountered. Error code: ' + str(rc))

print('')



