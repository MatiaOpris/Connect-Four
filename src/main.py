from src.domain.board import Board
from src.repository.board_repository import BoardActions, ComputerStrategy
from src.services.services import Services
from src.ui.user_interface import UserInterface
from src.repository.GUI_repository import GUIBoardRepository
import tkinter as tkinter

def main():
    board = Board()
    board_action = BoardActions(board, None)
    computer_strategy = ComputerStrategy(board_action)
    board_action.computer_strategy = computer_strategy
    services = Services(board_action)

    while True:
        try:
            choice = input("Choose interface (1 for CLI, 2 for GUI): ")
            if choice not in ['1', '2']:
                raise ValueError("Invalid option")
            break
        except ValueError as value_error:
            print(value_error)

    difficulty = None
    gui_repository, cli_repository = '2', '1'
    if choice == gui_repository:
        while True:
            try:
                difficulty = int(
                    input("Choose computer's difficulty level (1: Easy, 2: Medium, 3: Hard, 4: Godlike): "))
                if difficulty not in [1, 2, 3, 4]:
                    raise ValueError("Invalid option")
                break
            except ValueError as value_error:
                print(value_error)

    console_interface, gui_interface = '1', '2'

    if choice == console_interface:
        user_interface = UserInterface(services)
        user_interface.run_program()
    elif choice == gui_interface:
        root = tkinter.Tk()
        root.title("Connect Four")
        gui = GUIBoardRepository(root, board_action, difficulty)
        root.mainloop()
    else:
        print("Invalid choice. Please restart the program and choose a valid option.")

if __name__ == "__main__":
    main()