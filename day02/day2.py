def part1():
    # 'down' means depth increases, 'up' means a depth decrease.
    horizontal = depth = 0
    with open("input") as file:
        while line := file.readline().rstrip():
            info = line.split(" ")
            match info[0]:
                case 'forward':
                    horizontal += int(info[1])
                case 'down':
                    depth += int(info[1])
                case 'up':
                    depth -= int(info[1])

    return horizontal * depth


def part2():
    horizontal = depth = aim = 0
    with open("input") as file:
        while line := file.readline().rstrip():
            info = line.split(" ")
            match info[0]:
                case 'forward':
                    horizontal += int(info[1])
                    depth += aim * int(info[1])
                case 'down':
                    aim += int(info[1])
                case 'up':
                    aim -= int(info[1])

    return horizontal * depth


if __name__ == "__main__":
    print('Part 1 sln:', part1())
    print('Part 2 sln:', part2())
