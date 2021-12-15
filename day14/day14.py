from collections import defaultdict


def part1(steps):
    sln = 0
    with open("input") as file:
        formula = file.readline().rstrip()
        file.readline()
        polymer_dict = {}
        while line := file.readline().rstrip():
            (pair, insert) = line.split(" -> ")
            polymer_dict[pair] = insert

        # Count the letters in our initial formula as part of the final count for our answer
        letter_count = defaultdict(lambda: 0)
        for c in formula:
            letter_count[c] += 1

        for step in range(steps):
            next_formula = ""
            for i in range(len(formula) - 1):
                pair = formula[i:i + 2]
                letter_count[polymer_dict[pair]] += 1
                next_formula += pair[0] + polymer_dict[pair]

            # The last character isn't appended in the loop so add it here
            formula = next_formula + formula[-1]

        sln = max(letter_count.values()) - min(letter_count.values())
    return sln


"""
Key observation is that all that matters are the pair, the rest of the string doesnt matter.
This allows us to store pairs in a dict and just count pair occurrences, rather than storing in a string
Add to the count along the way.
e.g: formaula: {'NN':1, 'NC':1, 'CB':1} for NNCB, the continue on. If pair appears again, set it's value +1
We can do this specifically because the order of the pairs do not matter. as long as the pairs are correct.
"""


def part2(steps):
    sln = 0
    with open("input") as file:
        formula = file.readline().rstrip()
        file.readline()
        polymer_dict = {}
        while line := file.readline().rstrip():
            (pair, insert) = line.split(" -> ")
            polymer_dict[pair] = insert

        # Still need this to track most characters
        letter_count = defaultdict(lambda: 0)
        for c in formula:
            letter_count[c] += 1

        def insert(pair):
            pass

        # We're storing in a dict now instead of long continuous string
        # Allowing us to optimize for space, since len(polymer) now is >= len(polymer_dict)
        polymer = defaultdict(lambda: 0)
        for i in range(len(formula) - 1):  # And we're initializing this list here.
            pair = formula[i:i+2]
            polymer[pair] += 1

        for step in range(steps):
            new_polymer = defaultdict(lambda: 0)  # We must overwrite previous state each iteration
            for pair in polymer:
                (left, right) = pair
                inserted = polymer_dict[pair]  # Character to be inserted from lookup table
                occurrences = polymer[pair]  # How many times this pair appears in our polymer
                new_pair1 = left + inserted
                new_pair2 = inserted + right

                # So if we have NN:1, we will get Nx xN. if NN:2, we will get Nx xN Nx xN so new pairs scale
                # linearly by the number of occurrences from previous pairs.
                new_polymer[new_pair1] += occurrences
                new_polymer[new_pair2] += occurrences
                # If NN:1, one new character was inserted, if NN:2, then 2 were inserted, etc.
                letter_count[inserted] += occurrences

            polymer = new_polymer

        sln = max(letter_count.values()) - min(letter_count.values())
    return sln


if __name__ == "__main__":
    print('Part 1 sln:', part1(10))
    print('Part 2 sln:', part2(40))
