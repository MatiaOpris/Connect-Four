import tkinter
from tkinter import messagebox

from src.domain.board import Board
from src.repository.board_repository import BoardActions, BoardException


class GUIBoardRepository:
    def __init__(self, root, board_action, difficulty):
        self.root = root
        self.board_action = board_action
        self.__rows = 6
        self.__columns = 7
        self.buttons = [[' ' for _ in range(self.__columns)] for _ in range(self.__rows)]
        self.__difficulty = difficulty
        self.create_board()

    def create_board(self):
        rows, columns = 6, 7
        for column in range(columns):
            label = tkinter.Label(self.root, text=chr(ord('A') + column), width=10, height=3)
            label.grid(row=0, column=column + 1)

        for row in range(rows):
            label = tkinter.Label(self.root, text=str(row + 1), width=10, height=3)
            label.grid(row=row + 1, column=0)
            for column in range(columns):
                button = tkinter.Button(self.root, bg='white', width=10, height=3,
                                        command=lambda r=row, c=column: self.make_move(r, c))
                button.grid(row=row + 1, column=column + 1)
                self.buttons[row][column] = button

    def make_move(self, row, column):
        user, computer = '1', '2'
        try:
            self.board_action.add_move_on_board(column + 1, '1')
            self.update_board(user)
            if self.board_action.is_game_over()[0]:
                messagebox.showinfo("Game Over", "User wins!")
                self.board_action.restart_game()
                self.update_board()
            else:
                self.board_action.computer_move(self.__difficulty)
                self.update_board(computer)
                if self.board_action.is_game_over()[0]:
                    messagebox.showinfo("Game Over", "Computer wins!")
                    self.board_action.restart_game()
                    self.update_board()
        except BoardException as exception:
            messagebox.showerror("Error", str(exception))

    def update_board(self, player=None):
        rows, columns = 7, 8
        board = self.board_action.get_board()
        for row in range(1, rows):
            for column in range(1, columns):
                if board[row][column] == '1':
                    self.buttons[row - 1][column - 1].config(bg='blue')
                elif board[row][column] == '2':
                    self.buttons[row - 1][column - 1].config(bg='red')
                else:
                    self.buttons[row - 1][column - 1].config(bg='white')
