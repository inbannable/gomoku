#!/usr/bin/env python3


class Gomoku:
    def __init__(self, size=15, win_length=5):
        self.size = size
        self.win_length = win_length
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def make_move(self, x, y):
        if self.board[x][y] == ".":
            self.board[x][y] = self.current_player
            if self.check_win(x, y):
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move, try again.")
        return False

    def check_win(self, x, y):
        return (
            self.check_direction(x, y, 1, 0)  # Horizontal
            or self.check_direction(x, y, 0, 1)  # Vertical
            or self.check_direction(x, y, 1, 1)  # Diagonal /
            or self.check_direction(x, y, 1, -1)
        )  # Diagonal \

    def check_direction(self, x, y, dx, dy):
        count = 1
        for i in range(1, self.win_length):
            nx, ny = x + i * dx, y + i * dy
            if (
                0 <= nx < self.size
                and 0 <= ny < self.size
                and self.board[nx][ny] == self.current_player
            ):
                count += 1
            else:
                break
        for i in range(1, self.win_length):
            nx, ny = x - i * dx, y - i * dy
            if (
                0 <= nx < self.size
                and 0 <= ny < self.size
                and self.board[nx][ny] == self.current_player
            ):
                count += 1
            else:
                break
        return count >= self.win_length


def play_game():
    game = Gomoku()
    game.print_board()

    while True:
        try:
            x, y = map(
                int,
                input(
                    f"Player {game.current_player}, enter your move (row and column): "
                ).split(),
            )
            if x < 0 or x >= game.size or y < 0 or y >= game.size:
                print("Move out of bounds, try again.")
                continue
            if game.make_move(x, y):
                game.print_board()
                break
            game.print_board()
        except ValueError:
            print("Invalid input, please enter row and column numbers.")


if __name__ == "__main__":
    play_game()
