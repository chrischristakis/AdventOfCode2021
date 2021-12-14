from collections import defaultdict


def part1_and_part2(tunnel_filter):
    solution = 0

    with open("input") as file:
        # Assemble the connections of the tunnels into a map, key is a node and values are the edges.
        tunnel_map = defaultdict(list)
        while line := file.readline().rstrip():
            (n1, n2) = tuple(line.split("-"))
            if n2 != 'start':
                tunnel_map[n1].append(n2)
            if n1 != 'start':
                tunnel_map[n2].append(n1)
        print(dict(tunnel_map))

        paths = [['start']]  # Attack on Titan anyone?
        accepted_paths = []
        while len(paths) > 0:
            path = paths.pop(0)  # Get the FIFO path
            top = path[-1]

            if top == 'end':
                accepted_paths.append(path)
                continue

            for connection in tunnel_map[top]:
                if tunnel_filter(path, connection):
                    paths.append(path + [connection])

        solution = len(accepted_paths)
    return solution


if __name__ == "__main__":

    def p1_filter(path, connection):
        return connection not in path or connection.isupper()

    def p2_filter(path, connection):
        lower = [c for c in path if c.islower()]
        duplicates_dont_exist = len(lower) == len(set(lower))
        return connection not in path or connection.isupper() or duplicates_dont_exist

    print("Part 1 sln:", part1_and_part2(p1_filter))
    print("Part 2 sln:", part1_and_part2(p2_filter))