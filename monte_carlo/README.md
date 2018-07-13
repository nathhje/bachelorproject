## Code
The code simulates photons moving through tissue. Constants can be changed in  the init of classessimulation/properties.py. What each type of call does can be changed in helpers/simulations.py.

## Usage
The code should be called from this directory using the format "python main.py TYPEOFRUN". TYPEOFRUN can be chosen from this list:
-     Rvsr
      Runs the simulation once and shows the outcome of reflectance as a function of radial distance against the analytical outcome.
-     RvsMua
      Runs the simulation for a range of absorption coefficients and shows the outcome of reflectance as a function of absorption coefficient against the analytical solution at a fixed radial distance.
-     savePhotons
      Runs the simulation and saves the reflections to a .csv file.
-     RvsrThree
      Does the same a "Rvsr" but for three different absorption coefficients and shows the outcomes in one figure.
