## Code
The code uses an algorithm to calculate the inverse Laplace transform of the input signal. Most constants can be changed in the init of classes/property.py, other constants in helpers/analyticalvalues.py.

## Usage
The code should be called from this directory using the format "python main.py INPUTSIGNAL". INPUTSINGAL can be chosen from this list:
-     exponential
      Uses the Laplace transform of an exponential function as input.
-     exponentialSys
      Uses the Laplace transform of an exponential function as input, but multiplies the input signal by 1.1.
-     exponentialRand
      Uses the Laplace transform of an exponential function as input, but multiplies the input signal by a random number between 10/11 and 11/10.
-     exponentialNum
      Uses the Laplace transform of an exponential function as input, but uses a discrete set of points and interpolation to gain additional values instead of using a continuous function.
-     cosine
      Uses the Laplace transform of a cosine function as input.
-     fit
      Uses a fit of a very simple model to the data set as input.
-     dataset
      Uses the reflectance as a function of absorption coefficient from the data set as input
-     reflectance
      Uses the model of reflectance as a function of absorption coefficient as input.
-     reflectanceNum
      Uses the model of reflectance as a function of absorption coefficient as input, but uses a discrete set of points and interpolation to gain additional values instead of using a continuous function.
-     normalize
      Calculates the right normalization constant for "reflectance" and "reflectanceNum"
-     saveForFit
      Does not perfrom the algorithm. Saves a file with reflectance as a function of absorption coefficient from the data set to make a fit to.
