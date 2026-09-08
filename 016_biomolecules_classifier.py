# biomolecules classifier based on molecular formula and molecular mass 
import re


class BiomoleculeClassifier:
    # Average atomic masses (Da)
    ATOMIC_MASSES = {
        "H": 1.008,
        "C": 12.011,
        "N": 14.007,
        "O": 15.999,
        "P": 30.974,
        "S": 32.06,
    }

    @staticmethod
    def parse_formula(molecular_formula):
        """
        Parse a molecular formula such as C6H12O6
        into a dictionary of element counts.
        """

        molecular_formula = molecular_formula.strip()

        if not molecular_formula:
            raise ValueError("Molecular formula cannot be empty")

        # Accept formulas such as C6H12O6, CH4, C27H46O
        pattern = r"([A-Z][a-z]?)(\d*)"
        matches = re.findall(pattern, molecular_formula)

        # Reconstruct formula to ensure the entire input is valid
        reconstructed = "".join(
            element + count for element, count in matches
        )

        if reconstructed != molecular_formula:
            raise ValueError(
                "Invalid molecular formula. Use standard notation such as C6H12O6."
            )

        composition = {}

        for element, count in matches:
            if element not in BiomoleculeClassifier.ATOMIC_MASSES:
                raise ValueError(
                    f"Element '{element}' is not supported by this classifier."
                )

            count = int(count) if count else 1
            composition[element] = composition.get(element, 0) + count

        return composition

    @staticmethod
    def calculate_molecular_mass(composition):
        """Calculate approximate molecular mass from elemental composition."""

        molecular_mass = 0

        for element, count in composition.items():
            molecular_mass += (
                BiomoleculeClassifier.ATOMIC_MASSES[element] * count
            )

        return molecular_mass

    @staticmethod
    def classify_mass(molecular_mass):
        """
        Mass categories are computational bins, not universal
        biochemical definitions.
        """

        if molecular_mass <= 0:
            raise ValueError("Molecular mass must be greater than zero")

        if molecular_mass < 100:
            return "Very small molecule"
        elif molecular_mass < 1000:
            return "Small molecule"
        elif molecular_mass < 10000:
            return "Intermediate-sized molecule"
        else:
            return "Large biomolecule / macromolecular range"

    @staticmethod
    def classify_biomolecule(composition):
        """
        Estimate the likely biomolecular class from elemental composition.

        This is a heuristic classification and should not be treated
        as definitive structural identification.
        """

        elements = set(composition.keys())

        carbon = composition.get("C", 0)
        hydrogen = composition.get("H", 0)
        oxygen = composition.get("O", 0)
        nitrogen = composition.get("N", 0)
        phosphorus = composition.get("P", 0)
        sulfur = composition.get("S", 0)

        # No carbon generally indicates an inorganic/small molecule
        if carbon == 0:
            return "Non-carbon-based / inorganic molecule"

        # Strong carbohydrate-like elemental pattern
        if (
            nitrogen == 0
            and phosphorus == 0
            and sulfur == 0
            and oxygen > 0
            and carbon > 0
        ):
            return "Likely carbohydrate or carbohydrate-like molecule"

        # Nitrogen-rich composition
        if nitrogen > 0 and carbon > 0:
            if phosphorus > 0:
                return "Likely nucleic-acid-related or phosphorylated biomolecule"

            if sulfur > 0:
                return "Likely nitrogen- and sulfur-containing biomolecule"

            return "Likely nitrogen-containing biomolecule"

        # Phosphorus-containing molecule
        if phosphorus > 0:
            return "Likely phosphorylated biomolecule"

        # Carbon/hydrogen-rich compounds with little oxygen
        if carbon > 0 and hydrogen > 0:
            if oxygen == 0:
                return "Likely hydrocarbon-like / lipid-like molecule"

            return "Likely organic biomolecule"

        return "Uncertain biomolecular class"

    @staticmethod
    def analyze(molecular_formula):
        """
        Perform complete molecular analysis from molecular formula.
        """

        composition = BiomoleculeClassifier.parse_formula(
            molecular_formula
        )

        molecular_mass = BiomoleculeClassifier.calculate_molecular_mass(
            composition
        )

        mass_classification = BiomoleculeClassifier.classify_mass(
            molecular_mass
        )

        biomolecule_classification = BiomoleculeClassifier.classify_biomolecule(
            composition
        )

        return {
            "molecular_formula": molecular_formula,
            "elemental_composition": composition,
            "molecular_mass_Da": round(molecular_mass, 3),
            "mass_classification": mass_classification,
            "likely_biomolecule_class": biomolecule_classification,
            "warning": (
                "Classification is heuristic. Molecular formula alone "
                "cannot definitively determine molecular structure or "
                "biomolecular identity."
            ),
        }


# Example
result = BiomoleculeClassifier.analyze("C6H12O6")

for key, value in result.items():
    print(f"{key}: {value}")

