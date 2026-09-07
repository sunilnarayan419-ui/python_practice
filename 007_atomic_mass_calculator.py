# atomic mass calculator

"""atomic mass calculator by taking atomic symbols as input from CSV file and calculating the atomic mass of each atom and writing the results to a new CSV file"""

import csv

def calculate_atomic_mass(atomic_symbols):
    atomic_masses = {
        'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81,
        'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 19.007, 'Ne': 20.180,
        'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974,
        'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
        'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938,
        'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.38,
        'Ga': 69.723, 'Ge': 72.630, 'As': 74.922, 'Se': 78.971, 'Br': 79.904,
        'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.620
    }
    mass = sum(atomic_masses.get(symbol, 0) for symbol in atomic_symbols)
    return mass

def main():
    input_file = "atomic_symbols.csv"
    output_file = "atomic_masses.csv"

    with open(input_file, "r") as f:
        reader = csv.reader(f)
        atomic_symbols_list = [row[0].split() for row in reader]

    atomic_masses = [calculate_atomic_mass(symbols) for symbols in atomic_symbols_list]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Atomic Symbols", "Atomic Mass"])
        for symbols, mass in zip(atomic_symbols_list, atomic_masses):
            writer.writerow([", ".join(symbols), mass])

if __name__ == "__main__":
    main()