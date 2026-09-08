# atoms in molecules calculator
"""calculator for atoms in molecules by taking molecular formulas as input from CSV file and calculating the number of atoms of each element in the molecule and writing the results to a new CSV file"""

import csv
import re

def parse_molecular_formula(formula):
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, formula)
    if not formula or ''.join(element + count for element, count in matches) != formula:
        raise ValueError("Invalid molecular formula")

    atom_counts = {}
    for element, count in matches:
        count = int(count) if count else 1
        atom_counts[element] = atom_counts.get(element, 0) + count
    return atom_counts


def main():
    input_file = "molecular_formulas.csv"
    output_file = "molecule_atoms.csv"

    with open(input_file, "r", newline="") as input_handle:
        formulas = [row[0].strip() for row in csv.reader(input_handle) if row]

    with open(output_file, "w", newline="") as output_handle:
        writer = csv.writer(output_handle)
        writer.writerow(["Molecular Formula", "Atom Counts"])
        for formula in formulas:
            atom_counts = parse_molecular_formula(formula)
            writer.writerow([formula, "; ".join(
                f"{element}: {count}" for element, count in atom_counts.items()
            )])


if __name__ == "__main__":
    main()

