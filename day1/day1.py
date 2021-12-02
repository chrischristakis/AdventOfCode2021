import functools


def part1(depth_list):
    increments = 0
    for i, depth in enumerate(depth_list):
        if i == 0:
            last = depth
            continue

        if depth > last:
            increments += 1

        last = depth

    return increments


def part2(depth_list, slide_count):
    first_index= slide_count-1
    increments = 0
    for i, depth in enumerate(depth_list):
        # so we don't count out of bounds. In this example, must start at index 2.
        if i < first_index:
            continue

        # first measurement
        if i == first_index:
            last_measurement = functools.reduce(lambda accum, curr: accum+curr, depth_list[i::-1])
            continue

        curr_measurement = functools.reduce(lambda accum, curr: accum + curr, depth_list[i:i-slide_count:-1])

        if curr_measurement > last_measurement:
            increments += 1

        last_measurement = curr_measurement

    return increments


if __name__ == "__main__":
    with open('input') as file:
        depth_list = file.readlines()
        depth_list = [int(depth.rstrip()) for depth in depth_list]

    print('Part 1 Sln:', part1(depth_list))
    print('Part 2 sln:', part2(depth_list, 3))
