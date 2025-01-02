import random
from words import data
import string

def get_word(data):
    word = random.choice(data)
    while '-' in word or ',' in word:
        word = random.choice(data)
    return word.upper()

def hangman():
    word = get_word(data)
    word_letters = set(word)  # Unique letters in the word to guess
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    used_letters = set()  # Track letters guessed by the user
    
    while len(word_letters) > 0:
        # Show the used letters
        print('Used letters:', ' '.join(sorted(used_letters)))
        
        # Show the current state of the word with guessed letters revealed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        
        # Get a user's guess
        used_letter = input('Guess a letter: ').upper()
        
        # Handle valid guesses
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
                print(f"Good guess! '{used_letter}' is in the word.")
            else:
                print(f"'{used_letter}' is not in the word.")
        
        # Handle repeated guesses
        elif used_letter in used_letters:
            print(f"You've already guessed '{used_letter}'. Try again!")
        
        # Handle invalid input
        else:
            print("Invalid character. Please guess a valid letter.")
    
    # When the loop ends, the word is fully guessed
    print(f"Congratulations! You guessed the word '{word}'!")

# Run the game
hangman()