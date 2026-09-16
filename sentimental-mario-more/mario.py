# TODO

def main():
    height = input_height()
    for i in range(height):
        for space in range(height - i - 1):
            print(" ", end="")
        for j in range(i+1):
            print("#", end="")
        print("  ", end="")
        for j in range(i+1):
            print("#", end="")
        print()



def input_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                return n
        except ValueError:
            print("Not an integer")


main()

