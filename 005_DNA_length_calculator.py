# DNA length calculator 

import csv

def calculate_dna_length(dna_sequence):
    return len(dna_sequence)

def main():
    input_file = "dna_sequences.csv"
    output_file = "dna_lengths.csv"

    with open(input_file, "r") as f:
        reader = csv.reader(f)
        dna_sequences = [row[0] for row in reader]

    dna_lengths = [calculate_dna_length(seq) for seq in dna_sequences]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["DNA Sequence", "Length"])
        for seq, length in zip(dna_sequences, dna_lengths):
            writer.writerow([seq, length])

if __name__ == "__main__":
    main()