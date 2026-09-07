# number of people calculator
"""takes csv file as input with number of people in each household and calculates the total number of people and writes the results to a new csv file"""

import csv

def calculate_total_people(household_sizes):
    return sum(household_sizes)

def main():
    input_file = "household_sizes.csv"
    output_file = "total_people.csv"

    with open(input_file, "r") as f:
        reader = csv.reader(f)
        household_sizes = [int(row[0]) for row in reader]

    total_people = calculate_total_people(household_sizes)

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Total People"])
        writer.writerow([total_people])

if __name__ == "__main__":
    main() 