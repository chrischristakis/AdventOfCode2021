import heapq


def part1_and_part_2(cave):
    # We'll be using dijkstra's
    # {node: [weight, prev_node]}
    tracker = {}
    unvisited = [(0, (0, 0))]  # Start with top left and distance value of 0 since we're starting on it
    for row in range(len(cave)):
        for col in range(len(cave[0])):
            tracker[(row, col)] = [float('inf'), None]
    # We start at (0,0) so initialize it at 0
    tracker[(0, 0)] = [0, None]

    # A generator function
    def get_adjacent(row, col):
        for (row_offset, col_offset) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= row + row_offset < len(cave) and 0 <= col + col_offset < len(cave[0]):
                yield row+row_offset, col + col_offset

    visited = set()
    while unvisited:
        distance, (row, col) = heapq.heappop(unvisited)
        if (row, col) in visited:
            continue

        for r_adj, c_adj in get_adjacent(row, col):
            dist_adj = cave[r_adj][c_adj]
            dt = distance + dist_adj  # Distance from (0,0) to the adjacent nodde
            if dt < tracker[(r_adj, c_adj)][0]:
                tracker[(r_adj, c_adj)] = [dt, (row, col)]

            heapq.heappush(unvisited, (dt, (r_adj, c_adj)))

        visited.add((row, col))  # Never return to this node.

    # Our answer simply is the dist value at the end of dijkstra's at the bottom right coord.
    return tracker[(len(cave) - 1, len(cave[0]) - 1)][0]


if __name__ == "__main__":

    with open("input") as file:
        cave = [[int(node) for node in line.rstrip()] for line in file.readlines()]
        print("Part 1 sln:", part1_and_part_2(cave))

        tilew = len(cave)
        tileh = len(cave[0])
        # Credit to mebeim for part 2, couldn't get this one.
        # This loop extends the cave to the right and increments it by one on each tile
        for _ in range(4):
            for row in cave:
                tail = row[-tilew:]  # Basically make a selection of 100 elements each time starting from the end
                for x in tail:
                    x += 1
                    if x > 9:
                        x = 1
                    row.append(x)

        for _ in range(4):
            for row in cave[-tileh:]:
                row = [(x + 1) if x < 9 else 1 for x in row]
                cave.append(row)

        print("Part 2 sln:", part1_and_part_2(cave))
