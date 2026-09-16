def main():
    answer = input("What time is it? ")

    result = convert(answer)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    return float(hours) + minutes


if __name__ == "__main__":
    main()