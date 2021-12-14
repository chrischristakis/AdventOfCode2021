def part1_and_part2():
    sln1 = 0
    with open("input") as file:
        paper = []
        folds = []
        [largest_x, largest_y] = [0, 0]  # For printing.

        # Dots
        while line := file.readline().rstrip():
            (x, y) = tuple(line.split(","))
            largest_x = max(largest_x, int(x))
            largest_y = max(largest_y, int(y))
            paper.append(tuple((int(x), int(y))))

        # Folds
        while line := file.readline().rstrip():
            [axis, val] = line.split("=")
            axis = axis.split(" ")[-1]
            folds.append(tuple((axis, int(val))))

        def print_paper():
            for y in range(largest_y + 1):
                for x in range(largest_x + 1):
                    if (x, y) in paper:
                        print("\u2588", end=" ")
                    else:
                        print(".", end=" ")
                print()

        for i, (axis, line) in enumerate(folds):
            to_remove = set()
            for (x, y) in paper:
                if axis == 'x':
                    if x > line:
                        flipped_x = (line - (x - line))
                        paper.append((flipped_x, y))
                        to_remove.add((x, y))
                        largest_x = line
                if axis == 'y':
                    if y > line:
                        flipped_y = (line - (y - line))
                        paper.append((x, flipped_y))
                        to_remove.add((x, y))
                        largest_y = line

            paper = list(set(paper).difference(to_remove))
            if i == 0:
                sln1 = len(paper)
        print_paper()
    return sln1


if __name__ == "__main__":
    part1 = part1_and_part2()
    print("Part 1 sln:", part1)
    # Part 2 is implicit to the part1 function
