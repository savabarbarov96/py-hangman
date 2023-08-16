import requests
import os

def hangman():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    word = response.json()[0]
    word_chars = set(word)

    print(word)
    score = 5
    guessed_chars = set()

    while score > 0:

        guess = input("Try to guess my word, type a letter: ").lower()

        if guess in guessed_chars:
            print("You've already guessed that letter. Try again.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_chars.add(guess)

        if guess in word_chars:
            print("Correct!")
            word_chars.remove(guess)
            if len(word_chars) == 0:
                print("You win!")
                play_again = input("Do you want to play again? Yes/No\n")
                if play_again == "yes":
                    hangman()
                if play_again == "no":
                    print("Thank you for playing!")
                    return
        else:
            print("Incorrect. You have", score - 1, "guesses left.")
            score -= 1

        display_word = ""
        for letter in word:
            if letter in guessed_chars:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        if score == 0:
            print("You lose. The word was", word)
            play_again = input("Do you want to play again? Yes/No\n")
            if play_again == "yes":
                hangman()
            if play_again == "no":
                print("Thank you for playing!")
                return

hangman()
import requests
import os

def hangman():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    word = response.json()[0]
    word_chars = set(word)

    print(word)
    score = 5
    guessed_chars = set()

    while score > 0:

        guess = input("Try to guess my word, type a letter: ").lower()

        if guess in guessed_chars:
            print("You've already guessed that letter. Try again.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_chars.add(guess)

        if guess in word_chars:
            print("Correct!")
            word_chars.remove(guess)
            if len(word_chars) == 0:
                print("You win!")
                play_again = input("Do you want to play again? Yes/No\n")
                if play_again == "yes":
                    hangman()
                if play_again == "no":
                    print("Thank you for playing!")
                    return
        else:
            print("Incorrect. You have", score - 1, "guesses left.")
            score -= 1

        display_word = ""
        for letter in word:
            if letter in guessed_chars:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)

        if score == 0:
            print("You lose. The word was", word)
            play_again = input("Do you want to play again? Yes/No\n")
            if play_again == "yes":
                hangman()
            if play_again == "no":
                print("Thank you for playing!")
                return

hangman()
