def part1_and_part2():
    # This problem also assumes that the target is always x>0 and y<0, makes it easier.
    # No need to parse input, its too small. Lets just hardcode. target area: x=201..230, y=-99..-65
    x1 = 201; x2 = 230; y1 = -65; y2 = -99

    # max is y2 since vy at y=0 will always be -vy0, so if vyo=y2, then when we hit y=0 our next move will hit target
    # area in the y axis. Low bound is -y2 since we can go from origin to target in one move with x = x2orx1 y = y2ory1
    maxy = 0
    valid_velocities = set()
    for vx0 in range(x2+1):
        for vy0 in range(y2, -y2):
            y = x = 0
            vx = vx0; vy = vy0
            maxy_local = 0
            while y >= y2 and x <= x2:  # We only stop when one position is out of bounds of the target area.
                x += vx; y += vy
                vx -= (vx>0); vy -= 1
                maxy_local = max(y, maxy_local)
                if x1 <= x <= x2 and y1 >= y >= y2:
                    maxy = max(maxy_local, maxy)
                    valid_velocities.add((vx0, vy0))
    return maxy, len(valid_velocities)


if __name__ == "__main__":
    print("Part 1 and 2 sln:", part1_and_part2())
