class BingoBoard:
    board_dim = 5

    def check_val(self, val):
        for y in range(self.board_dim):
            for x in range(self.board_dim):
                if self.board_arr[y][x][0] == val:
                    self.board_arr[y][x][1] = True
                    self.result -= int(val)

                    # Check the neighbours in a + pattern to see if theres any matches
                    bingo = True
                    for x_neighbours in range(0, self.board_dim):
                        if not self.board_arr[y][x_neighbours][1]:
                            bingo = False
                            break

                    if bingo:
                        self.result *= int(val)
                        return True

                    bingo = True
                    for y_neighbours in range(0, self.board_dim):
                        if not self.board_arr[y_neighbours][x][1]:
                            bingo = False
                            break

                    if bingo:
                        self.result *= int(val)
                        return True
        return False

    def __init__(self, board_list):
        # Create 2d array in form of [[[elem, marked], [elem, marked]], [[elem. marked], etc ...
        self.board_arr = \
            [[[elem, False] for elem in board_line.split(" ")] for board_line in board_list
             * self.board_dim] * self.board_dim

        self.result = 0
        for x in range(self.board_dim):
            for y in range(self.board_dim):
                self.result += int(self.board_arr[x][y][0])


def part1_and_part2():
    boards = []
    with open("input") as file:
        selection = file.readline().rstrip().split(",")
        file.readline()  # skip next blank line.

        board_input = []
        while line := file.readline():
            line = " ".join(line.rstrip().split())  # input sometimes has double spaces, this removes that.
            if not line:
                boards.append(BingoBoard(board_input))
                board_input = []
                continue
            board_input.append(line)
        boards.append(BingoBoard(board_input))

    winners = []
    done = False
    for num in selection:
        for i, board in enumerate(boards):
            if i not in winners and board.check_val(num):
                winners.append(i)

    return boards[winners[0]].result, boards[winners[-1]].result


if __name__ == "__main__":
    part1, part2 = part1_and_part2()
    print("part 1 sln:", part1)
    print("part 2 sln:", part2)
