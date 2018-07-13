# Bachelorproject
## From reflectance as a function of absorption coefficient to path length distribution for photons in tissue using an inverse Laplace transform

Copyright (c) 2018 Nathalie van Sterkenburg

By: Nathalie van Sterkenburg

Username: nathhje

## About
This is the source code of my bachelor project, which I am doing as the last project in my bachelor of Physics. To understand the code, it is strongly recommended to read my thesis "From reflectance as a function of absorption coefficient to path length distribution for photons in tissue using an inverse Laplace transform". To summarize: I'm studying the relationship between reflectance as a function of absorption coefficient and path length distribution for photons moving through tissue. This relationship is an inverse Laplace transform. To perform this transformation, an algorithm is used on a signal, which gives the inverse Laplace transform of that signal. This algorithm can be found in the directory "InverseLaPlace". One of the signals that the algorithm can be used on, is from a data set with reflected photons. To create this data set, a Monte Carlo simulation was made that simulates photons moving through tissue. This simulation can be found in the directory "monte_carlo". The directory "LaPlaceTransform" contains some code that numerically performs a Laplace transform on a discrete path length distribution.

NOTE: the code in "LaPlaceTransform" and some of the possible ways to call main.py in "InverseLaPlace" require data out of .csv files to be used. These files are not included in this repository, but new data can be created by running the Monte Carlo simulation.

## Requirements
The code was written in Python 3.6. A list of required packages can be found in the file requirements.txt

## Usage
The usage of each of the three functions of the code, simulation, Laplace, inverse Laplace, can be found in their respective directories.
