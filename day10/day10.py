def part1_and_part2() -> (int, int):
    score = 0
    score2 = 0
    with open("input") as file:

        def brace_match(opened, c):
            if opened == '(' and c == ')':
                return True
            if opened == '{' and c == '}':
                return True
            if opened == '[' and c == ']':
                return True
            if opened == '<' and c == '>':
                return True
            return False

        def calculate_corrupt_score(c):
            if c == ')':
                return 3
            if c == ']':
                return 57
            if c == '}':
                return 1197
            if c == '>':
                return 25137

        def calculate_incomplete_score(c):
            if c == '(':
                return 1
            if c == '[':
                return 2
            if c == '{':
                return 3
            if c == '<':
                return 4

        incomplete_scores = []
        while line := file.readline().rstrip():
            opening_brace = []
            for i in range(len(line)):
                c = line[i]
                if c == '(' or c == '{' or c == '[' or c == '<':
                    opening_brace.append(c)
                if c == ')' or c == '}' or c == ']' or c == '>':
                    if len(opening_brace) > 0:
                        opened = opening_brace.pop()
                        if not brace_match(opened, c):
                            score += calculate_corrupt_score(c)
                            # We need to remove it since only incomplete lines should have data left in the list
                            opening_brace = []
                            break
                    else:
                        print("invalid line")
                        break

            # For incomplete lines
            if len(opening_brace) > 0:
                opening_brace = opening_brace[::-1]  # Reverse since were considering closing bracket
                incomplete_score = 0
                for c in opening_brace:
                    incomplete_score = 5 * incomplete_score + calculate_incomplete_score(c)
                incomplete_scores.append(incomplete_score)

        # Could implement fast custom sort, but it's late and don't need to for this problem.
        incomplete_scores.sort()
        score2 = incomplete_scores[int(len(incomplete_scores)/2)]

    return score, score2


if __name__ == "__main__":
    # For this problem, stacks are the key. Have to make sure the closing bracket matches what
    # we popped from the opening brackets.
    result = part1_and_part2()
    print("Part 1 sln:", result[0])
    print("Part 2 sln:", result[1])
