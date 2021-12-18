def part1():
    # This list tracks how many ones occur in each bit position.
    # If element is positive at the end, 1 is most common. otherwise 0.
    ones_list = []
    with open("input") as file:
        while line := file.readline().rstrip():
            # First, initialize list with zeros equal to the length one line of input (e.g, 1011 -> [0, 0, 0, 0])
            if len(ones_list) == 0:
                ones_list = [0] * len(line)

            # to save us the time of casting each individual character, we are using bitwise operators.
            for i in range(len(ones_list)):  # length of one input line, start at LSB
                if ((int(line, base=2) >> i) & 1) == 1:
                    ones_list[i] += 1
                else:
                    ones_list[i] -= 1

    # Reverse the list.
    ones_list.reverse()

    # Now that we know if ones or zeroes are the most common in each position, turn it back into a bit representation.
    gamma = 0
    epsilon_mask = 0  # We'll use this to get the unsigned inverse later on.
    for bit in ones_list:
        gamma = gamma << 1  # first loop result is 0, so it wont do anything.
        epsilon_mask = (epsilon_mask << 1) | 1
        if bit >= 0:
            gamma |= 1
        # Don't need to do anything for 0, it'll get shifted next loop.
    # Python doesn't let us trivially do bit NOTs since it deals with signed ints. Not pog.
    return gamma * (~gamma & epsilon_mask)


def part2():
    # Read in file
    # For oxygen, loop through and count how many ones vs zeroes.
    # while doing this, store numbers that start with individual bits in a temp list
    # (Ones in one list, zeroes in another.)
    # Whichever is greater becomes the ox list, and less becomes the co2 list.
    # Loop through again, pass in the new list and look at the next bit instead.

    with open("input") as file:
        oxygen_list = [line.rstrip() for line in file.readlines()]
    co2_list = oxygen_list.copy()

    def oxygen_c02_filter(list, bit, func):
        if len(list) == 1:
            return list

        ones = []
        zeroes = []
        for line in list:
            if line[bit] == "1":
                ones.append(line)
            else:
                zeroes.append(line)

        return func(zeroes, ones)

    line_length = len(oxygen_list[0])
    for i in range(line_length):
        print(oxygen_list)
        print(co2_list)
        oxygen_list = oxygen_c02_filter(oxygen_list, i,
                                        lambda zeroes, ones: ones if len(ones) >= len(zeroes) else zeroes)
        co2_list = oxygen_c02_filter(co2_list, i,
                                     lambda zeroes, ones: zeroes if len(ones) >= len(zeroes) else ones)
    return int(oxygen_list[0], base=2) * int(co2_list[0], base=2)


if __name__ == "__main__":
    print("Part 1 sln:", part1())
    print("Part 2 sln:", part2())