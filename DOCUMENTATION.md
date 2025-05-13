# Documentația Proiectului Connect Four

## 1. Introducere

Acest document descrie arhitectura, funcționalitățile și implementarea proiectului Connect Four, un joc clasic în care doi jucători (sau un jucător și calculatorul) încearcă să alinieze patru piese de aceeași culoare pe o tablă de joc. Proiectul oferă atât o interfață linie de comandă (CLI), cât și o interfață grafică (GUI) pentru a juca jocul.

## 2. Arhitectura Proiectului

Proiectul este structurat în mai multe module Python, fiecare având o responsabilitate clar definită. Diagrama de mai jos ilustrează relațiile principale dintre module:

### 2.1. Descrierea Modulelor

* **`main.py`**:
    * Punctul de intrare principal al aplicației.
    * Inițializează jocul și componentele sale.
    * Permite utilizatorului să aleagă între interfața CLI și GUI.
    * Configurează nivelul de dificultate al calculatorului (doar pentru GUI).

* **`user_interface.py`**:
    * Gestionează interacțiunea cu utilizatorul prin linia de comandă (CLI).
    * Afișează tabla de joc în format text.
    * Primește și validează input-ul utilizatorului (mutările).
    * Afișează rezultatele jocului și mesajele relevante.

* **`GUI_repository.py`**:
    * Implementează interfața grafică (GUI) utilizând `tkinter`.
    * Creează și gestionează elementele vizuale ale tablei de joc (butoane, ferestre).
    * Gestionează input-ul utilizatorului prin evenimente de click.
    * Actualizează interfața vizual după fiecare mutare.

* **`services.py`**:
    * Conține logica de afaceri centrală a jocului.
    * Coordonează interacțiunile dintre interfața utilizator și modulele de repository.
    * Oferă metode pentru a efectua mutări, verifica starea jocului și alte operațiuni conexe.

* **`board_repository.py`**:
    * Implementează logica de bază a jocului Connect Four.
    * Gestionează tabla de joc (reprezentarea datelor și manipularea).
    * Verifică validitatea mutărilor efectuate de jucători.
    * Detectează condițiile de câștig și terminare a jocului.
    * Implementează strategia calculatorului pentru diferite niveluri de dificultate.

* **`board.py`**:
    * Definește clasa `Board`, care reprezintă tabla de joc ca o structură de date.
    * Oferă metode pentru a inițializa și reseta tabla la starea inițială.

### 2.2. Fluxul Principal de Execuție

1.  Aplicația pornește din fișierul `main.py`.
2.  Utilizatorul este invitat să aleagă între interfața CLI și GUI.
3.  Dacă este selectată GUI, utilizatorul trebuie să aleagă și nivelul de dificultate al calculatorului.
4.  Jocul se desfășoară într-o buclă:
    * În modul CLI, `user_interface.py` gestionează input/output text.
    * În modul GUI, `GUI_repository.py` gestionează interacțiunea vizuală.
    * `services.py` coordonează logica jocului și apelează funcții din `board_repository.py`.
    * `board_repository.py` actualizează tabla și verifică regulile jocului.
5.  Jocul se termină când un jucător câștigă sau tabla este plină (rezultând într-o remiză).
6.  Utilizatorul poate alege să reînceapă jocul sau să iasă din aplicație.

## 3. Descrierea Funcționalităților

### 3.1. Interfețe de Joc

* **CLI (Command Line Interface):**
    * Interacțiune bazată pe text în terminal.
    * Utilizatorul introduce mutările folosind coordonatele coloanelor (A, B, C...).
    * Tabla de joc este afișată în format text folosind modulul `texttable`.

* **GUI (Graphical User Interface):**
    * Interfață vizuală interactivă cu ferestre și butoane.
    * Utilizatorul face mutări dând click pe butoanele corespunzătoare coloanelor.
    * Oferă o reprezentare grafică a tablei de joc și a pieselor.

### 3.2. Niveluri de Dificultate ale Calculatorului

* **Ușor:**
    * Calculatorul face mutări complet aleatorii, fără nicio strategie.

* **Mediu:**
    * Calculatorul încearcă să blocheze mutările potențial câștigătoare ale utilizatorului.
    * De asemenea, încearcă să creeze propriile oportunități de a câștiga.

* **Greu:**
    * Calculatorul folosește o strategie mai avansată, anticipând câteva mutări înainte.

* **Incredibil (Godlike):**
    * Calculatorul utilizează algoritmul Minimax cu tăiere Alpha-Beta pentru a lua decizii aproape optime.
    * Încearcă să maximizeze șansele sale de câștig și să minimizeze șansele utilizatorului.

### 3.3. Alte Funcționalități

* **Validarea mutărilor:**
    * Jocul verifică dacă mutările introduse de utilizator sunt valide (ex., coloana nu este plină).
    * Afișează mesaje de eroare pentru mutările invalide.

* **Detectarea câștigătorului:**
    * Jocul verifică automat după fiecare mutare dacă există un câștigător (patru piese aliniate).
    * De asemenea, verifică dacă jocul s-a terminat la egalitate (tabla este plină).

* **Gestionarea terminării jocului:**
    * Jocul se termină când un jucător câștigă sau când se atinge o remiză.
    * Afișează un mesaj corespunzător la finalul jocului.

* **Reînceperea jocului:**
    * Utilizatorul are opțiunea de a reîncepe un joc nou după ce unul s-a terminat.

## 4. Descrierea Claselor și Metodelor Cheie

### 4.1. Clasa `Board` (`board.py`)

* `__init__(self)`:
    * Constructorul clasei.
    * Inițializează tabla de joc ca o listă de liste, reprezentând celulele.

* `_initialize_board(self)`:
    * Metodă internă pentru a popula tabla cu etichetele coloanelor (A, B, C...) și valorile inițiale ('0' pentru celule goale).

* `reset_board(self)`:
    * Resetează tabla de joc la starea inițială, ștergând toate piesele.

### 4.2. Clasa `BoardActions` (`board_repository.py`)

* `__init__(self, board, computer_strategy)`:
    * Constructorul clasei.
    * Primește o instanță a clasei `Board` și o instanță a clasei `ComputerStrategy`.

* `add_move_on_board(self, move, type_finder)`:
    * Adaugă o mutare pe tablă pentru un jucător (utilizator sau calculator).
    * `move` reprezintă coloana în care se face mutarea.
    * `type_finder` indică jucătorul ('1' pentru utilizator, '2' pentru calculator).

* `verify_move(self, move)`:
    * Verifică dacă o mutare este validă (dacă coloana există și nu este plină).
    * Returnează un tuplu cu un boolean (True dacă validă, False altfel) și un mesaj de eroare (dacă este cazul).

* `check_winner(self, player)`:
    * Verifică dacă un jucător a câștigat jocul (are patru piese aliniate pe orizontală, verticală sau diagonală).
    * `player` reprezintă jucătorul pentru care se face verificarea.

* `is_game_over(self)`:
    * Verifică dacă jocul s-a terminat (fie a câștigat cineva, fie tabla este plină).
    * Returnează un tuplu cu un boolean (True dacă s-a terminat, False altfel) și jucătorul câștigător (dacă există).

* `restart_game(self)`:
    * Resetează tabla de joc pentru a începe un joc nou.

* `display_board(self)`:
    * Afișează tabla de joc în format text (utilizat în CLI).

* `get_board(self)`:
    * Returnează reprezentarea internă a tablei de joc (lista de liste).

* `computer_move(self, computer_difficulty)`:
    * Realizează mutarea calculatorului, apelând la metodele din clasa `ComputerStrategy`.
    * `computer_difficulty` specifică nivelul de dificultate al calculatorului.

### 4.3. Clasa `ComputerStrategy` (`board_repository.py`)

* `__init__(self, board_action)`:
    * Constructorul clasei.
    * Primește o instanță a clasei `BoardActions`.

* `set_computer_difficulty(self, difficulty)`:
    * Setează strategia de mutare a calculatorului în funcție de nivelul de dificultate ales de utilizator.

* `easy_difficulty_move(self)`:
    * Implementează strategia pentru nivelul ușor (mutări aleatorii).

* `medium_difficulty_move(self)`:
    * Implementează strategia pentru nivelul mediu (încearcă să blocheze jucătorul și să creeze oportunități).

* `hard_difficulty_move(self)`:
    * Implementează strategia pentru nivelul greu (strategie mai avansată, dar nu optimă).

* `godlike_difficulty_move(self, depth)`:
    * Implementează strategia pentru nivelul "Godlike" folosind algoritmul Minimax cu tăiere Alpha-Beta.
    * `depth` reprezintă adâncimea de căutare a algoritmului.

* `get_valid_moves(self)`:
    * Obține lista de mutări valide disponibile pe tabla curentă.

* `block_player_win(self)`:
    * Verifică dacă jucătorul este pe cale să câștige și încearcă să blocheze această mutare.

* `try_to_win(self)`:
    * Verifică dacă calculatorul poate câștiga și face mutarea respectivă.

* `minimax(self, board, depth, alpha, beta, maximizing_player)`:
    * Implementează algoritmul Minimax cu tăiere Alpha-Beta pentru luarea deciziilor strategice.
    * `board` este tabla de joc curentă.
    * `depth` este adâncimea de căutare.
    * `alpha` și `beta` sunt valorile pentru tăierea Alpha-Beta.
    * `maximizing_player` indică dacă se maximizează scorul calculatorului sau al jucătorului.

* `get_next_open_row(board, column)`:
    * Găsește următorul rând liber dintr-o coloană.

* `score_position(board, player)`:
    * Evaluează scorul unei poziții pe tablă pentru un jucător.

* `evaluate_window(window, piece)`:
    * Evaluează scorul unei ferestre de 4 celule consecutive.

### 4.4. Clasa `Services` (`services.py`)

* `__init__(self, board_repository)`:
    * Constructorul clasei.
    * Primește o instanță a clasei `BoardActions`.

* `is_game_over(self)`:
    * Delegează verificarea stării jocului către `board_repository`.

* `add_move_on_board(self, player, type_finder)`:
    * Delegează adăugarea unei mutări pe tablă către `board_repository`.

* `computer_move(self, computer_difficulty)`:
    * Delegează mutarea calculatorului către `board_repository`.

* `restart_game(self)`:
    * Delegează reînceperea jocului către `board_repository`.

* `display_board(self)`:
    * Delegează afișarea tablei către `board_repository`.

* `get_board(self)`:
    * Delegează obținerea tablei către `board_repository`.

### 4.5. Clasa `UserInterface` (`user_interface.py`)

* `__init__(self, service)`:
    * Constructorul clasei.
    * Primește o instanță a clasei `Services`.

* `try_and_except_input(left_bound, right_bound)`:
    * Gestionează input-ul utilizatorului cu validare și tratare a erorilor (pentru input-uri numerice).

* `computer_difficulty_level_menu(self)`:
    * Afișează meniul pentru alegerea nivelului de dificultate al calculatorului (în CLI).

* `verify_input(user_move)`:
    * Verifică dacă input-ul utilizatorului pentru mutare este valid (formatul coloanei).

* `run_program(self)`:
    * Rulează bucla principală a jocului în modul CLI.

### 4.6. Clasa `GUIBoardRepository` (`GUI_repository.py`)

* `__init__(self, root, board_action, difficulty)`:
    * Constructorul clasei.
    * Primește fereastra principală `root` (din `tkinter`), o instanță a clasei `BoardActions` și nivelul de dificultate al calculatorului.

* `create_board(self)`:
    * Creează elementele vizuale ale tablei de joc (butoane) folosind `tkinter`.

* `make_move(self, row, column)`:
    * Gestionează mutările utilizatorului prin evenimente de click pe butoane.
    * Apelează la metodele din `board_action` pentru a efectua mutarea.

* `update_board(self, player=None)`:
    * Actualizează aspectul vizual al tablei după o mutare (schimbă culoarea butoanelor).

## 5. Dependențe

* **Python 3.x**
* **tkinter** (pentru GUI - de obicei inclus în instalarea standard Python)
* **texttable** (pentru afișarea tablei în CLI - se poate instala cu `pip install texttable`)

## 6. Instrucțiuni de Instalare și Rulare

1.  Asigură-te că ai Python 3.x instalat pe sistemul tău.
2.  Clonează repository-ul proiectului pe calculator.
3.  Deschide un terminal sau linie de comandă și navighează în directorul proiectului.
4.  Rulează fișierul `main.py` folosind comanda: `python main.py`
5.  Urmează instrucțiunile afișate pentru a alege interfața (CLI sau GUI) și, dacă este cazul, nivelul de dificultate al calculatorului.

## 7. Testare

Proiectul include teste unitare implementate folosind modulul `unittest` din Python.