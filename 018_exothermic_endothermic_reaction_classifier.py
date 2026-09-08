# Exothermic and Endothermic Reaction Classifier 

class ExothermicEndothermicReactionClassifier:
    @staticmethod
    def classify_reaction(delta_h):
        if delta_h < 0:
            return "Exothermic"
        elif delta_h > 0:
            return "Endothermic"
        else:
            return "Neither exothermic nor endothermic (ΔH = 0)"

exothermic_endothermic_reaction_classifier = ExothermicEndothermicReactionClassifier()

try:
    delta_h = float(input("Enter the enthalpy change (ΔH) in kJ/mol: "))
    classification = exothermic_endothermic_reaction_classifier.classify_reaction(delta_h)
    print(f"The reaction is classified as: {classification}") 

except ValueError:
    print("Please enter a valid number for the enthalpy change (ΔH).") 