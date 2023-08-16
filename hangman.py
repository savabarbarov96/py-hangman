import requests

def hangman():
    word = requests.get("https://random-word-api.herokuapp.com/word").lower()
    print(word)
    word_chars = set(word)  # Convert to set for faster membership testing
    
    score = 5
    while score > 0:

        guess = input("Try to guess my word, type a letter: ").lower()
        
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
    
    return "You lose. The word was " + word

hangman()