# feasibility of reaction based on Gibbs free energy change 

import math


class ReactionFeasibility:
    """
    Calculate Gibbs free energy change and assess thermodynamic
    spontaneity of a reaction.

    Equation:
        ΔG = ΔH - TΔS

    Units:
        ΔH = kJ/mol
        ΔS = J/(mol·K)
        T  = K
        ΔG = kJ/mol
    """

    @staticmethod
    def _validate_inputs(delta_h, delta_s, temperature):
        """Validate thermodynamic input values."""

        values = {
            "ΔH": delta_h,
            "ΔS": delta_s,
            "Temperature": temperature
        }

        for name, value in values.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be a numerical value.")

            if not math.isfinite(value):
                raise ValueError(f"{name} must be a finite number.")

        if temperature <= 0:
            raise ValueError(
                "Temperature must be greater than 0 K."
            )

    @staticmethod
    def calculate_gibbs_free_energy(delta_h, delta_s, temperature):
        """
        Calculate Gibbs free energy change (ΔG).

        ΔH is provided in kJ/mol.
        ΔS is provided in J/(mol·K), so it is converted
        to kJ/(mol·K) before calculation.
        """

        ReactionFeasibility._validate_inputs(
            delta_h,
            delta_s,
            temperature
        )

        # Convert entropy from J/(mol·K) to kJ/(mol·K)
        delta_s_kj = delta_s / 1000

        # Gibbs free energy equation
        delta_g = delta_h - (temperature * delta_s_kj)

        return delta_g

    @staticmethod
    def assess_reaction(delta_h, delta_s, temperature):
        """
        Calculate ΔG and determine thermodynamic spontaneity.

        ΔG < 0  → spontaneous in the forward direction
        ΔG = 0  → equilibrium
        ΔG > 0  → non-spontaneous in the forward direction

        Note:
        Thermodynamic spontaneity does not indicate reaction rate.
        """

        delta_g = ReactionFeasibility.calculate_gibbs_free_energy(
            delta_h,
            delta_s,
            temperature
        )

        # Use a small tolerance for floating-point comparisons
        tolerance = 1e-9

        if delta_g < -tolerance:
            classification = "Thermodynamically spontaneous"
            direction = "Forward direction favored"

        elif abs(delta_g) <= tolerance:
            classification = "At equilibrium"
            direction = "Neither direction is thermodynamically favored"

        else:
            classification = "Thermodynamically non-spontaneous"
            direction = "Reverse direction favored"

        return {
            "delta_g": delta_g,
            "classification": classification,
            "direction": direction
        }


def main():
    print("=== Gibbs Free Energy Calculator ===")
    print("Calculate ΔG = ΔH - TΔS\n")

    try:
        delta_h = float(
            input("Enter ΔH (kJ/mol): ")
        )

        delta_s = float(
            input("Enter ΔS (J/(mol·K)): ")
        )

        temperature = float(
            input("Enter temperature (K): ")
        )

        result = ReactionFeasibility.assess_reaction(
            delta_h,
            delta_s,
            temperature
        )

        print("\n--- Results ---")
        print(f"ΔG: {result['delta_g']:.3f} kJ/mol")
        print(f"Classification: {result['classification']}")
        print(f"Thermodynamic direction: {result['direction']}")

        print(
            "\nNote: Thermodynamic spontaneity does not mean "
            "the reaction will occur rapidly. Reaction kinetics, "
            "activation energy, and reaction conditions also matter."
        )

    except ValueError as error:
        print(f"\nInput error: {error}")

    except TypeError as error:
        print(f"\nType error: {error}")


if __name__ == "__main__":
    main()

