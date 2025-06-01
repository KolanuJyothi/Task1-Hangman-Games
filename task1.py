import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'console']
    word = random.choice(words).lower()
    guessed_letters = set()
    correct_letters = set(word)
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0 and correct_letters:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            correct_letters.remove(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        # Display current progress
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(display_word))

    if not correct_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the game
hangman()