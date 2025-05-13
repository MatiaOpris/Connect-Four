import copy
import math
import random
import unittest
from src.domain.board import Board
import texttable


class BoardException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TestBoardActions(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.computer_strategy = ComputerStrategy(BoardActions(self.board, None))
        self.board_action = BoardActions(self.board, self.computer_strategy)

    def test_add_move_on_board(self):
        computer, user = '2', '1'
        self.board_action.add_move_on_board(1, user)
        self.assertEqual(self.board_action.get_board()[6][1], user)

    def test_verify_move(self):
        computer, user = '2', '1'
        self.assertTrue(self.board_action.verify_move(1)[0])
        self.board_action.add_move_on_board(1, user)
        self.assertTrue(self.board_action.verify_move(1)[0])
        for _ in range(5):
            self.board_action.add_move_on_board(1, user)
        self.assertFalse(self.board_action.verify_move(1)[0])

    def test_check_winner(self):
        computer, user = '2', '1'
        for i in range(1, 5):
            self.board_action.add_move_on_board(i, user)
        self.assertTrue(self.board_action.check_winner(user))
        self.assertFalse(self.board_action.check_winner(computer))

    def test_is_game_over(self):
        user = '1'
        self.assertFalse(self.board_action.is_game_over()[0])
        for i in range(1, 5):
            self.board_action.add_move_on_board(i, user)
        self.assertTrue(self.board_action.is_game_over()[0])

    def test_restart_game(self):
        user, empty = '1', '0'
        self.board_action.add_move_on_board(1, user)
        self.board_action.restart_game()
        self.assertEqual(self.board_action.get_board()[6][1], empty)

    def test_display_board(self):
        user = '1'
        self.board_action.add_move_on_board(1, user)
        self.board_action.display_board()

    def test_get_board(self):
        self.assertEqual(len(self.board_action.get_board()), 7)
        self.assertEqual(len(self.board_action.get_board()[0]), 8)


class TestComputerStrategy(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board_action = BoardActions(self.board, None)
        self.computer_strategy = ComputerStrategy(self.board_action)

    def test_set_computer_difficulty(self):
        first_columns, last_column, easy, medium, hard, godlike = 1, 8, 1, 2, 3, 4
        move = self.computer_strategy.set_computer_difficulty(easy)
        self.assertIn(move, range(first_columns, last_column))
        move = self.computer_strategy.set_computer_difficulty(medium)
        self.assertIn(move, range(first_columns, last_column))
        move = self.computer_strategy.set_computer_difficulty(hard)
        self.assertIn(move, range(first_columns, last_column))
        move = self.computer_strategy.set_computer_difficulty(godlike)
        self.assertIn(move, range(first_columns, last_column))

    def test_easy_difficulty_move(self):
        first_column, last_column = 1, 8
        move = self.computer_strategy.easy_difficulty_move()
        self.assertIn(move, range(first_column, last_column))

    def test_medium_difficulty_move(self):
        first_column, last_column = 1, 8
        move = self.computer_strategy.medium_difficulty_move()
        self.assertIn(move, range(first_column, last_column))

    def test_hard_difficulty_move(self):
        first_column, last_column = 1, 8
        move = self.computer_strategy.hard_difficulty_move()
        self.assertIn(move, range(first_column, last_column))

    def test_get_valid_moves(self):
        first_column, last_column = 1, 8
        valid_moves = self.computer_strategy.get_valid_moves()
        self.assertIsInstance(valid_moves, list)
        self.assertTrue(all(move in range(first_column, last_column) for move in valid_moves))

    def test_godlike_difficulty_move(self):
        first_column, last_column, easy = 1, 8, 1
        move = self.computer_strategy.godlike_difficulty_move(easy)
        self.assertIn(move, range(first_column, last_column))


class BoardActions:
    def __init__(self, board, computer_strategy):
        self._board = board.reset_board()
        self.computer_strategy = computer_strategy

    def add_move_on_board(self, move, type_finder):
        user, computer = '1', '2'
        move_available, row, column = self.verify_move(move)
        if move_available and type_finder == user:
            self._board[row][column] = user
        elif move_available and type_finder == computer:
            self._board[row][column] = computer
        elif not move_available:
            raise BoardException("You can't move here")

    def computer_move(self, computer_difficulty):
        computer_move = self.computer_strategy.set_computer_difficulty(computer_difficulty)
        self.add_move_on_board(computer_move, '2')

    def verify_move(self, move):
        rows = 6
        if move < 1 or move > 8:
            raise BoardException("You can't move here")
        for row in range(rows, 0, -1):
            if self._board[row][move] == '0':
                return True, row, move
        return False, None, None

    def check_winner(self, player):
        rows, columns, piece_alignment = 6, 7, 4
        # horizontal check
        for row in range(1, rows + 1):
            for column in range(1, columns - 2):
                if all(self._board[row][column + i] == player for i in range(piece_alignment)):
                    return True

        # vertical check
        for row in range(1, rows - 2):
            for column in range(1, columns + 1):
                if all(self._board[row + i][column] == player for i in range(piece_alignment)):
                    return True

        # upward diagonal check
        for row in range(1, rows - 2):
            for column in range(1, columns - 2):
                if all(self._board[row + i][column + i] == player for i in range(piece_alignment)):
                    return True

        # downwards diagonal check
        for row in range(piece_alignment, rows + 1):
            for column in range(1, columns - 2):
                if all(self._board[row - i][column + i] == player for i in range(piece_alignment)):
                    return True
        return False

    def is_game_over(self):
        user, computer, empty, rows, columns = '1', '2', '0', 7, 8
        if self.check_winner(user):
            return True, user
        elif self.check_winner(computer):
            return True, computer
        for row in range(1, rows):
            for column in range(1, columns):
                if self._board[row][column] == empty:
                    return False, None
        return True, None

    def restart_game(self):
        board = Board()
        self._board = board.reset_board()
        return self._board

    def display_board(self):
        board = texttable.Texttable()
        board.add_rows(self._board)
        return board.draw()

    def get_board(self):
        return self._board


class ComputerStrategy:
    def __init__(self, board_action):
        self.board_action = board_action
        self._board = board_action.get_board()

    def set_computer_difficulty(self, difficulty):
        easy_level, medium_level, hard_level, godlike_level, maximum_depth_of_analysis = 1, 2, 3, 4, 2
        if difficulty == easy_level:
            return self.easy_difficulty_move()
        elif difficulty == medium_level:
            return self.medium_difficulty_move()
        elif difficulty == hard_level:
            return self.hard_difficulty_move()
        elif difficulty == godlike_level:
            return self.godlike_difficulty_move(maximum_depth_of_analysis)

    def easy_difficulty_move(self):
        while True:
            computer_move = random.randint(1, 7)
            move_available, row, column = self.board_action.verify_move(computer_move)
            if move_available:
                return computer_move

    def medium_difficulty_move(self):
        user, computer, empty, columns, rows = '1', '2', '0', 7, 6
        for row in (rows, 0, -1):
            for column in (columns, 0, -1):
                if self._board[row][column] == user:
                    if self._board[row][column - 1] == empty and self.board_action.verify_move(column - 1)[
                        0] == True and row == self.board_action.verify_move(column - 1)[1]:
                        computer_move = column - 1
                        return computer_move
                    elif self._board[row][column + 1] == empty and self.board_action.verify_move(column + 1)[
                        0] == True and row == self.board_action.verify_move(column + 1)[1]:
                        computer_move = column + 1
                        return computer_move
                    elif self._board[row + 1][column] == empty and self.board_action.verify_move(column)[
                        0] == True and row + 1 == self.board_action.verify_move(column)[1]:
                        computer_move = column
                        return computer_move
        computer_move = random.choice(self.get_valid_moves())
        return computer_move

    def hard_difficulty_move(self):
        user, computer, empty, columns = '1', '2', '0', 7
        for column in range(columns, 0, -1):
            move_available, row, column = self.board_action.verify_move(column)
            if move_available:
                self._board[row][column] = user
                if not self.board_action.check_winner(user):
                    self._board[row][column] = empty
                    if self.block_player_win() is None:
                        if self.try_to_win() is not None:
                            computer_move = self.try_to_win()
                            return computer_move
                        elif self.try_to_win() is None:
                            computer_move = random.choice(self.get_valid_moves())
                            return computer_move
                    elif self.block_player_win() is not None:
                        computer_move = self.block_player_win()
                        return computer_move
                elif self.board_action.check_winner(user):
                    self._board[row][column] = empty
                    computer_move = column
                    return computer_move

    def get_valid_moves(self):
        valid_moves = []
        columns, rows, empty = 8, 6, '0'
        for column in range(1, columns):
            for row in range(rows, 0, -1):
                if self._board[row][column] == empty:
                    valid_moves.append(column)
                    break
        return valid_moves

    def block_player_win(self):
        user, empty = '1', '0'
        for move in self.get_valid_moves():
            move_available, row, column = self.board_action.verify_move(move)
            if move_available:
                self._board[row][column] = user
                if self.board_action.check_winner(user):
                    self._board[row][column] = empty
                    return move
                self._board[row][column] = empty
        return None

    def try_to_win(self):
        computer, empty = '2', '0'
        for move in self.get_valid_moves():
            move_available, row, column = self.board_action.verify_move(move)
            if move_available:
                self._board[row][column] = computer
                if self.board_action.check_winner(computer):
                    self._board[row][column] = empty
                    return move
                self._board[row][column] = empty
        return None

    def godlike_difficulty_move(self, depth):
        valid_locations = self.get_valid_moves()
        best_score = -math.inf
        best_column = random.choice(valid_locations)

        if self.block_player_win() is not None:
            computer_move = self.block_player_win()
            return computer_move
        if self.try_to_win() is not None:
            computer_move = self.try_to_win()
            return computer_move

        computer = '2'
        for column in valid_locations:
            row = self.get_next_open_row(self._board, column)
            temp_board = copy.deepcopy(self._board)
            temp_board[row][column] = computer
            score = self.minimax(temp_board, depth - 1, -math.inf, math.inf, False)

            if score > best_score:
                best_score = score
                best_column = column

        return best_column

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        user, computer = '1', '2'
        game_status, winner = self.board_action.is_game_over()

        if depth == 0 or game_status:
            if game_status:
                if winner == computer:
                    return 100000000000000
                elif winner == user:
                    return -10000000000000
                else:
                    return 0
            else:
                return self.score_position(board, computer)

        valid_locations = self.get_valid_moves()

        if maximizing_player:
            value = -math.inf
            for column in valid_locations:
                row = self.get_next_open_row(board, column)
                temp_board = copy.deepcopy(board)
                temp_board[row][column] = computer
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, False)
                value = max(value, new_score)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = math.inf
            for column in valid_locations:
                row = self.get_next_open_row(board, column)
                temp_board = copy.deepcopy(board)
                temp_board[row][column] = user
                new_score = self.minimax(temp_board, depth - 1, alpha, beta, True)
                value = min(value, new_score)
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    @staticmethod
    def get_next_open_row(board, column):
        for row in range(len(board) - 1, -1, -1):
            if board[row][column] == '0':
                return row

    def score_position(self, board, player):
        score = 0
        opponent_piece = '1' if player == '2' else '2'
        rows, columns = 6, 7

        center_column = columns // 2
        center_array = [board[row][center_column] for row in range(rows)]
        center_count = center_array.count(player)
        score += center_count * 3

        # horizontal score
        for row in range(rows):
            row_array = [board[row][column] for column in range(columns)]
            for column in range(columns - 3):
                window = row_array[column:column + 4]
                score += self.evaluate_window(window, player)

        # vertical score
        for column in range(columns):
            col_array = [board[row][column] for row in range(rows)]
            for row in range(rows - 3):
                window = col_array[row:row + 4]
                score += self.evaluate_window(window, player)

        # upward diagonal score
        for row in range(rows - 3):
            for column in range(columns - 3):
                window = [board[row + i][column + i] for i in range(4)]
                score += self.evaluate_window(window, player)

        # downward diagonal score
        for row in range(3, rows):
            for column in range(columns - 3):
                window = [board[row - i][column + i] for i in range(4)]
                score += self.evaluate_window(window, player)

        return score

    @staticmethod
    def evaluate_window(window, piece):
        score, empty_cell = 0, '0'
        opponent_piece = '1' if piece == '2' else '2'

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(empty_cell) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(empty_cell) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(empty_cell) == 1:
            score -= 4

        return score


if __name__ == '__main__':
    unittest.main()
