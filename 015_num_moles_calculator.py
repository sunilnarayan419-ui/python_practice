# number of moles calculator by deffernt methods

class MolesCalculator:
    """This class calculates the number of moles using different methods"""

    @staticmethod
    def moles_from_mass(mass, molar_mass):
        """Calculate moles from mass and molar mass"""
        if molar_mass <= 0:
            raise ValueError("Molar mass must be greater than zero")
        return mass / molar_mass

    @staticmethod
    def moles_from_volume(volume, molar_volume=22.4):
        """Calculate moles from volume and molar volume (default is 22.4 L for gases at STP)"""
        if molar_volume <= 0:
            raise ValueError("Molar volume must be greater than zero")
        return volume / molar_volume

    @staticmethod
    def moles_from_particles(particles, avogadro_number=6.022e23):
        """Calculate moles from number of particles and Avogadro's number"""
        if avogadro_number <= 0:
            raise ValueError("Avogadro's number must be greater than zero")
        return particles / avogadro_number 

num_moles_calculator = MolesCalculator() 

try:
    method = input("Choose a method to calculate moles (mass, volume, particles): ").strip().lower()

    if method == "mass":
        mass = float(input("Enter the mass in grams: "))
        molar_mass = float(input("Enter the molar mass in g/mol: "))
        moles = num_moles_calculator.moles_from_mass(mass, molar_mass)
    elif method == "volume":
        volume = float(input("Enter the volume in liters: "))
        molar_volume = float(input("Enter the molar volume in L (default is 22.4 L for gases at STP): ") or 22.4)
        moles = num_moles_calculator.moles_from_volume(volume, molar_volume)
    elif method == "particles":
        particles = float(input("Enter the number of particles: "))
        avogadro_number = float(input("Enter Avogadro's number (default is 6.022e23): ") or 6.022e23)
        moles = num_moles_calculator.moles_from_particles(particles, avogadro_number)
    else:
        raise ValueError("Invalid method selected. Please choose 'mass', 'volume', or 'particles'.")

    print(f"The number of moles calculated is: {moles:.4f} mol")
except ValueError as e:
    print(f"Error: {e}") 