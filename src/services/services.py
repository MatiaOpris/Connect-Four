import unittest
from unittest.mock import MagicMock


class TestServices(unittest.TestCase):
    def setUp(self):
        self.board_repository = MagicMock()
        self.services = Services(self.board_repository)

    def test_is_game_over(self):
        self.board_repository.is_game_over.return_value = True
        result = self.services.is_game_over()
        self.board_repository.is_game_over.assert_called_once()
        self.assertTrue(result)

    def test_add_move_on_board(self):
        self.services.add_move_on_board('1', 'type_finder')
        self.board_repository.add_move_on_board.assert_called_once_with('1', 'type_finder')

    def test_computer_move(self):
        move = 3
        self.services.computer_move(move)
        self.board_repository.computer_move.assert_called_once_with(move)

    def test_restart_game(self):
        self.board_repository.restart_game.return_value = True
        result = self.services.restart_game()
        self.board_repository.restart_game.assert_called_once()
        self.assertTrue(result)

    def test_display_board(self):
        self.board_repository.display_board.return_value = "Board Display"
        result = self.services.display_board()
        self.board_repository.display_board.assert_called_once()
        self.assertEqual(result, "Board Display")

    def test_get_board(self):
        columns, rows = 7, 6
        self.board_repository.get_board.return_value = [[0] * columns for _ in range(rows)]
        result = self.services.get_board()
        self.board_repository.get_board.assert_called_once()
        self.assertEqual(result, [[0] * columns for _ in range(rows)])


class Services:
    def __init__(self, board_repository):
        self.board_repository = board_repository

    def is_game_over(self):
        return self.board_repository.is_game_over()

    def add_move_on_board(self, player, type_finder):
        self.board_repository.add_move_on_board(player, type_finder)

    def computer_move(self, computer_difficulty):
        self.board_repository.computer_move(computer_difficulty)

    def restart_game(self):
        return self.board_repository.restart_game()

    def display_board(self):
        return self.board_repository.display_board()

    def get_board(self):
        return self.board_repository.get_board()


if __name__ == '__main__':
    unittest.main()
