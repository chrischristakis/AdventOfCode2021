def part1_and_part2():
    result1 = 0
    result2 = 0
    with open("input") as file:
        heightmap = [list(line.rstrip()) for line in file.readlines()]
        heightmap = list(map(lambda e: [int(x) for x in e], heightmap))

        def check_adjacents(basin, x, y):
            above = below = left = right = (x, y)
            if y > 0:
                if heightmap[y - 1][x] < 9:
                    above = (x, y - 1)
            if y < len(heightmap) - 1:
                if heightmap[y + 1][x] < 9:
                    below = (x, y + 1)
            if x > 0:
                if heightmap[y][x - 1] < 9:
                    left = (x - 1, y)
            if x < len(heightmap[0]) - 1:
                if heightmap[y][x + 1] < 9:
                    right = (x + 1, y)

            results = {above, below, left, right}.difference(set(basin))
            return list(results)

        basin_sizes = []
        for row in range(len(heightmap)):
            for col in range(len(heightmap[0])):
                above = below = left = right = 10  # No height will be > 10, initial values.
                if row > 0:
                    above = heightmap[row-1][col]
                if row < len(heightmap) - 1:
                    below = heightmap[row+1][col]
                if col > 0:
                    left = heightmap[row][col-1]
                if col < len(heightmap[0]) - 1:
                    right = heightmap[row][col+1]
                adjacents = [above, below, left, right]
                if heightmap[row][col] < min(adjacents):
                    result1 += 1 + heightmap[row][col]

                    low = (col, row)
                    basin = [low]
                    last_len = 0  # To check if the basin size hasn't changed and were done.
                    to_check = [low]
                    while len(basin) != last_len:
                        last_len = len(basin)
                        for coord in to_check:
                            to_add = check_adjacents(basin, coord[0], coord[1])
                            basin = basin + to_add
                            to_check += to_add
                    basin_sizes.append(len(basin))

        basin_sizes.sort()
        print(basin_sizes)
        result2 = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

    return result1, result2


if __name__ == "__main__":
    result = part1_and_part2()
    print("Part 1 sln:", result[0])
    print("Part 2 sln:", result[1])
