import random

def select_random_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print('Current progress: ' + display)

def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(stages[incorrect_guesses])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    incorrect_letters = []

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        display_current_progress(word, guessed_letters)
        print(f"Incorrect guesses: {', '.join(incorrect_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters or guess in incorrect_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_letters.append(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if all(letter in guessed_letters for letter in word):
            display_current_progress(word, guessed_letters)
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        display_hangman(incorrect_guesses)
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
