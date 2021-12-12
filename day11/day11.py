def part1_and_part2(days):
    flashes = 0
    sync_step = -1
    with open("input") as file:
        octopi = [[int(x) for x in list(line.rstrip())] for line in file.readlines()]

        beyond_initial_days = False
        step = 0
        while step < days:
            # First loop through all octopi and add 1, and store octopi in to_flash.
            to_flash = []  # Data: row, col
            all_zero = True  # For checking if all octopi synced for part 2
            for row in range(len(octopi)):
                for col in range(len(octopi[0])):
                    if octopi[row][col] != 0:
                        all_zero = False

                    octopi[row][col] += 1
                    if octopi[row][col] > 9:
                        to_flash.append((row, col))

            # Check if all are synced (all zero)
            if all_zero:
                sync_step = step

            # Increment all neighbors by 1, if another neightbor becomes > 9, then add it to to_flash
            for coords in to_flash:
                row = coords[0]
                col = coords[1]
                row_range = (max(0, row - 1), min(len(octopi) - 1, row + 1))
                col_range = (max(0, col - 1), min(len(octopi[0]) - 1, col + 1))
                neighbors = []
                for row_n in range(row_range[0], row_range[1] + 1):
                    for col_n in range(col_range[0], col_range[1] + 1):
                        if (row_n, col_n) not in coords and octopi[row_n][col_n] <= 9:
                            octopi[row_n][col_n] += 1
                            if octopi[row_n][col_n] > 9:
                                to_flash.append((row_n, col_n))

            if not beyond_initial_days:
                flashes += len(to_flash)

            # Finally, after everything flashes, we reset our > 9 octopi.
            for coords in to_flash:
                octopi[coords[0]][coords[1]] = 0

            # We need to find when they all sync, so keep going beyond initial days if hasn't synced yet
            if step == days-1 and sync_step == -1:
                beyond_initial_days = True
                days += 1
            step += 1

    return flashes, sync_step


if __name__ == '__main__':
    result = part1_and_part2(100)
    print("Part 1 sln:", result[0])
    print("Part 2 sln:", result[1])
