# calculation of H-bond in DNA sequence

class H_Bond_Calculator:
    @staticmethod
    def calculate_h_bonds(sequence):
        sequence = sequence.upper().strip()

        # Validate sequence
        if not sequence:
            return "Invalid DNA sequence: sequence is empty"

        if not all(nucleotide in "ATCG" for nucleotide in sequence):
            return "Invalid DNA sequence: use only A, T, C, and G"

        # Count nucleotides
        num_A = sequence.count("A")
        num_T = sequence.count("T")
        num_C = sequence.count("C")
        num_G = sequence.count("G")

        # Calculate hydrogen bonds
        return 2 * (num_A + num_T) + 3 * (num_C + num_G)

h_bond_calculator = H_Bond_Calculator()

try:
    dna_sequence = input("Enter a DNA sequence (only A, T, C, G): ")
    h_bonds = h_bond_calculator.calculate_h_bonds(dna_sequence)
    print(f"The estimated number of hydrogen bonds in the DNA sequence is: {h_bonds}")
except Exception as e:
    print(f"Error: {e}")  