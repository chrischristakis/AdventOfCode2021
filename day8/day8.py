def part1():
    with open("input") as file:
        count = 0
        while line := file.readline().rstrip():
            output_nums = list(filter(lambda e: len(e) == 2 or len(e) == 4 or len(e) == 3 or len(e) == 7
                                      , line.split(" | ")[1].split(" ")))
            count += len(output_nums)
        return count


def part2():
    sum = 0

    def contains_all(str1, str2) -> bool:
        return False not in [char in str1 for char in str2]

    def matches_all(str1, str2) -> bool:
        return False not in [char in str2 for char in str1] and False not in [char in str1 for char in str2]

    with open("input") as file:
        while line := file.readline().rstrip():
            input = [x for x in line.split(" | ")[0].split(" ")]
            output = [x for x in line.split(" | ")[1].split(" ")]
            segs = {}

            # Populate with our known values (1,4,7,8)
            for conns in input:
                if len(conns) == 2:
                    segs[1] = conns
                elif len(conns) == 4:
                    segs[4] = conns
                elif len(conns) == 3:
                    segs[7] = conns
                elif len(conns) == 7:
                    segs[8] = conns

            # Now, we'll start solving our unknowns using displays with 6 segments, so 0,6 and 9.
            # We can deduce which it is by comparing those values to our knowns. so:
            # 0: contains 7, 1 does not contain 4.
            # 6: does not contain 4 and 7 and 1
            # 9: contains 1, 7 and 4
            for conns in input:
                if len(conns) == 6:
                    if (contains_all(conns, segs[1])
                            and contains_all(conns, segs[7])
                            and contains_all(conns, segs[4])):
                        segs[9] = conns
                    if (contains_all(conns, segs[1])
                            and contains_all(conns, segs[7])
                            and not contains_all(conns, segs[4])):
                        segs[0] = conns
                    if (not contains_all(conns, segs[7])
                            and not contains_all(conns, segs[1])
                            and not contains_all(conns, segs[4])):
                        segs[6] = conns

            # All that's left are the 5 segs displays, so 2,3,5
            # 3: contains 7
            # 5: contains nothing, but 9 contains 5 and not 2.
            for conns in input:
                if len(conns) == 5:
                    if contains_all(conns, segs[7]):
                        segs[3] = conns
                    elif contains_all(segs[9], conns):
                        segs[5] = conns
                    else:
                        segs[2] = conns

            # Now we just deduce the output
            output_val = 0
            for out in output:
                for val, str in segs.items():
                    if matches_all(str, out):
                        output_val = val + (output_val * 10)
            sum += output_val
    return sum


if __name__ == "__main__":
    print("Part 1 sln:", part1())
    print("Part 2 sln:", part2())
