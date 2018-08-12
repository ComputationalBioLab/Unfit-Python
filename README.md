# Unfit Python

![unfit-logo](https://computationalbiolab.github.io/assets/img/unfit_logo.png)

This allows use of [Unfit](https://github.com/ComputationalBioLab/Unfit) through Python. Solve cost function problems with 6 different optimizers. Aims to smoothly interface the Unfit from C++ to Python.

![made-with-python](https://img.shields.io/badge/language-Python-blue.svg) ![language-c++](https://img.shields.io/badge/language-C%2B%2B-blue.svg) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) ![license-GPLv3.0](    https://img.shields.io/badge/license-GPLv3.0-green.svg) 

#### Table of Contents
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Running Tests](#running-tests)
* [Development Environment](#development-environment)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

### Getting Started
___
1. Download & install Code::Blocks ([http://www.codeblocks.org/](http://www.codeblocks.org)).

Note: if you are on Windows, choose the version with GCC (mingw)

2. Download Unfit-Python, e.g:

```terminal
git clone https://github.com/NicholasCF/Unfit-Python
```

3. Download Unfit in the **same** directory, e.g:
```terminal
git clone https://github.com/ComputationalBioLab/Unfit.git
```
4. Start Code::Blocks and open the Unfit project file (Unfit.cbp) in the Unfit folder
5. In the Unfit project, choose the Library option, then Build
6. Open the Unfit-Python project file (UnfitPython.cbp) in the Unfit-Python folder with Code::Blocks
7. Build the Unfit-Python project with the Debug option.

Currently, in MacOS, the result is a __*.dylib__ file. Simply rename this to a __*.so__ file.

8. Execute the _main.py_ Python file to run an example.

### Usage
___
#### Specifying model
Derive a class from the GenericCostFunction class in libUnfitPython module, as demonstrated in mycostfunction.py, changing the model in the following segment as needed:
~~~python
def __call__(self, x):
r = libUnfitPython.std_vector_double()
r[:] = self.y[:]
for i, ti in enumerate(self.t):
model = x[0] + x[1] * ti        #change this
r[i] -= model
return r
~~~
#### Solving problem
Do the following syntax, and the results will be stored in initial_guess:

~~~python
initial_guess = libUnfitPython.std_vector_double()
initial_guess[:] = [guess1, guess2, ...]

cf = CostFunction()
cf = Initialise(x_data, y_data)        #the data to be put into cost function

op = libUnfitPython.Optimizer()        #replace 'Optimizer' with any of the optimizer names
op.FindMin(cf, initial_guess)
~~~

Additionally, the SetBounds function needs to be called, using either of the following ways, for the optimizers except NelderMead and LevenbergMarquardt before calling FindMin:

~~~python
op.bounds.SetBounds(index, lower_bound, upper_bound)
op.bounds.SetBounds(lower_bounds, upper_bounds)        #The bounds are std_vector_double objects
~~~
For further modifications of the optimization process, check the options and bounds members of the optimizers, which is documented in the original [Unfit](https://github.com/ComputationalBioLab/Unfit).

### Running Tests
___
There are two sets of tests, in the TestExamples and Unittest folders, made with Python unittest. These tests can be run to check whether the build is successful.

The TestExamples tests serves as an example for users to follow in using Unfit, and check that access of Unfit through Python does not affect results. To run all tests, exectute the TestExamples module. To run individual tests, execute the relevant modules.

The Unittest tests ensures that the functions and objects behave in the same way as their C++ counterparts, and no compatibility issues arise between C++ and Python. Similarly, to run all tests, exectute the Unittest module. To run individual tests, execute the relevant modules.

### Development Environment
___
This project is built with:
* C++11
* CodeBlocks
* Python 2.7
* Python unittest

Development is mainly done in MacOS environment, but this is also ocassionally tested in Windows and Linux environment.

### Contributing
___
We are serious about this being around for a long time and hopefully becoming useful to more and more people. After much study, we have decided to require contributing license agreements (CLAs) from our contributors to keep our work open. Our CLA is adapted directly from the one used by the Apache Foundation, and can be found [here](https://computationalbiolab.github.io/assets/cla/IndividualContributorLicenseAgreement.pdf). If you are interested in how a CLA protects you as well as us, a good explanation is given [here](https://julien.ponge.org/blog/in-defense-of-contributor-license-agreements/). In case you can't be bothered reading the whole thing, here is our summary of the key points of the CLA:

1. (Just definitions)
2. You still own what you contribute, and can do **whatever you want** with it, but you allow us to use it forever, so we don't have to worry that you will change your mind and take it back
3. You promise you are not going to contribute something, then patent it and come after us for patent infringement
4. You are allowed to contribute what you are contributing
5. You are submitting something you have written, not something that belongs to someone else
6. You don't have to provide support unless you choose to do so

If you just want to use our work, you don't have to sign anything - just use it. If you want to contribute please sign, scan and email it back to us. You only have to do this once to be able to contribute to any of our projects.

### License
___
This project is licensed under the GNU General Public License version 3.0 - see the [LICENSE.md](https://github.com/NicholasCF/Unfit-Python/blob/master/LICENSE) file for details









