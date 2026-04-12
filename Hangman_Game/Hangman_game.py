
import random
import string


def wordchoice():
    words = ["python", "apple", "house", "tiger", "chair",]

    word = random.choice(words)
    return word

def play_hangman():
    word = wordchoice()
    guessed_word = ["_"] * len(word)
   
    attempts = 6

    print("Welcome to Hangman!")


# Game loop runs while attempts remain AND word is not fully guessed
    while attempts > 0 and "_" in guessed_word:
    # Display current progress (e.g., _ p p _ e)
        print("\nWord:", " ".join(guessed_word))
    
    # Take user input and convert to lowercase
        guess = input("Guess a letter: ").lower()
    
    # Check if input is a valid lowercase letter
        if guess not in string.ascii_lowercase:
            print("Only single letters a-z. Try again.")
            continue  # Skip rest of loop and ask again


  
    
        if guess in word:
        # Loop through the word to reveal ALL positions of the letter
            for i in range(len(word)):
               if word[i] == guess and guessed_word[i] == "_":
                   guessed_word[i] = guess
                   break 
                
                
        else:
        # Reduce attempts if guess is wrong
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)
    return word,guessed_word



while True:
    word, guessed_word = play_hangman()

    # After loop ends, check win or loss
    if "_" not in guessed_word:
        print("\nYou won! The word was:", word)
    else:
        print("\nYou lost! The word was:", word)

    ask = input("Do you want to play again?\n").lower()
    if ask == "no":
        print("Exiting program")
        exit()
