Jacobi_Method
=============

This is an implementation of the Jacobi method of diagonalization for symmetric matrices. See http://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm

It plots the offsets over time, and you can see that the error decreases exponentially.

The program runs well for smaller matrices (< 50x50), but after trying to diagonalize about 100x100 matrices, the program starts to suffer from roundoff error and may not terminate if the required precision is too low.

Features
========
--Diagonalize a random symmetric matrix, or extend for your own symmetric matrix
--Log the offsets over time to text files, or extend with your own callbacks
--Show simple plot of the offsets over time with the -p flag

Dependencies
============
This project depends on numpy for heavy matrix multiplication and matplotlib for graphing.

They can easily be installed in Ubuntu with the package manager:
```
sudo apt-get install python-numpy
sudo apt-get install python-matplotlib
```
Usage
=====
Run
```
        python jacobi.py
```
to execute the program, -h for help

