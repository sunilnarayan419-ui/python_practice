# Electricity Bill Calculate electricity bill using slab-based pricing.

class ElectricityBill:
    def __init__(self, units_consumed):
        self.units_consumed = units_consumed

    def calculate_bill(self):
        bill_amount = 0

        if self.units_consumed <= 100:
            bill_amount = self.units_consumed * 5
        elif self.units_consumed <= 200:
            bill_amount = (100 * 5) + ((self.units_consumed - 100) * 7)
        elif self.units_consumed <= 300:
            bill_amount = (100 * 5) + (100 * 7) + ((self.units_consumed - 200) * 10)
        else:
            bill_amount = (100 * 5) + (100 * 7) + (100 * 10) + ((self.units_consumed - 300) * 15)

        return bill_amount


# Example usage
units = float(input("Enter the number of units consumed: "))
electricity_bill = ElectricityBill(units)
bill = electricity_bill.calculate_bill()
print(f"Electricity bill for {units} units consumed: ${bill:.2f}")