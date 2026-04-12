# 🎮 Hangman Game (Python)

## 📌 Overview
This is a simple command-line Hangman game written in Python.  
The program randomly selects a word, and the player has to guess it letter by letter within a limited number of attempts.

---

## ⚙️ How It Works
1. A random word is selected from a predefined list.
2. The word is hidden using underscores (_ _ _).
3. The player guesses one letter at a time.
4. If the guess is correct:
   - The letter is revealed in its correct position(s).
5. If the guess is incorrect:
   - Attempts are reduced.
6. The game continues until:
   - The player guesses the word (WIN), or
   - The player runs out of attempts (LOSS).
7. After the game ends, the player can choose to play again.

---

## 🧠 Game Logic & Formula
- Word length = number of underscores shown
- Attempts = 6 (fixed)
- Correct Guess:
  - Replace "_" with the guessed letter at correct positions
- Wrong Guess:
  - attempts = attempts - 1

Winning Condition:
- No "_" left in guessed_word

Losing Condition:
- attempts == 0

---

## 📂 File Structure
hangman.py   → Main Python file containing all game logic

---

## ▶️ How to Run the Program
1. Install Python (if not already installed)
2. Save the file as:
   hangman.py
3. Open terminal or command prompt
4. Run the program:
   python hangman.py

---

## 💾 Data Storage
- No external files or databases are used.
- Words are stored in a list inside the program.
- Game state (guesses, attempts) is stored temporarily in variables.

---

## 🔁 Game Flow
Start Program  
↓  
Select Random Word  
↓  
Display Hidden Word  
↓  
User Inputs Letter  
↓  
Check:
    → Correct → Reveal Letter  
    → Wrong → Reduce Attempts  
↓  
Repeat Until Win/Loss  
↓  
Ask User to Play Again  

---

## ⚠️ Limitations
- Only single lowercase letters are accepted.
- No tracking of previously guessed letters.
- Small word list.
- No graphical interface (CLI only).

---

## 🚀 Future Improvements
- Add difficulty levels
- Track guessed letters
- Expand word list
- Add hints system
- Create GUI version (Tkinter or Web)

---

## 👩‍💻 Author
Alaiza  
BS Artificial Intelligence Student  
Focused on improving programming skills and building logic-based projects.
