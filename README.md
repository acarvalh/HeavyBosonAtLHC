# HeavyBosonAtLHC

Instalation is easier using CMSSW_7_4_0 enviroment on SLC6.
If one prefers local working version the requirements are doxygen , boost and matplotlib and 
Python 2.7 or higher (the writer did not succed in install locally, therefore do not take responsibility for this sentence).

commit dammit!
===============================
Download and install:

svn co https://ekptrac.physik.uni-karlsruhe.de/public/theta/tags/testing theta

cd theta

make -j10

===============================
Setting the example

cd utils2/examples

mkdir myExamples ; cd myExamples

download the .py scripts of this repo here

to run

../../theta-auto.py myscript.py

the common.py is a copy of the one in hatslpc2014

==============================

More examples and exercices are very nicelly decribed in 
/utils2/examples/hatslpc2014/exercise-sheet/html/setup.html


====================================

Increase errors tolerance in limits setting

 in ../utils2/theta_auto/theta_interface.py

minuit_tolerance_factor = 1 ==> 18 (if you put a tolerance of 100 it works for WZ full combo)


if do notwork and still increase spit edm = 3 error

======================================

Decrease the range of erros from model in datacard

rangenorm_shape = 2.5
rangenorm = 2.0
for p in model.distribution.get_parameters():
d = model.distribution.get_distribution(p)
#    if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p=='jesatlas' or p == 'mesatlas' or p == 'jescms' or p == 'param_VVJJ_HP' or p == 'param_VVJJ_LP'):
if d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and ( p == 'param_VVJJ_HP' or p == 'param_VVJJ_LP'):
model.distribution.set_distribution_parameters(p, range = [-rangenorm_shape, rangenorm_shape])
#    elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas':
elif d['typ'] == 'gauss' and d['mean'] == 0.0 and d['width'] == 1.0 and p !='jesatlas' and p != 'mesatlas' and p != 'param_VVJJ_HP' and p != 'param_VVJJ_LP':
model.distribution.set_distribution_parameters(p, range = [-rangenorm, rangenorm])

d = model.distribution.get_distribution(p)
print p, d
