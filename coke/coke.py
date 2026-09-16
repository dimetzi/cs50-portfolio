amount_due = 50


while amount_due > 0:
    print(f"Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due = amount_due - coin

change_owed = abs(amount_due)

print("Change Owed:", change_owed)