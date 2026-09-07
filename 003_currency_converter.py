# Currency Converter

class CurrencyConverter:

    @staticmethod
    def usd_to_eur(usd):
        return usd * 0.85

    @staticmethod
    def eur_to_usd(eur):
        return eur * 1.18


currency_converter = CurrencyConverter()

try:
    amount = float(input("Enter the amount: "))
    currency = input("Enter the currency (U for USD or E for EUR): ").strip().upper()

    if currency == "U":
        result = currency_converter.usd_to_eur(amount)
        print(f"{amount:.2f} USD is equal to {result:.2f} EUR")

    elif currency == "E":
        result = currency_converter.eur_to_usd(amount)
        print(f"{amount:.2f} EUR is equal to {result:.2f} USD")

    else:
        print("Invalid currency. Please enter 'U' for USD or 'E' for EUR.")

except ValueError:
    print("Invalid amount. Please enter a number.")