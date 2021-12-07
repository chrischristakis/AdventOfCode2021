def part1_and_part2():
    with open("input") as file:
        positions = [int(line) for line in file.readline().rstrip().split(",")]
        furthest = max(positions)

        def arithmetic_sequence(num):
            return int(num * ((1+num)/2))

        min_p1 = min_p2 = -1
        for i in range(furthest + 1):
            fuel1 = fuel2 = 0
            for pos in positions:
                fuel1 += abs(i - pos)
                fuel2 += arithmetic_sequence(abs(i - pos))
            if min_p1 == -1 or fuel1 < min_p1:
                min_p1 = fuel1
            if min_p2 == -1 or fuel2 < min_p2:
                min_p2 = fuel2

        return min_p1, min_p2


if __name__ == "__main__":
    sln = part1_and_part2()
    print("Part 1 sln:", sln[0])
    print("Part 2 sln:", sln[1])
