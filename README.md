# Connect-Four - English

This project is an implementation of the Connect Four (Four in a Row) game written in Python. It allows players to compete against the computer at different difficulty levels or interact through a graphical user interface (GUI).

## Project Structure

The project is organized into several Python files, each with a specific responsibility:

- **main.py**: The main execution file. It initializes the game, allows the user to choose between the command-line interface (CLI) and the graphical interface (GUI), and sets the computer's difficulty level, if applicable.
- **user_interface.py**: Manages user interaction via the command line (CLI). Displays the game board, receives user input, and shows game results.
- **GUI_repository.py**: Implements the graphical user interface (GUI) using `tkinter`. Creates a visual game board, handles user input via clicks, and updates the board after each move.
- **services.py**: The service layer that connects the user interface with the game logic. Coordinates the actions required for the game to proceed.
- **board_repository.py**: Contains the core game logic. Defines the game rules, validates moves, determines the winner, and manages the game board. It also includes the computer's strategy for different difficulty levels.
- **board.py**: Defines the `Board` class, which represents the game board and the methods to initialize and reset it.
- **src/domain/**: This directory may contain domain files (e.g., data classes). In the provided code, only `board.py` is included in this structure.
- **src/repository/**: This directory contains files that handle data persistence or interaction with data sources. In the provided code, we have `board_repository.py` and `GUI_repository.py`.
- **src/services/**: This directory contains files that implement the application's business logic. In the provided code, we have `services.py`.
- **src/ui/**: This directory contains files that manage user interaction. In the provided code, we have `user_interface.py`.

## How to Run the Game

1. Ensure you have Python 3.x installed.
2. Clone this repository to your computer.
3. Open a terminal or command line and navigate to the project directory.
4. Run the `main.py` file using the command: `python main.py`
5. Follow the instructions in the terminal to choose the interface (CLI or GUI) and, if you choose GUI, the computer's difficulty level.

## Dependencies

- **tkinter**: For the graphical user interface (GUI). (Usually included in the standard Python installation.)
- **texttable**: For displaying the board in text format in the CLI. Install with `pip install texttable`.

## Features

- **Two game interfaces:**
  - **CLI (Command Line Interface):** The game runs in the terminal, with text input for moves.
  - **GUI (Graphical User Interface):** An interactive visual interface with buttons for making moves.
- **Computer difficulty levels:** Players can choose from multiple difficulty levels (Easy, Medium, Hard, Incredible) to play against the computer.
- **Move validation:** The game checks if moves are valid and displays errors if they are not.
- **Winner detection:** The game automatically determines when a player has won or if the game has ended in a draw.
- **Option to restart the game:** Players can start a new game after one has ended.

## Notes

- The code is organized using a modular structure, which facilitates maintenance and extension.
- Unit tests are included to ensure the correct functioning of the game's various components.
- The computer's strategy varies depending on the difficulty level, from random moves to more advanced algorithms (e.g., minimax).

I hope this README is helpful!