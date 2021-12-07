def part1_and_part2(days):
    with open("input") as file:
        populace = [0] * 9  # Most days away from breeding a fish will be is 9 (7 days + 2 for newborns)
        for p in [int(x) - 1 for x in file.readline().rstrip().split(",")]:
            populace[p] += 1

        # First day doesnt count
        for i in range(days-1):
            to_create = populace[0]
            # List w/o first element, and add day 1 to end of list
            populace = populace[1:] + [to_create]
            populace[6] += to_create

        return sum(populace)


if __name__ == "__main__":
    print("Part 1 sln:", part1_and_part2(80))
    print("Part 2 sln:", part1_and_part2(256))
