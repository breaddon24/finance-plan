asterisks = "*" * 50
print(asterisks)
print("*           WEALTH GENERATOR           *")
print(asterisks)

while True:
    try:
        income_input = input("Enter your monthly income after tax ($): ")
        if income_input.lower() == "exit":
            exit()
        income = float(income_input)
        if income > 0:
            break
        print("Income must be greater than 0")
    except ValueError:
        print("Income must be an integer")

while True:
    print("\nChoose an Investment Strategy: ")
    print("1. Conservative (5% expected annual return)")
    print("2. Aggressive (10% expected annual return)")

    strategy = input("Enter your investment strategy: ")

    if strategy == "exit":
        exit()

    elif strategy == "1":
        rate = 0.05
        break

    elif strategy == "2":
        rate = 0.10
        break

    else:
        print("Invalid choice, Enter 1 or 2")

investment = income * 0.20
future_wealth = 0
for year in range(1, 11):
    future_wealth = (future_wealth + (investment * 12) * (1 + rate))

print(asterisks)
print(f"FINANCIAL RESULT:")
print(f"By investing 20% of your income (${investment:,.2f}/month) with your strategy,")
print(f"estimated wealth in 10 years will be: ${future_wealth:,.2f}]")
print(asterisks)
