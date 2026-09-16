# TODO
from cs50 import get_float

while True:
    cents = get_float("Cents: ")
    if cents > 0:
        break

cents = round(cents * 100)

count = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while cents >= 25:
    cents = cents - 25
    count += 1
    quarters += 1

print(f"Quarters: {quarters}")

while cents >= 10:
    cents = cents - 10
    count += 1
    dimes += 1

print(f"Dimes: {dimes}")

while cents >= 5:
    cents = cents - 5
    count += 1
    nickels += 1

print(f"Nickels: {nickels}")

while cents >= 1:
    cents = cents - 1
    count += 1
    pennies += 1


print(f"Pennies: {pennies}")
print(f"Total coins: {count}")
