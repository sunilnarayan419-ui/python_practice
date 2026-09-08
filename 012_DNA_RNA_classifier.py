# DNA RNA classifier 

class DNA_RNA_Classifier:
    @staticmethod
    def classify_sequence(sequence):
        sequence = sequence.strip().upper()
        if not sequence:
            return "Invalid sequence"

        if all(nucleotide in "ATCG" for nucleotide in sequence):
            return "DNA"
        elif all(nucleotide in "AUCG" for nucleotide in sequence):
            return "RNA"
        else:
            return "Invalid sequence"

    def classify_sequence_with_stability(self, stability):
        if stability == "more":
            return "DNA"
        elif stability == "less":
            return "RNA" 

    def classify_sequence_with_availability_OH_group_at_3_prime_end(self, availability):
        if availability == "available":
            return "RNA"
        elif availability == "not available":
            return "DNA"

dna_rna_classifier = DNA_RNA_Classifier()

try:
    sequence = input("Enter a DNA or RNA sequence: ")
    classification = dna_rna_classifier.classify_sequence(sequence)
    print(f"The sequence is classified as: {classification}")

    stability = input("Enter the stability of the sequence (more/less): ")
    classification_stability = dna_rna_classifier.classify_sequence_with_stability(stability)
    print(f"Based on stability, the sequence is classified as: {classification_stability}")

    availability = input("Is the OH group at the 3' end available? (available/not available): ")
    classification_availability = dna_rna_classifier.classify_sequence_with_availability_OH_group_at_3_prime_end(availability)
    print(f"Based on availability of OH group at 3' end, the sequence is classified as: {classification_availability}")     

except Exception as e:
    print(f"Error: {e}") 