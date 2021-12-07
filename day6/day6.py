import functools


def part1_and_part2(days):
    with open("input") as file:
        data = [int(x) - 1 for x in file.readline().rstrip().split(",")]
        populace = [0] * 9  # Most days away from breeding a fish will be is 9 (7 days + 2 for newborns)

        # Initial conditions
        for i in data:
            populace[i] += 1

        def shift_arr(l: list, end: int):
            temp = l[0]
            for j in range(len(l) - 1):
                l[j] = l[j+1]
            l[end] += temp

        # First day doesnt count
        for i in range(days-1):
            to_create = populace[0]
            shift_arr(populace, 6)
            populace[8] = to_create

        population = int(functools.reduce(lambda accum, e: accum+e, populace))
        return population


if __name__ == "__main__":
    print("Part 1 sln:", part1_and_part2(80))
    print("Part 2 sln:", part1_and_part2(256))
