from itertools import combinations


def solve() -> None:
    board_size = int(input())
    count_cases = 0

    # Each n queen composition always has one queen on each row.
    # There, the first row always has a queen.
    for i in range((board_size + 1) // 2):
        # in each node, index corresponds to row and value corresponds to column
        stack = [([i], {i}, {0 - i}, {i})]

        while len(stack) > 0:
            current, columns, diagonals, anti_diagonals = stack.pop()
            row = len(current)

            if row == board_size:
                if board_size % 2 == 1 and (board_size + 1) // 2 == row:
                    count_cases += 1
                else:
                    count_cases += 2

            for column in range(board_size):
                if column not in columns and row - column not in diagonals and row + column not in anti_diagonals:
                    new_board = current + [column]
                    new_columns = columns | {column}
                    new_diagonals = diagonals | {row - column}
                    new_anti_diagonals = anti_diagonals | {row + column}
                    stack.append(
                        (new_board, new_columns, new_diagonals, new_anti_diagonals))

    print(count_cases)


def is_threatened(current, row, column):
    for previous_row, previous_column in enumerate(current):
        if column == previous_column or \
                previous_column - column == previous_row - row or \
                column - previous_column == previous_row - row:
            return True
    return False


solve()
