def part1_and_part2():
    # This problem also assumes that the target is always x>0 and y<0, makes it easier.
    x1 = 201; x2 = 230; y1 = -65; y2 = -99

    def get_x(vx, x=0):
        while x <= x2:
            yield tuple((x >= x1, x)); x += vx; vx -= (vx > 0)

    def get_y(vy, y=0):
        while y >= y2:
            yield tuple((y <= y1, y)); y += vy; vy -= 1

    # max is y2 since vy at y=0 will always be -vy0, so if vyo=y2, then when we hit y=0 our next move will hit target
    # area in the y axis. Low bound is -y2 since we can go from origin to target in one move with x = x2orx1 y = y2ory1
    maxy = 0
    count = 0
    for vx0 in range(x2+1):
        for vy0 in range(y2, -y2):
            y_gen = get_y(vy0)
            x_gen = get_x(vx0)
            local_maxy = 0
            while (x_hit := next(x_gen, None)) is not None and (y_hit := next(y_gen, None)) is not None:
                local_maxy = max(y_hit[1], local_maxy)
                if x_hit[0] and y_hit[0]:
                    maxy = max(maxy, local_maxy)
                    count += 1
                    break

    return maxy, count


if __name__ == "__main__":
    print("Part 1 and 2 sln:", part1_and_part2())
