# protein molecular mass calculator
"""protein molecular mass calculator by taking protein sequence as input from CSV file and calculating the molecular mass of each protein sequence and writing the results to a new CSV file"""

import csv

def calculate_molecular_mass(protein_sequence):
    amino_acid_masses = {
        'A': 89.09, 'C': 121.15, 'D': 133.10, 'E': 147.13,
        'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.17,
        'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12,
        'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09,
        'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
    }
    mass = sum(amino_acid_masses.get(aa, 0) for aa in protein_sequence)
    return mass

def main():
    input_file = "protein_sequences.csv"
    output_file = "protein_masses.csv"

    with open(input_file, "r") as f:
        reader = csv.reader(f)
        protein_sequences = [row[0] for row in reader]

    protein_masses = [calculate_molecular_mass(seq) for seq in protein_sequences]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Protein Sequence", "Molecular Mass"])
        for seq, mass in zip(protein_sequences, protein_masses):
            writer.writerow([seq, mass])

if __name__ == "__main__":
    main()