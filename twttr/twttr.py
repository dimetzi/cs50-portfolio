text = input("Input : ")
list = ["a", "e", "i", "o", "u"]

print("Output: ", end="")

for c in text:
    if c.lower() not in list:
        print(c, end="")
print()