# atoms in molecules calculator
"""calculator for atoms in molecules by taking molecular formulas as input from CSV file and calculating the number of atoms of each element in the molecule and writing the results to a new CSV file"""

import csv
import re

def parse_molecular_formula(formula):
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, formula)
    atom_counts = {}
    for element, count in matches:
        count = int(count) if count else 1
        if element in atom_counts:
            atom_counts[element] += count
        else:
            atom_counts[element] = count
    return atom_counts

