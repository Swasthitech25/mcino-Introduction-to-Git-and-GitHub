# This program calculates compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

compound_interest = principal * ((1 + rate / 100) ** time)

print("Compound Interest is:", round(compound_interest, 2))
