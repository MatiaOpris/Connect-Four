"""
|---|---|---|---|---|---|---|---|
|---| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
"""
from src.repository.board_repository import BoardException


class UserInterface:
    def __init__(self, service):
        self.service = service

    @staticmethod
    def try_and_except_input(left_bound, right_bound) -> int:
        while True:
            try:
                input_variable = int(input("Choice > "))
                if input_variable < left_bound or input_variable > right_bound:
                    raise ValueError("Invalid option")
                return input_variable
            except ValueError as value_error:
                print(value_error)

    @staticmethod
    def computer_difficulty_level_menu():
        print("Choose computer's difficulty level > ")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Godlike")

    @staticmethod
    def verify_input(user_move) -> bool:
        if user_move < 1 or user_move > 7:
            return False
        return True

    def run_program(self):
        game_over = False
        user, computer = '1', '2'
        self.computer_difficulty_level_menu()
        computer_difficulty = self.try_and_except_input(1, 4)

        while not game_over:
            while True:
                try:
                    user_move = input("Your move > ").upper()
                    if user_move not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                        raise ValueError("Enter right move")
                    user_move = ord(user_move.upper()) - ord('A') + 1
                    break
                except ValueError as value_error:
                    print(value_error)
            self.verify_input(user_move)

            while True:
                try:
                    self.service.add_move_on_board(user_move, user)
                    break
                except BoardException:
                    user_move = input("Enter right move > ")
                    user_move = ord(user_move.upper()) - ord('A') + 1

            game_over, winner = self.service.is_game_over()
            if not game_over:
                self.service.computer_move(computer_difficulty)
                game_over, winner = self.service.is_game_over()
                if not game_over:
                    print(self.service.display_board())
            elif game_over:
                print(self.service.display_board())
                if winner == user:
                    print("User wins")
                elif winner == computer:
                    print("Computer wins")
                print("Game over\n")
                print("Restart / exit (1 or 2)")
                user_choice = self.try_and_except_input(1, 2)
                restart_option, exit_option = 1, 2
                if user_choice == restart_option:
                    self.service.restart_game()
                    game_over = False
                elif user_choice == exit_option:
                    print("Bye... for now")
                    break
