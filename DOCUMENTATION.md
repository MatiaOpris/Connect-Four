# Connect Four Project Documentation

## 1. Introduction

This document describes the architecture, features, and implementation of the Connect Four project, a classic game where two players (or a player versus the computer) attempt to align four pieces of the same color on a game board. The project offers both a command-line interface (CLI) and a graphical user interface (GUI) for playing the game.

## 2. Project Architecture

The project is structured into several Python modules, each with clearly defined responsibilities. The diagram below illustrates the main relationships between modules:

### 2.1. Module Descriptions

- **`main.py`**:
  - The main entry point of the application.
  - Initializes the game and its components.
  - Allows the user to choose between CLI and GUI interfaces.
  - Configures the computer's difficulty level (GUI only).

- **`user_interface.py`**:
  - Manages user interaction via the command line (CLI).
  - Displays the game board in text format.
  - Receives and validates user input (moves).
  - Displays game results and relevant messages.

- **`GUI_repository.py`**:
  - Implements the graphical user interface (GUI) using `tkinter`.
  - Creates and manages visual elements of the game board (buttons, windows).
  - Handles user input via click events.
  - Updates the visual interface after each move.

- **`services.py`**:
  - Contains the core business logic of the game.
  - Coordinates interactions between the user interface and repository modules.
  - Provides methods for making moves, checking game state, and other related operations.

- **`board_repository.py`**:
  - Implements the core logic of Connect Four.
  - Manages the game board (data representation and manipulation).
  - Validates player moves.
  - Detects win conditions and game termination.
  - Implements the computer's strategy for different difficulty levels.

- **`board.py`**:
  - Defines the `Board` class, which represents the game board as a data structure.
  - Provides methods to initialize and reset the board to its initial state.

### 2.2. Main Execution Flow

1. The application starts from the `main.py` file.
2. The user is prompted to choose between CLI and GUI interfaces.
3. If GUI is selected, the user must also choose the computer's difficulty level.
4. The game runs in a loop:
   - In CLI mode, `user_interface.py` handles text input/output.
   - In GUI mode, `GUI_repository.py` manages visual interaction.
   - `services.py` coordinates game logic and calls functions from `board_repository.py`.
   - `board_repository.py` updates the board and checks game rules.
5. The game ends when a player wins or the board is full (resulting in a draw).
6. The user can choose to restart the game or exit the application.

## 3. Feature Descriptions

### 3.1. Game Interfaces

- **CLI (Command Line Interface)**:
  - Text-based interaction in the terminal.
  - The user enters moves using column coordinates (A, B, C...).
  - The game board is displayed in text format using the `texttable` module.

- **GUI (Graphical User Interface)**:
  - Interactive visual interface with windows and buttons.
  - The user makes moves by clicking on the corresponding column buttons.
  - Provides a graphical representation of the game board and pieces.

### 3.2. Computer Difficulty Levels

- **Easy**:
  - The computer makes completely random moves with no strategy.

- **Medium**:
  - The computer attempts to block the player's potential winning moves.
  - Also tries to create its own winning opportunities.

- **Hard**:
  - The computer uses a more advanced strategy, anticipating several moves ahead.

- **Incredible (Godlike)**:
  - The computer uses the Minimax algorithm with Alpha-Beta pruning to make near-optimal decisions.
  - Attempts to maximize its chances of winning and minimize the player's chances.

### 3.3. Other Features

- **Move validation**:
  - The game checks if user moves are valid (e.g., the column is not full).
  - Displays error messages for invalid moves.

- **Winner detection**:
  - The game automatically checks after each move if there is a winner (four aligned pieces).
  - Also checks if the game has ended in a draw (board is full).

- **Game termination handling**:
  - The game ends when a player wins or a draw is reached.
  - Displays an appropriate message at the end of the game.

- **Game restart**:
  - The user can choose to start a new game after one has ended.

## 4. Key Classes and Methods

### 4.1. `Board` Class (`board.py`)

- `__init__(self)`:
  - Class constructor.
  - Initializes the game board as a list of lists representing the cells.

- `_initialize_board(self)`:
  - Internal method to populate the board with column labels (A, B, C...) and initial values ('0' for empty cells).

- `reset_board(self)`:
  - Resets the game board to its initial state, clearing all pieces.

### 4.2. `BoardActions` Class (`board_repository.py`)

- `__init__(self, board, computer_strategy)`:
  - Class constructor.
  - Receives an instance of the `Board` class and an instance of the `ComputerStrategy` class.

- `add_move_on_board(self, move, type_finder)`:
  - Adds a move to the board for a player (user or computer).
  - `move` represents the column where the move is made.
  - `type_finder` indicates the player ('1' for user, '2' for computer).

- `verify_move(self, move)`:
  - Checks if a move is valid (if the column exists and is not full).
  - Returns a tuple with a boolean (True if valid, False otherwise) and an error message (if applicable).

- `check_winner(self, player)`:
  - Checks if a player has won the game (has four aligned pieces horizontally, vertically, or diagonally).
  - `player` represents the player being checked.

- `is_game_over(self)`:
  - Checks if the game has ended (either someone won or the board is full).
  - Returns a tuple with a boolean (True if ended, False otherwise) and the winning player (if any).

- `restart_game(self)`:
  - Resets the game board to start a new game.

- `display_board(self)`:
  - Displays the game board in text format (used in CLI).

- `get_board(self)`:
  - Returns the internal representation of the game board (list of lists).

- `computer_move(self, computer_difficulty)`:
  - Executes the computer's move by calling methods from the `ComputerStrategy` class.
  - `computer_difficulty` specifies the computer's difficulty level.

### 4.3. `ComputerStrategy` Class (`board_repository.py`)

- `__init__(self, board_action)`:
  - Class constructor.
  - Receives an instance of the `BoardActions` class.

- `set_computer_difficulty(self, difficulty)`:
  - Sets the computer's move strategy based on the user-selected difficulty level.

- `easy_difficulty_move(self)`:
  - Implements the strategy for the easy level (random moves).

- `medium_difficulty_move(self)`:
  - Implements the strategy for the medium level (attempts to block the player and create opportunities).

- `hard_difficulty_move(self)`:
  - Implements the strategy for the hard level (more advanced but not optimal strategy).

- `godlike_difficulty_move(self, depth)`:
  - Implements the strategy for the "Godlike" level using the Minimax algorithm with Alpha-Beta pruning.
  - `depth` represents the search depth of the algorithm.

- `get_valid_moves(self)`:
  - Retrieves the list of valid moves available on the current board.

- `block_player_win(self)`:
  - Checks if the player is about to win and attempts to block that move.

- `try_to_win(self)`:
  - Checks if the computer can win and makes the corresponding move.

- `minimax(self, board, depth, alpha, beta, maximizing_player)`:
  - Implements the Minimax algorithm with Alpha-Beta pruning for strategic decision-making.
  - `board` is the current game board.
  - `depth` is the search depth.
  - `alpha` and `beta` are values for Alpha-Beta pruning.
  - `maximizing_player` indicates whether the computer's or player's score is being maximized.

- `get_next_open_row(board, column)`:
  - Finds the next open row in a column.

- `score_position(board, player)`:
  - Evaluates the score of a board position for a player.

- `evaluate_window(window, piece)`:
  - Evaluates the score of a window of 4 consecutive cells.

### 4.4. `Services` Class (`services.py`)

- `__init__(self, board_repository)`:
  - Class constructor.
  - Receives an instance of the `BoardActions` class.

- `is_game_over(self)`:
  - Delegates game state checking to `board_repository`.

- `add_move_on_board(self, player, type_finder)`:
  - Delegates adding a move to the board to `board_repository`.

- `computer_move(self, computer_difficulty)`:
  - Delegates the computer's move to `board_repository`.

- `restart_game(self)`:
  - Delegates game restart to `board_repository`.

- `display_board(self)`:
  - Delegates board display to `board_repository`.

- `get_board(self)`:
  - Delegates board retrieval to `board_repository`.

### 4.5. `UserInterface` Class (`user_interface.py`)

- `__init__(self, service)`:
  - Class constructor.
  - Receives an instance of the `Services` class.

- `try_and_except_input(left_bound, right_bound)`:
  - Handles user input with validation and error handling (for numeric inputs).

- `computer_difficulty_level_menu(self)`:
  - Displays the menu for selecting the computer's difficulty level (in CLI).

- `verify_input(user_move)`:
  - Checks if the user's move input is valid (column format).

- `run_program(self)`:
  - Runs the main game loop in CLI mode.

### 4.6. `GUIBoardRepository` Class (`GUI_repository.py`)

- `__init__(self, root, board_action, difficulty)`:
  - Class constructor.
  - Receives the main window `root` (from `tkinter`), an instance of the `BoardActions` class, and the computer's difficulty level.

- `create_board(self)`:
  - Creates visual elements of the game board (buttons) using `tkinter`.

- `make_move(self, row, column)`:
  - Handles user moves via button click events.
  - Calls methods from `board_action` to execute the move.

- `update_board(self, player=None)`:
  - Updates the visual appearance of the board after a move (changes button colors).

## 5. Dependencies

- **Python 3.x**
- **tkinter** (for GUI - usually included in standard Python installation)
- **texttable** (for displaying the board in CLI - can be installed with `pip install texttable`)

## 6. Installation and Running Instructions

1. Ensure Python 3.x is installed on your system.
2. Clone the project repository to your computer.
3. Open a terminal or command line and navigate to the project directory.
4. Run the `main.py` file using the command: `python main.py`
5. Follow the displayed instructions to choose the interface (CLI or GUI) and, if applicable, the computer's difficulty level.

## 7. Testing

The project includes unit tests implemented using Python's `unittest` module.