class MeltingPointCalculator:

    @staticmethod
    def calculate_melting_point(sequence):
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

        # Wallace rule
        melting_point = 2 * (num_A + num_T) + 4 * (num_C + num_G)

        return melting_point

melting_pint_calculator = MeltingPointCalculator()

try:
    dna_sequence = input("Enter a DNA sequence (only A, T, C, G): ")
    melting_point = melting_pint_calculator.calculate_melting_point(dna_sequence)
    print(f"The estimated melting point of the DNA sequence is: {melting_point} °C") 

except Exception as e:
    print(f"Error: {e}") 