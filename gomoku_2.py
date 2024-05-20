#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox


class Gomoku:
    def __init__(self, size=15, win_length=5):
        self.size = size
        self.win_length = win_length
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.current_player = "X"

    def make_move(self, x, y):
        if self.board[x][y] == ".":
            self.board[x][y] = self.current_player
            if self.check_win(x, y):
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
            return False
        return None

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


class GomokuGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = [[None for _ in range(game.size)] for _ in range(game.size)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                button = tk.Button(
                    self.root,
                    text=".",
                    width=2,
                    height=2,
                    command=lambda x=i, y=j: self.on_button_click(x, y),
                )
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, x, y):
        if self.game.board[x][y] == ".":
            self.buttons[x][y].config(text=self.game.current_player)
            game_won = self.game.make_move(x, y)
            if game_won:
                messagebox.showinfo(
                    "Game Over", f"Player {self.game.current_player} wins!"
                )
                self.reset_board()
            else:
                self.buttons[x][y].config(state="disabled")
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken.")

    def reset_board(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                self.buttons[i][j].config(text=".", state="normal")
        self.game = Gomoku(size=self.game.size, win_length=self.game.win_length)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gomoku")
    game = Gomoku()
    gui = GomokuGUI(root, game)
    root.mainloop()
