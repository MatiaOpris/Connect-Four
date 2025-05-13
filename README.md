# Connect-Four - Romanian

Acest proiect este o implementare a jocului Connect Four (Patru la rând) scris în Python. Permite jucătorilor să joace împotriva calculatorului cu diferite niveluri de dificultate sau să interacționeze prin intermediul unei interfețe grafice (GUI).

## Structura Proiectului

Proiectul este organizat în mai multe fișiere Python, fiecare având o responsabilitate specifică:

* **main.py**:  Fișierul principal de execuție. Acesta inițializează jocul, permite utilizatorului să aleagă între interfața linie de comandă (CLI) și interfața grafică (GUI), și setează nivelul de dificultate al calculatorului, dacă este cazul.
* **user_interface.py**:  Gestionarea interacțiunii cu utilizatorul prin linia de comandă (CLI). Afișează tabla de joc, primește input-ul utilizatorului și afișează rezultatele jocului.
* **GUI_repository.py**:  Implementarea interfeței grafice (GUI) folosind `tkinter`. Creează tabla de joc vizuală, gestionează input-ul utilizatorului prin click-uri și actualizează tabla după fiecare mutare.
* **services.py**:  Stratul de servicii care face legătura între interfața utilizator și logica jocului. Coordonează acțiunile necesare pentru desfășurarea jocului.
* **board_repository.py**:  Conține logica principală a jocului. Definește regulile jocului, verifică mutările, determină câștigătorul și gestionează tabla de joc. Include, de asemenea, strategia calculatorului pentru diferite niveluri de dificultate.
* **board.py**:  Definește clasa `Board`, care reprezintă tabla de joc și metodele pentru a o inițializa și reseta.
* **src/domain/**:  Acest director ar putea conține fișiere de domeniu (ex: clase de date). În codul furnizat, există doar `board.py` în această structură.
* **src/repository/**:  Acest director conține fișierele care gestionează persistenta datelor sau interacțiunea cu surse de date. În codul furnizat, avem `board_repository.py` și `GUI_repository.py`.
* **src/services/**:  Acest director conține fișierele care implementează logica de afaceri a aplicației. În codul furnizat, avem `services.py`.
* **src/ui/**:  Acest director conține fișierele care gestionează interacțiunea cu utilizatorul. În codul furnizat, avem `user_interface.py`.

## Cum rulezi jocul

1.  **Asigură-te că ai Python 3.x instalat.**
2.  **Clonează acest repository pe calculatorul tău.**
3.  **Deschide un terminal sau o linie de comandă și navighează în directorul proiectului.**
4.  **Rulează fișierul `main.py` folosind comanda:** `python main.py`
5.  **Urmează instrucțiunile din terminal pentru a alege interfața (CLI sau GUI) și, dacă alegi GUI, nivelul de dificultate al calculatorului.**

## Dependențe

* **tkinter**:  Pentru interfața grafică (GUI).  (De obicei inclus în instalarea standard Python)
* **texttable**: Pentru afișarea tablei in format text in CLI. Poti instala cu `pip install texttable`

## Funcționalități

* **Două interfețe de joc:**
    * **CLI (Command Line Interface):** Jocul se desfășoară în terminal, cu input text pentru mutări.
    * **GUI (Graphical User Interface):** Interfață vizuală interactivă, cu butoane pentru a face mutări.
* **Niveluri de dificultate pentru calculator:** Jucătorii pot alege dintre mai multe niveluri de dificultate (Ușor, Mediu, Greu, Incredibil) pentru a juca împotriva calculatorului.
* **Validarea mutărilor:** Jocul verifică dacă mutările sunt valide și afișează erori dacă nu sunt.
* **Detectarea câștigătorului:** Jocul determină automat când un jucător a câștigat sau când jocul s-a terminat la egalitate.
* **Opțiunea de a reîncepe jocul:** Jucătorii pot reîncepe un joc nou după ce unul s-a terminat.

## Note

* Codul este organizat folosind o structură modulară, ceea ce facilitează mentenanța și extinderea.
* Sunt incluse teste unitare pentru a asigura corectitudinea funcționării diferitelor componente ale jocului.
* Strategia calculatorului variază în funcție de nivelul de dificultate, de la mutări aleatorii la algoritmi mai avansați (minimax).

Sper ca acest readme este util!
