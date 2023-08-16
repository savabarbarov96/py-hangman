import requests


def hangman():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    word = response.json()
    word_chars = set(word[0])  # Convert to set for faster membership testing

    score = 5
    guessed_chars = set()  # To keep track of guessed characters

    while score > 0:

        guess = input("Try to guess my word, type a letter: ").lower()

        if guess in guessed_chars:
            print("You've already guessed that letter. Try again.")
            continue  # Skip the rest of the loop and go to the next iteration

        guessed_chars.add(guess)  # Add the guessed character to the set

        if guess in word_chars:
            print("Correct!")
            # Remove guessed letter from set to avoid counting it again
            word_chars.remove(guess)

            if len(word_chars) == 0:  # If all letters have been guessed
                print("You win!")
                break
        else:
            print("Incorrect. You have", score - 1, "guesses left.")
            score -= 1

    return "You lose. The word was " + word[0]


hangman()
