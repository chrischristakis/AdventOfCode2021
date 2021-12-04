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
                print(i, ((int(line, base=2) >> i) & 1))
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
        print(epsilon_mask)
        if bit >= 0:
            gamma |= 1
        # Don't need to do anything for 0, it'll get shifted next loop.

    print(gamma, (~gamma & epsilon_mask), gamma * (~gamma & epsilon_mask))
    # Python doesn't let us trivially do bit NOTs since it deals with signed ints. Not pog.
    return gamma * (~gamma & epsilon_mask)


if __name__ == "__main__":
    print("Part 1 sln:", part1())