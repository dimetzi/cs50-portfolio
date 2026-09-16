def main():
    string = input()
    result = convert(string)
    print(result)


def convert(str):
    msg = str.replace(":)", '🙂').replace(":(", '🙁')
    return msg

main()