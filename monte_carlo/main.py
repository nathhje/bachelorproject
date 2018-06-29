import sys
import helpers.simulations as sim

def main():
    """ Runs the simulation of photons moving through tissue in different ways."""

    # Runs the simulation for one mua and shows reflectance vs radial distance
    if sys.argv[1] == "Rvsr":
        
        sim.Rvsr()

    # Runs the simulation for a range of mua and shows reflectance vs mua
    # for a given radial distance
    elif sys.argv[1] == "RvsMua":
        
        sim.RvsMua()
    
    # Runs the simulation for a range of mua and saves all reflections in a file
    elif sys.argv[1] == "savePhotons":
        
        sim.savePhotons()
        
    # Runs the simulation for three different mua and shows reflectance vs
    # radial distance for each
    elif sys.argv[1] == "RvsrThree":
        
        sim.RvsrThree()

if __name__ == "__main__":
    main()