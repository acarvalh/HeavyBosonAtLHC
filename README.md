# HeavyBosonAtLHC

Instalation is easier using CMSSW_7_4_0 enviroment on SLC6.
If one prefers local working version the requirements are doxygen , boost and matplotlib and 
Python 2.7 or higher (the writer did not succed in install locally, therefore do not take responsibility for this sentence).

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


