teams = []
    # TODO: Read teams into memory from file
    with open("sys.argv[1]", newline=" ") as csvfile:
        reader = csv.DictReader(csvfile)
        for teams in reader:
            print(teams["name"], teams["rating"])