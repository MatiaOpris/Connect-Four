import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        columns, rows, user, empty = 8, 7, '1', '0'
        self.assertEqual(len(self.board._board), columns)
        self.assertEqual(len(self.board._board[0]), rows)
        self.assertEqual(self.board._board[0][1], 'A')
        self.assertEqual(self.board._board[1][0], user)
        self.assertEqual(self.board._board[1][1], empty)

    def test_initialize_board(self):
        user, empty = '1', '0'
        self.board._initialize_board()
        self.assertEqual(self.board._board[0][1], 'A')
        self.assertEqual(self.board._board[1][0], user)
        self.assertEqual(self.board._board[1][1], empty)

    def test_reset_board(self):
        user, empty = '1', '0'
        self.board._board[1][1] = user
        self.board.reset_board()
        self.assertEqual(self.board._board[1][1], empty)


class Board:
    def __init__(self):
        self._columns = 8
        self._rows = 7
        self._board = [[' ' for _ in range(self._columns)] for _ in range(self._rows)]
        self._initialize_board()

    def _initialize_board(self):
        for column in range(1, self._columns):
            self._board[0][column] = chr(ord('A') + column - 1)

        for row in range(1, self._rows):
            self._board[row][0] = str(row)

        empty = '0'
        for row in range(1, self._rows):
            for column in range(1, self._columns):
                self._board[row][column] = empty

    def reset_board(self):
        self._initialize_board()
        return self._board


if __name__ == '__main__':
    unittest.main()
