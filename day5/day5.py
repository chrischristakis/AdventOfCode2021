def part1_and_part2(lines):
    coords = {}
    for line in lines:
        p1 = line[0]
        p2 = line[1]
        # Unit steps in x and y (Problem definition states only 45 degrees, so these will only ever be 1,0,-1)
        dx = (p2[0] - p1[0]) / max(abs(p2[0] - p1[0]), 1)  # Max since we dont want to divide by 0
        dy = (p2[1] - p1[1]) / max(abs(p2[1] - p1[1]), 1)

        curr_x = p1[0]
        curr_y = p1[1]
        while (curr_x, curr_y) != (p2[0] + dx, p2[1] + dy):
            if (curr_x, curr_y) in coords:
                coords[(curr_x, curr_y)] += 1
            else:
                coords[(curr_x, curr_y)] = 1
            curr_x += dx
            curr_y += dy

    count = 0
    for key in coords:
        if coords[key] > 1:
            count += 1
    return count


if __name__ == "__main__":
    lines = []
    with open("input") as file:
        while line := file.readline().rstrip():
            lines.append([(int(coord.split(",")[0]), int(coord.split(",")[1])) for coord in line.split(" -> ")])

    # Only straight lines (No diagonals)
    lines_straight = list(filter(lambda e: (e[0][0] == e[1][0] or e[0][1] == e[1][1]), lines))
    print("Part 1 sln: ", part1_and_part2(lines_straight))
    print("Part 2 sln: ", part1_and_part2(lines))
